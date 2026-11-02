<!-- translation-navigation -->
[English](../../en/docs/bom.md) · [Русский](../../ru/docs/bom.md) · [Español](../../es/docs/bom.md) · [Français](bom.md) · [Deutsch](../../de/docs/bom.md) · [Português (Brasil)](../../pt-BR/docs/bom.md) · [简体中文](../../zh-CN/docs/bom.md) · [日本語](../../ja/docs/bom.md) · [हिन्दी](../../hi/docs/bom.md) · [العربية](../../ar/docs/bom.md)

[Original anglais](../../../bom.md)

[Documentation](../README.md) · [Impression](printing.md) · [Composants](bom.md) · [Montage](assembly-guide.md) · [Caractéristiques](specifications.md) · [Modèles](../models/README.md) · [Contribuer](../CONTRIBUTING.md) · [Licences](../LICENSING.md) · [Traductions](translations.md)

> Traduction intégrale du document. Les illustrations et le livret PDF original sont communs aux langues. Traduction assistée par IA, pas encore relue par des locuteurs natifs.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="bill-of-materials"></a>
# Nomenclature

Les quantités sont pour un kit complet: un bras robotique suivi et un bras robotique leader.Les pièces imprimées sont listées séparément dans [printing.md](printing.md).

<a id="estimated-kit-cost"></a>
## Coût estimatif de la trousse

**Un bras robot leader + un bras robot suiveur: $340 en composants, ou $374 y compris le matériel d'impression.**

| Catégorie | Coût des quantités utilisées (USD) | Acheter des paquets complets / bobines (USD) |
|---|---:|---:|
| Servos (12 pcs) | $240.72 | $240.72 |
| Électronique, caméra et alimentations électriques | $50.50 | $50.50 |
| Roulements, tiges de guidage en acier et pinces de table | $37.76 | $49.70 |
| Fixations | $11.24 | $28.60 |
| **Sous-total des composants** | **$340.22** | **$368.82** |
| Matériel d &apos; impression: 0.4 kg PET-CF17 + 0.75 kg PETG | $33.75 | $66.0 |
| **Total avec matériau d’impression** | **$373.97** | **$434.82** |

La colonne **Total (USD)** représente le coût de la quantité nécessaire pour un kit, en utilisant l'offre de référence derrière chaque total de ligne existant (et non la somme des offres des fournisseurs). Les vis incluses coûtent $0; les tubes carbone alternatifs sont exclus des totaux. Les estimations utilisent les prix de référence indiqués ci-dessous, avec chaque ligne arrondie au centime le plus proche. Ce ne sont pas de nouveaux devis fournisseurs: confirmez les variantes sélectionnées, les quantités minimales de commande et les prix avant de commander.

La colonne de pack complet comprend des pièces de rechange non utilisées, 0.5 kg PET-CF17 bobine et 1 kg PETG bobine. Les quantités d'impression sont des allocations budgétaires; coupez à nouveau en utilisant le trancheur d'impression 3D les 3MF projets fournis pour vos paramètres.

![Kit matériel](../../../../assets/images/assembly/hardware.jpg)

<a id="servos"></a>
## Servomoteurs

| Articulation | ID | Bras suiveur | Bras leader |
|---|:-:|---|---|
| Rotation de la base | 1 | ST-3235-С001 | ST-3215-C066, 1:191 |
| Élévation de l’épaule | 2 | ST-3250-С002 | ST-3215-C066, 1:191 |
| Flexion du coude | 3 | ST-3250-С002 | ST-3215-C066, 1:191 |
| Flexion du poignet | 4 | ST-3235-С001 | ST-3215-C066, 1:191 |
| Rotation du poignet | 5 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |
| Pince / gâchette | 6 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |

Total: 6 × STS3215 7.4V, 2 × STS3215 12V, 2 × STS3235 12V, 2 × STS3250 12V. Tous sont des servomoteurs à bus série Feetech TTL.

| Servomoteur | Qté | Sélection | Aliexpress lien | Prix unitaire (USD) | Alibaba lien | Prix unitaire (USD) | Total (USD) |
|---|---|---|---|---|---|---|---|
| STS3215 | 6 | 7.4V TTL version pour servomoteurs de bras robotique leader. Sélectionnez ST-3215-C066 (7.4V). | [Aliexpress](https://www.aliexpress.us/item/3256811860804361.html) | $32.8 | [Alibaba](https://www.alibaba.com/product-detail/Feetech-SO-ARM101-LeRobot-Open-Source_1601636174153.html) | $6.74 | $40.44 |
| STS3215 | 2 | Version 12V TTL pour les articulations des bras robotiques suiveurs 5 et 6. Sélectionnez ST-3215-C049 (12V30KG). | [Aliexpress](https://www.aliexpress.us/item/3256811832699316.html) | $55.8 pour 2pcs | [Alibaba](https://www.alibaba.com/product-detail/6pcs-12V-30KG-1-345-STS3215_1601900233170.html) | $14.70 | $29.40 |
| STS3235 | 2 | 12V TTL version pour les articulations de bras robotique suiveur 1 et 4. | [Aliexpress](https://www.aliexpress.us/item/3256810213842277.html) | $63 | [Alibaba](https://www.alibaba.com/product-detail/FEETECH-STS3235-12V-30KG-TTL-Dual_1601910640629.html) | $40.79 | $81.58 |
| STS3250 | 2 | 12V TTL version pour les articulations de bras robotique suiveur 2 et 3. | [Aliexpress](https://www.aliexpress.us/item/3256811995148799.html) | $126.4 pour 2pcs | [Alibaba](https://www.alibaba.com/product-detail/Feetech-STS3250-12V-50kg-Servo-High_1601711893549.html) | $44.65 | $89.30 |
| **Total** |  |  |  |  |  |  | **$240.72** |

- **Bras robotique suivant, 12V.** STS3250 est un servomoteur brushless de 50 kg·cm à 75 RPM. Il entraîne les deux articulations qui portent le plus de charge. STS3235 est un servomoteur de 30 kg·cm avec moins de jeu que le STS3215.
- **Bras robot leader, 5V.**Les servomoteurs du bras robot leader sont seulement lus, jamais chargés. Vous pouvez utiliser un ST-3215-C066 passif sans moteur et boîte de vitesses**uniquement** pour le bras robot leader.
- Les klaxons servo et les vis à claxon M3 × 6 sont livrés avec les servomoteurs.

<a id="electronics"></a>
## Électronique

| Article | Qté | Remarques | Achat aux États-Unis | Prix unitaire (États-Unis) | Achat aux États-Unis | Prix unitaire (États-Unis) | Achat dans l’UE | Prix unitaire (UE) | Total (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Waveshare Bus Servo Adapter | 2 | Contrôleur de servos | [Amazon](https://www.amazon.com/Waveshare-Integrates-Control-Applicable-Integrate/dp/B0CJ6TP3TP/) | $13.00 | [Aliexpress](https://www.aliexpress.us/item/3256810343532716.html) | $7.40 | [Amazon EU](https://www.amazon.fr/-/en/Serial-Integrates-Control-Circuit-Support/dp/B0CJBKQ8LJ/) | €11.90 | $14.80 |
| Alimentation 12V DC (12V 5A alimentation 5.5 2.1mm) | 1 | Bras suiveur. Alimentation de 60W / 5A ou plus recommandée. Le courant a atteint 3.3A sous une charge de 300g. Vérifiez la compatibilité avec le connecteur du Adapter (5.5x2.1mm). | [Amazon](https://www.amazon.com/Power-Supply-Adapter-5-5x2-1-2-5mm/dp/B0C3CJF313/) | $10.00 | [Aliexpress](https://www.aliexpress.us/item/3256812113231032.html) | $6.60 | [Amazon EU](https://www.amazon.fr/-/en/zstg-Universal-Power-Supply-Connector/dp/B0GTLSRM91/) | €12.00 | $6.60 |
| Alimentation 5V DC (5V 2A alimentation 5.5 2.1mm) | 1 | Connectez le connecteur de l'adaptateur (5.5x2.1mm) au bras robotique du leader. | [Amazon](https://www.amazon.com/MTDZKJG-Adapter-100V-240V-Transformer-Security/dp/B0BZP65GRW/) | $6.20 | [Aliexpress](https://www.aliexpress.us/item/3256812479558626.html) | $4.10 | [Amazon EU](https://www.amazon.fr/5V-2A-Supply-DC-Adapter/dp/B0GDXFRYJS/) | €11.00 | $4.10 |
| Câble de USB-C, 1.5 m (câble de données USB A vers USB C 1.5m) | 2 | Un par manette. Choisissez un câble de données, pas un câble de chargement seulement. | [Amazon](https://www.amazon.com/Data-Cable-1-5ft-10Gbps-Transfer/dp/B0FMJTHRCM/) | $6.00 | [Aliexpress](https://www.aliexpress.us/item/3256812299430938.html) | $3.00 | [Amazon EU](https://www.amazon.fr/-/en/10Gbps-Transfer-Charging-Samsung-External/dp/B0DHZ1R8FQ/) | €7.00 | $6.00 |
| Caméra USB (OV2735, 1080P Module caméra USB, 2MP 1920x1080, caméra UVC, 2.8 ou 3.0 mm objectif) | 1 | Le prototype utilisait un module OV2735. Vérifiez les dimensions du module et les trous de montage par rapport au support de la caméra. | [Amazon](https://www.amazon.com/innomaker-Computer-Raspberry-Support-Windows/dp/B0CNCSFQC1/) | $19.00 | [Aliexpress](https://www.aliexpress.us/item/3256804452094739.html) | $26.10 | [Amazon EU](https://www.amazon.fr/InnoMaker-Raspberry-Compatible-Windows-Android/dp/B0CNCSFQC1/) | €21.00 | $19.00 |
| **Total** |  |  |  |  |  |  |  |  | **$50.50** |

<a id="mechanical-parts"></a>
## Pièces mécaniques

| Article | Dimensions | Qté | Emplacement | Achat aux États-Unis | Prix unitaire (États-Unis) | Achat aux États-Unis | Prix unitaire (États-Unis) | Achat dans l’UE | Prix unitaire (UE) | Total (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Roulement à billes 6812 | 60 × 78 × 10 mm | 2 | Rotation de base, une par bras robotique | [Amazon](https://www.amazon.com/Othmro-6812-2RS-60x78x10mm-Accuracy-Bearing/dp/B081W9QL2Z/) | $5.90 | [Aliexpress](https://www.aliexpress.us/item/3256812369319030.html) | $39.60 / 2 | [Amazon EU](https://www.amazon.fr/-/en/XYWHPGV-6812-2RS-Groove-Bearings-Chrome/dp/B0CQLT6J6D/) | €7.40 / 2 | $11.80 |
| Roulement à bride MF106ZZ | 6 × 10 × 3 mm | 2 | Châssis principal de la pince | [Amazon](https://www.amazon.com/METERXITY-Shielded-Bearings-Wheelbarrow-Machines/dp/B0F4QXJSRQ/) | $6.60 / 4 | [Aliexpress](https://www.aliexpress.us/item/3256807821523719.html) | $6.00 / 10 | [Amazon EU](https://www.amazon.fr/-/en/PRECISCRY-DE-SGQ-FLZC-11-MF128ZZ-8x12x3-5-5Pcs/dp/B0GQK9BGWK/) | €11.60 / 5 | $1.20 |
| Tige (Tige ronde en acier inoxydable, 6mm Diamètre, Longueur 125mm) | Ø6 × 125 mm, carbone ou acier | 2 | Guides de la pince | [Amazon](https://www.amazon.com/SKYPRO-Stainless-Diameter-Industry-Working/dp/B0CLCSWSJ9?th=1) | $11.90 / 5 | [Aliexpress](https://www.aliexpress.us/item/3256805290944526.html) | $2.80 | [Amazon EU](https://www.amazon.fr/-/en/SKYPRO-Stainless-Diameter-Industry-Metalworking/dp/B0CLCSWSJ9/) | €14.40 / 5 | $4.76 |
| Tube de guidage en aluminium, alternative | Ø6 × 4 × 125 mm; couper 1 × 300 mm en 2 × 125 mm ; ébavurer | 2 | Alternative aux tiges de guidage en acier | [Amazon](https://www.amazon.com/dp/B0DRG94GJB/) | $9.99 / 3 pcs | [Aliexpress](https://www.aliexpress.us/item/3256804988048256.html) | $4.05 / 1 pc | [Amazon EU](https://www.amazon.de/dp/B0D266J2NF/) | €14.89 / 3 pcs | $3.33 (alternative) |
| Tube en carbone (Tube en carbone, 6mm x 4mm x 125mm), alternative | Ø6 × 4 × 125 mm | 2 | Alternative aux tiges de guidage en acier | [Amazon](https://www.amazon.com/MECCANIXITY-Carbon-Pultruded-Airplane-Quadcopter/dp/B0CZDCW2NL/) | $5.60 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256812851232051.html) | $5.90 / 2 | [Amazon EU](https://www.amazon.fr/-/en/QUARKZMAN-Carbon-Fiber-Tubes-Aircraft/dp/B0CZQVN7JB/) | €8.10 / 2 | $5.60 (alternative) |
| Serre-joint en C | 3 pouces, ouverture 0-75 mm | 4 | Deux par bras de robot, pour fixer la base à la table | [Amazon](https://www.amazon.com/Inch-Clamp-Woodworking-Precision-Carpentry/dp/B0FLHZVM7G/) | $10.00 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256813098676278.html) | $9.70 | [Amazon EU](https://www.amazon.fr/Performance-75mm-Adjustable-Stainless-Metalworking/dp/B0GSQL9BCN/) | €17.40 / 2 | $20.00 |
| **Total** |  |  |  |  |  |  |  |  |  | **$37.76** |

<a id="fasteners"></a>
## Fixations

Total du kit tel qu'il est emballé dans le livret d'assemblage.

Utilisez un frein-filet démontable compatible avec le plastique imprimé, par exemple [Vibra-Tite VC-3](https://www.vibra-tite.com/faq/if-vc-3-has-mek-how-can-it-be-plastic-compatible/). Appliquez VC-3 sur le filetage des vis métalliques et laissez sécher complètement avant assemblage (au moins 30 minutes selon la [fiche technique](https://www.vibra-tite.com/wp-content/uploads/213_tds.pdf)) ; ne l'appliquez pas humide sur le plastique. Vérifiez d'abord la compatibilité avec votre filament sur une pièce d'essai.

| Fixation | Norme | Qté | Achat aux États-Unis | Prix unitaire (États-Unis) | Achat aux États-Unis | Prix unitaire (États-Unis) | Achat dans l’UE | Prix unitaire (UE) | Total (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M2 × 6 à tête cylindrique | DIN 912 | 28 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY8XHB1/) | $6.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZP1XT/) | €6.60 / 60 | $1.04 |
| M2 × 8 à tête cylindrique | DIN 912 | 12 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY7L8YJ/) | $6.60 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZKVDN/) | €7.00 / 60 | $0.49 |
| M3 × 10 à tête fraisée | DIN 7991 | 64 | [Amazon](https://www.amazon.com/M3-0-5-Socket-Screws-Alloy-Threaded/dp/B08HNF3J3D/) | $9.00 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY12R93P/) | €8.00 / 60 | $4.59 |
| M3 × 16 à tête fraisée | DIN 7991 | 36 | [Amazon](https://www.amazon.com/Skweawert-40-Pcs-M3x16mm-countersunk/dp/B0D7MY32JZ/) | $6.20 / 40 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY138MGY/) | €8.00 / 60 | $2.95 |
| M3 × 4 vis sans tête | DIN 913 | 4 | [Amazon](https://www.amazon.com/Generic-Bathroom-Fixtures-Furniture-Project/dp/B0H8DPZJPQ/) | $4.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256805653005840.html) | $2.10 / 10 | [Amazon EU](https://www.amazon.fr/-/en/MIETONG-Hex-Socket-Grub-Screws/dp/B0FSKLJR93/) | €6.00 / 20 | $0.31 |
| Écrou hexagonal M2 | DIN 934 | 12 | [Amazon](https://www.amazon.com/1-10Pcs-M1-M20-Stainless-Steel-Loose/dp/B0GVMQ3VD5/) | $3.50 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC5QKH9/) | €6.00 / 20 | $0.42 |
| Écrou hexagonal M3 | DIN 934 | 36 | [Amazon](https://www.amazon.com/FOCMKEAS-Stainless-Hexagon-Fasteners-Hardware/dp/B0CR7WL4D6/) | $3.70 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.00 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC7PD4Q/) | €6.30 / 50 | $1.44 |
| M3 × 6 Vis à tête Phillips | Fourni avec le servo | 16 | Fourni avec les servos. | — | — | — | — | — | — |
| Vis autotaraudeuse 2 × 6 | Fourni avec le servo | 20 | Fourni avec les servos. | — | — | — | — | — | — |
| **Total** |  |  |  |  |  |  |  |  | **$11.24** |

Les attaches noires correspondent au look des enduit mais ne sont pas requises.

<a id="printing-materials"></a>
## Matériaux d’impression

| Matériau | Utilisation | Lien d’achat | Prix / budget (USD) | Total (USD) |
|---|---|---|---|---:|
| Fiberon PET-CF17 | Segments du bras et supports de servos | [Polymaker](https://shop.polymaker.com/products/fiberon-pet-cf17) | $44.99 / 1 kg | $18.00 (0.4 kg) |
| PETG ou PET-CF | Pinces de préhension, couvercles, poignée et déclencheur du bras robot leader | [Amazon](https://www.amazon.com/Bambu-Printer-Filament-1-75mm-Spool/dp/B0GS568LQ1/) | PETG: $21.00 / 1 kg | $15.75 (0.75 kg) |
| **Total** |  |  |  | **$33.75** |

Utilisez le [guide d'impression](printing.md) et coupez à nouveau les 3MF projets fournis à l'aide du slicer d'impression 3D pour déterminer la quantité de filament pour votre imprimante et vos paramètres.

<a id="tools"></a>
## Outils

Prévoyez environ **$10.00** pour une petite clé hexagonale et un tournevis si vous ne possédez pas déjà ces outils.

- Clé hexagonale 1.5 mm pour vis M2: [Amazon search](https://www.amazon.com/s?k=1.5mm+hex+key)
- Clé hexagonale 2 mm pour vis M3: [Amazon search](https://www.amazon.com/s?k=2mm+hex+key)
- Tournevis Phillips PH1 pour vis à corne de servomoteur: [Amazon search](https://www.amazon.com/s?k=PH1+Phillips+screwdriver)
<!-- /translated-content -->
