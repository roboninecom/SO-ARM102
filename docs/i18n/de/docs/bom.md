<!-- translation-navigation -->
[English](../../en/docs/bom.md) · [Русский](../../ru/docs/bom.md) · [Español](../../es/docs/bom.md) · [Français](../../fr/docs/bom.md) · [Deutsch](bom.md) · [Português (Brasil)](../../pt-BR/docs/bom.md) · [简体中文](../../zh-CN/docs/bom.md) · [日本語](../../ja/docs/bom.md) · [हिन्दी](../../hi/docs/bom.md) · [العربية](../../ar/docs/bom.md)

[Englisches Original](../../../bom.md)

[Dokumentation](../README.md) · [Drucken](printing.md) · [Stückliste](bom.md) · [Montage](assembly-guide.md) · [Technische Daten](specifications.md) · [Modelle](../models/README.md) · [Mitwirken](../CONTRIBUTING.md) · [Lizenzen](../LICENSING.md) · [Übersetzungen](translations.md)

> Vollständige Übersetzung des Dokuments. Abbildungen und die ursprüngliche PDF-Anleitung werden gemeinsam genutzt. Mit KI übersetzt; noch nicht von Muttersprachlern geprüft.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="bill-of-materials"></a>
# Stückliste

Die Mengenangaben beziehen sich auf einen kompletten Bausatz: einen Roboterarm und einen Leiterroboterarm.Gedruckte Teile sind separat in [printing.md](printing.md) aufgeführt.

<a id="estimated-kit-cost"></a>
## Geschätzte Kitkosten

**Ein Leiterroboterarm + ein Nachfolgerroboterarm: $340 in Komponenten oder $374 inklusive Druckmaterial.**

| Kategorie | Kosten der verwendeten Mengen (USD) | Kaufen Sie volle Packungen / Spulen (USD) |
|---|---:|---:|
| Servos (12 pcs) | $240.72 | $240.72 |
| Elektronik, Kamera und Netzteile | $50.50 | $50.50 |
| Lager, Stahlführungsstäbe und Tischklemmen | $37.76 | $49.70 |
| Befestigungsmittel | $11.24 | $28.60 |
| **Zwischensumme Bauteile** | **$340.22** | **$368.82** |
| Druckmaterial: 0.4 kg PET-CF17 + 0.75 kg PETG | $33.75 | $66.0 |
| **Gesamt mit Druckmaterial** | **$373.97** | **$434.82** |

Die Spalte **Gesamt (USD)** enthält die Kosten für die Menge, die für ein Kit benötigt wird, unter Verwendung des Referenzangebots hinter jeder bestehenden Zeile (nicht die Summe der Lieferantenangebote). Inklusive Schrauben kosten $0; alternative Carbonrohre sind von den Gesamtkosten ausgeschlossen. Schätzungen verwenden die unten aufgeführten Referenzpreise, wobei jede Zeile auf Cent gerundet ist. Es handelt sich nicht um neue Angebote von Lieferanten: Bestätigen Sie die gewählten Varianten, Mindestbestellmengen und Preise vor der Bestellung. Versand, Steuern, Werkzeuge, Computer, Drucker, Strom und Montageleistungen sind ausgeschlossen.

Das Komplettpaket beinhaltet unbenutzte Ersatzteile, 0.5 kg PET-CF17 Spule und 1 kg PETG Spule. Die Druckmengen sind Budgetgrenzen; schneiden Sie die mitgelieferten 3MF Projekte für Ihre Einstellungen erneut mit dem 3D-Druckschneider auf.Die Stangenkosten verwenden Stahl; Carbonrohre sind eine Alternative.

![Kit Hardware](../../../../assets/images/assembly/hardware.jpg)

<a id="servos"></a>
## Servos

| Gelenk | ID | Follower-Arm | Leader-Arm |
|---|:-:|---|---|
| Basisdrehung | 1 | ST-3235-С001 | ST-3215-C066, 1:191 |
| Schulterhub | 2 | ST-3250-С002 | ST-3215-C066, 1:191 |
| Ellbogenbeugung | 3 | ST-3250-С002 | ST-3215-C066, 1:191 |
| Handgelenkbeugung | 4 | ST-3235-С001 | ST-3215-C066, 1:191 |
| Handgelenkrotation | 5 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |
| Greifer / Abzug | 6 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |

Summen: 6 × STS3215 7.4V, 2 × STS3215 12V, 2 × STS3235 12V, 2 × STS3250 12V. Alle sind Feetech TTL serielle Bus-Servomotoren.

| Servo | Anzahl | Auswahl | Aliexpress link | Stückpreis (USD) | Alibaba link | Stückpreis (USD) | Gesamt (USD) |
|---|---|---|---|---|---|---|---|
| STS3215 | 6 | 7.4V TTL Ausführung für Servomotoren mit Roboterarm. Wählen Sie ST-3215-C066 (7.4V). | [Aliexpress](https://www.aliexpress.us/item/3256811860804361.html) | $32.8 | [Alibaba](https://www.alibaba.com/product-detail/Feetech-SO-ARM101-LeRobot-Open-Source_1601636174153.html) | $6.74 | $40.44 |
| STS3215 | 2 | 12V TTL Ausführung für Nachfolgeroboter-Armgelenke 5 und 6. Wählen Sie ST-3215-C049 (12V30KG). | [Aliexpress](https://www.aliexpress.us/item/3256811832699316.html) | $55.8 für 2pcs | [Alibaba](https://www.alibaba.com/product-detail/6pcs-12V-30KG-1-345-STS3215_1601900233170.html) | $14.70 | $29.40 |
| STS3235 | 2 | 12V TTL Ausführung für Nachfolgeroboterarmgelenke 1 und 4. | [Aliexpress](https://www.aliexpress.us/item/3256810213842277.html) | $63 | [Alibaba](https://www.alibaba.com/product-detail/FEETECH-STS3235-12V-30KG-TTL-Dual_1601910640629.html) | $40.79 | $81.58 |
| STS3250 | 2 | 12V TTL Ausführung für Nachfolgeroboterarmgelenke 2 und 3. | [Aliexpress](https://www.aliexpress.us/item/3256811995148799.html) | $126.4 für 2pcs | [Alibaba](https://www.alibaba.com/product-detail/Feetech-STS3250-12V-50kg-Servo-High_1601711893549.html) | $44.65 | $89.30 |
| **Gesamt** |  |  |  |  |  |  | **$240.72** |

- **Nachfolger Roboterarm, 12V.** STS3250 ist ein bürstenloser Servomotor von 50 kg·cm bei 75 RPM, der die beiden Gelenke antreibt, die die meiste Last aufnehmen. STS3235 ist ein Servomotor von 30 kg·cm mit geringerem Spiel als der STS3215.
- **Leader Roboterarm, 5V.**Die Servomotoren des Leader Roboterarms werden nur gelesen, nie belastet. Sie können einen passiven ST-3215-C066 ohne Motor und Getriebe**nur** für den Leader Roboterarm verwenden.
- Servohörner und die M3 × 6 Hornschrauben werden mit den Servomotoren geliefert.

<a id="electronics"></a>
## Elektronik

| Artikel | Anzahl | Hinweise | Kauf USA | Stückpreis (USA) | Kauf USA | Stückpreis (USA) | Kauf EU | Stückpreis (EU) | Gesamt (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Waveshare Bus Servo Adapter | 2 | Servocontroller | [Amazon](https://www.amazon.com/Waveshare-Integrates-Control-Applicable-Integrate/dp/B0CJ6TP3TP/) | $13.00 | [Aliexpress](https://www.aliexpress.us/item/3256810343532716.html) | $7.40 | [Amazon EU](https://www.amazon.fr/-/en/Serial-Integrates-Control-Circuit-Support/dp/B0CJBKQ8LJ/) | €11.90 | $14.80 |
| Stromversorgung 12V DC (12V 5A Stromversorgung 5.5 2.1mm) | 1 | Nachfolgerroboterarm. 60W / 5A oder mehr empfohlen. Der Roboterarm erreichte unter einer Last von 300g einen Spitzenwert bei 3.3A. Passen Sie den Verbinder des Adapter an (5.5x2.1mm). | [Amazon](https://www.amazon.com/Power-Supply-Adapter-5-5x2-1-2-5mm/dp/B0C3CJF313/) | $10.00 | [Aliexpress](https://www.aliexpress.us/item/3256812113231032.html) | $6.60 | [Amazon EU](https://www.amazon.fr/-/en/zstg-Universal-Power-Supply-Connector/dp/B0GTLSRM91/) | €12.00 | $6.60 |
| Stromversorgung 5V DC (5V 2A Stromversorgung 5.5 2.1mm) | 1 | Führen Sie den Roboterarm an. Passen Sie den Stecker des Adapters (5.5x2.1mm) an. | [Amazon](https://www.amazon.com/MTDZKJG-Adapter-100V-240V-Transformer-Security/dp/B0BZP65GRW/) | $6.20 | [Aliexpress](https://www.aliexpress.us/item/3256812479558626.html) | $4.10 | [Amazon EU](https://www.amazon.fr/5V-2A-Supply-DC-Adapter/dp/B0GDXFRYJS/) | €11.00 | $4.10 |
| USB-C Kabel, 1.5 USB A auf USB C Datenkabel 1.5m) | 2 | Ein Kabel pro Controller. Wählen Sie ein Datenkabel, nicht nur ein Ladekabel. | [Amazon](https://www.amazon.com/Data-Cable-1-5ft-10Gbps-Transfer/dp/B0FMJTHRCM/) | $6.00 | [Aliexpress](https://www.aliexpress.us/item/3256812299430938.html) | $3.00 | [Amazon EU](https://www.amazon.fr/-/en/10Gbps-Transfer-Charging-Samsung-External/dp/B0DHZ1R8FQ/) | €7.00 | $6.00 |
| USB-Kamera (OV2735, 1080P USB-Kameramodul, 2MP 1920x1080, UVC-Kamera, 2.8 oder 3.0 mm Objektiv) | 1 | Handgelenkkamera auf dem Greifer des Follower Roboters. Der Prototyp verwendete ein OV2735 Modul. Überprüfen Sie die Modulabmessungen und Befestigungslöcher gegen den Kamerahalter. | [Amazon](https://www.amazon.com/innomaker-Computer-Raspberry-Support-Windows/dp/B0CNCSFQC1/) | $19.00 | [Aliexpress](https://www.aliexpress.us/item/3256804452094739.html) | $26.10 | [Amazon EU](https://www.amazon.fr/InnoMaker-Raspberry-Compatible-Windows-Android/dp/B0CNCSFQC1/) | €21.00 | $19.00 |
| **Gesamt** |  |  |  |  |  |  |  |  | **$50.50** |

<a id="mechanical-parts"></a>
## Mechanische Teile

| Artikel | Abmessungen | Anzahl | Einbauort | Kauf USA | Stückpreis (USA) | Kauf USA | Stückpreis (USA) | Kauf EU | Stückpreis (EU) | Gesamt (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kugellager 6812 | 60 × 78 × 10 mm | 2 | Basisdrehung, eine pro Roboterarm | [Amazon](https://www.amazon.com/Othmro-6812-2RS-60x78x10mm-Accuracy-Bearing/dp/B081W9QL2Z/) | $5.90 | [Aliexpress](https://www.aliexpress.us/item/3256812369319030.html) | $39.60 / 2 | [Amazon EU](https://www.amazon.fr/-/en/XYWHPGV-6812-2RS-Groove-Bearings-Chrome/dp/B0CQLT6J6D/) | €7.40 / 2 | $11.80 |
| Flanschlager MF106ZZ | 6 × 10 × 3 mm | 2 | Hauptrahmen des Greifers | [Amazon](https://www.amazon.com/METERXITY-Shielded-Bearings-Wheelbarrow-Machines/dp/B0F4QXJSRQ/) | $6.60 / 4 | [Aliexpress](https://www.aliexpress.us/item/3256807821523719.html) | $6.00 / 10 | [Amazon EU](https://www.amazon.fr/-/en/PRECISCRY-DE-SGQ-FLZC-11-MF128ZZ-8x12x3-5-5Pcs/dp/B0GQK9BGWK/) | €11.60 / 5 | $1.20 |
| Stab (Edelstahl Rundstab, 6mm Durchmesser, Länge 125mm) | Ø 6 × 125 mm, Kohlenstoff oder Stahl | 2 | Greiferführungen | [Amazon](https://www.amazon.com/SKYPRO-Stainless-Diameter-Industry-Working/dp/B0CLCSWSJ9?th=1) | $11.90 / 5 | [Aliexpress](https://www.aliexpress.us/item/3256805290944526.html) | $2.80 | [Amazon EU](https://www.amazon.fr/-/en/SKYPRO-Stainless-Diameter-Industry-Metalworking/dp/B0CLCSWSJ9/) | €14.40 / 5 | $4.76 |
| Aluminium-Führungsrohr, Alternative | Ø6 × 4 × 125 mm; 1 × 300 mm auf 2 × 125 mm zuschneiden; entgraten | 2 | Alternative zu Greiferführungsstangen aus Stahl | [Amazon](https://www.amazon.com/dp/B0DRG94GJB/) | $9.99 / 3 Stk. | [Aliexpress](https://www.aliexpress.us/item/3256804988048256.html) | $4.05 / 1 Stk. | [Amazon EU](https://www.amazon.de/dp/B0D266J2NF/) | €14.89 / 3 Stk. | $3.33 (Alternative) |
| Kohlenstoffrohr (Kohlenstoffrohr, 6mm x 4mm x 125mm), alternative | Ø6 × 4 × 125 mm | 2 | Alternative zu Greiferführungsstangen aus Stahl | [Amazon](https://www.amazon.com/MECCANIXITY-Carbon-Pultruded-Airplane-Quadcopter/dp/B0CZDCW2NL/) | $5.60 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256812851232051.html) | $5.90 / 2 | [Amazon EU](https://www.amazon.fr/-/en/QUARKZMAN-Carbon-Fiber-Tubes-Aircraft/dp/B0CZQVN7JB/) | €8.10 / 2 | $5.60 (alternativ) |
| C-Schraubzwinge | 3 Zoll, 0–75 mm Öffnung | 4 | Zwei pro Roboterarm, um die Basis am Tisch zu befestigen | [Amazon](https://www.amazon.com/Inch-Clamp-Woodworking-Precision-Carpentry/dp/B0FLHZVM7G/) | $10.00 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256813098676278.html) | $9.70 | [Amazon EU](https://www.amazon.fr/Performance-75mm-Adjustable-Stainless-Metalworking/dp/B0GSQL9BCN/) | €17.40 / 2 | $20.00 |
| **Gesamt** |  |  |  |  |  |  |  |  |  | **$37.76** |

<a id="fasteners"></a>
## Befestigungsmittel

Kit-Gesamtsumme wie im Montagebuch verpackt.

Verwenden Sie eine lösbare, mit dem gedruckten Kunststoff verträgliche Schraubensicherung, z. B. [Vibra-Tite VC-3](https://www.vibra-tite.com/faq/if-vc-3-has-mek-how-can-it-be-plastic-compatible/). VC-3 auf Metallschraubengewinde auftragen und vor der Montage vollständig trocknen lassen (mindestens 30 Minuten laut [Datenblatt](https://www.vibra-tite.com/wp-content/uploads/213_tds.pdf)); nicht nass auf Kunststoff auftragen. Verträglichkeit zuerst an einem Probedruck mit Ihrem Filament prüfen.

| Befestigungsmittel | Norm | Anzahl | Kauf USA | Stückpreis (USA) | Kauf USA | Stückpreis (USA) | Kauf EU | Stückpreis (EU) | Gesamt (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M2 × 6 Zylinderkopf | DIN 912 | 28 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY8XHB1/) | $6.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZP1XT/) | €6.60 / 60 | $1.04 |
| M2 × 8 Zylinderkopf | DIN 912 | 12 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY7L8YJ/) | $6.60 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZKVDN/) | €7.00 / 60 | $0.49 |
| M3 × 10 Senkkopf | DIN 7991 | 64 | [Amazon](https://www.amazon.com/M3-0-5-Socket-Screws-Alloy-Threaded/dp/B08HNF3J3D/) | $9.00 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY12R93P/) | €8.00 / 60 | $4.59 |
| M3 × 16 Senkkopf | DIN 7991 | 36 | [Amazon](https://www.amazon.com/Skweawert-40-Pcs-M3x16mm-countersunk/dp/B0D7MY32JZ/) | $6.20 / 40 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY138MGY/) | €8.00 / 60 | $2.95 |
| M3 × 4 Gewindestift | DIN 913 | 4 | [Amazon](https://www.amazon.com/Generic-Bathroom-Fixtures-Furniture-Project/dp/B0H8DPZJPQ/) | $4.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256805653005840.html) | $2.10 / 10 | [Amazon EU](https://www.amazon.fr/-/en/MIETONG-Hex-Socket-Grub-Screws/dp/B0FSKLJR93/) | €6.00 / 20 | $0.31 |
| M2 Sechskantmutter | DIN 934 | 12 | [Amazon](https://www.amazon.com/1-10Pcs-M1-M20-Stainless-Steel-Loose/dp/B0GVMQ3VD5/) | $3.50 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC5QKH9/) | €6.00 / 20 | $0.42 |
| M3 Sechskantmutter | DIN 934 | 36 | [Amazon](https://www.amazon.com/FOCMKEAS-Stainless-Hexagon-Fasteners-Hardware/dp/B0CR7WL4D6/) | $3.70 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.00 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC7PD4Q/) | €6.30 / 50 | $1.44 |
| M3 × 6 Kreuzschlitzschraube | Aus dem Servo-Kit | 16 | Im Lieferumfang der Servos enthalten. | — | — | — | — | — | — |
| Selbstschneidende Schraube 2 × 6 | Aus dem Servo-Kit | 20 | Im Lieferumfang der Servos enthalten. | — | — | — | — | — | — |
| **Gesamt** |  |  |  |  |  |  |  |  | **$11.24** |

Schwarze Befestigungselemente passen zum Look der Putzteile, sind aber nicht erforderlich.

<a id="printing-materials"></a>
## Druckmaterialien

| Material | Verwendung | Bezugsquelle | Preis / Budget (USD) | Gesamt (USD) |
|---|---|---|---|---:|
| Fiberon PET-CF17 | Armglieder und Servohalter | [Polymaker](https://shop.polymaker.com/products/fiberon-pet-cf17) | $44.99 / 1 kg | $18.00 (0.4 kg) |
| PETG oder PET-CF | Greiferklemmen, Abdeckungen, Leiter Roboterarmgriff und Auslöser | [Amazon](https://www.amazon.com/Bambu-Printer-Filament-1-75mm-Spool/dp/B0GS568LQ1/) | PETG: $21.00 / 1 kg | $15.75 (0.75 kg) |
| **Gesamt** |  |  |  | **$33.75** |

Verwenden Sie den [Druckleitfaden](printing.md) und schneiden Sie die mitgelieferten 3MF Projekte erneut mit dem 3D-Druck-Slicer, um die Filamentmenge für Ihren Drucker und Einstellungen zu bestimmen.

<a id="tools"></a>
## Werkzeuge

Planen Sie ungefähr **$10.00** für ein kleines Sechskantschlüssel- und Schraubendreher-Set ein, wenn Sie diese Werkzeuge nicht bereits besitzen.

- Innensechskantschlüssel 1.5 mm für M2 Schrauben: [Amazon search](https://www.amazon.com/s?k=1.5mm+hex+key)
- Innensechskantschlüssel 2 mm für M3 Schrauben: [Amazon search](https://www.amazon.com/s?k=2mm+hex+key)
- Kreuzschlitzschraubendreher PH1 für Servomotor-Hornschrauben: [Amazon search](https://www.amazon.com/s?k=PH1+Phillips+screwdriver)
<!-- /translated-content -->
