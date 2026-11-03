<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[Original em inglês](../../../README.md)

[Documentação](README.md) · [Impressão](docs/printing.md) · [Materiais](docs/bom.md) · [Montagem](docs/assembly-guide.md) · [Especificações](docs/specifications.md) · [Modelos](models/README.md) · [Contribuir](CONTRIBUTING.md) · [Licenças](LICENSING.md) · [Traduções](docs/translations.md)

> Tradução completa do documento. As ilustrações e o manual PDF original são compartilhados entre os idiomas. Tradução feita com auxílio de IA; ainda não revisada por falantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102"></a>
# SO-ARM 102

<div align="center">

[![SO-ARM 102](../../../assets/images/photos/so-arm-102-live.jpg)](../../../assets/video/so-arm-102-preview.mp4)

**🎥 [Veja o vídeo de pré-visualização](../../../assets/video/so-arm-102-preview.mp4)**·**🛒 [Compre o kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

**SO-ARM 102 é um kit de braços robóticos líder–seguidor de código aberto para teleoperação e aprendizado por imitação. Cada braço tem cinco graus de liberdade e uma garra.**

<p align="left">
Com base no SO-ARM 100 e 101, combina uma estrutura de PET-CF mais rígida com uma garra paralela.
</p>

[![Hardware: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt) [![Software: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt) [![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt) [![GitHub release](https://img.shields.io/github/v/release/roboninecom/SO-ARM-102)](https://github.com/roboninecom/SO-ARM-102/releases/latest)

📩 [hello@robonine.com](mailto:hello@robonine.com)

**Orçamento DIY: ~$340 para componentes, ou ~$374 incluindo material de impressão.** [Resumo da lista de materiais](#bill-of-materials) · [Custos e links de compra detalhados](docs/bom.md#estimated-kit-cost)

> Prefere não obter as peças e imprimi-las você mesmo? **[Comprar o kit SO-ARM 102](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

</div>

---

<a id="-what-changed-against-so-arm-101"></a>
## ✨ O que mudou em relação a SO-ARM 101

|  | SO-ARM 101 | SO-ARM 102 |
|---|---|---|
| Garra | Mandíbula angular | Garrafa paralela, 85 mm span |
| Material da estrutura | PLA | PET-CF (Fiberon PET-CF17 testado) |
| Estrutura | Elos maciços | Elos otimizados por topologia |
| Faixa de rotação da base | 220° | **352°** |
| Alcance horizontal | 441 mm | **483 mm** |
| Deflexão na garra, 300 g carga ¹ | 7.5 mm | **3.4–3.9 mm** |
| Velocidade de ombro e cotovelo | 45 RPM (STS3215) | **75 RPM (STS3250)** |
| Ruído a 1 m | 70 dB | **60 dB** |

¹ Ambos os braços do robô foram construídos com manequins de servomotores impressos, portanto a estrutura é comparada, não os motores.Os resultados completos e as condições de teste estão em [docs/specifications.md](docs/specifications.md).

---

<a id="-preview"></a>
## 🎥 Pré-visualização

<div align="center">

[![SO-ARM 102 preview](../../../assets/video/so-arm-102-preview.gif)](../../../assets/video/so-arm-102-preview.mp4)

*Clique para ver o vídeo completo, 21 s*

</div>

---

<a id="-configurations"></a>
## 🤝 Configurações do sistema

<a id="single-arm-one-leader--one-follower"></a>
### Braço do único-robô: um braço de robô líder + um braço de robô seguidor

O kit padrão. Mova o braço do robô líder à mão, e o braço do robô seguidor repete o movimento.Use-o para teleoperação e para gravar demonstrações para aprendizagem por imitação.

![Um braço líder e um braço seguidor](../../../assets/images/renders/config-single-arm.jpg)

<a id="bimanual-two-leaders--two-followers"></a>
### Bimanual: dois líderes + dois seguidores

Dois kits lado a lado.Cada mão conduz seu próprio braço robótico líder, para que os seguidores possam passar objetos, segurar e trabalhar em uma peça ou fazer qualquer tarefa que precise de duas mãos.

![Dois braços líderes e dois braços seguidores](../../../assets/images/renders/config-dual-arm.jpg)

<a id="the-two-arms"></a>
### Os dois braços do robô

| Braço seguidor | Braço líder |
|:-:|:-:|
| ![Braço seguidor](../../../assets/images/renders/follower.jpg) | ![Braço líder](../../../assets/images/renders/leader.jpg) |
| Garrafa paralela, câmera de pulso, 12 V | Punho com gatilho, 5 V |

---

<a id="-build-it-in-four-steps"></a>
## 🚀 Construa-o em quatro etapas

Prefere um kit pronto? **[Comprar o SO-ARM 102 kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

<a id="1-print-the-parts"></a>
### 1. Imprimir as peças

As peças individuais se encaixam em uma placa de construção de impressora 3D 180 × 180 mm. A maior parte tem 160 mm comprimento. Os layouts de placa 3MF fornecidos usam uma placa de construção de impressora 3D 256 × 256 mm.

- 3MF projetos de slicer com configurações salvas de orientação e suporte: [`models/3mf/`](../../../models/3mf) — [braço robótico líder](../../../models/3mf/SO102_leader.3mf), [braço robótico seguidor](../../../models/3mf/SO102_follower_arms.3mf), [Garra e base do seguidor](../../../models/3mf/SO102_follower_gripper_base.3mf)
- Conteúdo do projeto e perfis de impressora: [models/README.md](models/README.md)
- STL arquivos, prontos para cortar: [`models/stl/`](../../../models/stl)
- STEP fontes: [`models/step/`](../../../models/step)
- Material, configurações e quantidades de peças: [docs/printing.md](docs/printing.md)


<a id="2-buy-the-hardware"></a>
### 2. Compre o hardware

Obtenha os componentes do [resumo da lista de materiais](#bill-of-materials) e [lista completa com links de compra](docs/bom.md).Orçamento **$340.22**para componentes, ou**$373.97** incluindo material de impressão, antes do envio e impostos.

| Braço | Servos | Controlador | Alimentação |
|---|---|---|---|
| Braço seguidor | 2 × STS3235, 2 × STS3250, 2 × STS3215 | Waveshare Bus Servo Adapter | **12 V** |
| Braço líder | 6 × STS3215 | Waveshare Bus Servo Adapter | **5 V** |

> ⚠️ **O braço líder funciona com 5 V e o braço seguidor com 12 V.** Não inverta as fontes de alimentação.

<a id="3-assemble"></a>
### 3. Assemble

- Livro imprimível, 32 páginas A5: [docs/SO-ARM102_assembly_A5_v0.7.pdf](../../SO-ARM102_assembly_A5_v0.7.pdf)
- Lista de passos com peças e fixadores: [docs/assembly-guide.md](docs/assembly-guide.md)

Ferramentas: chaves hexagonais 1.5 mm (M2 parafusos) e 2 mm (M3 parafusos).

<a id="4-set-up-the-software"></a>
### 4. Configurar o software

IDs de servo, calibração e lições: **[lab.robonine.com](https://lab.robonine.com)**.
Use o plugin do seguidor SO-ARM 102 com o tipo padrão `so101_leader`.
**[Instalação e configuração do LeRobot](docs/lerobot.md)**.

---

<a id="bill-of-materials"></a>
## Lista de materiais

Quantidades e custos de referência para **um braço robótico líder + um braço robótico seguidor**:

| Categoria / links de compra | Conteúdo do kit | Total (USD) |
|---|---|---:|
| [Servos](docs/bom.md#servos) | 6 × STS3215 7.4 V, 2 × STS3215 12 V, 2 × STS3235, 2 × STS3250 | $240.72 |
| [Eletrônica](docs/bom.md#electronics) | 2 controladores, 2 fontes de alimentação, 2 cabos USB, 1 câmera de pulso | $50.50 |
| [Peças mecânicas](docs/bom.md#mechanical-parts) | 4 rolamentos, 2 hastes de guia de aço, 4 grampos de mesa | $37.76 |
| [Fixadores](docs/bom.md#fasteners) | Parafusos e porcas; parafusos especificados do servomotor-kit incluídos | $11.24 |
| **Subtotal dos componentes** |  | **$340.22** |
| [Material de impressão](docs/bom.md#printing-materials) | 0.4 kg PET-CF17 + 0.75 kg PETG subsídio | $33.75 |
| **Total com material de impressão** |  | **$373.97** |

Comprar o exemplo de pacotes completos e carretéis de filamentos do zero custa cerca de **$435**, incluindo peças de reposição não utilizadas. Estas são estimativas de referência, não novas cotações de fornecedores. Envio, impostos, ferramentas, um computador, uma impressora, eletricidade e mão-de-obra de montagem estão excluídos. Confirme os preços dos fornecedores, variantes e quantidades mínimas de pedido antes de encomendar; corte novamente usando o slicer de impressão 3D os 3MF projetos para verificar o consumo de filamento.

[BOM completo, links de compra e pressupostos de custo](docs/bom.md#estimated-kit-cost).

---

<a id="urdf-export"></a>
## Exportar URDF

A exportação autônoma atual está em [`simulation/urdf/`](../../../simulation/urdf): [URDF](../../../simulation/urdf/so_arm_102.urdf) · [Xacro](../../../simulation/urdf/so_arm_102.xacro). Mantenha `meshes/` ao lado dos arquivos de descrição; caminhos de malha são relativos a esta pasta.

- **Visuals:**STL malhas.**Collisions:** caixas rotativas independentes em todos os oito links.
- **Estimativa de massa:**PLA, 30% de preenchimento, 6 perímetros, 6 camadas superiores/inferiores, 0.2 mm altura da camada e**0.40 mm largura da extrusão**.Estes são pressupostos de simulação; use [o guia de impressão](docs/printing.md) para configurações de fabricação.
- **Massas de hardware:**seis motores em 70 g cada; rolamento base em 105 g. Massa total estimada do modelo:**0.889 kg**.
- **Gripper:** `clamp2` imita `clamp1` com multiplicador `-1`.

[Configurações de exportação](../../../simulation/urdf/export_settings.json) e [propriedades da massa](../../../simulation/urdf/mass_properties.json) registram as suposições. Verificações de geometria e inércia são registradas em [export_verification.json](../../../simulation/urdf/export_verification.json).

---

<a id="-repository-structure"></a>
## 📁 Estrutura do repositório

```
├── models/
│   ├── 3mf/                 # Projetos do cortador: braço de robô líder, braço de robô seguidor, garra e caixa da placa
│   ├── stl/                 # Malhas prontas para impressão
│   │   ├── common/          # Peças comuns, incluindo caixas dos controladores
│   │   ├── follower/        # Garra paralela e suporte da câmera
│   │   └── leader/          # Punho, gatilho e rotação do pulso
│   └── step/                # CAD fontes, mesmo layout que stl/
├── docs/
│   ├── printing.md          # Material, configurações do slicer, quantidades
│   ├── bom.md               # Lista de materiais
│   ├── assembly-guide.md    # Lista de passos com peças e fixadores
│   ├── specifications.md    # Geometria, servomotores, resultados medidos vs SO-ARM 101
│   └── SO-ARM102_assembly_A5_v0.7.pdf
├── assets/
│   ├── images/              # Fotos, renderizações, páginas de livreto, fotos de teste
│   └── video/               # Visualização de vídeo e GIF
├── LICENSING.md             # Qual licença cobre qual arquivo
└── NOTICE                   # Atribuição de terceiros
```

---

<a id="-known-issues"></a>
## ⚠️ Problemas conhecidos

Notas de montagem de testes independentes; confira durante a montagem.

1. **Use o livreto v0.7.** Os anteriores mostram o controlador HAT e peças antigas da garra. A v0.7 instala um Bus Servo Adapter nos dois braços.
2. **M2 parafusos são difíceis de alcançar em vários lugares.** Espere lutar contra alguns deles.
3. **As braçadeiras da pinça funcionam firmemente em hastes de carbono.** Os orifícios das braçadeiras são dimensionados para 6.1 mm.Os diâmetros das hastes variam entre fornecedores, portanto verifique o ajuste antes da montagem.
4. **Verifique os comprimentos dos cabos do servomotor** antes de fechar cada junta, especialmente da base para o ombro.
5. **A ordem de montagem é estranha em dois lugares** do livreto.Leia dois passos antes de fixar.
6. **As articulações do braço do robô líder podem parecer soltas.** A adição de 8 × 2 mm anéis de borracha entre cada servomotor e sua buzina dá ao braço do robô líder um atrito suave e silencioso. Use dois por servomotor nas articulações 1–4 e um nas articulações 5–6.

Por favor, [abra um problema](https://github.com/roboninecom/SO-ARM-102/issues).

---

<a id="-star-history"></a>
## ⭐ Histórico de estrelas

[![Histórico de estrelas — SO-ARM 102](https://api.star-history.com/svg?repos=roboninecom/so-arm-102&type=date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm-102&type=date&legend=top-left)

---

<a id="-related-projects"></a>
## 🔗 Projetos relacionados

- [SO-ARM100/101 Parallel Gripper](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper), a pinça da qual o SO-ARM 102 cresceu
- [SO-ARM101](https://github.com/TheRobotStudio/SO-ARM100) por TheRobotStudio, o braço robótico deste projeto é bem sucedido
- [Comparação prática de servomotores serial inteligente](https://robonine.com/smart-serial-servo-motor-comparison-robotics/), os testes por trás da escolha do servomotor
- [Escolhendo um filamento para braços robóticos](https://robonine.com/choosing-filament-for-robotic-arm-applications/), os testes por trás de PET-CF

---

<a id="-license"></a>
## 📄 Licença de uso

Copyright (c) 2026 Robonine. Diferentes tipos de material carregam licenças diferentes:

| Material | Licença |
|---|---|
| Designs de hardware em `models/` | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| Software e configuração | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| Documentação e imagens em `docs/`, `assets/`, todos `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

Veja [LICENSING.md](LICENSING.md) e [REUSE.toml](../../../REUSE.toml) para o mapa arquivo-a-arquivo.

---

<a id="-team"></a>
## 👥 Team

| Nome | Função | Contato |
|------|------|---------|
| **Alan Subin** | Engenheiro de Projeto: projeto mecânico, CAD, folheto de montagem | [LinkedIn](https://www.linkedin.com/in/alan-subin/) |
| **Boris Kotov** | Engenheiro de Software e Testes: protótipos, impressão, bancos de teste | [Telegram](https://t.me/bkotov) |
| **Nikita Bragin** | Gerente de Projeto | [LinkedIn](https://www.linkedin.com/in/nikita-bragin-82296b29/) |
| **Mikhail Chistiakov** | Industrial Designer: aparência e forma do braço robótico | [Telegram](https://t.me/brrryska) |
| **Mikhail Zhmaylo** | Engenheiro Estrutural: modelos de rigidez, mudanças no projeto para reduzir a deflexão | [Telegram](https://t.me/mikhail_zhmaylo) |
| **Vladislav Eremenko** | Engenheiro Estrutural: análise de resistência e térmica, otimização topológica | [Telegram](https://t.me/v1ad_eremenko) |
| **Vladimir Osipov** | Tester e Consultor: construção de teste independente | [LinkedIn](https://www.linkedin.com/in/vladimirosipov/) |

<div align="center">

**Desenvolvido para a comunidade de robótica por [Robonine](https://robonine.com)** 🤖

</div>
<!-- /translated-content -->
