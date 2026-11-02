<!-- translation-navigation -->
[English](../../en/docs/bom.md) · [Русский](../../ru/docs/bom.md) · [Español](bom.md) · [Français](../../fr/docs/bom.md) · [Deutsch](../../de/docs/bom.md) · [Português (Brasil)](../../pt-BR/docs/bom.md) · [简体中文](../../zh-CN/docs/bom.md) · [日本語](../../ja/docs/bom.md) · [हिन्दी](../../hi/docs/bom.md) · [العربية](../../ar/docs/bom.md)

[Original en inglés](../../../bom.md)

[Documentación](../README.md) · [Impresión](printing.md) · [Materiales](bom.md) · [Montaje](assembly-guide.md) · [Especificaciones](specifications.md) · [Modelos](../models/README.md) · [Contribuir](../CONTRIBUTING.md) · [Licencias](../LICENSING.md) · [Traducciones](translations.md)

> Traducción completa del documento. Las ilustraciones y el manual PDF original se comparten entre idiomas. Traducción realizada con ayuda de IA; aún no revisada por hablantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="bill-of-materials"></a>
# Lista de materiales

Las cantidades son para un kit completo: un brazo robot seguidor y un brazo robot líder.Las piezas impresas se enumeran por separado en [printing.md](printing.md).

<a id="estimated-kit-cost"></a>
## Costo estimado del equipo

**Un brazo robot líder + un brazo robot seguidor: $340 en componentes, o $374 incluyendo material de impresión.**

| Categoría | Costo de las cantidades utilizadas (USD) | Comprar paquetes completos / carretes (USD) |
|---|---:|---:|
| Acerca de nosotros (12 pcs) | $240.72 | $240.72 |
| Electrónica, cámara y fuentes de alimentación | $50.50 | $50.50 |
| Rodamientos, barras guía de acero y abrazaderas de mesa | $37.76 | $49.70 |
| Elementos de fijación | $11.24 | $28.60 |
| **Subtotal de componentes** | **$340.22** | **$368.82** |
| Material de impresión: 0.4 kg PET-CF17 + 0.75 kg PETG | $33.75 | $66.0 |
| **Total con material de impresión** | **$373.97** | **$434.82** |

La columna **Total (USD)** es el coste de la cantidad necesaria para un kit, utilizando la oferta de referencia detrás del total de cada línea existente (no la suma de las ofertas de los proveedores). Los tornillos incluidos cuestan $0; los tubos de carbono alternativos se excluyen de los totales. Las estimaciones utilizan los precios de referencia que aparecen a continuación, con cada línea redondeada al céntimo. No son nuevas cotizaciones de proveedores: confirme las variantes seleccionadas, cantidades mínimas de pedido y precios antes de realizar el pedido. Se excluyen envío, impuestos, herramientas, ordenador, impresora, electricidad y mano de obra de montaje.

El paquete completo de columna incluye piezas de repuesto no utilizadas, 0.5 kg carrete PET-CF17 y 1 kg PETG carrete. Las cantidades de impresión son asignaciones presupuestarias; corte nuevamente utilizando el cortador de impresión 3D los 3MF proyectos suministrados para su configuración. Los costos de la varilla utilizan acero; los tubos de carbono son una alternativa.

![Kit hardware](../../../../assets/images/assembly/hardware.jpg)

<a id="servos"></a>
## Servos

| Articulación | ID | Brazo seguidor | Brazo líder |
|---|:-:|---|---|
| Giro de la base | 1 | ST-3235-С001 | ST-3215-C066, 1:191 |
| Elevación del hombro | 2 | ST-3250-С002 | ST-3215-C066, 1:191 |
| Flexión del codo | 3 | ST-3250-С002 | ST-3215-C066, 1:191 |
| Flexión de la muñeca | 4 | ST-3235-С001 | ST-3215-C066, 1:191 |
| Rotación de la muñeca | 5 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |
| Pinza / gatillo | 6 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |

Totales: 6 × STS3215 7.4V, 2 × STS3215 12V, 2 × STS3235 12V, 2 × STS3250 12V. Todos son servomotores de bus serie Feetech TTL.

| Servo | Cant. | Selección | Aliexpress enlace | Precio unitario (USD) | Alibaba enlace | Precio unitario (USD) | Total (USD) |
|---|---|---|---|---|---|---|---|
| STS3215 | 6 | 7.4V TTL versión para servomotores de brazo robot líder. Seleccione ST-3215-C066 (7.4V). | [Aliexpress](https://www.aliexpress.us/item/3256811860804361.html) | $32.8 | [Alibaba](https://www.alibaba.com/product-detail/Feetech-SO-ARM101-LeRobot-Open-Source_1601636174153.html) | $6.74 | $40.44 |
| STS3215 | 2 | Versión 12V TTL para articulaciones de brazo robot seguidor 5 y 6. Seleccione ST-3215-C049 (12V30KG). | [Aliexpress](https://www.aliexpress.us/item/3256811832699316.html) | $55.8 para 2pcs | [Alibaba](https://www.alibaba.com/product-detail/6pcs-12V-30KG-1-345-STS3215_1601900233170.html) | $14.70 | $29.40 |
| STS3235 | 2 | Versión 12V TTL para las articulaciones del brazo robot seguidor 1 y 4. | [Aliexpress](https://www.aliexpress.us/item/3256810213842277.html) | $63 | [Alibaba](https://www.alibaba.com/product-detail/FEETECH-STS3235-12V-30KG-TTL-Dual_1601910640629.html) | $40.79 | $81.58 |
| STS3250 | 2 | Versión 12V TTL para las articulaciones del brazo robot seguidor 2 y 3. | [Aliexpress](https://www.aliexpress.us/item/3256811995148799.html) | $126.4 para 2pcs | [Alibaba](https://www.alibaba.com/product-detail/Feetech-STS3250-12V-50kg-Servo-High_1601711893549.html) | $44.65 | $89.30 |
| **Total** |  |  |  |  |  |  | **$240.72** |

- **Brazo robot seguidor, 12V.** STS3250 es un servomotor sin escobillas de 50 kg·cm en 75 RPM que impulsa las dos articulaciones que soportan la mayor carga. STS3235 es un servomotor de 30 kg·cm con menor holgura que el STS3215.
- **Brazo de robot líder, 5V.**Los servomotores del brazo de robot líder solo se leen, nunca se cargan Puede usar un pasivo ST-3215-C066 sin motor y caja de engranajes**solo** para el brazo de robot líder.
- Los servocuernos y los tornillos de cuerno M3 × 6 vienen con los servomotores.

<a id="electronics"></a>
## Electrónica

| Artículo | Cant. | Notas | Comprar en EE. UU. | Precio unitario (EE. UU.) | Comprar en EE. UU. | Precio unitario (EE. UU.) | Comprar en la UE | Precio unitario (UE) | Total (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Waveshare Bus Servo Adapter | 2 | Controlador de servos | [Amazon](https://www.amazon.com/Waveshare-Integrates-Control-Applicable-Integrate/dp/B0CJ6TP3TP/) | $13.00 | [Aliexpress](https://www.aliexpress.us/item/3256810343532716.html) | $7.40 | [Amazon EU](https://www.amazon.fr/-/en/Serial-Integrates-Control-Circuit-Support/dp/B0CJBKQ8LJ/) | €11.90 | $14.80 |
| Fuente de alimentación 12V DC (12V 5A fuente de alimentación 5.5 2.1mm) | 1 | Brazo robot seguidor. Recomendado 60W / 5A o más. El brazo robot alcanzó su pico en 3.3A bajo una carga de 300g. Coincide con el conector del Adapter (5.5x2.1mm). | [Amazon](https://www.amazon.com/Power-Supply-Adapter-5-5x2-1-2-5mm/dp/B0C3CJF313/) | $10.00 | [Aliexpress](https://www.aliexpress.us/item/3256812113231032.html) | $6.60 | [Amazon EU](https://www.amazon.fr/-/en/zstg-Universal-Power-Supply-Connector/dp/B0GTLSRM91/) | €12.00 | $6.60 |
| Fuente de alimentación 5V DC (5V 2A fuente de alimentación 5.5 2.1mm) | 1 | Brazo robot líder. Coincide con el conector del adaptador (5.5x2.1mm). | [Amazon](https://www.amazon.com/MTDZKJG-Adapter-100V-240V-Transformer-Security/dp/B0BZP65GRW/) | $6.20 | [Aliexpress](https://www.aliexpress.us/item/3256812479558626.html) | $4.10 | [Amazon EU](https://www.amazon.fr/5V-2A-Supply-DC-Adapter/dp/B0GDXFRYJS/) | €11.00 | $4.10 |
| Cable de USB-C, 1.5 m (cable de datos USB A a USB C 1.5m) | 2 | Elige un cable de datos, no un cable que solo se use para cargar. | [Amazon](https://www.amazon.com/Data-Cable-1-5ft-10Gbps-Transfer/dp/B0FMJTHRCM/) | $6.00 | [Aliexpress](https://www.aliexpress.us/item/3256812299430938.html) | $3.00 | [Amazon EU](https://www.amazon.fr/-/en/10Gbps-Transfer-Charging-Samsung-External/dp/B0DHZ1R8FQ/) | €7.00 | $6.00 |
| Cámara USB (OV2735, 1080P Módulo de cámara USB, 2MP 1920x1080, cámara UVC, 2.8 o 3.0 mm lente) | 1 | Cámara de muñeca en la pinza del brazo robot seguidor. El prototipo utilizó un módulo OV2735 Compruebe las dimensiones del módulo y los orificios de montaje contra el soporte de cámara. | [Amazon](https://www.amazon.com/innomaker-Computer-Raspberry-Support-Windows/dp/B0CNCSFQC1/) | $19.00 | [Aliexpress](https://www.aliexpress.us/item/3256804452094739.html) | $26.10 | [Amazon EU](https://www.amazon.fr/InnoMaker-Raspberry-Compatible-Windows-Android/dp/B0CNCSFQC1/) | €21.00 | $19.00 |
| **Total** |  |  |  |  |  |  |  |  | **$50.50** |

<a id="mechanical-parts"></a>
## Piezas mecánicas

| Artículo | Tamaño | Cant. | Ubicación | Comprar en EE. UU. | Precio unitario (EE. UU.) | Comprar en EE. UU. | Precio unitario (EE. UU.) | Comprar en la UE | Precio unitario (UE) | Total (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rodamiento de bolas 6812 | 60 × 78 × 10 mm | 2 | Rotación de la base, una por brazo del robot | [Amazon](https://www.amazon.com/Othmro-6812-2RS-60x78x10mm-Accuracy-Bearing/dp/B081W9QL2Z/) | $5.90 | [Aliexpress](https://www.aliexpress.us/item/3256812369319030.html) | $39.60 / 2 | [Amazon EU](https://www.amazon.fr/-/en/XYWHPGV-6812-2RS-Groove-Bearings-Chrome/dp/B0CQLT6J6D/) | €7.40 / 2 | $11.80 |
| Cojinete de brida MF106ZZ | 6 × 10 × 3 mm | 2 | Bastidor principal de la pinza | [Amazon](https://www.amazon.com/METERXITY-Shielded-Bearings-Wheelbarrow-Machines/dp/B0F4QXJSRQ/) | $6.60 / 4 | [Aliexpress](https://www.aliexpress.us/item/3256807821523719.html) | $6.00 / 10 | [Amazon EU](https://www.amazon.fr/-/en/PRECISCRY-DE-SGQ-FLZC-11-MF128ZZ-8x12x3-5-5Pcs/dp/B0GQK9BGWK/) | €11.60 / 5 | $1.20 |
| Varilla (Varilla redonda de acero inoxidable, 6mm diámetro, longitud 125mm) | Ø6 × 125 mm, carbono o acero | 2 | Guías de la pinza | [Amazon](https://www.amazon.com/SKYPRO-Stainless-Diameter-Industry-Working/dp/B0CLCSWSJ9?th=1) | $11.90 / 5 | [Aliexpress](https://www.aliexpress.us/item/3256805290944526.html) | $2.80 | [Amazon EU](https://www.amazon.fr/-/en/SKYPRO-Stainless-Diameter-Industry-Metalworking/dp/B0CLCSWSJ9/) | €14.40 / 5 | $4.76 |
| Tubo guía de aluminio, alternativa | Ø6 × 4 × 125 mm; cortar 1 × 300 mm en 2 × 125 mm; desbarbar | 2 | Alternativa a las barras guía de acero | [Amazon](https://www.amazon.com/dp/B0DRG94GJB/) | $9.99 / 3 uds. | [Aliexpress](https://www.aliexpress.us/item/3256804988048256.html) | $4.05 / 1 ud. | [Amazon EU](https://www.amazon.de/dp/B0D266J2NF/) | €14.89 / 3 uds. | $3.33 (alternativa) |
| Tubo de carbono (Tubo de carbono, 6mm x 4mm x 125mm), alternativa | Ø6 × 4 × 125 mm | 2 | Alternativa a las barras guía de acero | [Amazon](https://www.amazon.com/MECCANIXITY-Carbon-Pultruded-Airplane-Quadcopter/dp/B0CZDCW2NL/) | $5.60 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256812851232051.html) | $5.90 / 2 | [Amazon EU](https://www.amazon.fr/-/en/QUARKZMAN-Carbon-Fiber-Tubes-Aircraft/dp/B0CZQVN7JB/) | €8.10 / 2 | $5.60 (alternativa) |
| Abrazadera en C | 3 pulgadas, 0–75 mm apertura | 4 | Dos por brazo robot, para fijar la base a la mesa | [Amazon](https://www.amazon.com/Inch-Clamp-Woodworking-Precision-Carpentry/dp/B0FLHZVM7G/) | $10.00 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256813098676278.html) | $9.70 | [Amazon EU](https://www.amazon.fr/Performance-75mm-Adjustable-Stainless-Metalworking/dp/B0GSQL9BCN/) | €17.40 / 2 | $20.00 |
| **Total** |  |  |  |  |  |  |  |  |  | **$37.76** |

<a id="fasteners"></a>
## Elementos de fijación

Totales del kit como se embala en el folleto de montaje.

Use un fijador de roscas desmontable compatible con el plástico impreso, como [Vibra-Tite VC-3](https://www.vibra-tite.com/faq/if-vc-3-has-mek-how-can-it-be-plastic-compatible/). Aplique VC-3 a la rosca del tornillo metálico y deje secar completamente antes del montaje (al menos 30 minutos según la [ficha técnica](https://www.vibra-tite.com/wp-content/uploads/213_tds.pdf)); no lo aplique húmedo sobre plástico. Compruebe primero la compatibilidad con su filamento en una pieza de prueba.

| Fijación | Norma | Cant. | Comprar en EE. UU. | Precio unitario (EE. UU.) | Comprar en EE. UU. | Precio unitario (EE. UU.) | Comprar en la UE | Precio unitario (UE) | Total (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M2 × 6 de cabeza cilíndrica | DIN 912 | 28 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY8XHB1/) | $6.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZP1XT/) | €6.60 / 60 | $1.04 |
| M2 × 8 de cabeza cilíndrica | DIN 912 | 12 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY7L8YJ/) | $6.60 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZKVDN/) | €7.00 / 60 | $0.49 |
| M3 × 10 avellanado | DIN 7991 | 64 | [Amazon](https://www.amazon.com/M3-0-5-Socket-Screws-Alloy-Threaded/dp/B08HNF3J3D/) | $9.00 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY12R93P/) | €8.00 / 60 | $4.59 |
| M3 × 16 avellanado | DIN 7991 | 36 | [Amazon](https://www.amazon.com/Skweawert-40-Pcs-M3x16mm-countersunk/dp/B0D7MY32JZ/) | $6.20 / 40 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY138MGY/) | €8.00 / 60 | $2.95 |
| M3 × 4 prisionero | DIN 913 | 4 | [Amazon](https://www.amazon.com/Generic-Bathroom-Fixtures-Furniture-Project/dp/B0H8DPZJPQ/) | $4.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256805653005840.html) | $2.10 / 10 | [Amazon EU](https://www.amazon.fr/-/en/MIETONG-Hex-Socket-Grub-Screws/dp/B0FSKLJR93/) | €6.00 / 20 | $0.31 |
| Tuerca hexagonal M2 | DIN 934 | 12 | [Amazon](https://www.amazon.com/1-10Pcs-M1-M20-Stainless-Steel-Loose/dp/B0GVMQ3VD5/) | $3.50 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC5QKH9/) | €6.00 / 20 | $0.42 |
| Tuerca hexagonal M3 | DIN 934 | 36 | [Amazon](https://www.amazon.com/FOCMKEAS-Stainless-Hexagon-Fasteners-Hardware/dp/B0CR7WL4D6/) | $3.70 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.00 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC7PD4Q/) | €6.30 / 50 | $1.44 |
| M3 × 6 Tornillo de cabeza Phillips | Del kit del servo | 16 | Incluido con los servos. | — | — | — | — | — | — |
| Tornillo autorroscante 2 × 6 | Del kit del servo | 20 | Incluido con los servos. | — | — | — | — | — | — |
| **Total** |  |  |  |  |  |  |  |  | **$11.24** |

Los sujetadores negros coinciden con el aspecto de los revocados, pero no son necesarios.

<a id="printing-materials"></a>
## Materiales de impresión

| Material | Uso | Enlace de compra | Precio / presupuesto (USD) | Total (USD) |
|---|---|---|---|---:|
| Fiberon PET-CF17 | Eslabones del brazo y soportes de servos | [Polymaker](https://shop.polymaker.com/products/fiberon-pet-cf17) | $44.99 / 1 kg | $18.00 (0.4 kg) |
| PETG o PET-CF | Abrazaderas de agarre, cubiertas, manija del brazo robot líder y gatillo | [Amazon](https://www.amazon.com/Bambu-Printer-Filament-1-75mm-Spool/dp/B0GS568LQ1/) | PETG: $21.00 / 1 kg | $15.75 (0.75 kg) |
| **Total** |  |  |  | **$33.75** |

Utilice la [guía de impresión](printing.md) y corte nuevamente con el cortador de impresión 3D los 3MF proyectos suministrados para determinar la cantidad de filamento para su impresora y ajustes.

<a id="tools"></a>
## Herramientas

Deja alrededor de **$10.00** para una pequeña llave hexagonal y un juego de destornilladores si no tienes estas herramientas.

- Llave hexagonal 1.5 mm para tornillos M2: [Amazon search](https://www.amazon.com/s?k=1.5mm+hex+key)
- Llave hexagonal 2 mm para tornillos M3: [Amazon search](https://www.amazon.com/s?k=2mm+hex+key)
- Destornillador Phillips PH1 para tornillos de cuerno de servomotor: [Amazon search](https://www.amazon.com/s?k=PH1+Phillips+screwdriver)
<!-- /translated-content -->
