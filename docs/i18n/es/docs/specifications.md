<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](specifications.md) · [Français](../../fr/docs/specifications.md) · [Deutsch](../../de/docs/specifications.md) · [Português (Brasil)](../../pt-BR/docs/specifications.md) · [简体中文](../../zh-CN/docs/specifications.md) · [日本語](../../ja/docs/specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[Original en inglés](../../../specifications.md)

[Documentación](../README.md) · [Impresión](printing.md) · [Materiales](bom.md) · [Montaje](assembly-guide.md) · [Especificaciones](specifications.md) · [Modelos](../models/README.md) · [Contribuir](../CONTRIBUTING.md) · [Licencias](../LICENSING.md) · [Traducciones](translations.md)

> Traducción completa del documento. Las ilustraciones y el manual PDF original se comparten entre idiomas. Traducción realizada con ayuda de IA; aún no revisada por hablantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="specifications-and-test-results"></a>
# Especificaciones y resultados de pruebas

Medido en Robonine prototipos en agosto y septiembre 2026.Los números marcados con *calculados* provienen de las hojas de datos del modelo URDF y el servomotor, no de una medición.

<a id="geometry"></a>
## Geometría

| Articulación | Rango |
|---|---|
| Giro de la base | −176° … +176° (352°) |
| Elevación del hombro | −43° … +181° (224°) |
| Flexión del codo | −166° … +77° (243°) |
| Flexión de la muñeca | −85° … +111° (196°) |
| Rotación de la muñeca | −165° … +163° (328°) |
| Pinza | 0 … 85 mm |

| Eslabón | Entre ejes |
|---|---|
| Rotación de la base al hombro | 85 mm |
| De hombro a codo | 119 mm |
| Flexión del codo a la muñeca | 139 mm |
| Flexión de la muñeca para rodar la muñeca | 62 mm |
| Rollo de la muñeca a la punta del agarrador | 132 mm |

| Alcance, centro de la punta de la pinza |  |
|---|---|
| Radio horizontal | 483 mm |
| Altura sobre el fondo de la base | Hasta 544 mm |
| Debajo de la parte inferior de la base, el brazo del robot sobre un borde de mesa | Hasta −301 mm |

El alcance se calculó a partir de 100,000 posturas aleatorias dentro de los límites de la articulación, sin autocolisiones.

<a id="servos"></a>
## Servos

| Articulación | Brazo seguidor | Brazo líder |
|---|---|---|
| 1 Rotación de la base | STS3235 | STS3215 |
| 2 Lifting de hombros | STS3250 | STS3215 |
| 3 Flexión del codo | STS3250 | STS3215 |
| 4 Flexión de la muñeca | STS3235 | STS3215 |
| 5 Rollo de muñeca | ST-3215-C049, 1:191 | STS3215 |
| 6 Pinza / gatillo | ST-3215-C049, 1:191 | STS3215 |
| Alimentación | 12 V | 5 V |

<a id="gripper"></a>
## Pinza

| | |
|---|---|
| Tipo | Paralelo, cremallera y piñón, dos mordazas móviles |
| Apertura | 85 mm |
| Caja, anchura máxima recomendada | Acerca de 75 mm |
| Cilindro, diámetro máximo recomendado | Acerca de 70 mm |
| Esfera, diámetro máximo recomendado | Acerca de 60 mm |
| Cámara | Cámara USB montada en la pinza |

<a id="measured-results-against-so-arm-101"></a>
## Resultados medidos contra SO-ARM 101

| Métrica | SO-ARM 101 | SO-ARM 102 | Cambio |
|---|---|---|---|
| Desviación en la punta de la pinza, 300 g, brazo del robot completamente extendido ¹ | 7.5 mm | 3.4 mm | −55 % |
| Igual, todos los enlaces en 100 % de relleno ¹ | — | 2.34 mm | −69 % |
| Radio horizontal | 441 mm | 483 mm | +9.5 % |
| Alcance detrás de la base | 377 mm | 473 mm | +25.5 % |
| Rango de giro de la base | 220° | 352° | +60 % |
| Rango del codo | 194° | 243° | +25 % |
| Velocidad sin carga del hombro y el codo, *calculada* | 270 °/s | 450 °/s | +67 % |
| Holgura de la base | 8.75 cuentas | 5.00 cuentas | −43 % |
| Error de punta horizontal desde la holgura base, *calculado* | ±2.96 mm | ±1.85 mm | −37.5 % |
| Repetibilidad | — | Acerca de 0.1 mm |  |
| Ruido a 1 m | 70 dB | 60 dB | −10 dB |
| Carga útil nominal | 150 g | 300 g |  |

¹ Ambos brazos robóticos se construyeron con maniquíes de servomotores impresos en las juntas 2, 3 y 4, por lo que solo se compara el marco. SO-ARM 101 impreso en PLA, SO-ARM 102 en Fiberon PET-CF17 al 25 % de relleno. Una segunda ejecución de la misma prueba SO-ARM 102 dio 3.9 mm.

| SO-ARM 101 | SO-ARM 102 |
|:-:|:-:|
| ![SO-ARM 101 prueba de rigidez](../../../../assets/images/tests/stiffness-so-arm-101.jpg) | ![SO-ARM 102 prueba de rigidez](../../../../assets/images/tests/stiffness-so-arm-102.jpg) |

<a id="current-and-temperature-follower"></a>
## Corriente y temperatura, brazo robot seguidor

Medido con una carga 300 g en una trayectoria repetida, ambiente 30 °C, seis servomotores STS3250.

| | |
|---|---|
| Corriente media | 1.26 A |
| Corriente máxima | 3.28 A |
| Temperatura máxima del servo | 46 °C |

<a id="absolute-accuracy"></a>
## Precisión absoluta

Todavía se está ajustando. Con la configuración PID de fábrica de los servos, la punta descendía unos 50 mm bajo el peso del propio brazo al extenderlo por completo. Tras ajustar el PID, este descenso se redujo a unos 5 mm. Se está preparando un perfil específico de precisión.
<!-- /translated-content -->
