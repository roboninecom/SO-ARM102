<!-- translation-navigation -->
[English](../../en/docs/bom.md) · [Русский](../../ru/docs/bom.md) · [Español](../../es/docs/bom.md) · [Français](../../fr/docs/bom.md) · [Deutsch](../../de/docs/bom.md) · [Português (Brasil)](../../pt-BR/docs/bom.md) · [简体中文](../../zh-CN/docs/bom.md) · [日本語](bom.md) · [हिन्दी](../../hi/docs/bom.md) · [العربية](../../ar/docs/bom.md)

[英語原文](../../../bom.md)

[ドキュメント](../README.md) · [印刷](printing.md) · [部品表](bom.md) · [組立](assembly-guide.md) · [仕様](specifications.md) · [モデル](../models/README.md) · [貢献方法](../CONTRIBUTING.md) · [ライセンス](../LICENSING.md) · [翻訳](translations.md)

> この文書の全文翻訳です。図と元のPDF冊子は各言語で共用します。AIを使用した翻訳であり、母語話者による確認は未実施です。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="bill-of-materials"></a>
# 部品表

数量はフォロワー1台とリーダー1台からなる1セット分です。印刷部品は [printing.md](printing.md) に別途記載しています。

<a id="estimated-kit-cost"></a>
## 予測キットコスト

**１本のリーダーロボットアーム＋１本のフォローアーム： $340 コンポーネントにも $374 印刷材料も含めて

| 分類 | 使用量コスト（米ドル） | フルパック/スプールを購入 (USD) |
|---|---:|---:|
| サーバ (12 pcs) | $240.72 | $240.72 |
| エレクトロニクス、カメラ、電源 | $50.50 | $50.50 |
| 軸受，鋼製ガイドロッド，テーブルクランプ | $37.76 | $49.70 |
| 締結部品 | $11.24 | $28.60 |
| **部品小計** | **$340.22** | **$368.82** |
| 印刷材料: 0.4 kg PET-CF17 + 0.75 kg PETG | $33.75 | $66.0 |
| **印刷材料込み合計** | **$373.97** | **$434.82** |

**Total (USD)** 列はキット1つに必要な数量のコストであり、既存の各行総額の後ろにある参考オファーを使用しています。スクリューは含まれていますが、価格は $0です。代替カーボンチューブは合計から除外されます。推定値は下記の参考価格を使用しており、各行はセントに丸められています。これらは新しいサプライヤーの提案ではありません:選択したバリエーション、最小注文数量と価格を確認してください。輸送、税金、ツール、コンピュータ、プリンタ、電気、組立労働は除外されています。

フルパックコラムには未使用のスペア、0.5 kg PET-CF17 スプールと1 kg PETG スプールが含まれています。印刷量は予算許容量です。3D プリンタスライサーを使って提供された 3MF プロジェクトを設定に合わせて再スライスしてください。ロッドコストは鋼鉄を使用します。カーボンチューブは代替品です。

![キットハードウェア](../../../../assets/images/assembly/hardware.jpg)

<a id="servos"></a>
## サーボ

| 関節 | ID | フォロワー | リーダー |
|---|:-:|---|---|
| ベース回転 | 1 | ST-3235-С001 | ST-3215-C066, 1:191 |
| 肩の上下動 | 2 | ST-3250-С002 | ST-3215-C066, 1:191 |
| 肘の屈曲 | 3 | ST-3250-С002 | ST-3215-C066, 1:191 |
| 手首の屈曲 | 4 | ST-3235-С001 | ST-3215-C066, 1:191 |
| 手首の回転 | 5 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |
| グリッパー / トリガー | 6 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |

合計：6 × STS3215 7.4V、2 × STS3215 12V、2 × STS3235 12V、2 × STS3250 12V。すべて Feetech TTL シリアルバスサーボです。

| サーボ | 数量 | 選択 | Aliexpress リンク | 単価 (USD) | Alibaba リンク | 単価 (USD) | 合計 (USD) |
|---|---|---|---|---|---|---|---|
| STS3215 | 6 | 7.4V TTL リーダーロボットアームサーボモーター用のバージョンです。 ST-3215-C066 (7.4V). | [Aliexpress](https://www.aliexpress.us/item/3256811860804361.html) | $32.8 | [Alibaba](https://www.alibaba.com/product-detail/Feetech-SO-ARM101-LeRobot-Open-Source_1601636174153.html) | $6.74 | $40.44 |
| STS3215 | 2 | フォローロボットのアーム関節 5 と 6 用のバージョン 12V TTL。 ST-3215-C049 (12V30KG) を選択してください。 | [Aliexpress](https://www.aliexpress.us/item/3256811832699316.html) | $55.8 から 2pcs | [Alibaba](https://www.alibaba.com/product-detail/6pcs-12V-30KG-1-345-STS3215_1601900233170.html) | $14.70 | $29.40 |
| STS3235 | 2 | 12V TTL フォローロボットアームジョイント用のバージョン 1 そして 4. | [Aliexpress](https://www.aliexpress.us/item/3256810213842277.html) | $63 | [Alibaba](https://www.alibaba.com/product-detail/FEETECH-STS3235-12V-30KG-TTL-Dual_1601910640629.html) | $40.79 | $81.58 |
| STS3250 | 2 | 12V TTL フォローロボットアームジョイント用のバージョン 2 そして 3. | [Aliexpress](https://www.aliexpress.us/item/3256811995148799.html) | $126.4 から 2pcs | [Alibaba](https://www.alibaba.com/product-detail/Feetech-STS3250-12V-50kg-Servo-High_1601711893549.html) | $44.65 | $89.30 |
| **合計** |  |  |  |  |  |  | **$240.72** |

- **ロボットアームの追従者 12V.** STS3250 それは 50 kg１０ｃｍブラシレスサーボモータ 75 RPM最大の負荷を受ける２つの関節を駆動する STS3235 それは 30 kgまた，サーボモータの回転速度は１００〜２００ｒｐｍ／ｓである。 STS3215.
- **リーダー、5V。** サーボは位置の読み取り専用で、負荷をかけません。モーターとギアボックスのないパッシブ型 ST-3215-C066 は、リーダーアームにのみ使用できます。
- サーボホーンと M3 × 6 ホーンネジは サーボモーターに付属してる

<a id="electronics"></a>
## 電子部品

| 品目 | 数量 | 備考 | 米国で購入 | 単価（米国） | 米国で購入 | 単価（米国） | EUで購入 | 単価（EU） | 合計 (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Waveshare Bus Servo Adapter | 2 | サーボコントローラー | [Amazon](https://www.amazon.com/Waveshare-Integrates-Control-Applicable-Integrate/dp/B0CJ6TP3TP/) | $13.00 | [Aliexpress](https://www.aliexpress.us/item/3256810343532716.html) | $7.40 | [Amazon EU](https://www.amazon.fr/-/en/Serial-Integrates-Control-Circuit-Support/dp/B0CJBKQ8LJ/) | €11.90 | $14.80 |
| 電源 12V DC (12V 5A 電源 5.5 2.1mm) | 1 | フォロワー用。60W / 5A 以上を推奨します。300g の負荷でアームの最大電流は 3.3A でした。Adapter のコネクター寸法（5.5x2.1mm）を合わせてください。 | [Amazon](https://www.amazon.com/Power-Supply-Adapter-5-5x2-1-2-5mm/dp/B0C3CJF313/) | $10.00 | [Aliexpress](https://www.aliexpress.us/item/3256812113231032.html) | $6.60 | [Amazon EU](https://www.amazon.fr/-/en/zstg-Universal-Power-Supply-Connector/dp/B0GTLSRM91/) | €12.00 | $6.60 |
| 電源 5V DC (5V 2A 電源 5.5 2.1mm) | 1 | リーダー用。アダプターのコネクター寸法（5.5x2.1mm）を合わせてください。 | [Amazon](https://www.amazon.com/MTDZKJG-Adapter-100V-240V-Transformer-Security/dp/B0BZP65GRW/) | $6.20 | [Aliexpress](https://www.aliexpress.us/item/3256812479558626.html) | $4.10 | [Amazon EU](https://www.amazon.fr/5V-2A-Supply-DC-Adapter/dp/B0GDXFRYJS/) | €11.00 | $4.10 |
| USB-Cケーブル、1.5 m (USB A から USB C データケーブル 1.5m) | 2 | コントローラごとに一つ 充電用のケーブルではなく データケーブルを選んでください | [Amazon](https://www.amazon.com/Data-Cable-1-5ft-10Gbps-Transfer/dp/B0FMJTHRCM/) | $6.00 | [Aliexpress](https://www.aliexpress.us/item/3256812299430938.html) | $3.00 | [Amazon EU](https://www.amazon.fr/-/en/10Gbps-Transfer-Charging-Samsung-External/dp/B0DHZ1R8FQ/) | €7.00 | $6.00 |
| USB カメラ (OV2735, 1080P USB カメラモジュール, 2MP 1920x1080, UVC カメラ, 2.8 または 3.0 mm レンズ) | 1 | フォローロボットアームグリップの手首カメラ。プロトタイプは OV2735 モジュールを使用しました。モジュールサイズとカメラホルダーに対する取付穴を確認してください。 | [Amazon](https://www.amazon.com/innomaker-Computer-Raspberry-Support-Windows/dp/B0CNCSFQC1/) | $19.00 | [Aliexpress](https://www.aliexpress.us/item/3256804452094739.html) | $26.10 | [Amazon EU](https://www.amazon.fr/InnoMaker-Raspberry-Compatible-Windows-Android/dp/B0CNCSFQC1/) | €21.00 | $19.00 |
| **合計** |  |  |  |  |  |  |  |  | **$50.50** |

<a id="mechanical-parts"></a>
## 機械部品

| 品目 | 寸法 | 数量 | 使用箇所 | 米国で購入 | 単価（米国） | 米国で購入 | 単価（米国） | EUで購入 | 単価（EU） | 合計 (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 玉軸受 6812 | 60 × 78 × 10 mm | 2 | ベース回転 ロボットアームごとに一つ | [Amazon](https://www.amazon.com/Othmro-6812-2RS-60x78x10mm-Accuracy-Bearing/dp/B081W9QL2Z/) | $5.90 | [Aliexpress](https://www.aliexpress.us/item/3256812369319030.html) | $39.60 / 2 | [Amazon EU](https://www.amazon.fr/-/en/XYWHPGV-6812-2RS-Groove-Bearings-Chrome/dp/B0CQLT6J6D/) | €7.40 / 2 | $11.80 |
| フランジ軸受 MF106ZZ | 6 × 10 × 3 mm | 2 | グリッパーのメインフレーム | [Amazon](https://www.amazon.com/METERXITY-Shielded-Bearings-Wheelbarrow-Machines/dp/B0F4QXJSRQ/) | $6.60 / 4 | [Aliexpress](https://www.aliexpress.us/item/3256807821523719.html) | $6.00 / 10 | [Amazon EU](https://www.amazon.fr/-/en/PRECISCRY-DE-SGQ-FLZC-11-MF128ZZ-8x12x3-5-5Pcs/dp/B0GQK9BGWK/) | €11.60 / 5 | $1.20 |
| ロッド (ステンレス鋼丸棒、直径 6mm、長さ 125mm) | Ø6×125 mm、炭素または鋼 | 2 | グリッパーのガイド | [Amazon](https://www.amazon.com/SKYPRO-Stainless-Diameter-Industry-Working/dp/B0CLCSWSJ9?th=1) | $11.90 / 5 | [Aliexpress](https://www.aliexpress.us/item/3256805290944526.html) | $2.80 | [Amazon EU](https://www.amazon.fr/-/en/SKYPRO-Stainless-Diameter-Industry-Metalworking/dp/B0CLCSWSJ9/) | €14.40 / 5 | $4.76 |
| アルミ製ガイドチューブ, 代替品 | Ø6 × 4 × 125 mm; 1 × 300 mm から 2 × 125 mm に切断し、バリを除去 | 2 | 鋼製グリップガイドロッドの代替品 | [Amazon](https://www.amazon.com/dp/B0DRG94GJB/) | $9.99 / 3 本 | [Aliexpress](https://www.aliexpress.us/item/3256804988048256.html) | $4.05 / 1 本 | [Amazon EU](https://www.amazon.de/dp/B0D266J2NF/) | €14.89 / 3 本 | $3.33 (代替品) |
| カーボンチューブ (カーボンチューブ, 6mm x 4mm x 125mm), 代替 | Ø6 × 4 × 125 mm | 2 | 鋼製グリップガイドロッドの代替品 | [Amazon](https://www.amazon.com/MECCANIXITY-Carbon-Pultruded-Airplane-Quadcopter/dp/B0CZDCW2NL/) | $5.60 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256812851232051.html) | $5.90 / 2 | [Amazon EU](https://www.amazon.fr/-/en/QUARKZMAN-Carbon-Fiber-Tubes-Aircraft/dp/B0CZQVN7JB/) | €8.10 / 2 | $5.60 (代替) |
| Cクランプ | 3インチ、0-75 mm開口 | 4 | ロボットアームごとに２つ テーブルの基礎を固定する | [Amazon](https://www.amazon.com/Inch-Clamp-Woodworking-Precision-Carpentry/dp/B0FLHZVM7G/) | $10.00 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256813098676278.html) | $9.70 | [Amazon EU](https://www.amazon.fr/Performance-75mm-Adjustable-Stainless-Metalworking/dp/B0GSQL9BCN/) | €17.40 / 2 | $20.00 |
| **合計** |  |  |  |  |  |  |  |  |  | **$37.76** |

<a id="fasteners"></a>
## 締結部品

組み立てブックレットに記載されているキットの総数です。

印刷した樹脂に適合する取り外し可能なねじロック剤（例：[Vibra-Tite VC-3](https://www.vibra-tite.com/faq/if-vc-3-has-mek-how-can-it-be-plastic-compatible/)）を使用してください。VC-3 は金属ねじのねじ部に塗布し、組立前に完全に乾燥させます（[技術資料](https://www.vibra-tite.com/wp-content/uploads/213_tds.pdf)では最低 30 分）。未乾燥の状態で樹脂に塗布しないでください。まず同じフィラメントの試作品で適合性を確認してください。

| 締結部品 | 規格 | 数量 | 米国で購入 | 単価（米国） | 米国で購入 | 単価（米国） | EUで購入 | 単価（EU） | 合計 (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M2 × 6 六角穴付きボルト | DIN 912 | 28 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY8XHB1/) | $6.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZP1XT/) | €6.60 / 60 | $1.04 |
| M2 × 8 六角穴付きボルト | DIN 912 | 12 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY7L8YJ/) | $6.60 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZKVDN/) | €7.00 / 60 | $0.49 |
| M3 × 10 皿ねじ | DIN 7991 | 64 | [Amazon](https://www.amazon.com/M3-0-5-Socket-Screws-Alloy-Threaded/dp/B08HNF3J3D/) | $9.00 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY12R93P/) | €8.00 / 60 | $4.59 |
| M3 × 16 皿ねじ | DIN 7991 | 36 | [Amazon](https://www.amazon.com/Skweawert-40-Pcs-M3x16mm-countersunk/dp/B0D7MY32JZ/) | $6.20 / 40 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY138MGY/) | €8.00 / 60 | $2.95 |
| M3 × 4 止めねじ | DIN 913 | 4 | [Amazon](https://www.amazon.com/Generic-Bathroom-Fixtures-Furniture-Project/dp/B0H8DPZJPQ/) | $4.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256805653005840.html) | $2.10 / 10 | [Amazon EU](https://www.amazon.fr/-/en/MIETONG-Hex-Socket-Grub-Screws/dp/B0FSKLJR93/) | €6.00 / 20 | $0.31 |
| M2 六角ナット | DIN 934 | 12 | [Amazon](https://www.amazon.com/1-10Pcs-M1-M20-Stainless-Steel-Loose/dp/B0GVMQ3VD5/) | $3.50 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC5QKH9/) | €6.00 / 20 | $0.42 |
| M3 六角ナット | DIN 934 | 36 | [Amazon](https://www.amazon.com/FOCMKEAS-Stainless-Hexagon-Fasteners-Hardware/dp/B0CR7WL4D6/) | $3.70 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.00 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC7PD4Q/) | €6.30 / 50 | $1.44 |
| M3 × 6 フィリップスヘッドねじ | サーボ付属品 | 16 | サーボに付属します。 | — | — | — | — | — | — |
| 自在ねじ 2 × 6 | サーボ付属品 | 20 | サーボに付属します。 | — | — | — | — | — | — |
| **合計** |  |  |  |  |  |  |  |  | **$11.24** |

黒色のファスナーはレンダリングに合うが必要ではない。

<a id="printing-materials"></a>
## 印刷材料

| 材料 | 用途 | 購入リンク | 価格 / 予算 (USD) | 合計 (USD) |
|---|---|---|---|---:|
| Fiberon PET-CF17 | アームのリンクとサーボホルダー | [Polymaker](https://shop.polymaker.com/products/fiberon-pet-cf17) | $44.99 / 1 kg | $18.00 (0.4 kg) |
| PETG または PET-CF | グリップクランプ，カバー，リーダーロボットアームハンドル，トリガー | [Amazon](https://www.amazon.com/Bambu-Printer-Filament-1-75mm-Spool/dp/B0GS568LQ1/) | PETG: $21.00 / 1 kg | $15.75 (0.75 kg) |
| **合計** |  |  |  | **$33.75** |

使用する [印刷ガイド](printing.md) 3Dプリンタのスライサーを使って また切り取ります 3MF プリンタのフィラメント量と設定を決めるプロジェクト

<a id="tools"></a>
## 工具

小さなヘキサゴンキーとスクリュードライバーのセットを持っていない場合は、**$10.00** 程度を許可してください。

- M2 ネジのヘキサゴンキー 1.5 mm: [Amazon search](https://www.amazon.com/s?k=1.5mm+hex+key)
- M3 ネジのヘキサゴンキー 2 mm: [Amazon search](https://www.amazon.com/s?k=2mm+hex+key)
- フィリップス PH1 サーボモーターのホーンねじ用のスクリュードライバー:Amazon search](https://www.amazon.com/s?k=PH1+Phillips+screwdriver)
<!-- /translated-content -->
