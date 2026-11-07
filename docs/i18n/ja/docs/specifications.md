<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](../../es/docs/specifications.md) · [Français](../../fr/docs/specifications.md) · [Deutsch](../../de/docs/specifications.md) · [Português (Brasil)](../../pt-BR/docs/specifications.md) · [简体中文](../../zh-CN/docs/specifications.md) · [日本語](specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[英語原文](../../../specifications.md)

[ドキュメント](../README.md) · [印刷](printing.md) · [部品表](bom.md) · [組立](assembly-guide.md) · [仕様](specifications.md) · [モデル](../models/README.md) · [貢献方法](../CONTRIBUTING.md) · [ライセンス](../LICENSING.md) · [翻訳](translations.md)

> この文書の全文翻訳です。図と元のPDF冊子は各言語で共用します。AIを使用した翻訳であり、母語話者による確認は未実施です。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="specifications-and-test-results"></a>
# 仕様と試験結果

測定日 Robonine 8月と9月にプロトタイプを作りました 2026*計算* と記された数字は URDF モデルとサーボモーターのデータシートです 測定ではありません

<a id="geometry"></a>
## 幾何形状

| 関節 | 範囲 |
|---|---|
| ベース回転 | −176° … +176° (352°) |
| 肩の上下動 | −43° … +181° (224°) |
| 肘の屈曲 | −166° … +77° (243°) |
| 手首の屈曲 | −85° … +111° (196°) |
| 手首の回転 | −165° … +163° (328°) |
| グリッパー | 0 … 85 mm |

| リンク | 軸間距離 |
|---|---|
| 肩への基部回転 | 85 mm |
| 肩から肘 | 119 mm |
| 肘から手首への屈曲 | 139 mm |
| 手首の屈曲から手首の転がり | 62 mm |
| 手首をグリップ先端に巻く | 132 mm |

| グリップ先端中央の距離 |  |
|---|---|
| 水平半径 | 483 mm |
| ベース底面からの高さ | 544 mmまで |
| ベース底部の下で、ロボットアームがテーブルの端を越えます。 | −301 mm まで |

これらのデータを用いて，リッチ度を計算した。 100,000 ランダムなポーズをとります 自己衝突はありません

<a id="servos"></a>
## サーボ

| 関節 | フォロワー | リーダー |
|---|---|---|
| 1 ベースの回転 | STS3235 | STS3215 |
| 2 肩甲挙上術 | STS3250 | STS3215 |
| 3 肘屈曲 | STS3250 | STS3215 |
| 4 手首の柔軟性 | STS3235 | STS3215 |
| 5 手首を回す | ST-3215-C049, 1:191 | STS3215 |
| 6 グリップ / トリガー | ST-3215-C049, 1:191 | STS3215 |
| 電源 | 12 V | 5 V |

<a id="gripper"></a>
## グリッパー

| | |
|---|---|
| 種類 | パラレル、ラック・ピニオン、2つの動く顎 |
| 開口幅 | 85 mm |
| 箱、推奨最大幅 | 75 mm について |
| シリンダー、推奨最大径 | 70 mm について |
| 球体、推奨最大径 | 60 mm について |
| カメラ | USBカメラをグリップに取り付ける |

<a id="measured-results-against-so-arm-101"></a>
## SO-ARM 101 に対する測定結果

| 指標 | SO-ARM 101 | SO-ARM 102 | 変化 |
|---|---|---|---|
| グリップ先端の偏向 300 gロボットアームが完全に伸びた状態で | 7.5 mm | 3.4 mm | −55 % |
| 同じ、すべてのリンクは 100% フィルタリング | — | 2.34 mm | −69 % |
| 水平半径 | 441 mm | 483 mm | +9.5 % |
| ベース後方へのリーチ | 377 mm | 473 mm | +25.5 % |
| ベース回転範囲 | 220° | 352° | +60 % |
| 肘の可動域 | 194° | 243° | +25 % |
| 肩・肘の無負荷速度 | 270 °/s | 450 °/s | +67 % |
| ベース関節のバックラッシュ | 8.75 の数 | 5.00 の数 | −43 % |
| ベースバックラッシュからの水平先端誤差，＊計算＊ | ±2.96 mm | ±1.85 mm | −37.5 % |
| 繰返し精度 | — | 0.1 mm について |  |
| 1 m のノイズ | 70 dB | 60 dB | −10 dB |
| 定格可搬質量 | 150 g | 300 g |  |

¹ 両アームとも関節 2、3、4 には印刷したサーボのダミーを使用し、フレームのみを比較しています。SO-ARM 101 は PLA、SO-ARM 102 は Fiberon PET-CF17 で印刷し、インフィルは 25 % です。同じ SO-ARM 102 試験の2回目の結果は 3.9 mm でした。

| SO-ARM 101 | SO-ARM 102 |
|:-:|:-:|
| ![SO-ARM 101 剛性テスト](../../../../assets/images/tests/stiffness-so-arm-101.jpg) | ![SO-ARM 102 剛性テスト](../../../../assets/images/tests/stiffness-so-arm-102.jpg) |

<a id="current-and-temperature-follower"></a>
## 電流と温度，フォローロボットアーム

測定した 300 g 繰り返しの軌道上に荷重をかけ 30 °C6人 STS3250 サーボモーター

| | |
|---|---|
| 平均電流 | 1.26 A |
| ピーク電流 | 3.28 A |
| サーボ最高温度 | 46 °C |

<a id="absolute-accuracy"></a>
## 絶対精度

調整はまだ進行中です。サーボの初期 PID 設定では、アームを最大まで伸ばした状態で、自重により先端が約 50 mm 下がりました。PID 調整後は約 5 mm に減少しました。専用の精度評価プロファイルを準備中です。
<!-- /translated-content -->
