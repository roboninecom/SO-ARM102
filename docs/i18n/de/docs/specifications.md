<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](../../es/docs/specifications.md) · [Français](../../fr/docs/specifications.md) · [Deutsch](specifications.md) · [Português (Brasil)](../../pt-BR/docs/specifications.md) · [简体中文](../../zh-CN/docs/specifications.md) · [日本語](../../ja/docs/specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[Englisches Original](../../../specifications.md)

[Dokumentation](../README.md) · [Drucken](printing.md) · [Stückliste](bom.md) · [Montage](assembly-guide.md) · [Technische Daten](specifications.md) · [Modelle](../models/README.md) · [Mitwirken](../CONTRIBUTING.md) · [Lizenzen](../LICENSING.md) · [Übersetzungen](translations.md)

> Vollständige Übersetzung des Dokuments. Abbildungen und die ursprüngliche PDF-Anleitung werden gemeinsam genutzt. Mit KI übersetzt; noch nicht von Muttersprachlern geprüft.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="specifications-and-test-results"></a>
# Technische Daten und Prüfergebnisse

Gemessen an Robonine Prototypen im August und September 2026.Zahlen, die mit *berechnet* gekennzeichnet sind, stammen aus den URDF Modell- und Servomotordatenblättern, nicht aus einer Messung.

<a id="geometry"></a>
## Geometrie

| Gelenk | Bereich |
|---|---|
| Basisdrehung | −176° … +176° (352°) |
| Schulterhub | −43° … +181° (224°) |
| Ellbogenbeugung | −166° … +77° (243°) |
| Handgelenkbeugung | −85° … +111° (196°) |
| Handgelenkrotation | −165° … +163° (328°) |
| Greifer | 0 … 85 mm |

| Glied | Achsabstand |
|---|---|
| Basisdrehung zur Schulter | 85 mm |
| Schulter bis Ellenbogen | 119 mm |
| Ellbogen bis Handgelenk Flex | 139 mm |
| Handgelenk Flex zu Handgelenk Rolle | 62 mm |
| Handgelenkrolle zur Greiferspitze | 132 mm |

| Reichweite, Greiferspitzenmitte |  |
|---|---|
| Horizontaler Radius | 483 mm |
| Höhe über dem Sockelboden | bis zu 544 mm |
| Roboterarm unterhalb des Bodenbodens über eine Tischkante | Bis zu −301 mm |

Die Reichweite wurde aus 100,000 zufälligen Posen innerhalb der Gelenkgrenzen ohne Selbstkollision berechnet.

<a id="servos"></a>
## Servos

| Gelenk | Follower-Arm | Leader-Arm |
|---|---|---|
| 1 Basisdrehung | STS3235 | STS3215 |
| 2 Schulterlifting | STS3250 | STS3215 |
| 3 Ellbogenbeugung | STS3250 | STS3215 |
| 4 Handgelenk Flex | STS3235 | STS3215 |
| 5 Handgelenkrollen | ST-3215-C049, 1:191 | STS3215 |
| 6 Greifer / Auslöser | ST-3215-C049, 1:191 | STS3215 |
| Versorgung | 12 V | 5 V |

<a id="gripper"></a>
## Greifer

| | |
|---|---|
| Typ | Parallel, Zahnstange und Ritzel, zwei bewegliche Backen |
| Öffnung | 85 mm |
| Box, empfohlene maximale Breite | über 75 mm |
| Zylinder, empfohlener maximaler Durchmesser | über 70 mm |
| Kugel, empfohlener maximaler Durchmesser | über 60 mm |
| Kamera | USB-Kamera am Greifer montiert |

<a id="measured-results-against-so-arm-101"></a>
## Gemessene Ergebnisse gegen SO-ARM 101

| Messgröße | SO-ARM 101 | SO-ARM 102 | Änderung |
|---|---|---|---|
| Ablenkung an der Greiferspitze, 300 g, Roboterarm voll ausgefahren ¹ | 7.5 mm | 3.4 mm | −55 % |
| Gleiches, alle Links bei 100 % Füllung ¹ | — | 2.34 mm | −69 % |
| Horizontaler Radius | 441 mm | 483 mm | +9.5 % |
| Reichweite hinter der Basis | 377 mm | 473 mm | +25.5 % |
| Drehbereich der Basis | 220° | 352° | +60 % |
| Ellbogenbereich | 194° | 243° | +25 % |
| Schulter- und Ellenbogen-Leerlaufgeschwindigkeit, *berechnet* | 270 °/s | 450 °/s | +67 % |
| Spiel des Basisgelenks | 8.75 zählt | 5.00 zählt | −43 % |
| Horizontaler Spitzenfehler vom Basisspiel, *berechnet* | ±2.96 mm | ±1.85 mm | −37.5 % |
| Wiederholgenauigkeit | — | über 0.1 mm |  |
| Geräuschpegel bei 1 m | 70 dB | 60 dB | −10 dB |
| Nennnutzlast | 150 g | 300 g |  |

¹ Beide Roboterarme wurden mit gedruckten Servomotor-Dummys in den Gelenken 2, 3 und 4 gebaut, daher wird nur der Rahmen verglichen. SO-ARM 101 wurde in PLA, SO-ARM 102 in Fiberon PET-CF17 bei 25 % Füllstand gedruckt. Ein zweiter Durchlauf des gleichen SO-ARM 102 Tests ergab 3.9 mm.

| SO-ARM 101 | SO-ARM 102 |
|:-:|:-:|
| ![SO-ARM 101 Steifigkeitsprüfung](../../../../assets/images/tests/stiffness-so-arm-101.jpg) | ![SO-ARM 102 Steifigkeitsprüfung](../../../../assets/images/tests/stiffness-so-arm-102.jpg) |

<a id="current-and-temperature-follower"></a>
## Strom und Temperatur, Follower Roboterarm

Gemessen mit einer 300 g Last auf einer sich wiederholenden Bahn, Umgebungstemperatur 30 °C, sechs STS3250 Servomotoren.

| | |
|---|---|
| Mittlerer Strom | 1.26 A |
| Spitzenstrom | 3.28 A |
| Maximale Servotemperatur | 46 °C |

<a id="absolute-accuracy"></a>
## Absolute Genauigkeit

Die Abstimmung läuft noch. Mit den werkseitigen Servo-PID-Einstellungen senkte sich die Spitze bei voller Ausstreckung unter dem Eigengewicht des Arms um etwa 50 mm. Angepasste PID-Einstellungen reduzierten dies auf etwa 5 mm. Ein gesondertes Genauigkeitsprofil ist in Arbeit.
<!-- /translated-content -->
