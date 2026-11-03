<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[Englisches Original](../../../README.md)

[Dokumentation](README.md) · [Drucken](docs/printing.md) · [Stückliste](docs/bom.md) · [Montage](docs/assembly-guide.md) · [Technische Daten](docs/specifications.md) · [Modelle](models/README.md) · [Mitwirken](CONTRIBUTING.md) · [Lizenzen](LICENSING.md) · [Übersetzungen](docs/translations.md)

> Vollständige Übersetzung des Dokuments. Abbildungen und die ursprüngliche PDF-Anleitung werden gemeinsam genutzt. Mit KI übersetzt; noch nicht von Muttersprachlern geprüft.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102"></a>
# SO-ARM 102

<div align="center">

[![SO-ARM 102](../../../assets/images/photos/so-arm-102-live.jpg)](../../../assets/video/so-arm-102-preview.mp4)

**🎥 [Sehen Sie sich das Vorschauvideo an](../../../assets/video/so-arm-102-preview.mp4)**·**🛒 [Kaufen Sie das Kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

**SO-ARM 102 ist ein quelloffenes Leader-Follower-Roboterarm-Kit für Teleoperation und Imitationslernen. Jeder Arm hat fünf Freiheitsgrade und einen zusätzlichen Greifer.**

<p align="left">
Aufbauend auf SO-ARM 100 und 101 verbindet es einen steiferen PET-CF-Rahmen mit einem Parallelgreifer.
</p>

[![Hardware: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt) [![Software: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt) [![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt) [![GitHub release](https://img.shields.io/github/v/release/roboninecom/SO-ARM-102)](https://github.com/roboninecom/SO-ARM-102/releases/latest)

📩 [hello@robonine.com](mailto:hello@robonine.com)

**DIY-Budget: ~$340 für Komponenten oder ~$374 inklusive Druckmaterial.** [Stücklistenzusammenfassung](#bill-of-materials) · [Einzelkosten und Kauflinks](docs/bom.md#estimated-kit-cost)

> Möchten Sie die Teile lieber nicht selbst beschaffen und drucken? **[Kaufen Sie das SO-ARM 102 Kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

</div>

---

<a id="-what-changed-against-so-arm-101"></a>
## ✨ Was hat sich gegenüber SO-ARM 101 geändert?

|  | SO-ARM 101 | SO-ARM 102 |
|---|---|---|
| Greifer | Winkelbacke | Parallelgreifer, 85 mm Spannweite |
| Rahmenmaterial | PLA | PET-CF (Fiberon PET-CF17 getestet) |
| Struktur | Massive Glieder | Topologieoptimierte Glieder |
| Drehbereich der Basis | 220° | **352°** |
| Horizontale Reichweite | 441 mm | **483 mm** |
| Umlenkung am Greifer, 300 g Last ¹ | 7.5 mm | **3.4–3.9 mm** |
| Schulter- und Ellenbogengeschwindigkeit | 45 RPM (STS3215) | **75 RPM (STS3250)** |
| Geräuschpegel bei 1 m | 70 dB | **60 dB** |

¹ Beide Roboterarme wurden mit gedruckten Servomotor-Dummys gebaut, daher wird der Rahmen verglichen, nicht die Motoren.Vollständige Ergebnisse und Testbedingungen finden Sie in [docs/specifications.md](docs/specifications.md).

---

<a id="-preview"></a>
## 🎥 Vorschau

<div align="center">

[![SO-ARM 102 preview](../../../assets/video/so-arm-102-preview.gif)](../../../assets/video/so-arm-102-preview.mp4)

*Klicken Sie für das vollständige Video, 21 s*

</div>

---

<a id="-configurations"></a>
## 🤝 Konfigurationen

<a id="single-arm-one-leader--one-follower"></a>
### Einzelroboterarm: ein Führer Roboterarm + ein Nachfolger Roboterarm

Der Standard-Bausatz. Bewegen Sie den Leiterroboterarm von Hand, und der Nachfolgerroboterarm wiederholt die Bewegung. Verwenden Sie ihn für Teleoperation und zur Aufzeichnung von Demonstrationen zum Imitationslernen.

![Ein Leader-Arm und ein Follower-Arm](../../../assets/images/renders/config-single-arm.jpg)

<a id="bimanual-two-leaders--two-followers"></a>
### Bimanual: zwei Führer + zwei Anhänger

Zwei Kits nebeneinander: Jede Hand treibt ihren eigenen Roboterarm an, sodass die Nachfolger Objekte weitergeben, ein Teil halten und daran arbeiten oder jede Aufgabe erledigen können, für die zwei Hände benötigt werden.

![Zwei Leader-Arme und zwei Follower-Arme](../../../assets/images/renders/config-dual-arm.jpg)

<a id="the-two-arms"></a>
### Die beiden Roboterarme

| Follower-Arm | Leader-Arm |
|:-:|:-:|
| ![Follower-Arm](../../../assets/images/renders/follower.jpg) | ![Leader-Arm](../../../assets/images/renders/leader.jpg) |
| Parallelgreifer, Handgelenkkamera, 12 V | Griff mit Abzug, 5 V |

---

<a id="-build-it-in-four-steps"></a>
## 🚀 Bauen Sie es in vier Schritten

Bevorzugen Sie ein fertiges Kit? **[Kaufen Sie das SO-ARM 102-Kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

<a id="1-print-the-parts"></a>
### 1. Drucken Sie die Teile

Die einzelnen Teile passen auf eine 180 × 180 mm 3D-Druckerbauplatte. Das größte Teil ist 160 mm lang, die mitgelieferten 3MF Plattenlayouts verwenden eine 256 × 256 mm 3D-Druckerbauplatte.

- 3MF Slicer-Projekte mit gespeicherten Orientierungs- und Stützeinstellungen: [`models/3mf/`](../../../models/3mf) — [führender Roboterarm](../../../models/3mf/SO102_leader.3mf), [Nachfolgerroboterarm](../../../models/3mf/SO102_follower_arms.3mf), [Greifer und Basis des Followers](../../../models/3mf/SO102_follower_gripper_base.3mf)
- Projektinhalte und Druckerprofile: [models/README.md](models/README.md)
- STL Dateien, bereit zum Schneiden: [`models/stl/`](../../../models/stl)
- STEP sources: [`models/step/`](../../../models/step)
- Material, Einstellungen und Teilemengen: [docs/printing.md](docs/printing.md)


<a id="2-buy-the-hardware"></a>
### 2. Hardware kaufen

Beziehen Sie die Komponenten aus der [BOM-Zusammenfassung](#bill-of-materials) und [vollständige BOM mit Kauflinks](docs/bom.md).Budget **$340.22**für Komponenten oder**$373.97** inklusive Druckmaterial, vor Versand und Steuern.

| Arm | Servos | Controller | Stromversorgung |
|---|---|---|---|
| Follower-Arm | 2 × STS3235, 2 × STS3250, 2 × STS3215 | Waveshare Bus Servo Adapter | **12 V** |
| Leader-Arm | 6 × STS3215 | Waveshare Bus Servo Adapter | **5 V** |

> ⚠️ **Der Leader-Arm wird mit 5 V betrieben, der Follower-Arm mit 12 V.** Vertauschen Sie die Netzteile nicht.

<a id="3-assemble"></a>
### 3

- Druckbares Heft, 32 Seiten A5: [docs/SO-ARM102_assembly_A5_v0.7.pdf](../../SO-ARM102_assembly_A5_v0.7.pdf)
- Schrittliste mit Teilen und Befestigungen: [docs/assembly-guide.md](docs/assembly-guide.md)

Werkzeuge: Sechskantschlüssel 1.5 mm (M2 Schrauben) und 2 mm (M3 Schrauben).

<a id="4-set-up-the-software"></a>
### 4. Die Software einrichten

Servo-IDs, Kalibrierung und Lektionen: **[lab.robonine.com](https://lab.robonine.com)**.
Verwenden Sie das SO-ARM 102 Follower-Plugin mit dem Standardtyp `so101_leader`.
**[LeRobot installieren und einrichten](docs/lerobot.md)**.

---

<a id="bill-of-materials"></a>
## Stückliste

Mengen und Referenzkosten für **einen Leader Roboterarm + einen Follower Roboterarm**:

| Kategorie / Kauflinks | Lieferumfang | Gesamt (USD) |
|---|---|---:|
| [Servos](docs/bom.md#servos) | 6 × STS3215 7.4 V, 2 × STS3215 12 V, 2 × STS3235, 2 × STS3250 | $240.72 |
| [Elektronik](docs/bom.md#electronics) | 2 Controller, 2 Netzteile, 2 USB-Kabel, 1 Handgelenkkamera | $50.50 |
| [Mechanische Teile](docs/bom.md#mechanical-parts) | 4 Lager, 2 Stahlführungsstäbe, 4 Tischklemmen | $37.76 |
| [Befestigungsmittel](docs/bom.md#fasteners) | Schrauben und Muttern; spezifizierte Servomotor-Kit-Schrauben enthalten | $11.24 |
| **Zwischensumme Bauteile** |  | **$340.22** |
| [Druckmaterial](docs/bom.md#printing-materials) | 0.4 kg PET-CF17 + 0.75 kg PETG Zuschuss | $33.75 |
| **Gesamt mit Druckmaterial** |  | **$373.97** |

Der Kauf der Beispiel-Vollpacks und Filament-Spulen von Grund auf neu kostet etwa **$435**, einschließlich unbenutzter Ersatzteile. Dies sind Richtschätzungen, keine neuen Lieferantenangebote. Versandkosten, Steuern, Werkzeuge, Computer, Drucker, Strom und Montageleistungen sind ausgeschlossen. Bestätigen Sie Lieferantenpreise, Varianten und Mindestbestellmengen vor der Bestellung; schneiden Sie die 3MF Projekte erneut mit dem 3D-Druck-Schneider, um den Filamentverbrauch zu überprüfen.

[Vollständige Stückliste, Kauflinks und Kostenannahmen](docs/bom.md#estimated-kit-cost).

---

<a id="urdf-export"></a>
## URDF exportieren

Der aktuelle Standalone-Export befindet sich in [`simulation/urdf/`](../../../simulation/urdf): [URDF](../../../simulation/urdf/so_arm_102.urdf) · [Xacro](../../../simulation/urdf/so_arm_102.xacro). `meshes/` neben den Beschreibungsdateien belassen; Netzpfade sind relativ zu diesem Ordner.

- **Visuals:**STL Meshes.**Collisions:** angepasste, unabhängig gedrehte Boxen auf allen acht Links.
- **Massenschätzung:**PLA, 30% Füllung, 6 Umfänge, 6 obere/untere Schichten, 0.2 mm Schichthöhe und**0.40 mm Extrusionsbreite** Dies sind Simulationsannahmen; verwenden Sie [die Druckanleitung](docs/printing.md) für die Fertigungseinstellungen.
- **Hardware-Massen:**sechs Motoren bei je 70 g; Basislager bei 105 g. Geschätzte Gesamtmodellmasse:**0.889 kg**.
- **Greifer:** `clamp2` imitiert `clamp1` mit Multiplikator `-1`.

[Exporteinstellungen](../../../simulation/urdf/export_settings.json) und [Masseneigenschaften](../../../simulation/urdf/mass_properties.json) zeichnen die Annahmen auf, Geometrie- und Trägheitsprüfungen werden in [export_verification.json](../../../simulation/urdf/export_verification.json).

---

<a id="-repository-structure"></a>
## 📁 Repository Struktur

```
├── models/
│   ├── 3mf/                 # Slicer-Projekte: Leader Roboterarm, Follower Roboterarm, Greifer und Board Case
│   ├── stl/                 # Druckfertige Netze
│   │   ├── common/          # Gemeinsame Teile einschließlich Controllergehäuse
│   │   ├── follower/        # Parallelgreifer und Kamerahalterung
│   │   └── leader/          # Griff, Abzug und Handgelenkrotation
│   └── step/                # CAD Quellen, gleiches Layout wie stl/
├── docs/
│   ├── printing.md          # Material, Schneideinstellungen, Mengen
│   ├── bom.md               # Stückliste
│   ├── assembly-guide.md    # Schrittliste mit Teilen und Befestigungselementen
│   ├── specifications.md    # Geometrie, Servomotoren, Messergebnisse vs SO-ARM 101
│   └── SO-ARM102_assembly_A5_v0.7.pdf
├── assets/
│   ├── images/              # Fotos, Renderings, Booklet-Seiten, Testfotos
│   └── video/               # Vorschau Video und GIF
├── LICENSING.md             # Welche Lizenz umfasst welche Datei
└── NOTICE                   # Attribution durch Dritte
```

---

<a id="-known-issues"></a>
## Bekannte Probleme

Hinweise aus unabhängigen Testaufbauten; beim Zusammenbau beachten.

1. **Verwenden Sie Heft v0.7.** Frühere Hefte zeigen den HAT-Controller und alte Greiferteile. In v0.7 wird an beiden Armen ein Bus Servo Adapter montiert.
2. **M2 Schrauben sind an mehreren Stellen schwer zu erreichen.** Erwarte, dass du gegen einige von ihnen kämpfen musst.
3. **Die Greiferklemmen laufen fest auf Carbonstäben.** Die Klemmbohrungen sind für 6.1 mm dimensioniert.Stangendurchmesser variieren je nach Hersteller, überprüfen Sie daher vor der Montage die Passform.
4. **Überprüfen Sie die Kabellängen der Servomotoren**, bevor Sie jede Verbindung schließen, insbesondere von der Basis bis zur Schulter.
5. **Die Montagereihenfolge ist an zwei Stellen unübersichtlich** Lesen Sie vor dem Befestigen zwei Schritte voraus.
6. **Die Gelenke des Leader-Roboterarms können sich locker anfühlen.** Durch das Hinzufügen von 8 × 2 mm Gummi-O-Ringen zwischen jedem Servomotor und seinem Horn erhält der Leader-Roboterarm eine glatte, leise Reibung. Verwenden Sie zwei pro Servomotor an den Gelenken 1–4 und einen an den Gelenken 5–6.

Haben Sie etwas anderes gefunden? Bitte [öffnen Sie ein Problem](https://github.com/roboninecom/SO-ARM-102/issues).

---

<a id="-star-history"></a>
## ⭐ Sterneverlauf

[![Sterneverlauf — SO-ARM 102](https://api.star-history.com/svg?repos=roboninecom/so-arm-102&type=date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm-102&type=date&legend=top-left)

---

<a id="-related-projects"></a>
## Verwandte Projekte

- [SO-ARM100/101 Parallel Gripper](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper), der Greifer, aus dem der SO-ARM 102 Greifer gewachsen ist
- [SO-ARM101](https://github.com/TheRobotStudio/SO-ARM100) bis TheRobotStudio, der Roboterarm dieser Konstruktion gelingt
- [Praktischer Vergleich von intelligenten seriellen Servomotoren](https://robonine.com/smart-serial-servo-motor-comparison-robotics/), die Tests hinter der Wahl des Servomotors
- [Auswahl eines Filament für Roboter-Arme](https://robonine.com/choosing-filament-for-robotic-arm-applications/), die Tests hinter PET-CF

---

<a id="-license"></a>
## 📄 Lizenz

Copyright (c) 2026 Robonine. Verschiedene Arten von Material tragen unterschiedliche Lizenzen:

| Material | Lizenz |
|---|---|
| Hardware-Designs in `models/` | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| Software und Konfiguration | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| Dokumentation und Bilder in `docs/`, `assets/`, alle `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

Siehe [LICENSING.md](LICENSING.md) und [REUSE.toml](../../../REUSE.toml) für die Datei-für-Datei-Zuordnung.

---

<a id="-team"></a>
## Team

| Name | Rolle | Kontakt |
|------|------|---------|
| **Alan Subin** | Konstrukteur: Mechanische Konstruktion, CAD, Montageheft | [LinkedIn](https://www.linkedin.com/in/alan-subin/) |
| **Boris Kotov** | Software und Test Engineer: Prototypen, Druck, Prüfstände | [Telegram](https://t.me/bkotov) |
| **Nikita Bragin** | Projektleiter/in | [LinkedIn](https://www.linkedin.com/in/nikita-bragin-82296b29/) |
| **Mikhail Chistiakov** | Industriedesigner: Optik und Form des Roboterarmes | [Telegram](https://t.me/brrryska) |
| **Mikhail Zhmaylo** | Konstrukteur: Steifigkeitsmodelle, Designänderungen zur Reduzierung der Durchbiegung | [Telegram](https://t.me/mikhail_zhmaylo) |
| **Vladislav Eremenko** | Tragwerksingenieur: Festigkeits- und thermische Analyse, Topologieoptimierung | [Telegram](https://t.me/v1ad_eremenko) |
| **Vladimir Osipov** | Tester und Berater: unabhängiger Testbau | [LinkedIn](https://www.linkedin.com/in/vladimirosipov/) |

<div align="center">

**Erstellt für die Robotik-Community von [Robonine](https://robonine.com)** 🤖

</div>
<!-- /translated-content -->
