<!-- translation-navigation -->
[English](../../en/docs/assembly-guide.md) · [Русский](../../ru/docs/assembly-guide.md) · [Español](../../es/docs/assembly-guide.md) · [Français](../../fr/docs/assembly-guide.md) · [Deutsch](../../de/docs/assembly-guide.md) · [Português (Brasil)](../../pt-BR/docs/assembly-guide.md) · [简体中文](../../zh-CN/docs/assembly-guide.md) · [日本語](assembly-guide.md) · [हिन्दी](../../hi/docs/assembly-guide.md) · [العربية](../../ar/docs/assembly-guide.md)

[英語原文](../../../assembly-guide.md)

[ドキュメント](../README.md) · [印刷](printing.md) · [部品表](bom.md) · [組立](assembly-guide.md) · [仕様](specifications.md) · [モデル](../models/README.md) · [貢献方法](../CONTRIBUTING.md) · [ライセンス](../LICENSING.md) · [翻訳](translations.md)

> この文書の全文翻訳です。図と元のPDF冊子は各言語で共用します。AIを使用した翻訳であり、母語話者による確認は未実施です。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="assembly-guide"></a>
# 組立ガイド

このガイドは、印刷されたブックレット [SO-ARM102_assembly_A5_v0.7.pdf](../../../SO-ARM102_assembly_A5_v0.7.pdf) をページごとに追従します。紙が好きな場合は、ブックレットを A5横長で印刷してください。

作業を始める前に：

- [printing.md](printing.md)からすべての部品を印刷し、[bom.md](bom.md)からハードウェアを集める。
- ヘキサデシマルキー 1.5 mm (M2) と 2 mm (M3) が必要です。
- 何かを締め付ける前に2段階先読みしてください。現在の順序で2つの場所が不都合です。[既知の問題](../README.md#-known-issues)を参照してください。

> ⚠️ **リーダーアームは 5 V、フォロワーアームは 12 V で動作します。** それぞれの電源を分けて管理してください。

印刷した樹脂に適合する取り外し可能なねじロック剤（例：[Vibra-Tite VC-3](https://www.vibra-tite.com/faq/if-vc-3-has-mek-how-can-it-be-plastic-compatible/)）を使用してください。VC-3 は金属ねじのねじ部に塗布し、組立前に完全に乾燥させます（[技術資料](https://www.vibra-tite.com/wp-content/uploads/213_tds.pdf)では最低 30 分）。未乾燥の状態で樹脂に塗布しないでください。まず同じフィラメントの試作品で適合性を確認してください。

![ツールと電圧警告](../../../../assets/images/assembly/tools-and-voltage.jpg)

<a id="order-of-work"></a>
## 作業順序

<a id="reading-the-illustrations"></a>
### 絵を読む

ベージュ色のハイライトが新しい部品を示し、グレー色は既に組み立てられた部品です。部品サムネイルと数量は追加するものを示します。番号付き円は組み立てステップであり、点は進行状況を示しています。部品番号、ファスナーサイズ、サーボモーター ID は言語ごとに同じです。

<a id="assembly-sequence"></a>
### 組み立てシーケンス

1. サーボモーターにホーンを取り付ける
2. アーム本体を**2回**組み立てます。フォロワー用とリーダー用にそれぞれ1回です（手順 1–13）。 手順 12–13 で各アームに Bus Servo Adapter を取り付けます。
3. パラレルグリップを構築する（グリップステップ 1-6）。
4. フォロワーを仕上げます：カメラホルダー、グリッパー、カメラ（フォロワーの手順 1–3）。
5. リーダーを仕上げます：ハンドルとトリガー（リーダーの手順 1–2）。

<a id="servo-ids"></a>
## サーボID

ロボットアームに入る前に各サーボモーターの ID を設定します。ID の設定とキャリブレーションツールは [lab.robonine.com](https://lab.robonine.com)で利用できます。

![サーボ ID の割り当て](../../../../assets/images/assembly/servo-ids.jpg)

| ID | 関節 | フォロワーのサーボ | リーダーのサーボ |
|:-:|---|---|---|
| 1 | ベース回転 | STS3235 | STS3215 |
| 2 | 肩の上下動 | STS3250 | STS3215 |
| 3 | 肘の屈曲 | STS3250 | STS3215 |
| 4 | 手首の屈曲 | STS3235 | STS3215 |
| 5 | 手首の回転 | STS3215 | STS3215 |
| 6 | グリッパー / トリガー | STS3215 | STS3215 |

<a id="0-servo-horns"></a>
## 0. サーボホーン

サーボモータ ID 1に M3 × 6 スクリューでホーンを一つ取り付けます。サーボ ID 2、3、4は両側にホーンがあります。ホーンスクリューはサーボモーターと共に提供されます。

リーダーロボットアームにＯリングを付ける場合は、サーボモーターとホーンの間に置く。この順序が間違えば、サーボモーターシェルとホーンの間のリングがジャンプする可能性があります。

<a id="111-arm-body-follower-and-leader"></a>
<a id="113-arm-body-follower-and-leader"></a>
## 1–13アームボディ，フォロワーロボットアーム，リーダロボットアームについて述べた。

両方のロボットアームに対してこれらのステップを繰り返す。 印刷部品の名前は [printing.md](printing.md) と一致します。

| 手順 | 部品 | 締結部品 |
|:-:|---|---|
| 1 | SO102.02.060 下サーボモーターホルダー,SO102.02.040 下トッププレート | 3 × M3×16, 3 × M3 ナット |
| 2 | — | 3 × M3×16, 3 × M3 ナット |
| 3 | サーバ ID 1 | 4 × M2×6 |
| 4 | SO102.02.020 ベースリング、ベアリング 6812、SO102.02.050 ボトムリング、SO102.02.010 ベース | 6 × M3×16, 6 × M3 ナット |
| 5 | SO102.02.030 ベースワッシャー | 4 × M3×10, 6 × M3×16 |
| 6 | サーボID 2 と ID 3、2 × SO102.02.070 ボトムロボットアーム、2短いケーブル、1長いケーブル | 16 × M2×6 |
| 7 | サーボID 4、SO102.02.080-01上部ロボットアーム右、1短いケーブル | 4 × M2×6 |
| 8 | SO102.02.080 左上のロボットアーム、2 × SO102.02.130 ケーブルスナップ | 4 × M2×6, 8 × M3×10 |
| 9 | サーボID 5,SO102.02.090 手首ホルダー、サーボモーターホーン | 1 × M3×6, 4 × 2×6 自己タップ |
| 10 | 1 短いケーブル | 8 × M3×10 |
| 11 | — | 8 × M3×10 |
| 12 | SO102.02.110 リーダー用ボードホルダー, Bus Servo Adapter | 4 × M2 ナット, 4 × M2×8 |
| 13 | SO102.02.110-01 リーダー用ボードカバー, 1 × 長いケーブル | — |

| | | |
|:-:|:-:|:-:|
| ![手順 1](../../../../assets/images/assembly/steps/shared-01.jpg) | ![手順 2](../../../../assets/images/assembly/steps/shared-02.jpg) | ![手順 3](../../../../assets/images/assembly/steps/shared-03.jpg) |
| ![手順 4](../../../../assets/images/assembly/steps/shared-04.jpg) | ![手順 5](../../../../assets/images/assembly/steps/shared-05.jpg) | ![手順 6](../../../../assets/images/assembly/steps/shared-06.jpg) |
| ![手順 7](../../../../assets/images/assembly/steps/shared-07.jpg) | ![手順 8](../../../../assets/images/assembly/steps/shared-08.jpg) | ![手順 9](../../../../assets/images/assembly/steps/shared-09.jpg) |
| ![手順 10](../../../../assets/images/assembly/steps/shared-10.jpg) | ![手順 11](../../../../assets/images/assembly/steps/shared-11.jpg) | ![手順 12](../../../../assets/images/assembly/steps/shared-12.jpg) |
| ![手順 13](../../../../assets/images/assembly/steps/shared-13.jpg) | | |

サーボモータのケーブルが次のジョイントに到達する前に，ジョイントを閉じる前に少しずつゆるみを持って確認した。

<a id="gripper-16-follower-only"></a>
## グリップ 1-6、フォローロボットアームのみ

| 手順 | 部品 | 締結部品 |
|:-:|---|---|
| 1 | RB9.01.062.040 サーボモータホーンのグリップ用ギヤ、サーボモータID6 | 4 × M3×4 セットネジ、1 × M3×6 |
| 2 | 2 × RB9.01.062.025 (D6.1) クランプ、2 × RB9.01.062.030 ギアラック、2 × RB9.01.062.100 釘 | — |
| 3 | 2 × 棒 Ø6 × 125 mm | — |
| 4 | RB9.01.062.012 メインフレーム (D6.1), 2 × ベアリング MF106, 2 × RB9.01.062.050 ワッシャー | 2 × M3×10 |
| 5 | ロッドをメインフレームにスナップ | — |
| 6 | クランプを外側の止め具に押し込み サーボモーターを挿入 | 3 × 2 × 6 自己タップ |

手順 2 の ×2 は、左右にそれぞれ一組のジョーを組み立てることを示します。表の数量は合計です。

ホーン側からギアに向かって止めねじを締め、両者の間に隙間ができないようにします。手順 6 の前に、ID 6 のサーボを最小位置に動かし、グリッパーが完全に閉じて最大 85 mm まで開くようにします。組み付けを閉じる前に、両方のクランプを手でロッドに沿って動かしてください。引っ掛かりなく自由に動くことを確認します。

| | | |
|:-:|:-:|:-:|
| ![グリッパーの手順 1](../../../../assets/images/assembly/steps/gripper-01.jpg) | ![グリッパーの手順 2](../../../../assets/images/assembly/steps/gripper-02.jpg) | ![グリッパーの手順 3](../../../../assets/images/assembly/steps/gripper-03.jpg) |
| ![グリッパーの手順 4](../../../../assets/images/assembly/steps/gripper-04.jpg) | ![グリッパーの手順 5](../../../../assets/images/assembly/steps/gripper-05.jpg) | ![グリッパーの手順 6](../../../../assets/images/assembly/steps/gripper-06.jpg) |

<a id="follower-15"></a>
<a id="follower-13"></a>
## フォローアーム 1–3

| 手順 | 部品 | 締結部品 |
|:-:|---|---|
| 1 | RB9.01.062.075 カメラホルダー | 4 × M3×10 |
| 2 | 手首にグリップを取り付ける | 4 × 2 × 6 自己タップ |
| 3 | RB9.01.062.090 カメラスペーサー、USBカメラ | 4 × M2×8, 4 × M2 ナット |

| | | |
|:-:|:-:|:-:|
| ![フォロワーの手順 1](../../../../assets/images/assembly/steps/follower-01.jpg) | ![フォロワーの手順 2](../../../../assets/images/assembly/steps/follower-02.jpg) | ![フォロワーの手順 3](../../../../assets/images/assembly/steps/follower-03.jpg) |

<a id="leader-14"></a>
<a id="leader-12"></a>
## リーダーロボットアーム 1–2

| 手順 | 部品 | 締結部品 |
|:-:|---|---|
| 1 | SO102 ハンドル、SO102 手首巻き | 4 × M3×6, 1 × 2×6 自己タップ |
| 2 | SO102 トリガー、サーボモーター ID 6 | 4 × M3×6, 4 × 2×6 自己タップ |

| | |
|:-:|:-:|
| ![リーダーの手順 1](../../../../assets/images/assembly/steps/leader-01.jpg) | ![リーダーの手順 2](../../../../assets/images/assembly/steps/leader-02.jpg) |

<a id="mounting-and-first-start"></a>
## 固定と初回起動

1. 2つのCクランプでテーブルに固定する
2. フォロワー側のコントローラーを 12 V 電源に、リーダー側のコントローラーを 5 V 電源に接続してください。
3. USB-Cで両方のコントローラをコンピュータに接続します。
4. 両方のロボットアームを調整し 遠隔操作を開始 [lab.robonine.com](https://lab.robonine.com)あるいは LeRobot SO-101 workflow.
<!-- /translated-content -->
