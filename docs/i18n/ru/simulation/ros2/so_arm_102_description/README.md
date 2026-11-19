[English](../../../../en/simulation/ros2/so_arm_102_description/README.md) · [Русский](README.md) · [Español](../../../../es/simulation/ros2/so_arm_102_description/README.md) · [Français](../../../../fr/simulation/ros2/so_arm_102_description/README.md) · [Deutsch](../../../../de/simulation/ros2/so_arm_102_description/README.md) · [Português (Brasil)](../../../../pt-BR/simulation/ros2/so_arm_102_description/README.md) · [简体中文](../../../../zh-CN/simulation/ros2/so_arm_102_description/README.md) · [日本語](../../../../ja/simulation/ros2/so_arm_102_description/README.md) · [हिन्दी](../../../../hi/simulation/ros2/so_arm_102_description/README.md) · [العربية](../../../../ar/simulation/ros2/so_arm_102_description/README.md)

<!-- translated-content -->
# Описание SO-ARM102 для ROS 2

Этот пакет устанавливает Xacro, URDF и сетки ведомого манипулятора и добавляет запуск RViz для ROS 2 Jazzy. [Xacro / URDF](../../../../../../simulation/urdf/)

## Сборка и запуск

Запустите команды из корня репозитория SO-ARM102 с установленными ROS 2 Jazzy и `colcon`:

```bash
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths simulation/ros2 --ignore-src -r -y
colcon build --base-paths simulation/ros2 --packages-select so_arm_102_description
source install/setup.bash
ros2 launch so_arm_102_description display.launch.py
```

Перемещайте ползунки пяти суставов и ползунок `clamp1`. Вторая губка следует за первой через связанный сустав URDF. Для просмотра коллизионных боксов выберите **SO-ARM102** в RViz, включите **Collision Enabled** и выключите **Visual Enabled**. Параметр `gui:=false` запускает RViz без ползунков с начальными положениями суставов.

Другие пакеты могут использовать установленный файл `urdf/so_arm_102.xacro` в каталоге share этого пакета. Установите `mesh_prefix:=package://so_arm_102_description/urdf/meshes`, чтобы искать сетки через индекс пакетов ROS. Для автономного использования префикс по умолчанию — `meshes`.
<!-- /translated-content -->
