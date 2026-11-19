[English](../../../../en/simulation/ros2/so_arm_102_description/README.md) · [Русский](../../../../ru/simulation/ros2/so_arm_102_description/README.md) · [Español](../../../../es/simulation/ros2/so_arm_102_description/README.md) · [Français](README.md) · [Deutsch](../../../../de/simulation/ros2/so_arm_102_description/README.md) · [Português (Brasil)](../../../../pt-BR/simulation/ros2/so_arm_102_description/README.md) · [简体中文](../../../../zh-CN/simulation/ros2/so_arm_102_description/README.md) · [日本語](../../../../ja/simulation/ros2/so_arm_102_description/README.md) · [हिन्दी](../../../../hi/simulation/ros2/so_arm_102_description/README.md) · [العربية](../../../../ar/simulation/ros2/so_arm_102_description/README.md)

<!-- translated-content -->
# Description du SO-ARM102 pour ROS 2

Ce paquet installe le Xacro, l’URDF et les maillages du bras suiveur et fournit un fichier de lancement RViz pour ROS 2 Jazzy. [Xacro / URDF](../../../../../../simulation/urdf/)

## Compilation et lancement

Exécutez ces commandes à la racine du dépôt SO-ARM102 avec ROS 2 Jazzy et `colcon` installés :

```bash
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths simulation/ros2 --ignore-src -r -y
colcon build --base-paths simulation/ros2 --packages-select so_arm_102_description
source install/setup.bash
ros2 launch so_arm_102_description display.launch.py
```

Déplacez les curseurs des cinq articulations et celui de `clamp1`. L’autre mors suit son mouvement grâce à l’articulation mimic de l’URDF. Pour afficher les boîtes de collision, sélectionnez **SO-ARM102** dans RViz, activez **Collision Enabled** et désactivez **Visual Enabled**. Passez `gui:=false` pour ouvrir RViz avec les positions par défaut et sans curseurs.

Les autres paquets peuvent utiliser `urdf/so_arm_102.xacro` dans le répertoire share installé. Définissez `mesh_prefix:=package://so_arm_102_description/urdf/meshes` pour localiser les maillages via l’index des paquets ROS. Le préfixe par défaut est `meshes` pour une utilisation autonome.
<!-- /translated-content -->
