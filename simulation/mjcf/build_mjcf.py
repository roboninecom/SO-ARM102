"""Generate the SO-ARM 102 MuJoCo model (so_arm_102.xml) from the URDF.

    python simulation/mjcf/build_mjcf.py

The URDF stays the source of truth: meshes, link frames, inertials, limits and the
adaptive collision boxes are copied from it. This script adds what the URDF cannot say:

- LeRobot joint names and the LeRobot degrees convention (zero = middle of the range),
- the parallel gripper as one actuator driving both jaws,
- servo actuators, joint damping and friction, contact exclusions.

Needs only the Python standard library.
"""

import math
import struct
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
URDF = HERE.parent / "urdf" / "so_arm_102.urdf"
OUT = HERE / "so_arm_102.xml"

# URDF joint -> (LeRobot name, servo class, zero at the middle of the range, sign).
# Wrist roll is calibrated as a full-turn motor: LeRobot puts its zero at the
# calibration pose, which is the CAD pose, so it is not shifted.
# sign -1 reverses the URDF axis. The follower is teleoperated by the standard
# SO-101 leader in degrees, one to one, so its joints must turn the SO-101 way
# (TheRobotStudio SO101 new_calib model): positive shoulder lift and elbow flex
# lower the arm, which is the opposite of the URDF axes.
JOINTS = {
    "base_to_link1": ("shoulder_pan", "sts3235", True, 1),
    "link1_to_link2": ("shoulder_lift", "sts3250", True, -1),
    "link2_to_link3": ("elbow_flex", "sts3250", True, -1),
    "link3_to_link4": ("wrist_flex", "sts3235", True, 1),
    "link4_to_link5": ("wrist_roll", "sts3215_c049", False, 1),
}
BODIES = {
    "base_link": "base",
    "link1_1": "shoulder",
    "link2_1": "upper_arm",
    "link3_1": "lower_arm",
    "link4_1": "wrist",
    "link5_1": "gripper",
    "clamp1_1": "jaw_left",
    "clamp2_1": "jaw_right",
}
COLORS = {
    "base": "0.15 0.15 0.15 1",
    "jaw_left": "0.12 0.35 0.75 1",
    "jaw_right": "0.12 0.35 0.75 1",
}
PRINTED = "0.22 0.22 0.24 1"

# Servo models. Stall torque is the URDF joint effort (STS3235 30 kg.cm, STS3250
# 50 kg.cm, ST-3215-C049 estimated in PR #32). kp and kv scale the SO-101 STS3215
# model (kp 998.22, kv 2.731 at 2.94 N.m; TheRobotStudio SO-ARM100, Apache-2.0)
# with stall torque: the servo firmware uses the same P gain, so the error at which
# the torque saturates is the same. Damping, friction and armature are the SO-101
# STS3215 identification; armature scales with the gear ratio squared for C049.
SERVOS = {
    "sts3235": dict(torque=2.942, armature=0.028),
    "sts3250": dict(torque=4.903, armature=0.028),
    "sts3215_c049": dict(torque=1.629, armature=0.028 * (191 / 345) ** 2),
}
SO101_KP, SO101_KV, SO101_TORQUE = 998.22, 2.731, 2.94

# Gripper: one pinion (7.2 mm pitch radius, PR #21) drives both racks. The
# actuator acts on the jaw span, so each jaw gets torque / (2 * radius).
PINION_RADIUS = 0.0072
GRIPPER_KP = 2000.0  # N per metre of span error: a 40 mm object squeezed at 80 N.


def f(x):
    return f"{0.0 if abs(x) < 1e-9 else x:.6g}"


def vec(values):
    return " ".join(f(v) for v in values)


def floats(text):
    return [float(v) for v in text.split()]


def mesh_max_x(name):
    """Largest x of a binary STL, in metres (URDF meshes are in mm, assembly frame)."""
    data = (URDF.parent / "meshes" / f"{name}.stl").read_bytes()
    count = struct.unpack_from("<I", data, 80)[0]
    return max(struct.unpack_from("<3f", data, 84 + 50 * i + 12 + 12 * k)[0]
               for i in range(count) for k in range(3)) / 1000


def rpy_quat(rpy):
    """URDF roll-pitch-yaw (fixed X, Y, Z) to a MuJoCo quaternion (w x y z)."""
    (cr, sr), (cp, sp), (cy, sy) = ((math.cos(a / 2), math.sin(a / 2)) for a in rpy)
    return [cr * cp * cy + sr * sp * sy, sr * cp * cy - cr * sp * sy,
            cr * sp * cy + sr * cp * sy, cr * cp * sy - sr * sp * cy]


def sub(parent, tag, **attrs):
    return ET.SubElement(parent, tag, {k.rstrip("_"): str(v) for k, v in attrs.items()})


def load_urdf():
    root = ET.parse(URDF).getroot()
    links = {link.get("name"): link for link in root.findall("link")}
    joints = {}
    for joint in root.findall("joint"):
        child = links[joint.find("child").get("link")]
        for elem in (joint.find("origin"), child.find("inertial/origin"), child.find("visual/origin")):
            if elem is not None and any(abs(a) > 1e-9 for a in floats(elem.get("rpy", "0 0 0"))):
                raise ValueError(f"{joint.get('name')}: rotated frames are not supported")
        joints[joint.find("child").get("link")] = joint
    return links, joints


def chain(name, joints):
    """Joints from link `name` up to the base."""
    while name in joints:
        yield joints[name]
        name = joints[name].find("parent").get("link")


def add_link(parent, name, links, joints, ranges):
    link = links[name]
    joint = joints.get(name)
    pos = floats(joint.find("origin").get("xyz")) if joint is not None else [0, 0, 0]
    body_name = BODIES[name]
    body = sub(parent, "body", name=body_name, pos=vec(pos))

    if joint is not None:
        axis = floats(joint.find("axis").get("xyz"))
        axis = [round(a) if abs(a - round(a)) < 1e-6 else a for a in axis]
        lo, hi = (float(joint.find("limit").get(k)) for k in ("lower", "upper"))
        jname = joint.get("name")
        if jname in JOINTS:
            jlabel, servo, centre, sign = JOINTS[jname]
            mid = (lo + hi) / 2 if centre else 0.0
            # q = sign * (q_urdf - mid); the CAD pose (q_urdf = 0) is q = ref.
            lo, hi = sorted([sign * (lo - mid), sign * (hi - mid)])
            attrs = dict(name=jlabel, axis=vec([sign * a for a in axis]), range=vec([lo, hi]), class_=servo)
            if mid:
                attrs["ref"] = f(-sign * mid)
            sub(body, "joint", **attrs)
            ranges[jlabel] = (lo, hi)
        else:
            sub(body, "joint", name=body_name, type="slide", axis=vec(axis), range=vec([lo, hi]), class_="jaw")
            ranges[body_name] = (lo, hi)

    inertial = link.find("inertial")
    i = {k: float(v) for k, v in inertial.find("inertia").attrib.items()}
    sub(body, "inertial", pos=vec(floats(inertial.find("origin").get("xyz"))),
        mass=f(float(inertial.find("mass").get("value"))),
        fullinertia=vec([i["ixx"], i["iyy"], i["izz"], i["ixy"], i["ixz"], i["iyz"]]))

    visual = link.find("visual")
    sub(body, "geom", class_="visual", mesh=body_name, pos=vec(floats(visual.find("origin").get("xyz"))),
        material=body_name)
    collision_class = "jaw_collision" if body_name.startswith("jaw") else "collision"
    for col in link.findall("collision"):
        size = [s / 2 for s in floats(col.find("geometry").find("box").get("size"))]
        origin = col.find("origin")
        attrs = dict(class_=collision_class, size=vec(size), pos=vec(floats(origin.get("xyz"))))
        rpy = floats(origin.get("rpy", "0 0 0"))
        if any(abs(a) > 1e-9 for a in rpy):
            attrs["quat"] = vec(rpy_quat(rpy))
        sub(body, "geom", **attrs)

    if body_name == "gripper":
        # Tip centre: on the wrist roll axis, level with the jaw ends.
        x = mesh_max_x("clamp1_1") - sum(floats(j.find("origin").get("xyz"))[0] for j in chain(name, joints))
        sub(body, "site", name="gripper_tip", pos=vec([x, 0, 0]), size="0.004", rgba="1 0.5 0 1", group="4")

    for child, j in joints.items():
        if j.find("parent").get("link") == name:
            add_link(body, child, links, joints, ranges)
    return body


def build():
    links, joints = load_urdf()
    m = ET.Element("mujoco", model="so_arm_102")
    m.append(ET.Comment(
        " Generated by build_mjcf.py from ../urdf/so_arm_102.urdf. Do not edit by hand. "
        "Joint names, directions and zeros follow LeRobot use_degrees=True as on the SO-101: zero is the "
        "middle of each range (wrist roll: the CAD pose); the CAD pose is keyframe 'cad'. "
        "Gripper control is the jaw span in metres (LeRobot 0..100 = span / max span * 100). "))
    sub(m, "compiler", angle="radian", meshdir="../urdf/meshes", autolimits="true")
    sub(m, "option", integrator="implicitfast")

    default = sub(sub(m, "default"), "default", class_="so_arm_102")
    sub(default, "joint", damping="0.6", frictionloss="0.052")
    sub(default, "position", inheritrange="1")
    vis = sub(default, "default", class_="visual")
    sub(vis, "geom", type="mesh", contype="0", conaffinity="0", group="2")
    col = sub(default, "default", class_="collision")
    sub(col, "geom", type="box", group="3", rgba="0.8 0.3 0.3 0.4")
    jaw_col = sub(default, "default", class_="jaw_collision")
    sub(jaw_col, "geom", type="box", group="3", rgba="0.8 0.3 0.3 0.4", condim="4", friction="1.5 0.02 0.001",
        solref="0.004 1", priority="1")
    for name, s in SERVOS.items():
        d = sub(default, "default", class_=name)
        sub(d, "joint", armature=f(s["armature"]))
        scale = s["torque"] / SO101_TORQUE
        sub(d, "position", kp=f(SO101_KP * scale), kv=f(SO101_KV * scale),
            forcerange=vec([-s["torque"], s["torque"]]))
    jaw = sub(default, "default", class_="jaw")
    sub(jaw, "joint", damping="5", frictionloss="0.5", armature="0.05")

    asset = sub(m, "asset")
    for urdf_name, name in BODIES.items():
        sub(asset, "mesh", name=name, file=f"{urdf_name}.stl", scale="0.001 0.001 0.001")
        sub(asset, "material", name=name, rgba=COLORS.get(name, PRINTED), specular="0.3", shininess="0.3")

    world = sub(m, "worldbody")
    ranges = {}
    base = add_link(world, "base_link", links, joints, ranges)
    base.set("childclass", "so_arm_102")

    hold = sub(m, "contact")
    # MuJoCo excludes neighbours across a joint, except a body and the fixed base.
    # The jaws slide side by side.
    for a, b in [("base", "shoulder"), ("jaw_left", "jaw_right")]:
        sub(hold, "exclude", body1=a, body2=b)

    jaw_max = ranges["jaw_left"][1] - ranges["jaw_left"][0]
    tendon = sub(sub(m, "tendon"), "fixed", name="gripper")
    sub(tendon, "joint", joint="jaw_left", coef="1")
    sub(tendon, "joint", joint="jaw_right", coef="-1")

    eq = sub(m, "equality")
    sub(eq, "joint", joint1="jaw_left", joint2="jaw_right", polycoef="0 -1 0 0 0", solref="0.005 1")

    act = sub(m, "actuator")
    for label, servo, _, _ in JOINTS.values():
        sub(act, "position", name=label, joint=label, class_=servo)
    torque = SERVOS["sts3215_c049"]["torque"]
    force = torque / (2 * PINION_RADIUS)
    sub(act, "position", name="gripper", tendon="gripper", kp=f(GRIPPER_KP), kv="40",
        forcerange=vec([-force, force]), ctrlrange=vec([0, 2 * jaw_max]))

    keys = sub(m, "keyframe")
    sub(keys, "key", name="home", qpos=vec([0] * 7), ctrl=vec([0] * 6))
    cad = [float(j.get("ref", 0)) for j in world.iter("joint") if j.get("class") != "jaw"]
    sub(keys, "key", name="cad", qpos=vec(cad + [0, 0]), ctrl=vec(cad + [0]))

    ET.indent(m, space="  ")
    OUT.write_text(ET.tostring(m, encoding="unicode") + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(HERE.parent.parent)}")


if __name__ == "__main__":
    build()
