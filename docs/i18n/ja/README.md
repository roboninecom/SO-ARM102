<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[英語原文](../../../README.md)

[ドキュメント](README.md) · [印刷](docs/printing.md) · [部品表](docs/bom.md) · [組立](docs/assembly-guide.md) · [仕様](docs/specifications.md) · [モデル](models/README.md) · [貢献方法](CONTRIBUTING.md) · [ライセンス](LICENSING.md) · [翻訳](docs/translations.md)

> この文書の全文翻訳です。図と元のPDF冊子は各言語で共用します。AIを使用した翻訳であり、母語話者による確認は未実施です。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102"></a>
# SO-ARM 102

<div align="center">

[![SO-ARM 102](../../../assets/images/photos/so-arm-102-live.jpg)](../../../assets/video/so-arm-102-preview.mp4)

**🎥 [プレビュービデオを見る](../../../assets/video/so-arm-102-preview.mp4)**·**🛒[キットを買う](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

**SO-ARM 102 は、遠隔操作と模倣学習のためのオープンソースのリーダー・フォロワーロボットアームキットです。各アームは五つの自由度とグリッパーを備えています。**

<p align="left">
SO-ARM 100 と 101 を基に、より剛性の高い PET-CF フレームと平行グリッパーを組み合わせています。
</p>

[![ハードウェア: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt) [![ソフトウェア: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt) [![ドキュメント: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt) [![GitHub release](https://img.shields.io/github/v/release/roboninecom/SO-ARM-102)](https://github.com/roboninecom/SO-ARM-102/releases/latest)

📩 [hello@robonine.com](mailto:hello@robonine.com)

**DIY製作の予算目安：部品のみで ~$340、造形材料を含めて ~$374。** [部品表の概要](#bill-of-materials) · [費用の内訳と購入リンク](docs/bom.md#estimated-kit-cost)

> 部品調達や造形の手間を省きたい方は、**[SO-ARM 102キットを購入できます](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**。

</div>

---

<a id="-what-changed-against-so-arm-101"></a>
## SO-ARM 101に対して何が変わったか

|  | SO-ARM 101 | SO-ARM 102 |
|---|---|---|
| グリッパー | 回転開閉式の爪 | 平行グリッパー、開口幅 85 mm |
| フレーム材料 | PLA | PET-CF (Fiberon PET-CF17 テスト済み) |
| 構造 | 中実リンク | トポロジー最適化リンク |
| ベース回転範囲 | 220° | **352°** |
| 水平リーチ | 441 mm | **483 mm** |
| 300 g 荷重時のグリッパー位置でのたわみ ¹ | 7.5 mm | **3.4–3.9 mm** |
| 肩・肘関節の速度 | 45 RPM (STS3215) | **75 RPM (STS3250)** |
| 距離 1 m での騒音 | 70 dB | **60 dB** |

¹ 両アームには印刷したサーボのダミーを使用しているため、比較対象はモーターではなくフレームです。詳しい結果と試験条件は [docs/specifications.md](docs/specifications.md) を参照してください。

---

<a id="-preview"></a>
## プレビュー

<div align="center">

[![SO-ARM 102 プレビュー](../../../assets/video/so-arm-102-preview.gif)](../../../assets/video/so-arm-102-preview.mp4)

*クリックすると動画全編（21 s）を再生します。*

</div>

---

<a id="-configurations"></a>
## 構成

<a id="single-arm-one-leader--one-follower"></a>
### 単腕構成：リーダーアーム1本＋フォロワーアーム1本

標準のキット構成です。リーダーアームを手で動かすと、フォロワーアームがその動きに追従します。遠隔操作や、模倣学習用のデモンストレーションの記録に使用できます。

![リーダー1台とフォロワー1台](../../../assets/images/renders/config-single-arm.jpg)

<a id="bimanual-two-leaders--two-followers"></a>
### 双腕構成：リーダーアーム2本＋フォロワーアーム2本

2セットを並べて配置します。それぞれの手でリーダーアームを操作することで、フォロワーは物を受け渡したり、部品を保持して作業したり、両手を必要とする作業を行えます。

![リーダー2台とフォロワー2台](../../../assets/images/renders/config-dual-arm.jpg)

<a id="the-two-arms"></a>
### 二つのロボットアーム

| フォロワー | リーダー |
|:-:|:-:|
| ![フォロワーアーム](../../../assets/images/renders/follower.jpg) | ![リーダーアーム](../../../assets/images/renders/leader.jpg) |
| 平行グリッパー、手首カメラ、12 V | トリガー付きハンドル、5 V |

---

<a id="-build-it-in-four-steps"></a>
## 4つのステップで作る

キットをご希望の方は、**[SO-ARM 102キットを購入できます](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**。

<a id="1-print-the-parts"></a>
### 1. 部品を3Dプリントする

各部品は 180 × 180 mm の造形ベッドに収まります。最大の部品の長さは 160 mm です。付属の 3MF ファイルのプレート配置は、256 × 256 mm の造形ベッドを想定しています。

- 造形方向とサポート設定を保存した 3MF スライサープロジェクト：[`models/3mf/`](../../../models/3mf) — [リーダーアーム](../../../models/3mf/SO102_leader.3mf)、[フォロワーアーム](../../../models/3mf/SO102_follower_arms.3mf)、[フォロワーのグリッパーとベース](../../../models/3mf/SO102_follower_gripper_base.3mf)
- プロジェクトの内容とプリンタプロファイル: [models/README.md](models/README.md)
- スライス用の STL ファイル：[`models/stl/`](../../../models/stl)
- STEP ソース: [`models/step/`](../../../models/step)
- 材料、設定、部品数量: [docs/printing.md](docs/printing.md)


<a id="2-buy-the-hardware"></a>
### 2. ハードウェアを購入する

部品は、[部品表の概要](#bill-of-materials) と [購入リンク付きの部品表全体](docs/bom.md) を参照して調達してください。予算の目安は部品のみで **$340.22**、造形材料を含めて **$373.97** です。送料と税金は含みません。

| アーム | サーボ | コントローラー | 電源 |
|---|---|---|---|
| フォロワー | 2 × STS3235, 2 × STS3250, 2 × STS3215 | Waveshare Bus Servo Adapter | **12 V** |
| リーダー | 6 × STS3215 | Waveshare Bus Servo Adapter | **5 V** |

> ⚠️ **リーダーアームは 5 V、フォロワーアームは 12 V で動作します。** 電源を取り違えないでください。

<a id="3-assemble"></a>
### 3. 組み立てる

- 印刷可能なブックレット、32ページA5：[docs/SO-ARM102_assembly_A5_v0.7.pdf](../../SO-ARM102_assembly_A5_v0.7.pdf)
- 各工程で使用する部品と締結部品の一覧：[docs/assembly-guide.md](docs/assembly-guide.md)

工具：1.5 mm（M2 ねじ用）と 2 mm（M3 ねじ用）の六角レンチ。

<a id="4-set-up-the-software"></a>
### 4. ソフトウェアを設定する

サーボID、キャリブレーション、レッスンについては **[lab.robonine.com](https://lab.robonine.com)**.
SO-ARM 102 フォロワープラグインと標準の `so101_leader` 型を使用してください。
**[LeRobot のインストールと設定](docs/lerobot.md)**.

---

<a id="bill-of-materials"></a>
## 部品表

**リーダーアーム1本＋フォロワーアーム1本**に必要な数量と参考費用：

| カテゴリ/購入リンク | キット内容 | 合計 (USD) |
|---|---|---:|
| [サーボ](docs/bom.md#servos) | 6 × STS3215 7.4 V, 2 × STS3215 12 V, 2 × STS3235, 2 × STS3250 | $240.72 |
| [電子部品](docs/bom.md#electronics) | 2 コントローラ、2 電源、2 USBケーブル、1 手首カメラ | $50.50 |
| [機械部品](docs/bom.md#mechanical-parts) | 軸受4、鋼製ガイドロッド2、テーブルクランプ4 | $37.76 |
| [締結部品](docs/bom.md#fasteners) | ねじとナット（指定のサーボキット付属ねじを含む） | $11.24 |
| **部品小計** |  | **$340.22** |
| [印刷素材](docs/bom.md#printing-materials) | 0.4 kg PET-CF17 + 0.75 kg PETG 割当 | $33.75 |
| **印刷材料込み合計** |  | **$373.97** |

掲載例の部品パックとフィラメントのスプールをすべて新規に購入する場合、使用せずに残る予備部品も含めて約 **$435** です。これらは参考見積もりであり、供給元から新たに取得した見積書ではありません。送料、税金、工具、コンピュータ、プリンタ、電気代、組立作業費は含みません。注文前に供給元の価格、製品バリエーション、最低注文数量を確認し、3MF プロジェクトを再スライスしてフィラメント使用量を確認してください。

[部品表の詳細、購入リンク、費用の前提条件](docs/bom.md#estimated-kit-cost)。

---

<a id="urdf-export"></a>
## URDF エクスポート

現在の単体で使用できるエクスポートは [`simulation/urdf/`](../../../simulation/urdf) にあります：[URDF](../../../simulation/urdf/so_arm_102.urdf) · [Xacro](../../../simulation/urdf/so_arm_102.xacro)。`meshes/` はロボット記述ファイルと同じフォルダ内に置いてください。メッシュのパスはこのフォルダからの相対パスです。

- **表示用形状：** STL メッシュ。**衝突判定用形状：** 全8リンクに、それぞれ形状に合わせて寸法と向きを設定した直方体を使用しています。
- **質量推定：** PLA、インフィル率 30%、外周壁 6 周、上面・下面それぞれ 6 層、積層ピッチ 0.2 mm、**押出し幅 0.40 mm** を想定しています。これらはシミュレーション上の仮定です。実際の造形設定は [造形ガイド](docs/printing.md) を参照してください。
- **ハードウェアの質量：**モーター6個は各 70 g、ベースのベアリングは 105 g です。モデルの推定総質量は**0.889 kg** です。
- **グリッパー：** `clamp2` は `clamp1` に倍率 `-1` で連動する mimic 関節です。

[エクスポート設定](../../../simulation/urdf/export_settings.json) と [質量特性](../../../simulation/urdf/mass_properties.json) に前提条件を記録しています。形状と慣性の検証結果は [export_verification.json](../../../simulation/urdf/export_verification.json) に記録しています。

---

<a id="-repository-structure"></a>
## リポジトリ構造

```
├── models/
│   ├── 3mf/                 # スライサープロジェクト：リーダー、フォロワー、グリッパー、基板ケース
│   ├── stl/                 # 印刷可能なメッシュ
│   │   ├── common/          # コントローラーケースを含む共通部品
│   │   ├── follower/        # 平行グリッパーとカメラマウント
│   │   └── leader/          # ハンドル、トリガー、手首回転部品
│   └── step/                # CAD ソース、stl/と同じレイアウト
├── docs/
│   ├── printing.md          # 素材、スライサーの設定、量
│   ├── bom.md               # 部品表
│   ├── assembly-guide.md    # 各工程の部品と締結部品の一覧
│   ├── specifications.md    # 寸法・形状、サーボ、SO-ARM 101 との実測比較
│   └── SO-ARM102_assembly_A5_v0.7.pdf
├── assets/
│   ├── images/              # 写真、レンダリング、ブックレットページ、テスト写真
│   └── video/               # 動画とGIFのプレビュー
├── LICENSING.md             # ファイルに適用されるライセンス
└── NOTICE                   # 第三者の著作物の帰属表示
```

---

<a id="-known-issues"></a>
## 既知の問題

独立した組立テストの注意点です。組立時に確認してください。

1. **v0.7 の冊子を使用してください。** 旧版には HAT コントローラーと旧グリッパー部品が掲載されています。v0.7 では両アームに Bus Servo Adapter を取り付けます。
2. **一部の M2 ねじは工具が届きにくい位置にあります。** 取り付けに手間がかかる箇所があります。
3. **グリッパーのクランプはカーボンロッド上で動きが固くなります。** クランプの穴は 6.1 mm に合わせてあります。ロッドの直径は供給元により異なるため、組立前に適合を確認してください。
4. 各関節を閉じる前に、**サーボケーブルの長さを確認してください。** 特にベースから肩までの区間に注意してください。
5. **冊子の組立順序には、作業しにくい箇所が2か所あります。** 部品を固定する前に、2工程先まで読んでください。
6. **リーダーの関節に緩さを感じる場合があります。** 各サーボとホーンの間に 8 × 2 mm のゴム製 O リングを入れると、滑らかで静かな摩擦が得られます。関節 1–4 はサーボごとに2個、関節 5–6 は1個使用します。

ほかにも問題が見つかった場合は、[issue を作成](https://github.com/roboninecom/SO-ARM-102/issues) してください。

---

<a id="-star-history"></a>
## ⭐ スター数の推移

[![スター数の推移 — SO-ARM 102](https://api.star-history.com/svg?repos=roboninecom/so-arm-102&type=date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm-102&type=date&legend=top-left)

---

<a id="-related-projects"></a>
## 関連プロジェクト

- [SO-ARM100/101 Parallel Gripper](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper) — SO-ARM 102 のグリッパーの設計元となったグリッパー
- [SO-ARM101](https://github.com/TheRobotStudio/SO-ARM100) — TheRobotStudio による、この設計の先行モデル
- [スマートシリアルサーボの実用比較](https://robonine.com/smart-serial-servo-motor-comparison-robotics/) — サーボ選定の根拠となった試験
- [ロボットアーム用フィラメントの選定](https://robonine.com/choosing-filament-for-robotic-arm-applications/) — PET-CF 採用の根拠となった試験

---

<a id="-license"></a>
## ライセンス

著作権 (c) 2026 Robonine。異なる種類の素材は異なるライセンスを持っています:

| 材料 | ライセンス |
|---|---|
| `models/` のハードウェア設計 | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| ソフトウェアと設定 | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| `docs/`、`assets/`、すべての `README.md` におけるドキュメントと画像 | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

ファイルごとのマップは [LICENSING.md](LICENSING.md)と [REUSE.toml](../../../REUSE.toml)を参照してください。

---

<a id="-team"></a>
## チーム

| 名称 | 役割 | 連絡先 |
|------|------|---------|
| **Alan Subin** | 設計エンジニア：機械設計、CAD、組立ブックレット | [LinkedIn](https://www.linkedin.com/in/alan-subin/) |
| **Boris Kotov** | ソフトウェアとテストエンジニア：プロトタイプ、印刷、テストリグ | [Telegram](https://t.me/bkotov) |
| **Nikita Bragin** | プロジェクト管理者 | [LinkedIn](https://www.linkedin.com/in/nikita-bragin-82296b29/) |
| **Mikhail Chistiakov** | インダストリアルデザイナー：ロボットアームの外観と形状 | [Telegram](https://t.me/brrryska) |
| **Mikhail Zhmaylo** | 構造技術者：剛性モデル，変形削減のための設計変更 | [Telegram](https://t.me/mikhail_zhmaylo) |
| **Vladislav Eremenko** | 構造エンジニア：強度と熱解析，トポロジー最適化 | [Telegram](https://t.me/v1ad_eremenko) |
| **Vladimir Osipov** | テスターとコンサルタント:独立したテストビルド | [LinkedIn](https://www.linkedin.com/in/vladimirosipov/) |

<div align="center">

**[Robonine](https://robonine.com) がロボティクスコミュニティのために開発しました。**

</div>
<!-- /translated-content -->
