[English](README.md) · [Русский](../../../../ru/simulation/ros2/so_arm_102_description/README.md) · [Español](../../../../es/simulation/ros2/so_arm_102_description/README.md) · [Français](../../../../fr/simulation/ros2/so_arm_102_description/README.md) · [Deutsch](../../../../de/simulation/ros2/so_arm_102_description/README.md) · [Português (Brasil)](../../../../pt-BR/simulation/ros2/so_arm_102_description/README.md) · [简体中文](../../../../zh-CN/simulation/ros2/so_arm_102_description/README.md) · [日本語](../../../../ja/simulation/ros2/so_arm_102_description/README.md) · [हिन्दी](../../../../hi/simulation/ros2/so_arm_102_description/README.md) · [العربية](../../../../ar/simulation/ros2/so_arm_102_description/README.md)

<!-- translated-content -->
# SO-ARM102 ROS 2 description

This package installs the follower's [Xacro, URDF and meshes](../../../../../../simulation/urdf/) and provides an RViz launch for ROS 2 Jazzy.

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
<!-- /translated-content -->
