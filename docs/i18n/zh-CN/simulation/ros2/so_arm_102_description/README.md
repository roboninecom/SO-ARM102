[English](../../../../en/simulation/ros2/so_arm_102_description/README.md) · [Русский](../../../../ru/simulation/ros2/so_arm_102_description/README.md) · [Español](../../../../es/simulation/ros2/so_arm_102_description/README.md) · [Français](../../../../fr/simulation/ros2/so_arm_102_description/README.md) · [Deutsch](../../../../de/simulation/ros2/so_arm_102_description/README.md) · [Português (Brasil)](../../../../pt-BR/simulation/ros2/so_arm_102_description/README.md) · [简体中文](README.md) · [日本語](../../../../ja/simulation/ros2/so_arm_102_description/README.md) · [हिन्दी](../../../../hi/simulation/ros2/so_arm_102_description/README.md) · [العربية](../../../../ar/simulation/ros2/so_arm_102_description/README.md)

<!-- translated-content -->
# SO-ARM102 的 ROS 2 描述包

本软件包安装从臂的 Xacro、URDF 和网格，并为 ROS 2 Jazzy 提供 RViz 启动文件。 [Xacro / URDF](../../../../../../simulation/urdf/)

## 构建和启动

安装 ROS 2 Jazzy 和 `colcon` 后，在 SO-ARM102 仓库根目录运行以下命令：

```bash
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths simulation/ros2 --ignore-src -r -y
colcon build --base-paths simulation/ros2 --packages-select so_arm_102_description
source install/setup.bash
ros2 launch so_arm_102_description display.launch.py
```

拖动五个手臂关节的滑块和 `clamp1` 滑块。另一侧夹爪通过 URDF 的 mimic 关节随动。要查看碰撞盒，在 RViz 中选择 **SO-ARM102**，启用 **Collision Enabled** 并关闭 **Visual Enabled**。使用 `gui:=false` 可在默认关节位置下打开 RViz，且不显示滑块。

其他软件包可以使用已安装的 share 目录中的 `urdf/so_arm_102.xacro`。将 `mesh_prefix:=package://so_arm_102_description/urdf/meshes` 作为参数，即可通过 ROS 软件包索引查找网格。独立使用时，默认前缀仍为 `meshes`。
<!-- /translated-content -->
