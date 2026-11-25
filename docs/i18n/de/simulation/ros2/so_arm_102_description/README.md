[English](../../../../en/simulation/ros2/so_arm_102_description/README.md) · [Русский](../../../../ru/simulation/ros2/so_arm_102_description/README.md) · [Español](../../../../es/simulation/ros2/so_arm_102_description/README.md) · [Français](../../../../fr/simulation/ros2/so_arm_102_description/README.md) · [Deutsch](README.md) · [Português (Brasil)](../../../../pt-BR/simulation/ros2/so_arm_102_description/README.md) · [简体中文](../../../../zh-CN/simulation/ros2/so_arm_102_description/README.md) · [日本語](../../../../ja/simulation/ros2/so_arm_102_description/README.md) · [हिन्दी](../../../../hi/simulation/ros2/so_arm_102_description/README.md) · [العربية](../../../../ar/simulation/ros2/so_arm_102_description/README.md)

<!-- translated-content -->
# Beschreibung des SO-ARM102 für ROS 2

Dieses Paket installiert Xacro, URDF und Meshes des Folgearms und stellt einen RViz-Start für ROS 2 Jazzy bereit. [Xacro / URDF](../../../../../../simulation/urdf/)

## Bauen und starten

Führe die Befehle im Stammverzeichnis des SO-ARM102-Repositories mit installiertem ROS 2 Jazzy und `colcon` aus:

```bash
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths simulation/ros2 --ignore-src -r -y
colcon build --base-paths simulation/ros2 --packages-select so_arm_102_description
source install/setup.bash
ros2 launch so_arm_102_description display.launch.py
```

Bewege die Schieberegler der fünf Armgelenke und von `clamp1`. Die andere Greiferbacke folgt über das Mimic-Gelenk im URDF. Wähle für die Kollisionsquader in RViz **SO-ARM102**, aktiviere **Collision Enabled** und deaktiviere **Visual Enabled**. Mit `gui:=false` startet RViz mit den Standardpositionen und ohne Schieberegler.

Andere Pakete können `urdf/so_arm_102.xacro` im installierten Share-Verzeichnis verwenden. Setze `mesh_prefix:=package://so_arm_102_description/urdf/meshes`, um die Meshes über den ROS-Paketindex zu finden. Für die eigenständige Verwendung bleibt `meshes` das Standardpräfix.
<!-- /translated-content -->
