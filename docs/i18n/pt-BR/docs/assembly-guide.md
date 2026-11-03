<!-- translation-navigation -->
[English](../../en/docs/assembly-guide.md) · [Русский](../../ru/docs/assembly-guide.md) · [Español](../../es/docs/assembly-guide.md) · [Français](../../fr/docs/assembly-guide.md) · [Deutsch](../../de/docs/assembly-guide.md) · [Português (Brasil)](assembly-guide.md) · [简体中文](../../zh-CN/docs/assembly-guide.md) · [日本語](../../ja/docs/assembly-guide.md) · [हिन्दी](../../hi/docs/assembly-guide.md) · [العربية](../../ar/docs/assembly-guide.md)

[Original em inglês](../../../assembly-guide.md)

[Documentação](../README.md) · [Impressão](printing.md) · [Materiais](bom.md) · [Montagem](assembly-guide.md) · [Especificações](specifications.md) · [Modelos](../models/README.md) · [Contribuir](../CONTRIBUTING.md) · [Licenças](../LICENSING.md) · [Traduções](translations.md)

> Tradução completa do documento. As ilustrações e o manual PDF original são compartilhados entre os idiomas. Tradução feita com auxílio de IA; ainda não revisada por falantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="assembly-guide"></a>
# Guia de montagem

Este guia segue o livreto impresso [SO-ARM102_assembly_A5_v0.7.pdf](../../../SO-ARM102_assembly_A5_v0.7.pdf) página por página.Imprima o livreto em A5 horizontal se preferir papel.

Antes de começar:

- Imprima todas as peças de [printing.md](printing.md) e colete o hardware de [bom.md](bom.md).
- Você precisa das chaves hexadecimais 1.5 mm (M2) e 2 mm (M3).
- Dois lugares na ordem atual são estranhos, veja [Problemas conhecidos](Dois lugares na ordem atual são estranhos, veja [Problemas conhecidos](../README.md#-known-issues).

> ⚠️ **O braço líder funciona com 5 V, e o braço seguidor com 12 V.** Mantenha as fontes de alimentação separadas.

Use um trava-roscas removível compatível com o plástico impresso, como [Vibra-Tite VC-3](https://www.vibra-tite.com/faq/if-vc-3-has-mek-how-can-it-be-plastic-compatible/). Aplique VC-3 na rosca do parafuso metálico e deixe secar completamente antes da montagem (pelo menos 30 minutos conforme a [ficha técnica](https://www.vibra-tite.com/wp-content/uploads/213_tds.pdf)); não aplique o produto úmido no plástico. Teste primeiro a compatibilidade com seu filamento em uma peça de teste.

![Ferramentas e aviso de tensão](../../../../assets/images/assembly/tools-and-voltage.jpg)

<a id="order-of-work"></a>
## Ordem de trabalho

<a id="reading-the-illustrations"></a>
### Lendo as ilustrações

A miniatura da peça e a quantidade mostram o que adicionar. O círculo numerado é a etapa de montagem; os pontos mostram o progresso. Os números das peças, tamanhos dos fixadores e IDs dos servomotores são iguais em todos os idiomas.

<a id="assembly-sequence"></a>
### Sequência de montagem

1. Monte os chifres nos servomotores.
2. Construa o corpo do braço robótico **duas vezes**, uma vez para o braço robótico seguidor e outra para o braço robótico líder (etapas 1–13). Nas etapas 12–13, instale um Bus Servo Adapter em cada braço.
3. Construa a pinça paralela (etapas da pinça 1–6).
4. Finalize o seguidor: suporte da câmera, garra e câmera (etapas 1–3 do seguidor).
5. Finalize o líder: alça e gatilho (etapas 1–2 do líder).

<a id="servo-ids"></a>
## IDs dos servos

Configure o ID de cada servomotor antes que ele entre no braço do robô. Ferramentas para configurar IDs e calibração estão em [lab.robonine.com](https://lab.robonine.com).

![Servo IDs](../../../../assets/images/assembly/servo-ids.jpg)

| ID | Junta | Servo do seguidor | Servo do líder |
|:-:|---|---|---|
| 1 | Rotação da base | STS3235 | STS3215 |
| 2 | Elevação do ombro | STS3250 | STS3215 |
| 3 | Flexão do cotovelo | STS3250 | STS3215 |
| 4 | Flexão do punho | STS3235 | STS3215 |
| 5 | Rotação do punho | STS3215 | STS3215 |
| 6 | Garra / gatilho | STS3215 | STS3215 |

<a id="0-servo-horns"></a>
## 0. Servo chifres

Monte um chifre com um parafuso M3 × 6 no servomotor ID 1. Servos ID 2, 3 e 4 obtêm um chifre em ambos os lados. Parafusos de chifre vêm com os servomotores.

Se você adicionar anéis de vedação ao braço do robô líder, coloque-os entre o servomotor e a buzina agora.Obter essa ordem errada pode bloquear o anel entre a carcaça do servomotor e a buzina.

<a id="111-arm-body-follower-and-leader"></a>
<a id="113-arm-body-follower-and-leader"></a>
## 1–13. Corpo do braço: seguidor e líder

Repita esses passos para ambos os braços do robô. Os nomes das peças impressas correspondem a [printing.md](printing.md).

| Etapa | Peças | Fixadores |
|:-:|---|---|
| 1 | SO102.02.060 Suporte inferior do servomotor, SO102.02.040 Placa superior inferior | Porca 3 × M3×16, 3 × M3 |
| 2 | — | Porca 3 × M3×16, 3 × M3 |
| 3 | ID do Serviço 1 | 4 × M2×6 |
| 4 | SO102.02.020 anel de base, rolamento 6812, SO102.02.050 anel inferior, SO102.02.010 Base | Porca 6 × M3×16, 6 × M3 |
| 5 | SO102.02.030 Arruela de base | 4 × M3×10, 6 × M3×16 |
| 6 | Servos ID 2 e ID 3, 2 × SO102.02.070 braço inferior do robô, 2 cabos curtos, 1 cabo longo | 16 × M2×6 |
| 7 | Servo ID 4, SO102.02.080-01 braço superior direito do robô, 1 cabo curto | 4 × M2×6 |
| 8 | SO102.02.080 Braço superior do robô esquerdo, 2 × SO102.02.130 Encaixe de cabo | 4 × M2×6, 8 × M3×10 |
| 9 | Servo ID 5, SO102.02.090 Suporte de pulso, chifre do servomotor | 1 × M3×6, 4 × 2×6 auto-roscante |
| 10 | 1 cabo curto | 8 × M3×10 |
| 11 | — | 8 × M3×10 |
| 12 | SO102.02.110 Suporte da placa do líder, Bus Servo Adapter | 4 × porca M2, 4 × M2×8 |
| 13 | SO102.02.110-01 Tampa da placa do líder, 1 × cabo longo | — |

| | | |
|:-:|:-:|:-:|
| ![Passo 1](../../../../assets/images/assembly/steps/shared-01.jpg) | ![Passo 2](../../../../assets/images/assembly/steps/shared-02.jpg) | ![Passo 3](../../../../assets/images/assembly/steps/shared-03.jpg) |
| ![Passo 4](../../../../assets/images/assembly/steps/shared-04.jpg) | ![Passo 5](../../../../assets/images/assembly/steps/shared-05.jpg) | ![Passo 6](../../../../assets/images/assembly/steps/shared-06.jpg) |
| ![Passo 7](../../../../assets/images/assembly/steps/shared-07.jpg) | ![Passo 8](../../../../assets/images/assembly/steps/shared-08.jpg) | ![Passo 9](../../../../assets/images/assembly/steps/shared-09.jpg) |
| ![Passo 10](../../../../assets/images/assembly/steps/shared-10.jpg) | ![Passo 11](../../../../assets/images/assembly/steps/shared-11.jpg) | ![Passo 12](../../../../assets/images/assembly/steps/shared-12.jpg) |
| ![Passo 13](../../../../assets/images/assembly/steps/shared-13.jpg) | | |

Verifique se cada cabo do servomotor atinge a próxima junta com alguma folga antes de fechar a junta.

<a id="gripper-16-follower-only"></a>
## Pinça 1–6, braço de robô seguidor apenas

| Etapa | Peças | Fixadores |
|:-:|---|---|
| 1 | RB9.01.062.040 Engrenagem para garra no chifre do servomotor, ID do servomotor 6 | 4 × M3×4 parafuso de fixação, 1 × M3×6 |
| 2 | 2 × RB9.01.062.025 (D6.1) braçadeira, 2 × RB9.01.062.030 cremalheira de engrenagem, 2 × RB9.01.062.100 prego | — |
| 3 | 2 × haste Ø6 × 125 mm | — |
| 4 | RB9.01.062.012 Quadro principal (D6.1), 2 × rolamento MF106, 2 × RB9.01.062.050 Arruela | 2 × M3×10 |
| 5 | Encaixe as hastes no quadro principal | — |
| 6 | Empurre as braçadeiras para suas paradas exteriores, introduza o servomotor | 3 × 2×6 auto-roscante |

O ×2 na etapa 2 indica um conjunto de mandíbula para cada lado. As quantidades na tabela são os totais.

Aperte os parafusos de fixação do lado do braço do servo em direção à engrenagem, sem deixar folga entre eles. Antes da etapa 6, mova o servo de ID 6 para a posição mínima, para que a garra feche completamente e abra até os 85 mm. Antes de fechar o conjunto, deslize manualmente as duas garras ao longo das hastes. Elas devem se mover livremente, sem travar.

| | | |
|:-:|:-:|:-:|
| ![Gripper 1](../../../../assets/images/assembly/steps/gripper-01.jpg) | ![Gripper 2](../../../../assets/images/assembly/steps/gripper-02.jpg) | ![Gripper 3](../../../../assets/images/assembly/steps/gripper-03.jpg) |
| ![Gripper 4](../../../../assets/images/assembly/steps/gripper-04.jpg) | ![Gripper 5](../../../../assets/images/assembly/steps/gripper-05.jpg) | ![Gripper 6](../../../../assets/images/assembly/steps/gripper-06.jpg) |

<a id="follower-15"></a>
<a id="follower-13"></a>
## Braço robótico seguidor 1–3

| Etapa | Peças | Fixadores |
|:-:|---|---|
| 1 | RB9.01.062.075 Suporte para câmera | 4 × M3×10 |
| 2 | Conjunto do prendedor no pulso | 4 × 2×6 auto-roscante |
| 3 | RB9.01.062.090 Espaçador de câmera, câmera USB | Porca 4 × M2×8, 4 × M2 |

| | | |
|:-:|:-:|:-:|
| ![Braço robótico seguidor 1](../../../../assets/images/assembly/steps/follower-01.jpg) | ![Braço robótico seguidor 2](../../../../assets/images/assembly/steps/follower-02.jpg) | ![Braço robótico seguidor 3](../../../../assets/images/assembly/steps/follower-03.jpg) |

<a id="leader-14"></a>
<a id="leader-12"></a>
## Braço robótico líder 1–2

| Etapa | Peças | Fixadores |
|:-:|---|---|
| 1 | SO102 Punho, SO102 Rolo de pulso | 4 × M3×6, 1 × 2×6 auto-roscante |
| 2 | SO102 Gatilho, servomotor ID 6 | 4 × M3×6, 4 × 2×6 auto-roscante |

| | |
|:-:|:-:|
| ![Braço robótico líder 1](../../../../assets/images/assembly/steps/leader-01.jpg) | ![Braço robótico líder 2](../../../../assets/images/assembly/steps/leader-02.jpg) |

<a id="mounting-and-first-start"></a>
## Fixação e primeira inicialização

1. Prenda cada base à mesa com dois grampos em C.
2. Conecte o controlador do braço seguidor à fonte de 12 V e o controlador do braço líder à fonte de 5 V.
3. Conecte ambos os controles ao computador com USB-C.
4. Calibre ambos os braços do robô e inicie a teleoperação em [lab.robonine.com](https://lab.robonine.com), ou com o fluxo de trabalho LeRobot SO-101.
<!-- /translated-content -->
