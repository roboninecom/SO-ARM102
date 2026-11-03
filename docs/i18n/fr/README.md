<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[Original anglais](../../../README.md)

[Documentation](README.md) · [Impression](docs/printing.md) · [Composants](docs/bom.md) · [Montage](docs/assembly-guide.md) · [Caractéristiques](docs/specifications.md) · [Modèles](models/README.md) · [Contribuer](CONTRIBUTING.md) · [Licences](LICENSING.md) · [Traductions](docs/translations.md)

> Traduction intégrale du document. Les illustrations et le livret PDF original sont communs aux langues. Traduction assistée par IA, pas encore relue par des locuteurs natifs.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102"></a>
# SO-ARM 102

<div align="center">

[![SO-ARM 102](../../../assets/images/photos/so-arm-102-live.jpg)](../../../assets/video/so-arm-102-preview.mp4)

**🎥 [Regardez la vidéo d'aperçu](../../../assets/video/so-arm-102-preview.mp4)**·**🛒 [Achetez le kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

**SO-ARM 102 est un kit de bras robotiques leader–suiveur open source pour la téléopération et l’apprentissage par imitation. Chaque bras possède cinq degrés de liberté et une pince.**

<p align="left">
Dans la continuité des SO-ARM 100 et 101, il associe une structure en PET-CF plus rigide à une pince parallèle.
</p>

[![Hardware: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt) [![Software: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt) [![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt) [![GitHub release](https://img.shields.io/github/v/release/roboninecom/SO-ARM-102)](https://github.com/roboninecom/SO-ARM-102/releases/latest)

📩 [hello@robonine.com](mailto:hello@robonine.com)

**Budget DIY: ~$340 pour les composants, ou ~$374 y compris le matériel d'impression.** [résumé de la nomenclature](#bill-of-materials) · [coûts détaillés et liens d'achat](docs/bom.md#estimated-kit-cost)

> Vous préférez ne pas vous procurer les pièces et les imprimer vous-même ? **[Achetez le kit SO-ARM 102](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

</div>

---

<a id="-what-changed-against-so-arm-101"></a>
## ✨ Ce qui a changé par rapport à SO-ARM 101

|  | SO-ARM 101 | SO-ARM 102 |
|---|---|---|
| Pince | Mâchoire angulaire | Pince parallèle, 85 mm portée |
| Matériau du châssis | PLA | PET-CF (Fiberon PET-CF17 testé) |
| Structure | Segments pleins | Segments optimisés topologiquement |
| Plage de rotation de la base | 220° | **352°** |
| Portée horizontale | 441 mm | **483 mm** |
| Déviation au niveau de la pince, charge 300 g ¹ | 7.5 mm | **3.4–3.9 mm** |
| Vitesse de l'épaule et du coude | 45 RPM (STS3215) | **75 RPM (STS3250)** |
| Bruit à 1 m | 70 dB | **60 dB** |

¹ Les deux bras robotisés ont été construits avec des mannequins de servomoteurs imprimés. Le cadre est donc comparé, pas les moteurs. Les résultats complets et les conditions d'essai sont disponibles dans [docs/specifications.md](docs/specifications.md).

---

<a id="-preview"></a>
## 🎥 Aperçu du film

<div align="center">

[![SO-ARM 102 preview](../../../assets/video/so-arm-102-preview.gif)](../../../assets/video/so-arm-102-preview.mp4)

*Cliquez pour la vidéo complète, 21 s*

</div>

---

<a id="-configurations"></a>
## 🤝 Configurations de base

<a id="single-arm-one-leader--one-follower"></a>
### Bras robotisé unique: un bras robot leader + un bras robot disciple

Le kit standard. Déplacez le bras robotique leader à la main, et le bras robotique suiveur répète le mouvement.Utilisez-le pour la téléopération et pour enregistrer des démonstrations pour l'apprentissage par imitation.

![Un bras maître et un bras suiveur](../../../assets/images/renders/config-single-arm.jpg)

<a id="bimanual-two-leaders--two-followers"></a>
### Bimanual: deux leaders + deux disciples

Deux kits côte à côte. Chaque main pilote son propre bras robotique de chef, afin que les disciples puissent passer des objets, tenir et travailler sur une pièce ou effectuer toute tâche nécessitant deux mains.

![Deux bras maîtres et deux bras suiveurs](../../../assets/images/renders/config-dual-arm.jpg)

<a id="the-two-arms"></a>
### Les deux bras robotiques

| Bras suiveur | Bras leader |
|:-:|:-:|
| ![Bras suiveur](../../../assets/images/renders/follower.jpg) | ![Bras maître](../../../assets/images/renders/leader.jpg) |
| Pince parallèle, caméra de poignet, 12 V | Poignée avec déclencheur, 5 V |

---

<a id="-build-it-in-four-steps"></a>
## 🚀 Construisez-le en quatre étapes

Préférez-vous un kit prêt ? **[Achetez le kit SO-ARM 102](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

<a id="1-print-the-parts"></a>
### 1. Imprimer les pièces

Les pièces individuelles s'adaptent à une plaque de construction d'imprimante 3D 180 × 180 mm. La plus grande partie est longue de 160 mm.Les 3MF plans de plaques fournis utilisent une plaque de construction d'imprimante 3D 256 × 256 mm.

- 3MF projets de trancheuse avec des paramètres d'orientation et de support enregistrés: [`models/3mf/`](../../../models/3mf) — [bras robot leader](../../../models/3mf/SO102_leader.3mf), [bras robot suiveur](../../../models/3mf/SO102_follower_arms.3mf), [Pince et base du suiveur](../../../models/3mf/SO102_follower_gripper_base.3mf)
- Contenu du projet et profils d'imprimante: [models/README.md](models/README.md)
- STL fichiers, prêts à trancher: [`models/stl/`](../../../models/stl)
- STEP sources: [`models/step/`](../../../models/step)
- Matériau, réglages et quantités de pièces: [docs/printing.md](docs/printing.md)


<a id="2-buy-the-hardware"></a>
### 2. Acheter le matériel

Recherchez les composants dans [résumé de la nomenclature](#bill-of-materials) et [nomenklature complète avec liens d'achat](docs/bom.md).Budget **$340.22**pour les composants, ou**$373.97** y compris le matériel d'impression, avant expédition et taxes.

| Bras | Servomoteurs | Contrôleur | Alimentation |
|---|---|---|---|
| Bras suiveur | 2 × STS3235, 2 × STS3250, 2 × STS3215 | Waveshare Bus Servo Adapter | **12 V** |
| Bras leader | 6 × STS3215 | Waveshare Bus Servo Adapter | **5 V** |

> ⚠️ **Le bras maître fonctionne sous 5 V et le bras suiveur sous 12 V.** N'intervertissez pas les alimentations.

<a id="3-assemble"></a>
### 3. Assembler

- Livret imprimable, 32 pages A5: [docs/SO-ARM102_assembly_A5_v0.7.pdf](../../SO-ARM102_assembly_A5_v0.7.pdf)
- Liste des étapes avec pièces et fixations: [docs/assembly-guide.md](docs/assembly-guide.md)

Outils: clés hexagonales 1.5 mm (M2 vis) et 2 mm (M3 vis).

<a id="4-set-up-the-software"></a>
### 4. Configurer le logiciel

Servo IDs, calibration et leçons: **[lab.robonine.com](https://lab.robonine.com)**.
Utilisez le plugin du suiveur SO-ARM 102 avec le type standard `so101_leader`.
**[Installation et configuration de LeRobot](docs/lerobot.md)**.

---

<a id="bill-of-materials"></a>
## Nomenclature

Quantités et coûts de référence pour **un bras robot leader + un bras robot follower**:

| Catégorie / liens d'achat | Contenu du kit | Total (USD) |
|---|---|---:|
| [Servomoteurs](docs/bom.md#servos) | 6 × STS3215 7.4 V, 2 × STS3215 12 V, 2 × STS3235, 2 × STS3250 | $240.72 |
| [Électronique](docs/bom.md#electronics) | 2 contrôleurs, 2 blocs d'alimentation, 2 câbles USB, 1 caméra au poignet | $50.50 |
| [Pièces mécaniques](docs/bom.md#mechanical-parts) | 4 roulements, 2 tiges de guidage en acier, 4 pinces de table | $37.76 |
| [Fixations](docs/bom.md#fasteners) | Vis et écrous; vis spécifiées pour kit servomoteur incluses | $11.24 |
| **Sous-total des composants** |  | **$340.22** |
| [Matériel d'impression](docs/bom.md#printing-materials) | 0.4 kg PET-CF17 + 0.75 kg PETG allocation | $33.75 |
| **Total avec matériau d’impression** |  | **$373.97** |

L'achat de l'exemple des paquets complets et des bobines de filament à partir de zéro coûte environ **$435**, y compris les pièces détachées non utilisées. Ce sont des estimations de référence, pas de nouveaux devis fournisseurs. Les frais d'expédition, les taxes, les outils, un ordinateur, une imprimante, l'électricité et la main-d'œuvre d'assemblage sont exclus. Confirmez les prix du fournisseur, les variantes et les quantités minimales de commande avant de commander; coupez à nouveau en utilisant le trancheur d'impression 3D les 3MF projets pour vérifier la consommation de filament.

[Nomenclature complète, liens d'achat et hypothèses de coût](docs/bom.md#estimated-kit-cost).

---

<a id="urdf-export"></a>
## URDF exporter

L'exportation autonome actuelle est dans [`simulation/urdf/`](../../../simulation/urdf): [URDF](../../../simulation/urdf/so_arm_102.urdf) · [Xacro](../../../simulation/urdf/so_arm_102.xacro). Gardez `meshes/` à côté des fichiers de description; les chemins de maillage sont relatifs à ce dossier.

- **Visuals:**STL**Collisions:** boîtes ajustées, indépendamment tournées sur les huit maillons.
- ** Estimation de la masse:**PLA, remplissage à 30%, périmètres à 6, couches supérieures/inférieures à 6, hauteur des couches à 0.2 mm et largeur d'extrusion à**0.40 mm**. Ce sont des hypothèses de simulation. Utilisez [le guide d'impression](docs/printing.md) pour les paramètres de fabrication.
- **Mases matérielles:**six moteurs à 70 g chacun; roulement de base à 105 g. Masse totale estimée du modèle:**0.889 kg**.
- **Gripper:** `clamp2` imite `clamp1` avec multiplicateur `-1`.

[Paramètres d'exportation](../../../simulation/urdf/export_settings.json) et [propriétés de masse](../../../simulation/urdf/mass_properties.json) enregistrent les hypothèses. Les vérifications de géométrie et d'inertie sont enregistrées dans [export_verification.json](../../../simulation/urdf/export_verification.json).

---

<a id="-repository-structure"></a>
## 📁 Structure du dépôt

```
├── models/
│   ├── 3mf/                 # Projets de trancheuse: bras robot leader, bras robot disciple, pince et boîtier
│   ├── stl/                 # Maillages prêts à imprimer
│   │   ├── common/          # Pièces communes, dont les boîtiers de contrôleur
│   │   ├── follower/        # Pince parallèle et support de caméra
│   │   └── leader/          # Poignée, gâchette et rotation du poignet
│   └── step/                # CAD sources, même disposition que stl/
├── docs/
│   ├── printing.md          # Matériau, réglages de trancheuse, quantités
│   ├── bom.md               # Nomenclature
│   ├── assembly-guide.md    # Liste étape par étape avec pièces et fixations
│   ├── specifications.md    # Géométrie, servomoteurs, résultats de mesure vs SO-ARM 101
│   └── SO-ARM102_assembly_A5_v0.7.pdf
├── assets/
│   ├── images/              # Photos, rendus, pages de livret, photos de test
│   └── video/               # Aperçu vidéo et GIF
├── LICENSING.md             # Quelle licence couvre quel fichier
└── NOTICE                   # Attribution par un tiers
```

---

<a id="-known-issues"></a>
## ⚠️ Problèmes connus

Remarques issues de tests indépendants ; vérifiez-les au montage.

1. **Utilisez le livret v0.7.** Les anciens livrets montrent le contrôleur HAT et les anciennes pièces de pince. La v0.7 installe un Bus Servo Adapter sur les deux bras.
2. **M2 vis sont difficiles à atteindre dans plusieurs endroits.** Attendez-vous à combattre quelques-uns d'entre eux.
3. **Les pinces de préhension sont serrées sur les tiges en carbone.** Les trous de serrage sont dimensionnés pour 6.1 mm.Le diamètre des tiges varie selon les fournisseurs, vérifiez donc l'ajustement avant le montage.
4. **Vérifiez les longueurs de câble du servomoteur** avant de fermer chaque joint, en particulier de la base à l'épaule.
5. **L'ordre de montage est maladroit à deux endroits** du livret.Lire deux étapes avant la fixation.
6. **Les articulations du bras robot leader peuvent sembler lâches.** En ajoutant 8 × 2 mm joints toriques en caoutchouc entre chaque servomoteur et son claxon, le bras robot leader obtient un frottement doux et silencieux. Utilisez deux par servomoteur sur les articulations 1–4 et une sur les articulations 5–6.

Vous avez trouvé quelque chose d'autre ? Veuillez [ouvrir un problème](https://github.com/roboninecom/SO-ARM-102/issues).

---

<a id="-star-history"></a>
## ⭐ Historique des étoiles

[![Historique des étoiles — SO-ARM 102](https://api.star-history.com/svg?repos=roboninecom/so-arm-102&type=date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm-102&type=date&legend=top-left)

---

<a id="-related-projects"></a>
## Projets connexes

- [SO-ARM100/101 Pince parallèle](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper), la pince à partir de laquelle est née la pince SO-ARM 102
- [SO-ARM101](https://github.com/TheRobotStudio/SO-ARM100) par TheRobotStudio, le bras robotique de cette conception réussit
- [Comparaison pratique des servomoteurs série intelligents](https://robonine.com/smart-serial-servo-motor-comparison-robotics/), les tests derrière le choix du servomoteur
- [Choisir un filament pour les bras robotiques](https://robonine.com/choosing-filament-for-robotic-arm-applications/), les tests derrière PET-CF

---

<a id="-license"></a>
## 📄 Licence d'utilisation

Copyright (c) 2026 Robonine. Différents types de matériel portent différentes licences:

| Matériau | Licence |
|---|---|
| Designs de matériel dans `models/` | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| Logiciel et configuration | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| Documentation et images dans `docs/`, `assets/`, tous `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

Voir [LICENSING.md](LICENSING.md) et [REUSE.toml](../../../REUSE.toml) pour le mappage fichier par fichier.

---

<a id="-team"></a>
## 👥 Team

| Nom | Rôle | Contact |
|------|------|---------|
| **Alan Subin** | Ingénieur de conception: conception mécanique, CAD, livret d'assemblage | [LinkedIn](https://www.linkedin.com/in/alan-subin/) |
| **Boris Kotov** | Ingénieur logiciel et test: prototypage, impression, bancs d'essai | [Telegram](https://t.me/bkotov) |
| **Nikita Bragin** | Project Manager | [LinkedIn](https://www.linkedin.com/in/nikita-bragin-82296b29/) |
| **Mikhail Chistiakov** | Industrial Designer: look et forme du bras robotique | [Telegram](https://t.me/brrryska) |
| **Mikhail Zhmaylo** | Ingénieur Structural: modèles de rigidité, modifications de conception pour réduire la déviation | [Telegram](https://t.me/mikhail_zhmaylo) |
| **Vladislav Eremenko** | Ingénieur Structural: analyse de résistance et thermique, optimisation topologique | [Telegram](https://t.me/v1ad_eremenko) |
| **Vladimir Osipov** | Testeur et consultant: construction de test indépendante | [LinkedIn](https://www.linkedin.com/in/vladimirosipov/) |

<div align="center">

**Construit pour la communauté robotique par [Robonine](https://robonine.com)** 🤖

</div>
<!-- /translated-content -->
