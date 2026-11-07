<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](../../es/docs/specifications.md) · [Français](../../fr/docs/specifications.md) · [Deutsch](../../de/docs/specifications.md) · [Português (Brasil)](../../pt-BR/docs/specifications.md) · [简体中文](specifications.md) · [日本語](../../ja/docs/specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[英文原文](../../../specifications.md)

[文档](../README.md) · [打印](printing.md) · [物料清单](bom.md) · [装配](assembly-guide.md) · [规格](specifications.md) · [模型](../models/README.md) · [参与贡献](../CONTRIBUTING.md) · [许可说明](../LICENSING.md) · [翻译](translations.md)

> 本文为完整译文。各语言共用插图和原始 PDF 手册。翻译由人工智能辅助完成，尚未经母语使用者审校。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="specifications-and-test-results"></a>
# 规格与测试结果

8月和9月2026在 Robonine 原型上进行测量。 标记为 *计算 * 的数字来自 URDF 模型和伺服电机数据表,而非测量结果。

<a id="geometry"></a>
## 几何尺寸

| 关节 | 范围 |
|---|---|
| 底座旋转 | −176° … +176° (352°) |
| 肩部抬升 | −43° … +181° (224°) |
| 肘部屈伸 | −166° … +77° (243°) |
| 腕部屈伸 | −85° … +111° (196°) |
| 腕部旋转 | −165° … +163° (328°) |
| 夹爪 | 0 … 85 mm |

| 连杆 | 轴间距 |
|---|---|
| 基础旋转到肩膀 | 85 mm |
| 肩到肘 | 119 mm |
| 肘部至手腕弯曲 | 139 mm |
| 手腕弯曲到手腕滚动 | 62 mm |
| 腕部滚动到抓具尖端 | 132 mm |

| 伸展范围,夹具尖端中心 |  |
|---|---|
| 水平半径 | 483 mm |
| 基座底部以上的高度 | 至多 544 mm |
| 在底座底部下方,机器人臂在桌面边缘上 | 下降到 −301 mm |

从关节极限内的 100,000 个随机姿势中计算了距离,没有自我碰撞。

<a id="servos"></a>
## 舵机

| 关节 | 从臂 | 主臂 |
|---|---|---|
| 1 基础轮换 | STS3235 | STS3215 |
| 2 肩部提升 | STS3250 | STS3215 |
| 3 肘部弯曲 | STS3250 | STS3215 |
| 4 手腕弯曲 | STS3235 | STS3215 |
| 5 关于我们 | ST-3215-C049, 1:191 | STS3215 |
| 6 抓具/触发器 | ST-3215-C049, 1:191 | STS3215 |
| 供电 | 12 V | 5 V |

<a id="gripper"></a>
## 夹爪

| | |
|---|---|
| 类型 | 平行,齿轮箱和小齿轮,两个移动颚 |
| 开口宽度 | 85 mm |
| 箱子,建议最大宽度 | 关于 75 mm |
| 气缸,推荐最大直径 | 关于 70 mm |
| 球形,推荐最大直径 | 关于 60 mm |
| 相机 | 安装在抓具上的 USB 摄像头 |

<a id="measured-results-against-so-arm-101"></a>
## 对 SO-ARM 101 的测量结果

| 指标 | SO-ARM 101 | SO-ARM 102 | 变化 |
|---|---|---|---|
| 抓具尖端的偏转,300 g,机器人臂完全伸出 ¹ | 7.5 mm | 3.4 mm | −55 % |
| 同样,所有链接的填充率为 100 % ¹ | — | 2.34 mm | −69 % |
| 水平半径 | 441 mm | 483 mm | +9.5 % |
| 底座后方臂展 | 377 mm | 473 mm | +25.5 % |
| 底座旋转范围 | 220° | 352° | +60 % |
| 肘部范围 | 194° | 243° | +25 % |
| 肩膀和肘部无负载速度, *计算 * | 270 °/s | 450 °/s | +67 % |
| 底座关节间隙 | 8.75 计数 | 5.00 计数 | −43 % |
| 从底座回弹的水平尖端误差,*计算 * | ±2.96 mm | ±1.85 mm | −37.5 % |
| 重复性 | — | 关于 0.1 mm |  |
| 1 米处的噪音 | 70 dB | 60 dB | −10 dB |
| 额定负载 | 150 g | 300 g |  |

¹ 两个机械臂的关节 2、3 和 4 均使用打印的舵机占位件，因此仅比较框架。SO-ARM 101 使用 PLA 打印，SO-ARM 102 使用 Fiberon PET-CF17 打印，填充率均为 25 %。同一 SO-ARM 102 测试的第二次测量结果为 3.9 mm。

| SO-ARM 101 | SO-ARM 102 |
|:-:|:-:|
| ![SO-ARM 101 刚度测试](../../../../assets/images/tests/stiffness-so-arm-101.jpg) | ![SO-ARM 102 刚度测试](../../../../assets/images/tests/stiffness-so-arm-102.jpg) |

<a id="current-and-temperature-follower"></a>
## 电流和温度,跟踪机器人臂

在重复轨迹上的 300 g 负载、环境条件 30 °C 和六台 STS3250 伺服电机下进行测量。

| | |
|---|---|
| 平均电流 | 1.26 A |
| 峰值电流 | 3.28 A |
| 舵机最高温度 | 46 °C |

<a id="absolute-accuracy"></a>
## 绝对精度

仍在调试中。使用舵机出厂 PID 设置时，机械臂完全伸展后，末端在机械臂自身重量作用下下垂约 50 mm。调整 PID 后，下垂量降至约 5 mm。专门的精度测试方案正在准备中。
<!-- /translated-content -->
