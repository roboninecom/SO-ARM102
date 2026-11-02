# 3D models

<!-- documentation-languages -->
[English](../docs/i18n/en/models/README.md) · [Русский](../docs/i18n/ru/models/README.md) · [Español](../docs/i18n/es/models/README.md) · [Français](../docs/i18n/fr/models/README.md) · [Deutsch](../docs/i18n/de/models/README.md) · [Português (Brasil)](../docs/i18n/pt-BR/models/README.md) · [简体中文](../docs/i18n/zh-CN/models/README.md) · [日本語](../docs/i18n/ja/models/README.md) · [हिन्दी](../docs/i18n/hi/models/README.md) · [العربية](../docs/i18n/ar/models/README.md)
<!-- /documentation-languages -->

| Folder | Content |
|---|---|
| `3mf/` | Bambu Studio projects with saved plate layouts, orientation and support settings |
| `stl/` | Print-ready meshes, binary STL, millimetres |
| `step/` | CAD parts and assemblies |

The `stl/` and `step/` folders use the same split:

- `common/` — Shared parts, including controller cases.
- `follower/` — Parallel gripper and camera mount.
- `leader/` — Handle, trigger and wrist roll.

## [3MF slicer projects](3mf)

| Project | Contents | Saved filament profile |
|---|---|---|
| Follower table 1 | Follower arm links and base holder | Fiberon PET-CF17 |
| Follower table 2 | Follower gripper and base parts | Bambu PETG-CF |
| Leader table | Full leader arm | Bambu PLA+ |
| Aruco cube | Aruco cube parts | Bambu PLA |
| Colored figures | Figures of 3 colors and 4 types  | Bambu PLA |

Open these files as projects in **Bambu Studio** to retain the saved settings.
All three use the **Bambu Lab A1, 0.4 mm nozzle** profile and one **256 × 256 mm** plate each.
Select your printer, nozzle and filament before slicing. For a smaller bed, split the parts
across additional plates while preserving their orientations and support settings.

For one leader + one follower print all three projects once.

Saved settings, layout previews, part numbers, quantities and print settings are in [docs/printing.md](../docs/printing.md).

## Test plate for Gripper Rods

![Gripper rods test plate](../assets/images/3d%20print/rod-test-plate.png)

To make your Follower Gripper move smooth you need to fit Clamps hole sizes with diameter of Rods. For this purpose at first you have to print the [test plate](../models/stl/test/Gripper%20rods%20test%20plate%20D6.0-D6.2.STL) with the same material and settings as the Clamps (PETG-CF). Then try to insert 6 mm rod into the 6.0–6.2 mm holes starting from largest to smallest ones; choose hole with a smooth fit with minimal play. This will be your choice for next step. After this test you should print one of 3 versions of **Follower table 2** 3mf files - with ending **D6.0**, **D6.1** or **D6.2** in file name.
