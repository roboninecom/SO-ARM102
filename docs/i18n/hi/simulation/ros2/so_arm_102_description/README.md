[English](../../../../en/simulation/ros2/so_arm_102_description/README.md) · [Русский](../../../../ru/simulation/ros2/so_arm_102_description/README.md) · [Español](../../../../es/simulation/ros2/so_arm_102_description/README.md) · [Français](../../../../fr/simulation/ros2/so_arm_102_description/README.md) · [Deutsch](../../../../de/simulation/ros2/so_arm_102_description/README.md) · [Português (Brasil)](../../../../pt-BR/simulation/ros2/so_arm_102_description/README.md) · [简体中文](../../../../zh-CN/simulation/ros2/so_arm_102_description/README.md) · [日本語](../../../../ja/simulation/ros2/so_arm_102_description/README.md) · [हिन्दी](README.md) · [العربية](../../../../ar/simulation/ros2/so_arm_102_description/README.md)

<!-- translated-content -->
# SO-ARM102 का ROS 2 डिस्क्रिप्शन पैकेज

यह पैकेज फॉलोअर आर्म की Xacro, URDF और मेश फ़ाइलें इंस्टॉल करता है और ROS 2 Jazzy के लिए RViz लॉन्च उपलब्ध कराता है। [Xacro / URDF](../../../../../../simulation/urdf/)

## बिल्ड और लॉन्च

ROS 2 Jazzy और `colcon` इंस्टॉल होने पर SO-ARM102 रिपॉज़िटरी की रूट डायरेक्टरी से ये कमांड चलाएँ:

```bash
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths simulation/ros2 --ignore-src -r -y
colcon build --base-paths simulation/ros2 --packages-select so_arm_102_description
source install/setup.bash
ros2 launch so_arm_102_description display.launch.py
```

पाँच आर्म जॉइंट के स्लाइडर और `clamp1` का स्लाइडर चलाएँ। दूसरी ग्रिपर जॉ URDF के mimic जॉइंट के ज़रिए उसका अनुसरण करती है। टक्कर के लिए इस्तेमाल होने वाले बॉक्स देखने के लिए RViz में **SO-ARM102** चुनें, **Collision Enabled** चालू करें और **Visual Enabled** बंद करें। सामान्य जॉइंट पोज़िशन और बिना स्लाइडर के RViz खोलने के लिए `gui:=false` दें।

अन्य पैकेज इंस्टॉल की गई share डायरेक्टरी में `urdf/so_arm_102.xacro` इस्तेमाल कर सकते हैं। ROS पैकेज इंडेक्स से मेश ढूँढने के लिए `mesh_prefix:=package://so_arm_102_description/urdf/meshes` सेट करें। अलग से चलाने पर डिफ़ॉल्ट प्रीफ़िक्स `meshes` है।
<!-- /translated-content -->
