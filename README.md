# SO-ARM 102

<!-- documentation-languages -->
[English](docs/i18n/en/README.md) · [Русский](docs/i18n/ru/README.md) · [Español](docs/i18n/es/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [Português (Brasil)](docs/i18n/pt-BR/README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md)
<!-- /documentation-languages -->

<div align="center">

[![SO-ARM 102](assets/images/photos/so-arm-102-live.jpg)](assets/video/so-arm-102-preview.mp4)

**🎥 [Watch the preview video](assets/video/so-arm-102-preview.mp4)** · **🛒 [Buy the kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

**SO-ARM 102 is an open-source leader–follower robot arm kit for teleoperation and imitation learning. Each arm has five degrees of freedom plus a gripper.**

<p align="left">
Building on SO-ARM 100 and 101, it combines a stiffer PET-CF frame with a parallel gripper.
</p>

[![Hardware: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](HARDWARE-LICENSE.txt)
[![Software: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](SOFTWARE-LICENSE.txt)
[![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](DOCS-LICENSE.txt)
[![GitHub release](https://img.shields.io/github/v/release/roboninecom/SO-ARM-102)](https://github.com/roboninecom/SO-ARM-102/releases/latest)

📩 [hello@robonine.com](mailto:hello@robonine.com)

**DIY budget: ~$340 for components, or ~$374 including printing material.**
[BOM summary](#bill-of-materials) · [Itemised costs and purchase links](docs/bom.md#estimated-kit-cost)

> Rather not source the parts and print them yourself? **[Buy the SO-ARM 102 kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

</div>

---

## ✨ What changed against SO-ARM 101

| | SO-ARM 101 | SO-ARM 102 |
|---|---|---|
| Gripper | Angular jaw | Parallel gripper, 85 mm span |
| Frame material | PLA | PET-CF (Fiberon PET-CF17 tested) |
| Structure | Solid links | Topology-optimised links |
| Base rotation range | 220° | **352°** |
| Horizontal reach | 441 mm | **483 mm** |
| Deflection at the gripper, 300 g load ¹ | 7.5 mm | **3.4–3.9 mm** |
| Shoulder and elbow speed | 45 RPM (STS3215) | **75 RPM (STS3250)** |
| Noise at 1 m | 70 dB | **60 dB** |

¹ Both arms built with printed servo dummies, so the frame is compared, not the motors.
Full results and test conditions are in [docs/specifications.md](docs/specifications.md).

---

## 🎥 Preview

<div align="center">

[![SO-ARM 102 preview](assets/video/so-arm-102-preview.gif)](assets/video/so-arm-102-preview.mp4)

*Click for the full video, 21 s*

</div>

---

## 🤝 Configurations

### Single-arm: one leader + one follower

The standard kit. Move the leader by hand, and the follower repeats the motion.
Use it for teleoperation and for recording demonstrations for imitation learning.

![One leader and one follower](assets/images/renders/config-single-arm.jpg)

### Bimanual: two leaders + two followers

Two kits side by side. Each hand drives its own leader, so the followers can pass objects,
hold and work on a part, or do any task that needs two hands.

![Two leaders and two followers](assets/images/renders/config-dual-arm.jpg)

### The two arms

| Follower | Leader |
|:-:|:-:|
| ![Follower arm](assets/images/renders/follower.jpg) | ![Leader arm](assets/images/renders/leader.jpg) |
| Parallel gripper, wrist camera, 12 V | Handle with trigger, 5 V |

---

## 🚀 Build it in four steps

Prefer a ready kit? **[Buy the SO-ARM 102 kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

### 1. Print the parts

Individual parts fit a 180 × 180 mm bed. The largest part is 160 mm long.
The supplied 3MF plate layouts use a 256 × 256 mm bed.

- 3MF slicer projects with saved orientation and support settings: [`models/3mf/`](models/3mf/)
  — [leader](models/3mf/SO102_leader.3mf), [follower arms](models/3mf/SO102_follower_arms.3mf),
  [Follower gripper and base](models/3mf/SO102_follower_gripper_base.3mf)
- Project contents and printer profiles: [models/README.md](models/README.md)
- STL files, ready to slice: [`models/stl/`](models/stl/)
- STEP sources: [`models/step/`](models/step/)
- Material, settings and part quantities: [docs/printing.md](docs/printing.md)

### 2. Buy the hardware

Source the components from the [BOM summary](#bill-of-materials) and
[full BOM with purchase links](docs/bom.md). Budget **$340.22** for components,
or **$373.97** including printing material, before shipping and taxes.

| Arm | Servos | Controller | Power |
|---|---|---|---|
| Follower | 2 × STS3235, 2 × STS3250, 2 × STS3215 | Waveshare Bus Servo Adapter | **12 V** |
| Leader | 6 × STS3215 | Waveshare Bus Servo Adapter | **5 V** |

> ⚠️ **The leader runs on 5 V and the follower on 12 V.** Do not swap the power supplies.

### 3. Assemble

- Printable booklet, 32 pages A5: [docs/SO-ARM102_assembly_A5_v0.7.pdf](docs/SO-ARM102_assembly_A5_v0.7.pdf)
- Step list with parts and fasteners: [docs/assembly-guide.md](docs/assembly-guide.md)

Tools: hex keys 1.5 mm (M2 screws) and 2 mm (M3 screws).

### 4. Set up the software

Servo IDs, calibration and lessons: **[lab.robonine.com](https://lab.robonine.com)**.
Use the SO-ARM 102 follower plugin with the standard `so101_leader` type.
**[LeRobot installation and setup](docs/lerobot.md)**.

---

## Bill of materials

Quantities and reference costs for **one leader + one follower**:

| Category / purchase links | Kit contents | Total (USD) |
|---|---|---:|
| [Servos](docs/bom.md#servos) | 6 × STS3215 7.4 V, 2 × STS3215 12 V, 2 × STS3235, 2 × STS3250 | $240.72 |
| [Electronics](docs/bom.md#electronics) | 2 controllers, 2 power supplies, 2 USB cables, 1 wrist camera | $50.50 |
| [Mechanical parts](docs/bom.md#mechanical-parts) | 4 bearings, 2 steel guide rods, 4 table clamps | $37.76 |
| [Fasteners](docs/bom.md#fasteners) | Screws and nuts; specified servo-kit screws included | $11.24 |
| **Components subtotal** | | **$340.22** |
| [Printing material](docs/bom.md#printing-materials) | 0.4 kg PET-CF17 + 0.75 kg PETG allowance | $33.75 |
| **Total with printing material** | | **$373.97** |

Buying the example full packs and filament spools from scratch costs about **$435**,
including unused spares. These are reference estimates, not new supplier quotes.
Shipping, taxes, tools, a computer, a printer, electricity and assembly labour are excluded.
Confirm supplier prices, variants and minimum order quantities before ordering;
re-slice the 3MF projects to check filament consumption.

[Full BOM, purchase links and cost assumptions](docs/bom.md#estimated-kit-cost).

---

## URDF export

The current standalone export is in [`simulation/urdf/`](simulation/urdf/):
[URDF](simulation/urdf/so_arm_102.urdf) · [Xacro](simulation/urdf/so_arm_102.xacro).
Keep `meshes/` beside the description files; mesh paths are relative to this folder.

- **Visuals:** STL meshes. **Collisions:** fitted, independently rotated boxes on all eight links.
- **Mass estimate:** PLA, 30% infill, 6 perimeters, 6 top/bottom layers,
  0.2 mm layer height, and **0.40 mm extrusion width**. These are simulation
  assumptions; use [the printing guide](docs/printing.md) for fabrication settings.
- **Hardware masses:** six motors at 70 g each; base bearing at 105 g.
  Total estimated model mass: **0.889 kg**.
- **Gripper:** `clamp2` mimics `clamp1` with multiplier `-1`.

[Export settings](simulation/urdf/export_settings.json) and
[mass properties](simulation/urdf/mass_properties.json) record the assumptions.
Geometry and inertia checks are recorded in [export_verification.json](simulation/urdf/export_verification.json).

---

## 📁 Repository structure

```
├── models/
│   ├── 3mf/                 # Slicer projects: leader, follower, gripper and board case
│   ├── stl/                 # Print-ready meshes
│   │   ├── common/          # Shared parts, including controller cases
│   │   ├── follower/        # Parallel gripper and camera mount
│   │   └── leader/          # Handle, trigger and wrist roll
│   └── step/                # CAD sources, same layout as stl/
├── docs/
│   ├── printing.md          # Material, slicer settings, quantities
│   ├── bom.md               # Bill of materials
│   ├── assembly-guide.md    # Step list with parts and fasteners
│   ├── specifications.md    # Geometry, servos, measured results vs SO-ARM 101
│   └── SO-ARM102_assembly_A5_v0.7.pdf
├── assets/
│   ├── images/              # Photos, renders, booklet pages, test photos
│   └── video/               # Preview video and GIF
├── LICENSING.md             # Which licence covers which file
└── NOTICE                   # Third-party attribution
```

---

## ⚠️ Known issues

Build notes from independent testing; check these when assembling.

1. **Use booklet v0.7.** Earlier booklets show the HAT controller and older gripper parts. v0.7 fits a Bus Servo Adapter on both arms.
2. **M2 screws are hard to reach in several places.** Expect to fight a few of them.
3. **The gripper clamps run tight on carbon rods.** The clamp bores are sized for 6.1 mm. Rod diameters vary between suppliers, so check the fit before assembly.
4. **Check the servo cable lengths** before closing each joint, especially from the base to the shoulder.
5. **The assembly order is awkward in two places** of the booklet. Read two steps ahead before fastening.
6. **Leader joints can feel loose.** Adding 8 × 2 mm rubber O-rings between each servo and its horn gives the leader smooth, silent friction. Use two per servo on joints 1–4 and one on joints 5–6.

Found something else? Please [open an issue](https://github.com/roboninecom/SO-ARM-102/issues).

---

## ⭐ Star History

[![Star History Chart for SO-ARM 102](https://api.star-history.com/svg?repos=roboninecom/so-arm-102&type=date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm-102&type=date&legend=top-left)

---

## 🔗 Related projects

- [SO-ARM100/101 Parallel Gripper](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper), the gripper the SO-ARM 102 gripper grew from
- [SO-ARM101](https://github.com/TheRobotStudio/SO-ARM100) by TheRobotStudio, the arm this design succeeds
- [Practical comparison of smart serial servos](https://robonine.com/smart-serial-servo-motor-comparison-robotics/), the tests behind the servo choice
- [Choosing a filament for robotic arms](https://robonine.com/choosing-filament-for-robotic-arm-applications/), the tests behind PET-CF

---

## 📄 License

Copyright (c) 2026 Robonine. Different kinds of material carry different licences:

| Material | Licence |
|---|---|
| Hardware designs in `models/` | [CERN-OHL-P-2.0](HARDWARE-LICENSE.txt) |
| Software and configuration | [Apache-2.0](SOFTWARE-LICENSE.txt) |
| Documentation and images in `docs/`, `assets/`, all `README.md` | [CC BY 4.0](DOCS-LICENSE.txt) |

See [LICENSING.md](LICENSING.md) and [REUSE.toml](REUSE.toml) for the file-by-file map.

---

## 👥 Team

| Name | Role | Contact |
|------|------|---------|
| **Alan Subin** | Design Engineer: mechanical design, CAD, assembly booklet | [LinkedIn](https://www.linkedin.com/in/alan-subin/) |
| **Boris Kotov** | Software and Test Engineer: prototypes, printing, test rigs | [Telegram](https://t.me/bkotov) |
| **Nikita Bragin** | Project Manager | [LinkedIn](https://www.linkedin.com/in/nikita-bragin-82296b29/) |
| **Mikhail Chistiakov** | Industrial Designer: look and form of the arm | [Telegram](https://t.me/brrryska) |
| **Mikhail Zhmaylo** | Structural Engineer: stiffness models, design changes to cut deflection | [Telegram](https://t.me/mikhail_zhmaylo) |
| **Vladislav Eremenko** | Structural Engineer: strength and thermal analysis, topology optimisation | [Telegram](https://t.me/v1ad_eremenko) |
| **Vladimir Osipov** | Tester and Consultant: independent test build | [LinkedIn](https://www.linkedin.com/in/vladimirosipov/) |

<div align="center">

**Built for the robotics community by [Robonine](https://robonine.com)** 🤖

</div>
