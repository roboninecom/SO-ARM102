[English](../../../../en/simulation/ros2/so_arm_102_description/README.md) · [Русский](../../../../ru/simulation/ros2/so_arm_102_description/README.md) · [Español](../../../../es/simulation/ros2/so_arm_102_description/README.md) · [Français](../../../../fr/simulation/ros2/so_arm_102_description/README.md) · [Deutsch](../../../../de/simulation/ros2/so_arm_102_description/README.md) · [Português (Brasil)](../../../../pt-BR/simulation/ros2/so_arm_102_description/README.md) · [简体中文](../../../../zh-CN/simulation/ros2/so_arm_102_description/README.md) · [日本語](../../../../ja/simulation/ros2/so_arm_102_description/README.md) · [हिन्दी](../../../../hi/simulation/ros2/so_arm_102_description/README.md) · [العربية](README.md)

<!-- translated-content -->
# وصف SO-ARM102 لنظام ROS 2

تثبّت هذه الحزمة ملفات Xacro وURDF والشبكات الهندسية للذراع التابع، وتوفّر ملف تشغيل RViz لنظام ROS 2 Jazzy. [Xacro / URDF](../../../../../../simulation/urdf/)

## البناء والتشغيل

نفّذ الأوامر التالية من المجلد الجذر لمستودع SO-ARM102 بعد تثبيت ROS 2 Jazzy و`colcon`:

```bash
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths simulation/ros2 --ignore-src -r -y
colcon build --base-paths simulation/ros2 --packages-select so_arm_102_description
source install/setup.bash
ros2 launch so_arm_102_description display.launch.py
```

حرّك منزلقات مفاصل الذراع الخمسة ومنزلق `clamp1`. يتبع الفك الآخر حركته عبر مفصل mimic في URDF. لعرض صناديق التصادم، اختر **SO-ARM102** في RViz وفعّل **Collision Enabled** وعطّل **Visual Enabled**. استخدم `gui:=false` لفتح RViz بمواضع المفاصل الافتراضية ومن دون منزلقات.

يمكن للحزم الأخرى استخدام `urdf/so_arm_102.xacro` من مجلد share المثبّت. اضبط `mesh_prefix:=package://so_arm_102_description/urdf/meshes` للعثور على الشبكات عبر فهرس حزم ROS. البادئة الافتراضية للاستخدام المستقل هي `meshes`.
<!-- /translated-content -->
