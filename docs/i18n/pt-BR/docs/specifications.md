<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](../../es/docs/specifications.md) · [Français](../../fr/docs/specifications.md) · [Deutsch](../../de/docs/specifications.md) · [Português (Brasil)](specifications.md) · [简体中文](../../zh-CN/docs/specifications.md) · [日本語](../../ja/docs/specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[Original em inglês](../../../specifications.md)

[Documentação](../README.md) · [Impressão](printing.md) · [Materiais](bom.md) · [Montagem](assembly-guide.md) · [Especificações](specifications.md) · [Modelos](../models/README.md) · [Contribuir](../CONTRIBUTING.md) · [Licenças](../LICENSING.md) · [Traduções](translations.md)

> Tradução completa do documento. As ilustrações e o manual PDF original são compartilhados entre os idiomas. Tradução feita com auxílio de IA; ainda não revisada por falantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="specifications-and-test-results"></a>
# Especificações e resultados de testes

Medido em Robonine protótipos em agosto e setembro 2026.Os números marcados com *calculados* vêm das folhas de dados do modelo URDF e servomotor, não de uma medição.

<a id="geometry"></a>
## Geometria

| Junta | Faixa |
|---|---|
| Rotação da base | −176° … +176° (352°) |
| Elevação do ombro | −43° … +181° (224°) |
| Flexão do cotovelo | −166° … +77° (243°) |
| Flexão do punho | −85° … +111° (196°) |
| Rotação do punho | −165° … +163° (328°) |
| Garra | 0 … 85 mm |

| Elo | Entre eixos |
|---|---|
| Rotação base para ombro | 85 mm |
| Ombro ao cotovelo | 119 mm |
| Flexão do cotovelo ao pulso | 139 mm |
| Pulso flexível para rolo de pulso | 62 mm |
| Rolo do pulso à ponta do prendedor | 132 mm |

| Alcance, centro da ponta do prendedor |  |
|---|---|
| Raio horizontal | 483 mm |
| Altura acima da parte inferior baixa | até 544 mm |
| Abaixo da parte inferior da base, braço do robô sobre uma borda de mesa | até −301 mm |

O alcance foi calculado a partir de 100,000 poses aleatórias dentro dos limites da articulação, sem autocolisão.

<a id="servos"></a>
## Servos

| Junta | Braço seguidor | Braço líder |
|---|---|---|
| 1 Rotação da base | STS3235 | STS3215 |
| 2 Elevação de ombro | STS3250 | STS3215 |
| 3 Flexão do cotovelo | STS3250 | STS3215 |
| 4 Flexão do pulso | STS3235 | STS3215 |
| 5 Rolo de pulso | ST-3215-C049, 1:191 | STS3215 |
| 6 Pinça / gatilho | ST-3215-C049, 1:191 | STS3215 |
| Alimentação | 12 V | 5 V |

<a id="gripper"></a>
## Garra

| | |
|---|---|
| Tipo | Paralelo, cremalheira e pinhão, duas maxilas móveis |
| Abertura | 85 mm |
| Caixa, largura máxima recomendada | sobre 75 mm |
| Cilindro, diâmetro máximo recomendado | sobre 70 mm |
| Esfera, diâmetro máximo recomendado | sobre 60 mm |
| Câmera | Câmera USB montada no prendedor |

<a id="measured-results-against-so-arm-101"></a>
## Resultados medidos contra SO-ARM 101

| Métrica | SO-ARM 101 | SO-ARM 102 | Variação |
|---|---|---|---|
| Deflexão na ponta da garra, 300 g, braço do robô totalmente estendido ¹ | 7.5 mm | 3.4 mm | −55 % |
| Mesmo, todos os links em 100% de preenchimento ¹ | — | 2.34 mm | −69 % |
| Raio horizontal | 441 mm | 483 mm | +9.5 % |
| Alcance atrás da base | 377 mm | 473 mm | +25.5 % |
| Faixa de rotação da base | 220° | 352° | +60 % |
| Faixa do cotovelo | 194° | 243° | +25 % |
| Velocidade sem carga do ombro e cotovelo, *calculada* | 270 °/s | 450 °/s | +67 % |
| Folga da junta da base | 8.75 contagens | 5.00 contagens | −43 % |
| Erro de ponta horizontal da folga base, *calculado* | ±2.96 mm | ±1.85 mm | −37.5 % |
| Repetibilidade | — | sobre 0.1 mm |  |
| Ruído a 1 m | 70 dB | 60 dB | −10 dB |
| Carga útil nominal | 150 g | 300 g |  |

¹ Ambos os braços do robô foram construídos com manequins de servomotores impressos nas juntas 2, 3 e 4, portanto apenas a estrutura é comparada. SO-ARM 101 impresso em PLA, SO-ARM 102 em Fiberon PET-CF17 com 25% de preenchimento. Uma segunda execução do mesmo teste SO-ARM 102 deu 3.9 mm.

| SO-ARM 101 | SO-ARM 102 |
|:-:|:-:|
| ![SO-ARM 101 teste de rigidez](../../../../assets/images/tests/stiffness-so-arm-101.jpg) | ![SO-ARM 102 teste de rigidez](../../../../assets/images/tests/stiffness-so-arm-102.jpg) |

<a id="current-and-temperature-follower"></a>
## Corrente e temperatura, braço de robô seguidor

Medido com uma carga 300 g em uma trajetória repetida, ambiente 30 °C, seis servomotores STS3250.

| | |
|---|---|
| Corrente média | 1.26 A |
| Corrente de pico | 3.28 A |
| Temperatura máxima do servo | 46 °C |

<a id="absolute-accuracy"></a>
## Precisão absoluta

Os ajustes ainda estão em andamento. Com os parâmetros PID de fábrica dos servos, a ponta cedia cerca de 50 mm sob o peso do próprio braço totalmente estendido. O ajuste do PID reduziu isso para cerca de 5 mm. Um perfil específico de precisão está em desenvolvimento.
<!-- /translated-content -->
