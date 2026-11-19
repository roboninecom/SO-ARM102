[English](../../../../en/simulation/ros2/so_arm_102_description/README.md) · [Русский](../../../../ru/simulation/ros2/so_arm_102_description/README.md) · [Español](README.md) · [Français](../../../../fr/simulation/ros2/so_arm_102_description/README.md) · [Deutsch](../../../../de/simulation/ros2/so_arm_102_description/README.md) · [Português (Brasil)](../../../../pt-BR/simulation/ros2/so_arm_102_description/README.md) · [简体中文](../../../../zh-CN/simulation/ros2/so_arm_102_description/README.md) · [日本語](../../../../ja/simulation/ros2/so_arm_102_description/README.md) · [हिन्दी](../../../../hi/simulation/ros2/so_arm_102_description/README.md) · [العربية](../../../../ar/simulation/ros2/so_arm_102_description/README.md)

<!-- translated-content -->
# Descripción del SO-ARM102 para ROS 2

Este paquete instala el Xacro, el URDF y las mallas del brazo seguidor y añade un archivo de lanzamiento de RViz para ROS 2 Jazzy. [Xacro / URDF](../../../../../../simulation/urdf/)

## Compilación y lanzamiento

Ejecuta estos comandos desde la raíz del repositorio SO-ARM102, con ROS 2 Jazzy y `colcon` instalados:

```bash
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths simulation/ros2 --ignore-src -r -y
colcon build --base-paths simulation/ros2 --packages-select so_arm_102_description
source install/setup.bash
ros2 launch so_arm_102_description display.launch.py
```

Mueve los deslizadores de las cinco articulaciones y el de `clamp1`. La otra mordaza sigue el movimiento mediante la articulación mimic de URDF. Para ver las cajas de colisión, selecciona **SO-ARM102** en RViz, activa **Collision Enabled** y desactiva **Visual Enabled**. Usa `gui:=false` para abrir RViz con las posiciones predeterminadas y sin deslizadores.

Otros paquetes pueden usar `urdf/so_arm_102.xacro` en el directorio share instalado. Configura `mesh_prefix:=package://so_arm_102_description/urdf/meshes` para localizar las mallas mediante el índice de paquetes de ROS. Para uso independiente, el prefijo predeterminado es `meshes`.
<!-- /translated-content -->
