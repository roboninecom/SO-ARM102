<!-- translation-navigation -->
[English](../../en/docs/bom.md) · [Русский](../../ru/docs/bom.md) · [Español](../../es/docs/bom.md) · [Français](../../fr/docs/bom.md) · [Deutsch](../../de/docs/bom.md) · [Português (Brasil)](bom.md) · [简体中文](../../zh-CN/docs/bom.md) · [日本語](../../ja/docs/bom.md) · [हिन्दी](../../hi/docs/bom.md) · [العربية](../../ar/docs/bom.md)

[Original em inglês](../../../bom.md)

[Documentação](../README.md) · [Impressão](printing.md) · [Materiais](bom.md) · [Montagem](assembly-guide.md) · [Especificações](specifications.md) · [Modelos](../models/README.md) · [Contribuir](../CONTRIBUTING.md) · [Licenças](../LICENSING.md) · [Traduções](translations.md)

> Tradução completa do documento. As ilustrações e o manual PDF original são compartilhados entre os idiomas. Tradução feita com auxílio de IA; ainda não revisada por falantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="bill-of-materials"></a>
# Lista de materiais

As quantidades são para um kit completo: um braço de robô seguidor e um braço de robô líder.As peças impressas estão listadas separadamente em [printing.md](printing.md).

<a id="estimated-kit-cost"></a>
## Custo estimado do kit

**Um braço de robô líder + um braço de robô seguidor: $340 em componentes, ou $374 incluindo material de impressão.**

| Categoria | Custo das quantidades utilizadas (USD) | Comprar pacotes completos / carretéis (USD) |
|---|---:|---:|
| Serviços (12 pcs) | $240.72 | $240.72 |
| Eletrônica, câmera e fontes de alimentação | $50.50 | $50.50 |
| Rolamentos, barras de guia de aço e grampos de mesa | $37.76 | $49.70 |
| Fixadores | $11.24 | $28.60 |
| **Subtotal dos componentes** | **$340.22** | **$368.82** |
| Material de impressão: 0.4 kg PET-CF17 + 0.75 kg PETG | $33.75 | $66.0 |
| **Total com material de impressão** | **$373.97** | **$434.82** |

A coluna **Total (USD)** é o custo da quantidade necessária para um kit, usando a oferta de referência por trás do total de cada linha existente (não a soma das ofertas dos fornecedores). Os parafusos incluídos custam $0; os tubos de carbono alternativos são excluídos dos totais. As estimativas usam os preços de referência listados abaixo, com cada linha arredondada aos centésimos. Não são cotações de novos fornecedores: confirme as variantes selecionadas, quantidades mínimas de pedido e preços antes de encomendar. Envio, impostos, ferramentas, computador, impressora, eletricidade e trabalho de montagem estão excluídos.

A coluna de pacote completo inclui peças de reposição não utilizadas, 0.5 kg PET-CF17 bobina e 1 kg PETG bobina. As quantidades de impressão são as permissões do orçamento; corte novamente usando o slicer de impressão 3D os 3MF projetos fornecidos para suas configurações.

![Hardware do kit](../../../../assets/images/assembly/hardware.jpg)

<a id="servos"></a>
## Servos

| Junta | ID | Braço seguidor | Braço líder |
|---|:-:|---|---|
| Rotação da base | 1 | ST-3235-С001 | ST-3215-C066, 1:191 |
| Elevação do ombro | 2 | ST-3250-С002 | ST-3215-C066, 1:191 |
| Flexão do cotovelo | 3 | ST-3250-С002 | ST-3215-C066, 1:191 |
| Flexão do punho | 4 | ST-3235-С001 | ST-3215-C066, 1:191 |
| Rotação do punho | 5 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |
| Garra / gatilho | 6 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |

Totais: 6 × STS3215 7.4V, 2 × STS3215 12V, 2 × STS3235 12V, 2 × STS3250 12V. Todos são servomotores de barramento serial Feetech TTL.

| Servo | Qtd. | Seleção | Aliexpress link | Preço unitário (USD) | Alibaba link | Preço unitário (USD) | Total (USD) |
|---|---|---|---|---|---|---|---|
| STS3215 | 6 | 7.4V TTL versão para servomotores de braço de robô líder. Selecione ST-3215-C066 (7.4V). | [Aliexpress](https://www.aliexpress.us/item/3256811860804361.html) | $32.8 | [Alibaba](https://www.alibaba.com/product-detail/Feetech-SO-ARM101-LeRobot-Open-Source_1601636174153.html) | $6.74 | $40.44 |
| STS3215 | 2 | Versão 12V TTL para articulações de braço de robô seguidor 5 e 6. Selecione ST-3215-C049 (12V30KG). | [Aliexpress](https://www.aliexpress.us/item/3256811832699316.html) | $55.8 para 2pcs | [Alibaba](https://www.alibaba.com/product-detail/6pcs-12V-30KG-1-345-STS3215_1601900233170.html) | $14.70 | $29.40 |
| STS3235 | 2 | Versão 12V TTL para articulações de braço de robô seguidor 1 e 4. | [Aliexpress](https://www.aliexpress.us/item/3256810213842277.html) | $63 | [Alibaba](https://www.alibaba.com/product-detail/FEETECH-STS3235-12V-30KG-TTL-Dual_1601910640629.html) | $40.79 | $81.58 |
| STS3250 | 2 | Versão 12V TTL para articulações de braço de robô seguidor 2 e 3. | [Aliexpress](https://www.aliexpress.us/item/3256811995148799.html) | $126.4 para 2pcs | [Alibaba](https://www.alibaba.com/product-detail/Feetech-STS3250-12V-50kg-Servo-High_1601711893549.html) | $44.65 | $89.30 |
| **Total** |  |  |  |  |  |  | **$240.72** |

- **Braço de robô seguidor, 12V.** STS3250 é um servomotor sem escovas de 50 kg·cm em 75 RPM. Ele aciona as duas articulações que carregam a maior carga. STS3235 é um servomotor de 30 kg·cm com folga menor do que o STS3215.
- **Braço do robô líder, 5V.**Os servomotores do braço do robô líder são apenas lidos, nunca carregados. Você pode usar um passivo ST-3215-C066 sem motor e caixa de engrenagens**somente** para o braço do robô líder.
- Servo chifres e os M3 × 6 parafusos de chifre vêm com os servomotores.

<a id="electronics"></a>
## Eletrônica

| Item | Qtd. | Observações | Comprar nos EUA | Preço unitário (EUA) | Comprar nos EUA | Preço unitário (EUA) | Comprar na UE | Preço unitário (UE) | Total (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Waveshare Bus Servo Adapter | 2 | Controlador de servos | [Amazon](https://www.amazon.com/Waveshare-Integrates-Control-Applicable-Integrate/dp/B0CJ6TP3TP/) | $13.00 | [Aliexpress](https://www.aliexpress.us/item/3256810343532716.html) | $7.40 | [Amazon EU](https://www.amazon.fr/-/en/Serial-Integrates-Control-Circuit-Support/dp/B0CJBKQ8LJ/) | €11.90 | $14.80 |
| Fonte de alimentação 12V DC (12V 5A fonte de alimentação 5.5 2.1mm) | 1 | Braço de robô seguidor. 60W - Sim, sim. 5A ou mais recomendado. O braço do robô atingiu o pico em 3.3A sob uma 300g Combine o conector do Adapter (5.5x2.1mm). | [Amazon](https://www.amazon.com/Power-Supply-Adapter-5-5x2-1-2-5mm/dp/B0C3CJF313/) | $10.00 | [Aliexpress](https://www.aliexpress.us/item/3256812113231032.html) | $6.60 | [Amazon EU](https://www.amazon.fr/-/en/zstg-Universal-Power-Supply-Connector/dp/B0GTLSRM91/) | €12.00 | $6.60 |
| Fonte de alimentação 5V DC (5V 2A fonte de alimentação 5.5 2.1mm) | 1 | Braço de robô líder. Combine o conector do adaptador (5.5x2.1mm). | [Amazon](https://www.amazon.com/MTDZKJG-Adapter-100V-240V-Transformer-Security/dp/B0BZP65GRW/) | $6.20 | [Aliexpress](https://www.aliexpress.us/item/3256812479558626.html) | $4.10 | [Amazon EU](https://www.amazon.fr/5V-2A-Supply-DC-Adapter/dp/B0GDXFRYJS/) | €11.00 | $4.10 |
| Cabo de USB-C, 1.5 m (cabo de dados USB A para USB C 1.5m) | 2 | Escolha um cabo de dados, não um cabo apenas para carregamento. | [Amazon](https://www.amazon.com/Data-Cable-1-5ft-10Gbps-Transfer/dp/B0FMJTHRCM/) | $6.00 | [Aliexpress](https://www.aliexpress.us/item/3256812299430938.html) | $3.00 | [Amazon EU](https://www.amazon.fr/-/en/10Gbps-Transfer-Charging-Samsung-External/dp/B0DHZ1R8FQ/) | €7.00 | $6.00 |
| Câmera USB (OV2735, Módulo de câmera USB 1080P, 2MP 1920x1080, câmera UVC, lente 2.8 ou 3.0 mm) | 1 | Câmera de pulso na pinça do braço do robô seguidor. O protótipo usou um módulo OV2735. Verifique as dimensões do módulo e os orifícios de montagem contra o suporte da câmera. | [Amazon](https://www.amazon.com/innomaker-Computer-Raspberry-Support-Windows/dp/B0CNCSFQC1/) | $19.00 | [Aliexpress](https://www.aliexpress.us/item/3256804452094739.html) | $26.10 | [Amazon EU](https://www.amazon.fr/InnoMaker-Raspberry-Compatible-Windows-Android/dp/B0CNCSFQC1/) | €21.00 | $19.00 |
| **Total** |  |  |  |  |  |  |  |  | **$50.50** |

<a id="mechanical-parts"></a>
## Peças mecânicas

| Item | Dimensões | Qtd. | Localização | Comprar nos EUA | Preço unitário (EUA) | Comprar nos EUA | Preço unitário (EUA) | Comprar na UE | Preço unitário (UE) | Total (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rolamento de esferas 6812 | 60 × 78 × 10 mm | 2 | Rotação da base, uma por braço do robô | [Amazon](https://www.amazon.com/Othmro-6812-2RS-60x78x10mm-Accuracy-Bearing/dp/B081W9QL2Z/) | $5.90 | [Aliexpress](https://www.aliexpress.us/item/3256812369319030.html) | $39.60 / 2 | [Amazon EU](https://www.amazon.fr/-/en/XYWHPGV-6812-2RS-Groove-Bearings-Chrome/dp/B0CQLT6J6D/) | €7.40 / 2 | $11.80 |
| Rolamento flangeado MF106ZZ | 6 × 10 × 3 mm | 2 | Estrutura principal da garra | [Amazon](https://www.amazon.com/METERXITY-Shielded-Bearings-Wheelbarrow-Machines/dp/B0F4QXJSRQ/) | $6.60 / 4 | [Aliexpress](https://www.aliexpress.us/item/3256807821523719.html) | $6.00 / 10 | [Amazon EU](https://www.amazon.fr/-/en/PRECISCRY-DE-SGQ-FLZC-11-MF128ZZ-8x12x3-5-5Pcs/dp/B0GQK9BGWK/) | €11.60 / 5 | $1.20 |
| Haste (Haste redonda de aço inoxidável, 6mm diâmetro, comprimento 125mm) | Ø 6 × 125 mm, carbono ou aço | 2 | Guias da garra | [Amazon](https://www.amazon.com/SKYPRO-Stainless-Diameter-Industry-Working/dp/B0CLCSWSJ9?th=1) | $11.90 / 5 | [Aliexpress](https://www.aliexpress.us/item/3256805290944526.html) | $2.80 | [Amazon EU](https://www.amazon.fr/-/en/SKYPRO-Stainless-Diameter-Industry-Metalworking/dp/B0CLCSWSJ9/) | €14.40 / 5 | $4.76 |
| Tubo guia de alumínio, alternativa | Ø6 × 4 × 125 mm; cortar 1 × 300 mm em 2 × 125 mm; remover rebarbas | 2 | Alternativa às hastes de guia de aço do prendedor | [Amazon](https://www.amazon.com/dp/B0DRG94GJB/) | $9.99 / 3 un. | [Aliexpress](https://www.aliexpress.us/item/3256804988048256.html) | $4.05 / 1 un. | [Amazon EU](https://www.amazon.de/dp/B0D266J2NF/) | €14.89 / 3 un. | $3.33 (alternativa) |
| Tubo de carbono (Tubo de carbono, 6mm x 4mm x 125mm), alternativa | Ø6 × 4 × 125 mm | 2 | Alternativa às hastes de guia de aço do prendedor | [Amazon](https://www.amazon.com/MECCANIXITY-Carbon-Pultruded-Airplane-Quadcopter/dp/B0CZDCW2NL/) | $5.60 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256812851232051.html) | $5.90 / 2 | [Amazon EU](https://www.amazon.fr/-/en/QUARKZMAN-Carbon-Fiber-Tubes-Aircraft/dp/B0CZQVN7JB/) | €8.10 / 2 | $5.60 (alternativa) |
| Grampo tipo C | 3 polegadas, abertura 0–75 mm | 4 | Dois por braço de robô, para fixar a base à mesa | [Amazon](https://www.amazon.com/Inch-Clamp-Woodworking-Precision-Carpentry/dp/B0FLHZVM7G/) | $10.00 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256813098676278.html) | $9.70 | [Amazon EU](https://www.amazon.fr/Performance-75mm-Adjustable-Stainless-Metalworking/dp/B0GSQL9BCN/) | €17.40 / 2 | $20.00 |
| **Total** |  |  |  |  |  |  |  |  |  | **$37.76** |

<a id="fasteners"></a>
## Fixadores

Kit totais como embalado no livreto de montagem.

Use um trava-roscas removível compatível com o plástico impresso, como [Vibra-Tite VC-3](https://www.vibra-tite.com/faq/if-vc-3-has-mek-how-can-it-be-plastic-compatible/). Aplique VC-3 na rosca do parafuso metálico e deixe secar completamente antes da montagem (pelo menos 30 minutos conforme a [ficha técnica](https://www.vibra-tite.com/wp-content/uploads/213_tds.pdf)); não aplique o produto úmido no plástico. Teste primeiro a compatibilidade com seu filamento em uma peça de teste.

| Fixador | Norma | Qtd. | Comprar nos EUA | Preço unitário (EUA) | Comprar nos EUA | Preço unitário (EUA) | Comprar na UE | Preço unitário (UE) | Total (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M2 × 6 cabeça cilíndrica | DIN 912 | 28 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY8XHB1/) | $6.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZP1XT/) | €6.60 / 60 | $1.04 |
| M2 × 8 cabeça cilíndrica | DIN 912 | 12 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY7L8YJ/) | $6.60 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZKVDN/) | €7.00 / 60 | $0.49 |
| M3 × 10 cabeça escareada | DIN 7991 | 64 | [Amazon](https://www.amazon.com/M3-0-5-Socket-Screws-Alloy-Threaded/dp/B08HNF3J3D/) | $9.00 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY12R93P/) | €8.00 / 60 | $4.59 |
| M3 × 16 cabeça escareada | DIN 7991 | 36 | [Amazon](https://www.amazon.com/Skweawert-40-Pcs-M3x16mm-countersunk/dp/B0D7MY32JZ/) | $6.20 / 40 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY138MGY/) | €8.00 / 60 | $2.95 |
| M3 × 4 parafuso sem cabeça | DIN 913 | 4 | [Amazon](https://www.amazon.com/Generic-Bathroom-Fixtures-Furniture-Project/dp/B0H8DPZJPQ/) | $4.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256805653005840.html) | $2.10 / 10 | [Amazon EU](https://www.amazon.fr/-/en/MIETONG-Hex-Socket-Grub-Screws/dp/B0FSKLJR93/) | €6.00 / 20 | $0.31 |
| Porca sextavada M2 | DIN 934 | 12 | [Amazon](https://www.amazon.com/1-10Pcs-M1-M20-Stainless-Steel-Loose/dp/B0GVMQ3VD5/) | $3.50 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC5QKH9/) | €6.00 / 20 | $0.42 |
| Porca sextavada M3 | DIN 934 | 36 | [Amazon](https://www.amazon.com/FOCMKEAS-Stainless-Hexagon-Fasteners-Hardware/dp/B0CR7WL4D6/) | $3.70 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.00 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC7PD4Q/) | €6.30 / 50 | $1.44 |
| M3 × 6 Parafuso de cabeça Phillips | Do kit do servo | 16 | Incluído com os servos. | — | — | — | — | — | — |
| Parafuso auto-roscante 2 × 6 | Do kit do servo | 20 | Incluído com os servos. | — | — | — | — | — | — |
| **Total** |  |  |  |  |  |  |  |  | **$11.24** |

Os fixadores pretos combinam com a aparência dos renders, mas não são necessários.

<a id="printing-materials"></a>
## Materiais de impressão

| Material | Uso | Link de compra | Preço / orçamento (USD) | Total (USD) |
|---|---|---|---|---:|
| Fiberon PET-CF17 | Elos do braço e suportes de servos | [Polymaker](https://shop.polymaker.com/products/fiberon-pet-cf17) | $44.99 / 1 kg | $18.00 (0.4 kg) |
| PETG ou PET-CF | Braçadeiras de garra, tampas, punho e gatilho do braço robótico líder | [Amazon](https://www.amazon.com/Bambu-Printer-Filament-1-75mm-Spool/dp/B0GS568LQ1/) | PETG: $21.00 / 1 kg | $15.75 (0.75 kg) |
| **Total** |  |  |  | **$33.75** |

Use o [guia de impressão](printing.md) e corte novamente usando o slicer de impressão 3D os 3MF projetos fornecidos para determinar a quantidade de filamento para sua impressora e configurações.

<a id="tools"></a>
## Ferramentas

Permita cerca de **$10.00** para uma pequena chave hexagonal e um conjunto de chaves de fenda, se você ainda não possui essas ferramentas.

- Chave hexagonal 1.5 mm para M2 parafusos: [Amazon search](https://www.amazon.com/s?k=1.5mm+hex+key)
- Chave hexagonal 2 mm para M3 parafusos: [Amazon search](https://www.amazon.com/s?k=2mm+hex+key)
- Chave de fenda Phillips PH1 para parafusos de chifre servomotor: [Amazon search](https://www.amazon.com/s?k=PH1+Phillips+screwdriver)
<!-- /translated-content -->
