# SO-ARM102 ROS 2 description

<!-- documentation-languages -->
[English](../../../docs/i18n/en/simulation/ros2/so_arm_102_description/README.md) · [Русский](../../../docs/i18n/ru/simulation/ros2/so_arm_102_description/README.md) · [Español](../../../docs/i18n/es/simulation/ros2/so_arm_102_description/README.md) · [Français](../../../docs/i18n/fr/simulation/ros2/so_arm_102_description/README.md) · [Deutsch](../../../docs/i18n/de/simulation/ros2/so_arm_102_description/README.md) · [Português (Brasil)](../../../docs/i18n/pt-BR/simulation/ros2/so_arm_102_description/README.md) · [简体中文](../../../docs/i18n/zh-CN/simulation/ros2/so_arm_102_description/README.md) · [日本語](../../../docs/i18n/ja/simulation/ros2/so_arm_102_description/README.md) · [हिन्दी](../../../docs/i18n/hi/simulation/ros2/so_arm_102_description/README.md) · [العربية](../../../docs/i18n/ar/simulation/ros2/so_arm_102_description/README.md)
<!-- /documentation-languages -->

This package installs the follower's [Xacro, URDF and meshes](../../urdf/) and provides an RViz launch for ROS 2 Jazzy.

## Build and launch

Run from the root of the SO-ARM102 checkout, with ROS 2 Jazzy and `colcon` installed:

```bash
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths simulation/ros2 --ignore-src -r -y
colcon build --base-paths simulation/ros2 --packages-select so_arm_102_description
source install/setup.bash
ros2 launch so_arm_102_description display.launch.py
```

Move the five arm sliders and the `clamp1` slider. The other jaw follows it through the URDF mimic joint. To check the fitted collision boxes, select **SO-ARM102** in RViz and enable **Collision Enabled** and disable **Visual Enabled**. Pass `gui:=false` to open RViz with the default joint positions and no sliders.

Downstream packages can use the installed Xacro at `urdf/so_arm_102.xacro` in this package's share directory. Set `mesh_prefix:=package://so_arm_102_description/urdf/meshes` to resolve the visuals through the ROS package index. The default prefix remains `meshes` for standalone use.
