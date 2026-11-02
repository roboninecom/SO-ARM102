<div dir="rtl" lang="ar">

<!-- translation-navigation -->
[English](../../en/docs/bom.md) · [Русский](../../ru/docs/bom.md) · [Español](../../es/docs/bom.md) · [Français](../../fr/docs/bom.md) · [Deutsch](../../de/docs/bom.md) · [Português (Brasil)](../../pt-BR/docs/bom.md) · [简体中文](../../zh-CN/docs/bom.md) · [日本語](../../ja/docs/bom.md) · [हिन्दी](../../hi/docs/bom.md) · [العربية](bom.md)

[الأصل الإنجليزي](../../../bom.md)

[الوثائق](../README.md) · [الطباعة](printing.md) · [قائمة المواد](bom.md) · [التجميع](assembly-guide.md) · [المواصفات](specifications.md) · [النماذج](../models/README.md) · [المساهمة](../CONTRIBUTING.md) · [التراخيص](../LICENSING.md) · [الترجمات](translations.md)

> هذه ترجمة كاملة للوثيقة. الرسوم وكتيب PDF الأصلي مشتركة بين اللغات. أعدت الترجمة بمساعدة الذكاء الاصطناعي ولم يراجعها متحدثون أصليون بعد.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="bill-of-materials"></a>
# قائمة المواد

الكميات هي لمجموعة كاملة واحدة: ذراع روبوت متتبع واحد وذرع روبوت قائد واحد. وترد الأجزاء المطبوعة بصورة منفصلة في [printing.md](printing.md).

<a id="estimated-kit-cost"></a>
## التكلفة التقديرية للمجموعة

** ذراع روبوت رئيسي واحد + ذراع روبوت متابعة واحد: $340 في المكونات، أو $374 بما في ذلك مواد الطباعة**.

| الفئة | تكلفة الكميات المستخدمة (بدولارات الولايات المتحدة) | شراء عبوات كاملة/أسطوانات (بدولارات الولايات المتحدة) |
|---|---:|---:|
| سيرفو (12 pcs) | $240.72 | $240.72 |
| الكترونيات وكاميرات وإمدادات كهربائية | $50.50 | $50.50 |
| المحامل، قضبان التوجيه الفولاذية وملاصقات الجداول | $37.76 | $49.70 |
| المثبتات | $11.24 | $28.60 |
| **المجموع الفرعي للمكونات** | **$340.22** | **$368.82** |
| مادة الطباعة: 0.4 kg PET-CF17 + 0.75 kg PETG | $33.75 | $66.0 |
| **الإجمالي مع مواد الطباعة** | **$373.97** | **$434.82** |

العمود ** المجموع (بدولارات الولايات المتحدة)** هو تكلفة الكمية اللازمة لمجموعة واحدة، باستخدام العطاء المرجعي خلف مجموع كل سطر قائم (وليس مجموع عروض الموردين). وتبلغ تكلفة المسامير المدرجة $0؛ ويستبعد من المجاميع الأنابيب الكربونية البديلة. وتستخدم التقديرات الأسعار المرجعية المبينة أدناه، مع تقريب كل سطر إلى السنت. وهي ليست عروضا جديدة للموردين: تأكد من المتغيرات المختارة والحد الأدنى لكميات الطلب والأسعار قبل طلبها. ولا يشمل ذلك الشحن والضرائب والأدوات والحاسوب والطابعة والكهرباء وعمل التجميع.

تشمل العلبة الكاملة قطع الغيار غير المستخدمة، 0.5 kg PET-CF17 spool و1 kg PETG spool. كميات الطباعة هي مخصصات الميزانية؛ شرائح مرة أخرى باستخدام شريحة الطباعة ثلاثية الأبعاد المشاريع 3MF المقدمة لوضعك. تكاليف القضيب تستخدم الفولاذ؛ أنبوب الكربون هو بديل.

![مجموعة معدات](../../../../assets/images/assembly/hardware.jpg)

<a id="servos"></a>
## محركات السيرفو

| المفصل | ID | الذراع التابع | الذراع القائد |
|---|:-:|---|---|
| دوران القاعدة | 1 | ST-3235-С001 | ST-3215-C066, 1:191 |
| رفع الكتف | 2 | ST-3250-С002 | ST-3215-C066, 1:191 |
| ثني المرفق | 3 | ST-3250-С002 | ST-3215-C066, 1:191 |
| ثني المعصم | 4 | ST-3235-С001 | ST-3215-C066, 1:191 |
| دوران المعصم | 5 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |
| القابض / الزناد | 6 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |

الإجمالي: 6 × STS3215 7.4V، 2 × STS3215 12V، 2 × STS3235 12V، 2 × STS3250 12V. كلها محركات سيرفو Feetech TTL ذات ناقل تسلسلي.

| محرك سيرفو | الكمية | الاختيار | رابط Aliexpress | سعر الوحدة (USD) | رابط Alibaba | سعر الوحدة (USD) | الإجمالي (USD) |
|---|---|---|---|---|---|---|---|
| STS3215 | 6 | 7.4V TTL نسخة للمحركات المساعدة لذراع الروبوت الرائد. اختار ST-3215-C066 (7.4V). | [Aliexpress](https://www.aliexpress.us/item/3256811860804361.html) | $32.8 | [Alibaba](https://www.alibaba.com/product-detail/Feetech-SO-ARM101-LeRobot-Open-Source_1601636174153.html) | $6.74 | $40.44 |
| STS3215 | 2 | صيغة 12V TTL لمفاصل ذراع الروبوت المتتبع 5 و6. اختار ST-3215-C049 (12V30KG). | [Aliexpress](https://www.aliexpress.us/item/3256811832699316.html) | $55.8 لـ 2pcs | [Alibaba](https://www.alibaba.com/product-detail/6pcs-12V-30KG-1-345-STS3215_1601900233170.html) | $14.70 | $29.40 |
| STS3235 | 2 | صيغة 12V TTL لمفاصل ذراع الروبوت المتتبع 1 و4. | [Aliexpress](https://www.aliexpress.us/item/3256810213842277.html) | $63 | [Alibaba](https://www.alibaba.com/product-detail/FEETECH-STS3235-12V-30KG-TTL-Dual_1601910640629.html) | $40.79 | $81.58 |
| STS3250 | 2 | صيغة 12V TTL لمفاصل ذراع الروبوت المتتبع 2 و3. | [Aliexpress](https://www.aliexpress.us/item/3256811995148799.html) | $126.4 لـ 2pcs | [Alibaba](https://www.alibaba.com/product-detail/Feetech-STS3250-12V-50kg-Servo-High_1601711893549.html) | $44.65 | $89.30 |
| **الإجمالي** |  |  |  |  |  |  | **$240.72** |

- ** الذراع الروبوتية التالية، 12V.** STS3250 هو محرك خدمة بدون فرش 50 kg × سم عند 75 RPM، وهو يقود المفصلين اللذين يحملان أكبر قدر من الحمولة. STS3235 هو محرك خدمة بحجم 30 kg × سم مع حركة عكسية أقل من STS3215.
- **ذراع الروبوت القيادي، 5V.**محركات سيرفو ذراع الروبوت القيادي تقرأ فقط، ولا تحمل أبدا. يمكنك استخدام ST-3215-C066 سلبي بدون محرك وعجلة نقل** فقط** لذرع الروبوت القيادي.
- تتوفر مع محركات السيرفو قرون سيرفو و M3 × 6 مسمار سيرفو.

<a id="electronics"></a>
## الإلكترونيات

| العنصر | الكمية | ملاحظات | الشراء في الولايات المتحدة | تكلفة الوحدة (الولايات المتحدة) | الشراء في الولايات المتحدة | تكلفة الوحدة (الولايات المتحدة) | الشراء في الاتحاد الأوروبي | تكلفة الوحدة (الاتحاد الأوروبي) | الإجمالي (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Waveshare Bus Servo Adapter | 2 | متحكم السيرفو | [Amazon](https://www.amazon.com/Waveshare-Integrates-Control-Applicable-Integrate/dp/B0CJ6TP3TP/) | $13.00 | [Aliexpress](https://www.aliexpress.us/item/3256810343532716.html) | $7.40 | [Amazon EU](https://www.amazon.fr/-/en/Serial-Integrates-Control-Circuit-Support/dp/B0CJBKQ8LJ/) | €11.90 | $14.80 |
| إمداد الطاقة 12V DC (12V 5A إمداد الطاقة 5.5 2.1mm) | 1 | للذراع التابعة. يوصى بمزوّد بقدرة 60W / 5A أو أكثر. بلغ تيار الذراع ذروته عند 3.3A تحت حمل 300g. تأكد من مطابقة موصل لوحة Adapter (5.5x2.1mm). | [Amazon](https://www.amazon.com/Power-Supply-Adapter-5-5x2-1-2-5mm/dp/B0C3CJF313/) | $10.00 | [Aliexpress](https://www.aliexpress.us/item/3256812113231032.html) | $6.60 | [Amazon EU](https://www.amazon.fr/-/en/zstg-Universal-Power-Supply-Connector/dp/B0GTLSRM91/) | €12.00 | $6.60 |
| إمداد الطاقة 5V DC (5V 2A إمداد الطاقة 5.5 2.1mm) | 1 | ذراع الروبوت القائد. توافق موصل المُعدّل (5.5x2.1mm). | [Amazon](https://www.amazon.com/MTDZKJG-Adapter-100V-240V-Transformer-Security/dp/B0BZP65GRW/) | $6.20 | [Aliexpress](https://www.aliexpress.us/item/3256812479558626.html) | $4.10 | [Amazon EU](https://www.amazon.fr/5V-2A-Supply-DC-Adapter/dp/B0GDXFRYJS/) | €11.00 | $4.10 |
| كابل USB-C، 1.5 متر (كابل بيانات USB A إلى USB C 1.5 متر) | 2 | واحد لكل جهاز تحكم اختار كابل بيانات وليس كابل شحن فقط | [Amazon](https://www.amazon.com/Data-Cable-1-5ft-10Gbps-Transfer/dp/B0FMJTHRCM/) | $6.00 | [Aliexpress](https://www.aliexpress.us/item/3256812299430938.html) | $3.00 | [Amazon EU](https://www.amazon.fr/-/en/10Gbps-Transfer-Charging-Samsung-External/dp/B0DHZ1R8FQ/) | €7.00 | $6.00 |
| آلة تصوير USB (OV2735، 1080P USB Camera Module, 2 MP 1920x1080, UVC camera, 2.8 or 3.0 mm lens) | 1 | كاميرا اليد على ذراع الروبوت المتتبع. استخدم النموذج الأولي وحدة OV2735. تحقق من أبعاد الوحدة وثقوب التثبيت ضد حامل الكاميرا. | [Amazon](https://www.amazon.com/innomaker-Computer-Raspberry-Support-Windows/dp/B0CNCSFQC1/) | $19.00 | [Aliexpress](https://www.aliexpress.us/item/3256804452094739.html) | $26.10 | [Amazon EU](https://www.amazon.fr/InnoMaker-Raspberry-Compatible-Windows-Android/dp/B0CNCSFQC1/) | €21.00 | $19.00 |
| **الإجمالي** |  |  |  |  |  |  |  |  | **$50.50** |

<a id="mechanical-parts"></a>
## الأجزاء الميكانيكية

| العنصر | المقاس | الكمية | الموضع | الشراء في الولايات المتحدة | تكلفة الوحدة (الولايات المتحدة) | الشراء في الولايات المتحدة | تكلفة الوحدة (الولايات المتحدة) | الشراء في الاتحاد الأوروبي | تكلفة الوحدة (الاتحاد الأوروبي) | الإجمالي (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| محمل كروي 6812 | 60 × 78 × 10 mm | 2 | قاعدة تناوب، واحدة لكل ذراع آلي | [Amazon](https://www.amazon.com/Othmro-6812-2RS-60x78x10mm-Accuracy-Bearing/dp/B081W9QL2Z/) | $5.90 | [Aliexpress](https://www.aliexpress.us/item/3256812369319030.html) | $39.60 / 2 | [Amazon EU](https://www.amazon.fr/-/en/XYWHPGV-6812-2RS-Groove-Bearings-Chrome/dp/B0CQLT6J6D/) | €7.40 / 2 | $11.80 |
| المحامل الشفافة MF106ZZ | 6 × 10 × 3 mm | 2 | الإطار الرئيسي للقابض | [Amazon](https://www.amazon.com/METERXITY-Shielded-Bearings-Wheelbarrow-Machines/dp/B0F4QXJSRQ/) | $6.60 / 4 | [Aliexpress](https://www.aliexpress.us/item/3256807821523719.html) | $6.00 / 10 | [Amazon EU](https://www.amazon.fr/-/en/PRECISCRY-DE-SGQ-FLZC-11-MF128ZZ-8x12x3-5-5Pcs/dp/B0GQK9BGWK/) | €11.60 / 5 | $1.20 |
| قضيب دائري من الفولاذ المقاوم للصدأ، قطره 6mm وطوله 125mm | قطر 6 × 125 mm، كربون أو فولاذ | 2 | أدلة القابض | [Amazon](https://www.amazon.com/SKYPRO-Stainless-Diameter-Industry-Working/dp/B0CLCSWSJ9?th=1) | $11.90 / 5 | [Aliexpress](https://www.aliexpress.us/item/3256805290944526.html) | $2.80 | [Amazon EU](https://www.amazon.fr/-/en/SKYPRO-Stainless-Diameter-Industry-Metalworking/dp/B0CLCSWSJ9/) | €14.40 / 5 | $4.76 |
| أنبوب توجيه من الألومنيوم, بديل | Ø6 × 4 × 125 mm; قص 1 × 300 mm إلى 2 × 125 mm؛ أزل النتوءات | 2 | بديل عن قضبان التوجيه الممسك الصلب | [Amazon](https://www.amazon.com/dp/B0DRG94GJB/) | $9.99 / 3 قطع | [Aliexpress](https://www.aliexpress.us/item/3256804988048256.html) | $4.05 / 1 قطعة | [Amazon EU](https://www.amazon.de/dp/B0D266J2NF/) | €14.89 / 3 قطع | $3.33 (بديل) |
| أنبوب كربوني (أنبوب كربوني، 6mm x 4mm x 125mm)، بديل | Ø6 × 4 × 125 mm | 2 | بديل عن قضبان التوجيه الممسك الصلب | [Amazon](https://www.amazon.com/MECCANIXITY-Carbon-Pultruded-Airplane-Quadcopter/dp/B0CZDCW2NL/) | $5.60 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256812851232051.html) | $5.90 / 2 | [Amazon EU](https://www.amazon.fr/-/en/QUARKZMAN-Carbon-Fiber-Tubes-Aircraft/dp/B0CZQVN7JB/) | €8.10 / 2 | $5.60 (بديل) |
| مشبك على شكل C | 3 بوصة، فتحة 0-75 mm | 4 | اثنان لكل ذراع آلي، لتثبيت القاعدة على الطاولة | [Amazon](https://www.amazon.com/Inch-Clamp-Woodworking-Precision-Carpentry/dp/B0FLHZVM7G/) | $10.00 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256813098676278.html) | $9.70 | [Amazon EU](https://www.amazon.fr/Performance-75mm-Adjustable-Stainless-Metalworking/dp/B0GSQL9BCN/) | €17.40 / 2 | $20.00 |
| **الإجمالي** |  |  |  |  |  |  |  |  |  | **$37.76** |

<a id="fasteners"></a>
## المثبتات

المجموع الكلي للمجموعات كما هو معبأ في كتيب التجميع.

استخدم مثبت لولب قابلاً للفك ومتوافقاً مع البلاستيك المطبوع، مثل [Vibra-Tite VC-3](https://www.vibra-tite.com/faq/if-vc-3-has-mek-how-can-it-be-plastic-compatible/). ضع VC-3 على لولب البرغي المعدني واتركه يجف تماماً قبل التجميع (30 دقيقة على الأقل وفق [ورقة البيانات الفنية](https://www.vibra-tite.com/wp-content/uploads/213_tds.pdf))؛ لا تضعه وهو رطب على البلاستيك. اختبر أولاً توافقه مع خيط الطباعة على قطعة تجريبية.

| المثبت | المعيار | الكمية | الشراء في الولايات المتحدة | تكلفة الوحدة (الولايات المتحدة) | الشراء في الولايات المتحدة | تكلفة الوحدة (الولايات المتحدة) | الشراء في الاتحاد الأوروبي | تكلفة الوحدة (الاتحاد الأوروبي) | الإجمالي (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M2 × 6 برأس أسطواني | DIN 912 | 28 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY8XHB1/) | $6.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZP1XT/) | €6.60 / 60 | $1.04 |
| M2 × 8 برأس أسطواني | DIN 912 | 12 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY7L8YJ/) | $6.60 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZKVDN/) | €7.00 / 60 | $0.49 |
| M3 × 10 برأس غاطس | DIN 7991 | 64 | [Amazon](https://www.amazon.com/M3-0-5-Socket-Screws-Alloy-Threaded/dp/B08HNF3J3D/) | $9.00 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY12R93P/) | €8.00 / 60 | $4.59 |
| M3 × 16 برأس غاطس | DIN 7991 | 36 | [Amazon](https://www.amazon.com/Skweawert-40-Pcs-M3x16mm-countersunk/dp/B0D7MY32JZ/) | $6.20 / 40 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY138MGY/) | €8.00 / 60 | $2.95 |
| M3 × 4 برغي تثبيت | DIN 913 | 4 | [Amazon](https://www.amazon.com/Generic-Bathroom-Fixtures-Furniture-Project/dp/B0H8DPZJPQ/) | $4.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256805653005840.html) | $2.10 / 10 | [Amazon EU](https://www.amazon.fr/-/en/MIETONG-Hex-Socket-Grub-Screws/dp/B0FSKLJR93/) | €6.00 / 20 | $0.31 |
| صامولة سداسية M2 | DIN 934 | 12 | [Amazon](https://www.amazon.com/1-10Pcs-M1-M20-Stainless-Steel-Loose/dp/B0GVMQ3VD5/) | $3.50 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC5QKH9/) | €6.00 / 20 | $0.42 |
| صامولة سداسية M3 | DIN 934 | 36 | [Amazon](https://www.amazon.com/FOCMKEAS-Stainless-Hexagon-Fasteners-Hardware/dp/B0CR7WL4D6/) | $3.70 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.00 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC7PD4Q/) | €6.30 / 50 | $1.44 |
| M3 × 6 مسمار رأس فيليبس | من طقم السيرفو | 16 | مرفق مع محركات السيرفو. | — | — | — | — | — | — |
| مسمار ذاتي الملء 2 × 6 | من طقم السيرفو | 20 | مرفق مع محركات السيرفو. | — | — | — | — | — | — |
| **الإجمالي** |  |  |  |  |  |  |  |  | **$11.24** |

وتتماشى الملحقات السوداء مع مظهر الجص ولكنها غير مطلوبة.

<a id="printing-materials"></a>
## مواد الطباعة

| المادة | الاستخدام | رابط الشراء | السعر / الميزانية (USD) | الإجمالي (USD) |
|---|---|---|---|---:|
| Fiberon PET-CF17 | وصلات الذراع وحوامل السيرفو | [Polymaker](https://shop.polymaker.com/products/fiberon-pet-cf17) | $44.99 / 1 kg | $18.00 (0.4 kg) |
| PETG أو PET-CF | صمامات، وأغطية، ومقبض الذراع الروبوتي الرئيسي، والزناد | [Amazon](https://www.amazon.com/Bambu-Printer-Filament-1-75mm-Spool/dp/B0GS568LQ1/) | PETG: $21.00 / 1 kg | $15.75 (0.75 kg) |
| **الإجمالي** |  |  |  | **$33.75** |

استخدم [دليل الطباعة](printing.md) وقطع مرة أخرى باستخدام شريحة الطباعة الثلاثية الأبعاد المشاريع 3MF المقدمة لتحديد كمية الفتيل لطابعتك وإعداداتها.

<a id="tools"></a>
## الأدوات

أترك حوالي **$10.00** لمفتاح سداسي صغير ومجموعة من المراوح إذا كنت لا تمتلك هذه الأدوات.

- مفاتيح سداسية 1.5 mm للمراوح M2: [Amazon search](https://www.amazon.com/s?k=1.5mm+hex+key)
- مفاتيح سداسية 2 mm للمراوح M3: [Amazon search](https://www.amazon.com/s?k=2mm+hex+key)
- مكرِّر Phillips PH1 لمسامير القرن المحركات المساعدة: [Amazon search](https://www.amazon.com/s?k=PH1+Phillips+screwdriver)
<!-- /translated-content -->

</div>
