[English](../../../../en/simulation/ros2/so_arm_102_description/README.md) · [Русский](../../../../ru/simulation/ros2/so_arm_102_description/README.md) · [Español](../../../../es/simulation/ros2/so_arm_102_description/README.md) · [Français](../../../../fr/simulation/ros2/so_arm_102_description/README.md) · [Deutsch](../../../../de/simulation/ros2/so_arm_102_description/README.md) · [Português (Brasil)](../../../../pt-BR/simulation/ros2/so_arm_102_description/README.md) · [简体中文](../../../../zh-CN/simulation/ros2/so_arm_102_description/README.md) · [日本語](README.md) · [हिन्दी](../../../../hi/simulation/ros2/so_arm_102_description/README.md) · [العربية](../../../../ar/simulation/ros2/so_arm_102_description/README.md)

<!-- translated-content -->
# SO-ARM102 の ROS 2 記述パッケージ

このパッケージはフォロワーアームの Xacro、URDF、メッシュをインストールし、ROS 2 Jazzy 向けの RViz 起動ファイルを提供します。 [Xacro / URDF](../../../../../../simulation/urdf/)

## ビルドと起動

ROS 2 Jazzy と `colcon` をインストールし、SO-ARM102 リポジトリのルートで次を実行します。

```bash
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths simulation/ros2 --ignore-src -r -y
colcon build --base-paths simulation/ros2 --packages-select so_arm_102_description
source install/setup.bash
ros2 launch so_arm_102_description display.launch.py
```

アームの五つの関節と `clamp1` のスライダーを動かします。反対側の爪は URDF の mimic 関節を通じて追従します。衝突判定用のボックスを表示するには、RViz で **SO-ARM102** を選び、**Collision Enabled** を有効にして **Visual Enabled** を無効にします。`gui:=false` を指定すると、既定の関節位置でスライダーを表示せずに RViz が起動します。

他のパッケージは、インストール先の share ディレクトリにある `urdf/so_arm_102.xacro` を利用できます。`mesh_prefix:=package://so_arm_102_description/urdf/meshes` を指定すると、ROS のパッケージインデックスからメッシュを検索できます。単独で使う場合の既定の接頭辞は `meshes` です。
<!-- /translated-content -->
