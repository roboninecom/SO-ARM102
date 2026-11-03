<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](README.md) · [العربية](../ar/README.md)

[अंग्रेज़ी मूल](../../../README.md)

[दस्तावेज़](README.md) · [प्रिंटिंग](docs/printing.md) · [सामग्री सूची](docs/bom.md) · [असेंबली](docs/assembly-guide.md) · [विनिर्देश](docs/specifications.md) · [मॉडल](models/README.md) · [योगदान](CONTRIBUTING.md) · [लाइसेंस](LICENSING.md) · [अनुवाद](docs/translations.md)

> यह दस्तावेज़ का पूर्ण अनुवाद है। चित्र और मूल PDF पुस्तिका सभी भाषाओं में साझा हैं। अनुवाद AI की सहायता से तैयार किया गया है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102"></a>
# SO-ARM 102

<div align="center">

[![SO-ARM 102](../../../assets/images/photos/so-arm-102-live.jpg)](../../../assets/video/so-arm-102-preview.mp4)

**🎥 [पूर्वावलोकन वीडियो देखें](../../../assets/video/so-arm-102-preview.mp4)**·**🛒 [किट खरीदें](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

**SO-ARM 102 टेलीऑपरेशन और अनुकरण से सीखने के लिए एक ओपन-सोर्स लीडर–फॉलोअर रोबोट आर्म किट है। प्रत्येक आर्म में पाँच स्वतंत्रता की डिग्रियाँ और एक ग्रिपर है।**

<p align="left">
SO-ARM 100 और 101 पर आधारित यह किट अधिक कठोर PET-CF फ्रेम को समानांतर ग्रिपर के साथ जोड़ता है।
</p>

[![हार्डवेयर: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt) [![सॉफ्टवेयर: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt) [![डॉक्यूमेंट्स: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt) [![GitHub release](https://img.shields.io/github/v/release/roboninecom/SO-ARM-102)](https://github.com/roboninecom/SO-ARM-102/releases/latest)

📩 [hello@robonine.com](mailto:hello@robonine.com)

**DIY बजट: ~$340 घटकों के लिए, या ~$374 मुद्रण सामग्री सहित. ** [BOM सारांश](#bill-of-materials) · [Itemised लागत और खरीद लिंक](docs/bom.md#estimated-kit-cost)

> बजाय भागों का स्रोत नहीं और उन्हें स्वयं मुद्रित करें? **[SO-ARM 102 किट खरीदें](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

</div>

---

<a id="-what-changed-against-so-arm-101"></a>
## ✨ SO-ARM 101 के खिलाफ क्या बदल गया

|  | SO-ARM 101 | SO-ARM 102 |
|---|---|---|
| ग्रिपर | कोणीय जबड़ा | समानांतर ग्रिपर, 85 mm क्षेत्र |
| फ़्रेम की सामग्री | PLA | PET-CF (Fiberon PET-CF17 परीक्षण) |
| संरचना | ठोस लिंक | टोपोलॉजी-अनुकूलित लिंक |
| आधार के घूमने की सीमा | 220° | **352°** |
| क्षैतिज पहुँच | 441 mm | **483 mm** |
| ग्रिपर पर विवर्तन, 300 g लोड ¹ | 7.5 mm | **3.4–3.9 mm** |
| कंधे तथा कुल्हाड़ी गति | 45 RPM (STS3215) | **75 RPM (STS3250)** |
| 1 m पर शोर | 70 dB | **60 dB** |

¹ दोनों रोबोट हाथों को प्रिंटेड सर्वोमोटर डमी के साथ बनाया गया है, इसलिए फ्रेम की तुलना की जाती है, मोटर नहीं. पूर्ण परिणाम और परीक्षण स्थिति [docs/specifications.md](docs/specifications.md) में हैं.

---

<a id="-preview"></a>
## 🎥 पूर्वावलोकन

<div align="center">

[![SO-ARM 102 पूर्वावलोकन](../../../assets/video/so-arm-102-preview.gif)](../../../assets/video/so-arm-102-preview.mp4)

* पूर्ण वीडियो के लिए क्लिक करें, 21 s *

</div>

---

<a id="-configurations"></a>
## कॉन्फ़िगरेशन

<a id="single-arm-one-leader--one-follower"></a>
### एकल रोबोट हाथ: एक नेता रोबोट हाथ + एक अनुयायी रोबोट हाथ

मानक किट. लीडर रोबोट हाथ को हाथ से चलाएं, और फॉलोवर रोबोट हाथ इस गति को दोहराता है. इसे दूरसंचार के लिये तथा अनुकरण सीखने के लिये प्रदर्शन रिकॉर्ड करने के लिये प्रयोग करें.

![एक लीडर और एक फॉलोअर](../../../assets/images/renders/config-single-arm.jpg)

<a id="bimanual-two-leaders--two-followers"></a>
### द्वि- हस्त: दो नेता + दो अनुयायी

दो किट्स एक दूसरे के पास. हर हाथ अपने नेता रोबोट आर्म को चलाता है, इसलिये अनुयायी वस्तुओँ को पार कर सकते है, किसी भाग पर काम कर सकते है या कोई कार्य कर सकते है जिसके लिये दो हाथों की जरुरत होती है.

![दो लीडर और दो फॉलोअर](../../../assets/images/renders/config-dual-arm.jpg)

<a id="the-two-arms"></a>
### दो रोबोट हाथ

| फ़ॉलोअर | लीडर |
|:-:|:-:|
| ![फॉलोअर आर्म](../../../assets/images/renders/follower.jpg) | ![लीडर आर्म](../../../assets/images/renders/leader.jpg) |
| समानांतर ग्रिपर, कलाई कैमरा, 12 V | ट्रिगर के साथ हैंडल करें, 5 V |

---

<a id="-build-it-in-four-steps"></a>
## 🚀 इसे चार चरणों में बनाएं

तैयार किट पसंद करते हैं? **[SO-ARM 102 किट खरीदें](https://robonine.com/shop/so-arm102-robotic-arm-kit/) **.

<a id="1-print-the-parts"></a>
### 1. भागों को छापें

व्यक्तिगत भाग 180 × 180 mm 3D प्रिंटर बिल्ड प्लेट में फिट होते हैं. सबसे बड़ा हिस्सा 160 mm लंबा है. उपलब्ध 3MF प्लेट लेआउट 256 × 256 mm 3D प्रिंटर बिल्ड प्लेट का उपयोग करते हैं.

- 3MF सहेजे गए अभिमुखीकरण और समर्थन विन्यास के साथ स्लाइसर परियोजनाएँ: [`models/3mf/`](../../../models/3mf) - [लीडर रोबोट आर्म](../../../models/3mf/SO102_leader.3mf), [फ़ोलोअर रोबोट आर्म](../../../models/3mf/SO102_follower_arms.3mf), [फॉलोअर ग्रिपर और बेस](../../../models/3mf/SO102_follower_gripper_base.3mf)
- परियोजना सामग्री और प्रिंटर प्रोफ़ाइल: [models/README.md](models/README.md)
- STL फ़ाइलें, स्लाइस करने के लिए तैयार: [`models/stl/`](../../../models/stl)
- STEP स्रोत: [`models/step/`](../../../models/step)
- सामग्री, विन्यास और भाग मात्रा: [docs/printing.md](docs/printing.md)


<a id="2-buy-the-hardware"></a>
### 2. हार्डवेयर खरीदें

[BOM सारांश](#bill-of-materials) से घटकों का स्रोत और [पूरा BOM खरीदारी लिंक के साथ](docs/bom.md). घटकों के लिए बजट **$340.22**, या **$373.97** प्रिंटिंग सामग्री सहित, शिपिंग और करों से पहले.

| भुजा | सर्वो | नियंत्रक | बिजली आपूर्ति |
|---|---|---|---|
| फ़ॉलोअर | 2 × STS3235, 2 × STS3250, 2 × STS3215 | Waveshare Bus Servo Adapter | **12 V** |
| लीडर | 6 × STS3215 | Waveshare Bus Servo Adapter | **5 V** |

> ⚠️ **लीडर आर्म 5 V पर और फॉलोअर आर्म 12 V पर चलता है।** दोनों की बिजली आपूर्ति आपस में न बदलें।

<a id="3-assemble"></a>
### 3. इकट्ठा करें

- मुद्रण योग्य पुस्तिका, 32 पृष्ठ A5: [docs/SO-ARM102_assembly_A5_v0.7.pdf](../../SO-ARM102_assembly_A5_v0.7.pdf)
- भागों और फास्टनर के साथ चरण सूची: [docs/assembly-guide.md](docs/assembly-guide.md)

औज़ार: हेक्स कुंजियाँ 1.5 mm (M2 स्क्रू) और 2 mm (M3 स्क्रू).

<a id="4-set-up-the-software"></a>
### 4. सॉफ्टवेयर सेटअप करें

सर्वो आईडी, कैलिब्रेशन तथा पाठ: **[lab.robonine.com](https://lab.robonine.com)**.
SO-ARM 102 फॉलोअर प्लगइन का उपयोग मानक `so101_leader` प्रकार के साथ करें।
**[LeRobot इंस्टॉलेशन और सेटअप](docs/lerobot.md)**.

---

<a id="bill-of-materials"></a>
## सामग्री सूची

**एक लीडर रोबोट आर्म + एक फॉलोवर रोबोट आर्म** के लिए मात्रा और संदर्भ लागत:

| श्रेणी / खरीदारी लिंक | किट की सामग्री | कुल (USD) |
|---|---|---:|
| [सर्वो](docs/bom.md#servos) | 6 × STS3215 7.4 V, 2 × STS3215 12 V, 2 × STS3235, 2 × STS3250 | $240.72 |
| [इलेक्ट्रॉनिक्स](docs/bom.md#electronics) | 2 नियंत्रक, 2 पावर सप्लाई, 2 यूएसबी केबल, 1 कलाई कैमरा | $50.50 |
| [यांत्रिक पुर्ज़े](docs/bom.md#mechanical-parts) | 4 बेयरिंग्स, 2 स्टील गाइड रॉड्स, 4 टेबल क्लैंप्स | $37.76 |
| [फ़ास्टनर](docs/bom.md#fasteners) | स्क्रू तथा नट्स; निर्दिष्ट सर्वोमोटर- किट स्क्रू शामिल हैं | $11.24 |
| **पुर्ज़ों का उप-योग** |  | **$340.22** |
| [मुद्रण सामग्री](docs/bom.md#printing-materials) | 0.4 kg PET-CF17 + 0.75 kg PETG आवंटन | $33.75 |
| **प्रिंट सामग्री सहित कुल** |  | **$373.97** |

उदाहरण के पूर्ण पैक और फ़िलामेंट स्पूल को खरीदने में **$435** की लागत होती है, जिसमें अप्रयुक्त spares शामिल हैं. ये संदर्भ अनुमान हैं, नए आपूर्तिकर्ता उद्धरण नहीं. शिपिंग, कर, उपकरण, एक कंप्यूटर, एक प्रिंटर, बिजली और इकट्ठा श्रम को बाहर किया जाता है. आदेश देने से पहले आपूर्तिकर्ता मूल्यों, भिन्नताओं और न्यूनतम आदेश मात्रा की पुष्टि करें; फ़िलामेंट खपत जाँचने के लिए 3MF परियोजना को फिर से 3D प्रिंटिंग स्लाइसर का उपयोग करके काट लें.

[पूर्ण BOM, खरीद लिंक और लागत धारणा](docs/bom.md#estimated-kit-cost).

---

<a id="urdf-export"></a>
## URDF निर्यात

मौज़ूदा स्टैंडअलोन निर्यात [`simulation/urdf/`](../../../simulation/urdf): [URDF](../../../simulation/urdf/so_arm_102.urdf) · [Xacro](../../../simulation/urdf/so_arm_102.xacro) में है. `meshes/` को वर्णन फ़ाइल के बगल में रखें; मेश पथ इस फ़ोल्डर से संबंधित हैं.

- **विज़ुअल्स:**STL मेश.**टकराएँ:** सभी आठ लिंक पर फिट, स्वतंत्र रूप से घूमते बक्से.
- **द्रव्यमान अनुमान:**PLA, 30% भरें, 6 परिधि, 6 शीर्ष/निचला परत, 0.2 mm परत ऊंचाई, और**0.40 mm एक्सट्र्यूशन चौड़ाई**. ये सिमुलेशन धारणाएँ हैं; प्रयोग करें [मुद्रण मार्गदर्शक](docs/printing.md) निर्माण विन्यास के लिए.
- **हार्डवेयर द्रव्यमान:**प्रत्येक 70 g पर छह मोटर; आधार bearing 105 g पर. कुल अनुमानित मॉडल द्रव्यमान:**0.889 kg**.
- ** ग्रिपर:** `clamp2` गुणक `-1` के साथ `clamp1` की नकल करता है.

[निर्यात विन्यास](../../../simulation/urdf/export_settings.json) और [द्रव्यमान गुण](../../../simulation/urdf/mass_properties.json) धारणाओं को रिकॉर्ड करते हैं. ज्यामिति तथा जड़ता जाँच में रिकॉर्ड किए जाते हैं [export_verification.json](../../../simulation/urdf/export_verification.json).

---

<a id="-repository-structure"></a>
## रिपोजिटरी संरचना

```
├── models/
│   ├── 3mf/                 # स्लाइसर परियोजनाएँ: लीडर रोबोट आर्म, फॉलोवर रोबोट आर्म, ग्रिपर तथा बोर्ड केस
│   ├── stl/                 # प्रिंट- तैयार मेश
│   │   ├── common/          # कंट्रोलर केस सहित साझा भाग
│   │   ├── follower/        # समानांतर ग्रिपर और कैमरा माउंट
│   │   └── leader/          # हैंडल, ट्रिगर और कलाई रोल
│   └── step/                # CAD स्रोत, stl / के रूप में एक ही खाका
├── docs/
│   ├── printing.md          # सामग्री, स्लाइसर विन्यास, मात्रा
│   ├── bom.md               # सामग्री सूची
│   ├── assembly-guide.md    # भागों और फास्टनर के साथ चरण सूची
│   ├── specifications.md    # ज्यामिति, सर्वोमोटर, मापा परिणाम vs SO-ARM 101
│   └── SO-ARM102_assembly_A5_v0.7.pdf
├── assets/
│   ├── images/              # फोटो, रेंडर, पुस्तिका पृष्ठ, परीक्षण फोटो
│   └── video/               # वीडियो तथा GIF का पूर्वावलोकन करें
├── LICENSING.md             # कौन सा लाइसेंस किस फ़ाइल को कवर करता है
└── NOTICE                   # तृतीय पक्ष श्रेय
```

---

<a id="-known-issues"></a>
## ⚠️ ज्ञात समस्याएँ

स्वतंत्र परीक्षण से मिले असेंबली नोट; जोड़ते समय इन्हें जाँचें।

1. **v0.7 पुस्तिका का उपयोग करें।** पुरानी पुस्तिकाएँ HAT नियंत्रक और पुराने ग्रिपर भाग दिखाती हैं। v0.7 में दोनों आर्म पर Bus Servo Adapter लगाया जाता है।
2. **M2 स्क्रू कई स्थानों पर पहुँचना कठिन है.** उनमें से कुछ के साथ लड़ने की उम्मीद करें.
3. **ग्रिपर्स क्लैंप्स कार्बन रॉड्स पर सख्त चलते हैं.** क्लैंप बोर 6.1 mm के लिए आकार में होते हैं. रोड व्यास आपूर्तिकर्ताओं के बीच भिन्न होता है, इसलिए इकाई से पहले फिट को जाँचें.
4. ** प्रत्येक जोड़ को बंद करने से पहले सर्वोमोटर केबल की लंबाई को जाँचें, विशेष रूप से आधार से कंधे तक।
5. ** पुस्तक के दो स्थानों पर इकट्ठा करने का अनुक्रम असुविधाजनक है. फिक्सिंग से पहले दो कदम आगे पढ़ें.
6.  ** लीडर रोबोट हाथ जोड़े लचीले महसूस कर सकते हैं.** प्रत्येक सर्वोमोटर और इसके हॉर्न के बीच 8 × 2 mm रबर ओ-रिंग्स जोड़ने से लीडर रोबोट हाथ को सुचारू, शांत घर्षण मिलता है. जोड़ों 1–4 पर प्रति सर्वोमोटर दो का उपयोग करें और जोड़ों 5–6 पर एक।

कुछ और मिला? कृपया [एक मुद्दा खोलें](https://github.com/roboninecom/SO-ARM-102/issues).

---

<a id="-star-history"></a>
## ⭐ स्टार का इतिहास

[![स्टार का इतिहास — SO-ARM 102](https://api.star-history.com/svg?repos=roboninecom/so-arm-102&type=date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm-102&type=date&legend=top-left)

---

<a id="-related-projects"></a>
## संबंधित परियोजनाएँ

- [SO-ARM100/101 पैरेलल ग्रिपर](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper), ग्रिपर जिसे SO-ARM 102 ग्रिपर से विकसित किया गया
- [SO-ARM101](https://github.com/TheRobotStudio/SO-ARM100) द्वारा TheRobotStudio, रोबोट हाथ इस डिजाइन सफल है
- [स्मार्ट सीरियल सर्वोमोटर की व्यावहारिक तुलना](https://robonine.com/smart-serial-servo-motor-comparison-robotics/), सर्वोमोटर विकल्प के पीछे परीक्षण
- [रोबोटिक रोबोट हाथों के लिए एक फिलामेंट चुनें](https://robonine.com/choosing-filament-for-robotic-arm-applications/), PET-CF के पीछे परीक्षण

---

<a id="-license"></a>
## लाइसेंस

सर्वाधिकार (c) 2026 Robonine. विभिन्न प्रकार की सामग्री के लिए भिन्न लाइसेंस हैं:

| सामग्री | लाइसेंस |
|---|---|
| `models/` में हार्डवेयर डिजाइन | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| सॉफ्टवेयर तथा कॉन्फ़िगरेशन | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| `docs/`, `assets/`, सभी `README.md` में दस्तावेज़ीकरण और छवियाँ | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

फ़ाइल-दर-फ़ाइल मैप के लिए [LICENSING.md](LICENSING.md) और [REUSE.toml](../../../REUSE.toml) देखें.

---

<a id="-team"></a>
## टीम

| नाम | भूमिका | संपर्क |
|------|------|---------|
| **Alan Subin** | डिज़ाइन इंजीनियर: यांत्रिक डिजाइन, CAD, एसेम्बलिंग पुस्तिका | [LinkedIn](https://www.linkedin.com/in/alan-subin/) |
| **Boris Kotov** | सॉफ्टवेयर तथा परीक्षण इंजीनियर: प्रोटोटाइप, मुद्रण, परीक्षण rigs | [Telegram](https://t.me/bkotov) |
| **Nikita Bragin** | परियोजना प्रबंधक | [LinkedIn](https://www.linkedin.com/in/nikita-bragin-82296b29/) |
| **Mikhail Chistiakov** | औद्योगिक डिज़ाइनर: रोबोट हाथ का रूप व आकार | [Telegram](https://t.me/brrryska) |
| **Mikhail Zhmaylo** |  संरचनात्मक इंजीनियर: कठोरता मॉडल, विवर्तन को कम करने के लिए डिजाइन परिवर्तन | [Telegram](https://t.me/mikhail_zhmaylo) |
| **Vladislav Eremenko** |  संरचनात्मक इंजीनियर: शक्ति और थर्मल विश्लेषण, टोपोलॉजी अनुकूलन | [Telegram](https://t.me/v1ad_eremenko) |
| **Vladimir Osipov** | जाँचकर्ता तथा सलाहकार: स्वतंत्र परीक्षण निर्माण | [LinkedIn](https://www.linkedin.com/in/vladimirosipov/) |

<div align="center">

** [Robonine](https://robonine.com) द्वारा रोबोटिक्स समुदाय के लिए बनाया गया** 🤖

</div>
<!-- /translated-content -->
