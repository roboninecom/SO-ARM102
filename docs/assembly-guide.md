# Assembly guide

<!-- documentation-languages -->
[English](i18n/en/docs/assembly-guide.md) · [Русский](i18n/ru/docs/assembly-guide.md) · [Español](i18n/es/docs/assembly-guide.md) · [Français](i18n/fr/docs/assembly-guide.md) · [Deutsch](i18n/de/docs/assembly-guide.md) · [Português (Brasil)](i18n/pt-BR/docs/assembly-guide.md) · [简体中文](i18n/zh-CN/docs/assembly-guide.md) · [日本語](i18n/ja/docs/assembly-guide.md) · [हिन्दी](i18n/hi/docs/assembly-guide.md) · [العربية](i18n/ar/docs/assembly-guide.md)
<!-- /documentation-languages -->

This guide follows the printed booklet
[SO-ARM102_assembly_A5_v0.7.pdf](SO-ARM102_assembly_A5_v0.7.pdf) page by page.
Print the booklet on A5 landscape if you prefer paper.

Before you start:

- Print all parts from [printing.md](printing.md) and collect the hardware from [bom.md](bom.md).
- You need hex keys 1.5 mm (M2) and 2 mm (M3).
- Read two steps ahead before tightening anything. Two places in the current order are awkward, see [Known issues](../README.md#-known-issues).

> ⚠️ **The leader runs on 5 V, the follower on 12 V.** Keep the power supplies apart.

Use a removable threadlocker compatible with the printed plastic, e.g. [Vibra-Tite VC-3](https://www.vibra-tite.com/faq/if-vc-3-has-mek-how-can-it-be-plastic-compatible/). Apply VC-3 to metal screw threads and let it dry fully before assembly (at least 30 minutes per its [technical data sheet](https://www.vibra-tite.com/wp-content/uploads/213_tds.pdf)); do not apply it wet to plastic. Confirm compatibility with your filament on a spare print first.

![Tools and voltage warning](../assets/images/assembly/tools-and-voltage.jpg)

## Order of work

### Reading the illustrations

Beige highlights mark new parts; grey parts are already assembled. The part thumbnail
and quantity show what to add. The numbered circle is the assembly step; the dots show
progress. Part numbers, fastener sizes and servo IDs are the same in every language.

### Assembly sequence

1. Mount the horns on the servos.
2. Build the arm body **twice**, once for the follower and once for the leader (steps 1–13). Steps 12–13 fit a Bus Servo Adapter on each arm.
3. Build the parallel gripper (gripper steps 1–6).
4. Finish the follower: camera holder, gripper, camera (follower steps 1–3).
5. Finish the leader: handle and trigger (leader steps 1–2).

## Servo IDs

Set each servo ID before it goes into the arm. Tools for setting IDs and calibrating are at
[lab.robonine.com](https://lab.robonine.com).

![Servo IDs](../assets/images/assembly/servo-ids.jpg)

| ID | Joint | Follower servo | Leader servo |
|:-:|---|---|---|
| 1 | Base rotation | STS3235 | STS3215 |
| 2 | Shoulder lift | STS3250 | STS3215 |
| 3 | Elbow flex | STS3250 | STS3215 |
| 4 | Wrist flex | STS3235 | STS3215 |
| 5 | Wrist roll | STS3215 | STS3215 |
| 6 | Gripper / trigger | STS3215 | STS3215 |

## 0. Servo horns

Mount one horn with an M3 × 6 screw on servo ID 1.
Servos ID 2, 3 and 4 get a horn on both sides. Horn screws come with the servos.

If you add O-rings to the leader, put them between the servo and the horn now. Getting this order wrong can jam the ring between the servo shell and the horn.

## 1–13. Arm body, follower and leader

Repeat these steps for both arms. Printed part names match [printing.md](printing.md).

| Step | Parts | Fasteners |
|:-:|---|---|
| 1 | SO102.02.060 Bottom servo holder, SO102.02.040 Bottom top plate | 3 × M3×16, 3 × M3 nut |
| 2 | — | 3 × M3×16, 3 × M3 nut |
| 3 | Servo ID 1 | 4 × M2×6 |
| 4 | SO102.02.020 Base ring, bearing 6812, SO102.02.050 Bottom ring, SO102.02.010 Base | 6 × M3 nut, 6 × M3×16 |
| 5 | SO102.02.030 Base washer | 4 × M3×10, 6 × M3×16 |
| 6 | Servos ID 2 and ID 3, 2 × SO102.02.070 Bottom arm, 2 × Short Wire, 1 × Long Wire | 16 × M2×6 |
| 7 | Servo ID 4, SO102.02.080-01 Upper arm right, 1 × Short Wire | 4 × M2×6 |
| 8 | SO102.02.080 Upper arm left, 2 × SO102.02.130 Cable snap | 4 × M2×6, 8 × M3×10 |
| 9 | Servo ID 5, SO102.02.090 Wrist holder, servo horn | 1 × M3×6, 4 × 2×6 self-tapping |
| 10 | 1 × Short Wire | 8 × M3×10 |
| 11 | — | 8 × M3×10 |
| 12 | SO102.02.110 Board holder leader, Bus Servo Adapter | 4 × M2 nut, 4 × M2×8 |
| 13 | SO102.02.110-01 Board cap leader, 1 × Long Wire | — |

| | | |
|:-:|:-:|:-:|
| ![Step 1](../assets/images/assembly/steps/shared-01.jpg) | ![Step 2](../assets/images/assembly/steps/shared-02.jpg) | ![Step 3](../assets/images/assembly/steps/shared-03.jpg) |
| ![Step 4](../assets/images/assembly/steps/shared-04.jpg) | ![Step 5](../assets/images/assembly/steps/shared-05.jpg) | ![Step 6](../assets/images/assembly/steps/shared-06.jpg) |
| ![Step 7](../assets/images/assembly/steps/shared-07.jpg) | ![Step 8](../assets/images/assembly/steps/shared-08.jpg) | ![Step 9](../assets/images/assembly/steps/shared-09.jpg) |
| ![Step 10](../assets/images/assembly/steps/shared-10.jpg) | ![Step 11](../assets/images/assembly/steps/shared-11.jpg) | ![Step 12](../assets/images/assembly/steps/shared-12.jpg) |
| ![Step 13](../assets/images/assembly/steps/shared-13.jpg) | | |

Check that each servo cable reaches the next joint with some slack before you close the joint.

## Gripper 1–6, follower only

| Step | Parts | Fasteners |
|:-:|---|---|
| 1 | RB9.01.062.040 Gear for gripper on the servo horn, servo ID 6 | 4 × M3×4 set screw, 1 × M3×6 |
| 2 | 2 × RB9.01.062.025 Clamp (D6.1), 2 × RB9.01.062.030 Gear rack, 2 × RB9.01.062.100 Nail | — |
| 3 | 2 × rod Ø6 × 125 mm | — |
| 4 | RB9.01.062.012 Main frame (D6.1), 2 × bearing MF106, 2 × RB9.01.062.050 Washer | 2 × M3×10 |
| 5 | Click the rods into the main frame | — |
| 6 | Push the clamps to their outer stops, insert the servo | 3 × 2×6 self-tapping |

The ×2 on step 2 is one jaw assembly for each side. The quantities in the table are the total.
Tighten the set screws from the horn side towards the gear, so no gap opens between them.
Before step 6, move servo ID 6 to its minimum position, so the gripper closes fully and opens to the full 85 mm.
Slide both clamps along the rods by hand before closing up. They should move freely without binding.

| | | |
|:-:|:-:|:-:|
| ![Gripper 1](../assets/images/assembly/steps/gripper-01.jpg) | ![Gripper 2](../assets/images/assembly/steps/gripper-02.jpg) | ![Gripper 3](../assets/images/assembly/steps/gripper-03.jpg) |
| ![Gripper 4](../assets/images/assembly/steps/gripper-04.jpg) | ![Gripper 5](../assets/images/assembly/steps/gripper-05.jpg) | ![Gripper 6](../assets/images/assembly/steps/gripper-06.jpg) |

## Follower 1–3

| Step | Parts | Fasteners |
|:-:|---|---|
| 1 | RB9.01.062.075 Camera holder | 4 × M3×10 |
| 2 | Gripper assembly onto the wrist | 4 × 2×6 self-tapping |
| 3 | RB9.01.062.090 Camera spacer, USB camera | 4 × M2×8, 4 × M2 nut |

| | | |
|:-:|:-:|:-:|
| ![Follower 1](../assets/images/assembly/steps/follower-01.jpg) | ![Follower 2](../assets/images/assembly/steps/follower-02.jpg) | ![Follower 3](../assets/images/assembly/steps/follower-03.jpg) |

## Leader 1–2

| Step | Parts | Fasteners |
|:-:|---|---|
| 1 | SO102 Handle, SO102 Wrist roll | 4 × M3×6, 1 × 2×6 self-tapping |
| 2 | SO102 Trigger, servo ID 6 | 4 × M3×6, 4 × 2×6 self-tapping |

| | |
|:-:|:-:|
| ![Leader 1](../assets/images/assembly/steps/leader-01.jpg) | ![Leader 2](../assets/images/assembly/steps/leader-02.jpg) |

## Mounting and first start

1. Clamp each base to the table with two C-clamps.
2. Connect the follower controller to the 12 V supply and the leader controller to the 5 V supply.
3. Connect both controllers to the computer with USB-C.
4. Calibrate both arms and start teleoperation at [lab.robonine.com](https://lab.robonine.com), or with the LeRobot SO-101 workflow.
