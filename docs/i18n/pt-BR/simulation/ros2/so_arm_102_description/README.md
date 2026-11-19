[English](../../../../en/simulation/ros2/so_arm_102_description/README.md) · [Русский](../../../../ru/simulation/ros2/so_arm_102_description/README.md) · [Español](../../../../es/simulation/ros2/so_arm_102_description/README.md) · [Français](../../../../fr/simulation/ros2/so_arm_102_description/README.md) · [Deutsch](../../../../de/simulation/ros2/so_arm_102_description/README.md) · [Português (Brasil)](README.md) · [简体中文](../../../../zh-CN/simulation/ros2/so_arm_102_description/README.md) · [日本語](../../../../ja/simulation/ros2/so_arm_102_description/README.md) · [हिन्दी](../../../../hi/simulation/ros2/so_arm_102_description/README.md) · [العربية](../../../../ar/simulation/ros2/so_arm_102_description/README.md)

<!-- translated-content -->
# Descrição do SO-ARM102 para ROS 2

Este pacote instala o Xacro, o URDF e as malhas do braço seguidor e fornece um launch do RViz para ROS 2 Jazzy. [Xacro / URDF](../../../../../../simulation/urdf/)

## Compilar e executar

Execute os comandos na raiz do repositório SO-ARM102, com ROS 2 Jazzy e `colcon` instalados:

```bash
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths simulation/ros2 --ignore-src -r -y
colcon build --base-paths simulation/ros2 --packages-select so_arm_102_description
source install/setup.bash
ros2 launch so_arm_102_description display.launch.py
```

Mova os controles deslizantes das cinco juntas e o de `clamp1`. A outra mandíbula acompanha o movimento pela junta mimic do URDF. Para ver as caixas de colisão, selecione **SO-ARM102** no RViz, ative **Collision Enabled** e desative **Visual Enabled**. Use `gui:=false` para abrir o RViz com as posições padrão e sem os controles deslizantes.

Outros pacotes podem usar `urdf/so_arm_102.xacro` no diretório share instalado. Defina `mesh_prefix:=package://so_arm_102_description/urdf/meshes` para localizar as malhas pelo índice de pacotes do ROS. Para uso independente, o prefixo padrão continua sendo `meshes`.
<!-- /translated-content -->
