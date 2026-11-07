<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](../../es/docs/specifications.md) · [Français](specifications.md) · [Deutsch](../../de/docs/specifications.md) · [Português (Brasil)](../../pt-BR/docs/specifications.md) · [简体中文](../../zh-CN/docs/specifications.md) · [日本語](../../ja/docs/specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[Original anglais](../../../specifications.md)

[Documentation](../README.md) · [Impression](printing.md) · [Composants](bom.md) · [Montage](assembly-guide.md) · [Caractéristiques](specifications.md) · [Modèles](../models/README.md) · [Contribuer](../CONTRIBUTING.md) · [Licences](../LICENSING.md) · [Traductions](translations.md)

> Traduction intégrale du document. Les illustrations et le livret PDF original sont communs aux langues. Traduction assistée par IA, pas encore relue par des locuteurs natifs.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="specifications-and-test-results"></a>
# Caractéristiques et résultats d’essais

Mesurées sur Robonine prototypes en août et septembre 2026.Les chiffres marqués *calculés* proviennent des fiches techniques du URDF modèle et du servomoteur, pas d'une mesure.

<a id="geometry"></a>
## Géométrie

| Articulation | Plage |
|---|---|
| Rotation de la base | −176° … +176° (352°) |
| Élévation de l’épaule | −43° … +181° (224°) |
| Flexion du coude | −166° … +77° (243°) |
| Flexion du poignet | −85° … +111° (196°) |
| Rotation du poignet | −165° … +163° (328°) |
| Pince | 0 … 85 mm |

| Segment | Entre axes |
|---|---|
| Rotation de base vers l'épaule | 85 mm |
| De l'épaule au coude | 119 mm |
| Flexion du coude au poignet | 139 mm |
| Flexion du poignet pour rouler le poignet | 62 mm |
| Rouleau de poignet à la pointe de pince | 132 mm |

| Portée, pointe de préhenseur centre |  |
|---|---|
| Rayon horizontal | 483 mm |
| Hauteur au-dessus du fond de base | Jusqu'à 544 mm |
| Sous le fond de la base, bras du robot sur un bord de table | Jusqu'à −301 mm |

La portée a été calculée à partir de 100,000 poses aléatoires dans les limites de l'articulation, sans collision.

<a id="servos"></a>
## Servomoteurs

| Articulation | Bras suiveur | Bras leader |
|---|---|---|
| 1 Rotation de base | STS3235 | STS3215 |
| 2 Lifting des épaules | STS3250 | STS3215 |
| 3 Flexion du coude | STS3250 | STS3215 |
| 4 Flexion du poignet | STS3235 | STS3215 |
| 5 Rouleau de poignet | ST-3215-C049, 1:191 | STS3215 |
| 6 Préhenseur / déclencheur | ST-3215-C049, 1:191 | STS3215 |
| Alimentation | 12 V | 5 V |

<a id="gripper"></a>
## Pince

| | |
|---|---|
| Type | Parallèle, crémaillère et pignon, deux mâchoires mobiles |
| Ouverture | 85 mm |
| Boîte, largeur maximale recommandée | À propos de 75 mm |
| Cylindre, diamètre maximal recommandé | À propos de 70 mm |
| Sphère, diamètre maximal recommandé | À propos de 60 mm |
| Caméra | Caméra USB montée sur la pince |

<a id="measured-results-against-so-arm-101"></a>
## Résultats mesurés par rapport à SO-ARM 101

| Indicateur | SO-ARM 101 | SO-ARM 102 | Variation |
|---|---|---|---|
| Déviation à l'extrémité de la pince, 300 g, bras robot entièrement étendu ¹ | 7.5 mm | 3.4 mm | −55 % |
| Identique, tous les liens à 100 % de remplissage ¹ | — | 2.34 mm | −69 % |
| Rayon horizontal | 441 mm | 483 mm | +9.5 % |
| Portée derrière la base | 377 mm | 473 mm | +25.5 % |
| Plage de rotation de la base | 220° | 352° | +60 % |
| Plage du coude | 194° | 243° | +25 % |
| Vitesse à vide de l'épaule et du coude, *calculée* | 270 °/s | 450 °/s | +67 % |
| Jeu de l’articulation de base | 8.75 comptes | 5.00 comptes | −43 % |
| Erreur horizontale de pointe à partir du jeu de base, *calculée* | ±2.96 mm | ±1.85 mm | −37.5 % |
| Répétabilité | — | À propos de 0.1 mm |  |
| Bruit à 1 m | 70 dB | 60 dB | −10 dB |
| Charge utile nominale | 150 g | 300 g |  |

¹ Les deux bras robotiques ont été construits avec des mannequins de servomoteurs imprimés dans les articulations 2, 3 et 4, donc seul le cadre est comparé. SO-ARM 101 imprimé en PLA, SO-ARM 102 en Fiberon PET-CF17 à 25 % de remplissage. Une deuxième exécution du même test SO-ARM 102 a donné 3.9 mm.

| SO-ARM 101 | SO-ARM 102 |
|:-:|:-:|
| ![SO-ARM 101 essai de rigidité](../../../../assets/images/tests/stiffness-so-arm-101.jpg) | ![SO-ARM 102 essai de rigidité](../../../../assets/images/tests/stiffness-so-arm-102.jpg) |

<a id="current-and-temperature-follower"></a>
## Courant et température, bras robotique suiveur

Mesurée avec une charge 300 g sur une trajectoire répétitive, ambiance 30 °C, six STS3250 servomoteurs.

| | |
|---|---|
| Courant moyen | 1.26 A |
| Courant de pointe | 3.28 A |
| Température maximale du servo | 46 °C |

<a id="absolute-accuracy"></a>
## Précision absolue

Les réglages sont encore en cours. Avec les paramètres PID d'origine des servos, l'extrémité s'affaissait d'environ 50 mm sous le poids du bras en extension maximale. Le réglage du PID a ramené cet affaissement à environ 5 mm. Un profil de précision dédié est en préparation.
<!-- /translated-content -->
