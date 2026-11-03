<!-- translation-navigation -->
[English](../../en/docs/assembly-guide.md) · [Русский](../../ru/docs/assembly-guide.md) · [Español](../../es/docs/assembly-guide.md) · [Français](../../fr/docs/assembly-guide.md) · [Deutsch](../../de/docs/assembly-guide.md) · [Português (Brasil)](../../pt-BR/docs/assembly-guide.md) · [简体中文](assembly-guide.md) · [日本語](../../ja/docs/assembly-guide.md) · [हिन्दी](../../hi/docs/assembly-guide.md) · [العربية](../../ar/docs/assembly-guide.md)

[英文原文](../../../assembly-guide.md)

[文档](../README.md) · [打印](printing.md) · [物料清单](bom.md) · [装配](assembly-guide.md) · [规格](specifications.md) · [模型](../models/README.md) · [参与贡献](../CONTRIBUTING.md) · [许可说明](../LICENSING.md) · [翻译](translations.md)

> 本文为完整译文。各语言共用插图和原始 PDF 手册。翻译由人工智能辅助完成，尚未经母语使用者审校。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="assembly-guide"></a>
# 装配指南

本指南按照印刷的小册子[SO-ARM102_assembly_A5_v0.7.pdf ](../../../SO-ARM102_assembly_A5_v0.7.pdf)逐页进行说明。 如果您喜欢纸张,可以将小册子以横向 A5 格式打印出来。

开始之前：

- 从 [printing.md ](printing.md) 打印所有部件,并从 [bom.md ](bom.md) 收集硬件。
- 您需要六进制密钥 1.5 mm (M2) 和 2 mm (M3) 。
- 当前顺序中有两个位置很尴尬,请参阅 [已知问题 ](../README.md#-known-issues) 。

> ⚠️ **主臂使用 5 V 电源，从臂使用 12 V 电源。** 请将两种电源分开放置。

使用与打印塑料兼容的可拆卸螺纹锁固剂，例如 [Vibra-Tite VC-3](https://www.vibra-tite.com/faq/if-vc-3-has-mek-how-can-it-be-plastic-compatible/)。将 VC-3 涂在金属螺钉的螺纹上，完全干燥后再组装（按[技术资料](https://www.vibra-tite.com/wp-content/uploads/213_tds.pdf)至少等待 30 分钟）；不要将未干的锁固剂涂在塑料上。先用同种耗材的试打印件验证兼容性。

![工具和电压警告](../../../../assets/images/assembly/tools-and-voltage.jpg)

<a id="order-of-work"></a>
## 操作顺序

<a id="reading-the-illustrations"></a>
### 阅读插图

米色高亮显示新零件;灰色部件已装配。 零件缩略图和数量显示需要添加的零件。 编号圆圈表示装配步骤,点表示进度。

<a id="assembly-sequence"></a>
### 組裝序列

1. 安装喇叭在伺服电机上。
2. 建造机器人臂体 **两次 **,一次用于跟随机器人臂,一次用于领导机器人臂(步骤 1–13 ) 。 步骤 12–13 为每只机械臂安装一个 Bus Servo Adapter。
3. 构建平行抓具(抓具步骤 1 – 6 ) 。
4. 完成从臂：相机支架、夹爪和相机（从臂步骤 1–3）。
5. 完成主臂：手柄和扳机（主臂步骤 1–2）。

<a id="servo-ids"></a>
## 舵机 ID

在每个伺服电机进入机器人臂之前设置其 ID。 用于设置 ID 和校准的工具可在 [lab.robonine.com ](https://lab.robonine.com) 中找到。

![舵机 ID 分配](../../../../assets/images/assembly/servo-ids.jpg)

| ID | 关节 | 从臂舵机 | 主臂舵机 |
|:-:|---|---|---|
| 1 | 底座旋转 | STS3235 | STS3215 |
| 2 | 肩部抬升 | STS3250 | STS3215 |
| 3 | 肘部屈伸 | STS3250 | STS3215 |
| 4 | 腕部屈伸 | STS3235 | STS3215 |
| 5 | 腕部旋转 | STS3215 | STS3215 |
| 6 | 夹爪 / 扳机 | STS3215 | STS3215 |

<a id="0-servo-horns"></a>
## 0. 伺服喇叭

在伺服电机 ID 1 上用 M3 × 6 螺丝安装一个喇叭。 伺服 ID 2、3 和 4 两侧都有喇叭。 喇叭螺丝与伺服电机一起提供。

如果在机器人手臂上加上O型圈,那么现在就把它们放在伺服电机和喇叭之间。 错误的顺序会导致伺服电机壳体和喇叭之间的O型圈堵塞。

<a id="111-arm-body-follower-and-leader"></a>
<a id="113-arm-body-follower-and-leader"></a>
## 1–13 。 机械臂主体、跟随机器人手臂和领导机器人手臂

为两个机器人臂重复这些步骤。 打印零件名称与 [printing.md](printing.md) 一致。

| 步骤 | 零件 | 紧固件 |
|:-:|---|---|
| 1 | SO102.02.060 底部伺服电机支架, SO102.02.040 底部顶板 | 3×M3×16、3×M3螺母 |
| 2 | — | 3×M3×16、3×M3螺母 |
| 3 | 服务器ID 1 | 4 × M2×6 |
| 4 | SO102.02.020 底环,轴承 6812 , SO102.02.050 底环,SO102.02.010 基座 | 6×M3×16、6×M3螺母 |
| 5 | SO102.02.030 基础垫圈 | 4 × M3×10, 6 × M3×16 |
| 6 | 伺服器 ID 2 和 ID 3, 2 × SO102.02.070 底部机器人臂, 2 短电缆, 1 长电缆 | 16 × M2×6 |
| 7 | 伺服 ID 4 , SO102.02.080-01 右上机器人臂,1 短线 | 4 × M2×6 |
| 8 | SO102.02.080 左侧上部机器人臂,2 × SO102.02.130 电缆紧固件 | 4 × M2×6, 8 × M3×10 |
| 9 | 伺服 ID 5 , SO102.02.090 手腕支架,伺服电机喇叭 | 1 × 数目 M3×6, 4 × 数目 2× 数目6 自攻螺栓 |
| 10 | 1 短线缆 | 8 × M3×10 |
| 11 | — | 8 × M3×10 |
| 12 | SO102.02.110 主臂控制板支架, Bus Servo Adapter | 4 × M2 螺母, 4 × M2×8 |
| 13 | SO102.02.110-01 主臂控制板盖, 1 × 长线 | — |

| | | |
|:-:|:-:|:-:|
| ![步骤 1](../../../../assets/images/assembly/steps/shared-01.jpg) | ![步骤 2](../../../../assets/images/assembly/steps/shared-02.jpg) | ![步骤 3](../../../../assets/images/assembly/steps/shared-03.jpg) |
| ![步骤 4](../../../../assets/images/assembly/steps/shared-04.jpg) | ![步骤 5](../../../../assets/images/assembly/steps/shared-05.jpg) | ![步骤 6](../../../../assets/images/assembly/steps/shared-06.jpg) |
| ![步骤 7](../../../../assets/images/assembly/steps/shared-07.jpg) | ![步骤 8](../../../../assets/images/assembly/steps/shared-08.jpg) | ![步骤 9](../../../../assets/images/assembly/steps/shared-09.jpg) |
| ![步骤 10](../../../../assets/images/assembly/steps/shared-10.jpg) | ![步骤 11](../../../../assets/images/assembly/steps/shared-11.jpg) | ![步骤 12](../../../../assets/images/assembly/steps/shared-12.jpg) |
| ![步骤 13](../../../../assets/images/assembly/steps/shared-13.jpg) | | |

在关闭接头之前,检查每个伺服电机电缆到达下一个接头是否有一定的松动。

<a id="gripper-16-follower-only"></a>
## 抓具 1–6,仅适用于跟踪机器人臂

| 步骤 | 零件 | 紧固件 |
|:-:|---|---|
| 1 | RB9.01.062.040 伺服电机角上的夹持器齿轮,伺服电机ID 6 | 4×M3×4固定螺丝，1×M3×6 |
| 2 | 2×RB9.01.062.025 (D6.1)夹具，2×RB9.01.062.030齿轮架，2×RB9.01.062.100钉子 | — |
| 3 | 2 × 杆径6 × 125 mm | — |
| 4 | RB9.01.062.012 主框架 (D6.1), 2 × 轴承 MF106, 2 × RB9.01.062.050 垫圈 | 2 × M3×10 |
| 5 | 将杆子插入主框架 | — |
| 6 | 将夹具推至外部停止位置,插入伺服电机 | 3 × 数目 2× 数目6 自攻螺栓 |

步骤 2 中的 ×2 表示两侧各安装一组夹爪。表格中的数量为总数。

从舵盘一侧朝齿轮方向拧紧紧定螺钉，确保两者之间没有间隙。在步骤 6 之前，将 ID 为 6 的舵机移到最小位置，使夹爪能够完全闭合并张开至完整的 85 mm。封闭组件前，用手沿导杆滑动两个夹块。它们应能自由移动，不发生卡滞。

| | | |
|:-:|:-:|:-:|
| ![夹爪步骤 1](../../../../assets/images/assembly/steps/gripper-01.jpg) | ![夹爪步骤 2](../../../../assets/images/assembly/steps/gripper-02.jpg) | ![夹爪步骤 3](../../../../assets/images/assembly/steps/gripper-03.jpg) |
| ![夹爪步骤 4](../../../../assets/images/assembly/steps/gripper-04.jpg) | ![夹爪步骤 5](../../../../assets/images/assembly/steps/gripper-05.jpg) | ![夹爪步骤 6](../../../../assets/images/assembly/steps/gripper-06.jpg) |

<a id="follower-15"></a>
<a id="follower-13"></a>
## 跟随机器人臂 1–3

| 步骤 | 零件 | 紧固件 |
|:-:|---|---|
| 1 | RB9.01.062.075 相机支架 | 4 × M3×10 |
| 2 | 夹具装配到腕部 | 4 × 数目 2× 数目6 自攻螺栓 |
| 3 | RB9.01.062.090 摄像头间距,USB摄像头 | 4×M2×8、4×M2螺母 |

| | | |
|:-:|:-:|:-:|
| ![从臂步骤 1](../../../../assets/images/assembly/steps/follower-01.jpg) | ![从臂步骤 2](../../../../assets/images/assembly/steps/follower-02.jpg) | ![从臂步骤 3](../../../../assets/images/assembly/steps/follower-03.jpg) |

<a id="leader-14"></a>
<a id="leader-12"></a>
## Leader机器人臂 1–2

| 步骤 | 零件 | 紧固件 |
|:-:|---|---|
| 1 | SO102手柄,SO102手腕滚筒 | 4 × 数目 M3×6, 1 × 数目 2× 数目6 自攻螺栓 |
| 2 | SO102 伺服电机触发器 ID 6 | 4 × 数目 M3×6, 4 × 数目 2× 数目6 自攻螺栓 |

| | |
|:-:|:-:|
| ![主臂步骤 1](../../../../assets/images/assembly/steps/leader-01.jpg) | ![主臂步骤 2](../../../../assets/images/assembly/steps/leader-02.jpg) |

<a id="mounting-and-first-start"></a>
## 固定与首次启动

1. 用两个C型夹把每个底座固定在桌子上。
2. 将从臂控制器连接到 12 V 电源，将主臂控制器连接到 5 V 电源。
3. 使用 USB-C 将两个控制器连接到计算机。
4. 校准两个机器人臂,并在 [lab.robonine.com ](https://lab.robonine.com) 或 LeRobot SO-101 工作流程中启动远程操作。
<!-- /translated-content -->
