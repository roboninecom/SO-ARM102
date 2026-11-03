<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[Original en inglés](../../../README.md)

[Documentación](README.md) · [Impresión](docs/printing.md) · [Materiales](docs/bom.md) · [Montaje](docs/assembly-guide.md) · [Especificaciones](docs/specifications.md) · [Modelos](models/README.md) · [Contribuir](CONTRIBUTING.md) · [Licencias](LICENSING.md) · [Traducciones](docs/translations.md)

> Traducción completa del documento. Las ilustraciones y el manual PDF original se comparten entre idiomas. Traducción realizada con ayuda de IA; aún no revisada por hablantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102"></a>
# SO-ARM 102

<div align="center">

[![SO-ARM 102](../../../assets/images/photos/so-arm-102-live.jpg)](../../../assets/video/so-arm-102-preview.mp4)

**🎥 [Ver el video de vista previa](../../../assets/video/so-arm-102-preview.mp4)**·**🛒 [Comprar el kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

**SO-ARM 102 es un kit de brazos robóticos líder–seguidor de código abierto para teleoperación y aprendizaje por imitación. Cada brazo tiene cinco grados de libertad y una pinza.**

<p align="left">
Basado en SO-ARM 100 y 101, combina una estructura de PET-CF más rígida con una pinza paralela.
</p>

[![Hardware: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt) [![Software: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt) [![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt) [![GitHub release](https://img.shields.io/github/v/release/roboninecom/SO-ARM-102)](https://github.com/roboninecom/SO-ARM-102/releases/latest)

📩 [hello@robonine.com](mailto:hello@robonine.com)

**Presupuesto de bricolaje: ~$340 para componentes, o ~$374 incluyendo material de impresión.** [Resumen del BOM](#bill-of-materials) · [Costos detallados y enlaces de compra](docs/bom.md#estimated-kit-cost)

> ¿Prefieres no obtener las piezas e imprimirlas tú mismo? **[Compra el kit SO-ARM 102](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

</div>

---

<a id="-what-changed-against-so-arm-101"></a>
## ✨ Lo que cambió contra SO-ARM 101

|  | SO-ARM 101 | SO-ARM 102 |
|---|---|---|
| Pinza | Mordaza angular | Pinza paralela, 85 mm span |
| Material de la estructura | PLA | PET-CF (Fiberon PET-CF17 probado) |
| Estructura | Eslabones macizos | Eslabones optimizados topológicamente |
| Rango de giro de la base | 220° | **352°** |
| Alcance horizontal | 441 mm | **483 mm** |
| Desviación en la pinza, carga 300 g ¹ | 7.5 mm | **3.4–3.9 mm** |
| Velocidad de hombro y codo | 45 RPM (STS3215) | **75 RPM (STS3250)** |
| Ruido a 1 m | 70 dB | **60 dB** |

¹ Ambos brazos robóticos se construyeron con maniquíes de servomotores impresos, por lo que se compara el bastidor, no los motores.Los resultados completos y las condiciones de prueba están en [docs/specifications.md](docs/specifications.md).

---

<a id="-preview"></a>
## 🎥 Vista previa

<div align="center">

[![SO-ARM 102 preview](../../../assets/video/so-arm-102-preview.gif)](../../../assets/video/so-arm-102-preview.mp4)

*Haz clic para ver el vídeo completo, 21 s*

</div>

---

<a id="-configurations"></a>
## 🤝 Configuraciones

<a id="single-arm-one-leader--one-follower"></a>
### Brazo de un solo robot: un brazo robot líder + un brazo robot seguidor

El kit estándar. Mueva el brazo robot líder a mano, y el brazo robot seguidor repite el movimiento.Úselo para teleoperación y para grabar demostraciones para aprendizaje por imitación.

![Un brazo líder y un brazo seguidor](../../../assets/images/renders/config-single-arm.jpg)

<a id="bimanual-two-leaders--two-followers"></a>
### Bimanual: dos líderes + dos seguidores

Cada mano controla su propio brazo robot líder, por lo que los seguidores pueden pasar objetos, sujetar y trabajar en una pieza o hacer cualquier tarea que requiera dos manos.

![Dos brazos líderes y dos brazos seguidores](../../../assets/images/renders/config-dual-arm.jpg)

<a id="the-two-arms"></a>
### Los dos brazos robóticos

| Brazo seguidor | Brazo líder |
|:-:|:-:|
| ![Brazo seguidor](../../../assets/images/renders/follower.jpg) | ![Brazo líder](../../../assets/images/renders/leader.jpg) |
| Pinza paralela, cámara de muñeca, 12 V | Mango con gatillo, 5 V |

---

<a id="-build-it-in-four-steps"></a>
## 🚀 Construye en cuatro pasos

¿Prefieres un kit listo? **[Compra el SO-ARM 102 kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

<a id="1-print-the-parts"></a>
### 1. Imprimir las piezas

Las piezas individuales se ajustan a una placa de construcción de impresora 3D 180 × 180 mm. La parte más grande tiene 160 mm largo. Los diseños de placa 3MF suministrados utilizan una placa de construcción de impresora 3D 256 × 256 mm.

- 3MF proyectos slicer con configuraciones de orientación y soporte guardadas: [`models/3mf/`](../../../models/3mf) — [brazo robot líder](../../../models/3mf/SO102_leader.3mf), [brazo robot seguidor](../../../models/3mf/SO102_follower_arms.3mf), [Pinza y base del seguidor](../../../models/3mf/SO102_follower_gripper_base.3mf)
- Contenido del proyecto y perfiles de impresora: [models/README.md](models/README.md)
- STL archivos, listos para cortar: [`models/stl/`](../../../models/stl)
- STEP sources: [`models/step/`](../../../models/step)
- Material, ajustes y cantidades de piezas: [docs/printing.md](docs/printing.md)


<a id="2-buy-the-hardware"></a>
### 2. Comprar el hardware

Obtenga los componentes del [resumen de la lista de materiales](#bill-of-materials) y [lista completa con enlaces de compra](docs/bom.md). Presupuesto **$340.22**para componentes, o**$373.97** incluyendo material de impresión, antes del envío e impuestos.

| Brazo | Servos | Controlador | Alimentación |
|---|---|---|---|
| Brazo seguidor | 2 × STS3235, 2 × STS3250, 2 × STS3215 | Waveshare Bus Servo Adapter | **12 V** |
| Brazo líder | 6 × STS3215 | Waveshare Bus Servo Adapter | **5 V** |

> ⚠️ **El brazo líder funciona a 5 V y el brazo seguidor a 12 V.** No intercambie las fuentes de alimentación.

<a id="3-assemble"></a>
### 3. Ensamblar

- Folleto imprimible, 32 páginas A5: [docs/SO-ARM102_assembly_A5_v0.7.pdf](../../SO-ARM102_assembly_A5_v0.7.pdf)
- Lista de pasos con piezas y sujetadores: [docs/assembly-guide.md](docs/assembly-guide.md)

Herramientas: llaves hexagonales 1.5 mm (M2 tornillos) y 2 mm (M3 tornillos).

<a id="4-set-up-the-software"></a>
### 4. Configurar el software

Servo IDs, calibración y lecciones: **[lab.robonine.com](https://lab.robonine.com)**.
Utilice el plugin del seguidor SO-ARM 102 con el tipo estándar `so101_leader`.
**[Instalación y configuración de LeRobot](docs/lerobot.md)**.

---

<a id="bill-of-materials"></a>
## Lista de materiales

Cantidades y costos de referencia para **un brazo robot líder + un brazo robot seguidor**:

| Categoría / enlaces de compra | Contenido del kit | Total (USD) |
|---|---|---:|
| [Servos](docs/bom.md#servos) | 6 × STS3215 7.4 V, 2 × STS3215 12 V, 2 × STS3235, 2 × STS3250 | $240.72 |
| [Electrónica](docs/bom.md#electronics) | 2 controladores, 2 fuentes de alimentación, 2 cables USB, 1 cámara de muñeca | $50.50 |
| [Piezas mecánicas](docs/bom.md#mechanical-parts) | 4 rodamientos, 2 barras guía de acero, 4 abrazaderas de mesa | $37.76 |
| [Elementos de fijación](docs/bom.md#fasteners) | Tornillos y tuercas; tornillos especificados del juego del servomotor incluidos | $11.24 |
| **Subtotal de componentes** |  | **$340.22** |
| [Material de impresión](docs/bom.md#printing-materials) | 0.4 kg PET-CF17 + 0.75 kg PETG asignación | $33.75 |
| **Total con material de impresión** |  | **$373.97** |

Comprar el ejemplo de paquetes completos y carretes de filamentos desde cero cuesta alrededor de **$435**, incluyendo repuestos no utilizados. Estas son estimaciones de referencia, no nuevas cotizaciones de proveedores. El envío, los impuestos, las herramientas, una computadora, una impresora, la electricidad y el trabajo de montaje están excluidos. Confirme los precios del proveedor, las variantes y las cantidades mínimas de pedido antes de realizar el pedido; corte nuevamente con el cortador de impresión 3D los 3MF proyectos para verificar el consumo de filamento.

[BOM completo, enlaces de compra y supuestos de costo](docs/bom.md#estimated-kit-cost).

---

<a id="urdf-export"></a>
## URDF exportación

La exportación independiente actual está en [`simulation/urdf/`](../../../simulation/urdf): [URDF](../../../simulation/urdf/so_arm_102.urdf) · [Xacro](../../../simulation/urdf/so_arm_102.xacro). Mantenga `meshes/` junto a los archivos de descripción; las rutas de malla son relativas a esta carpeta.

- **Visuales:**STL mallas.**Colisiones:** cajas rotativas independientes en los ocho enlaces.
- **Estimación de masa:**PLA, 30% de relleno, 6 perímetros, 6 capas superior/inferior, 0.2 mm altura de capa y**0.40 mm ancho de extrusión** Estos son supuestos de simulación; utilice [la guía de impresión](docs/printing.md) para los ajustes de fabricación.
- **Masas de hardware:**seis motores a 70 g cada uno; cojinete base a 105 g. Masa total estimada del modelo:**0.889 kg**.
- **Gripper:** `clamp2` imita `clamp1` con multiplicador `-1`.

[Configuración de exportación](../../../simulation/urdf/export_settings.json) y [Propiedades de masa](../../../simulation/urdf/mass_properties.json) registran los supuestos.La geometría y las comprobaciones de inercia se registran en [export_verification.json](../../../simulation/urdf/export_verification.json).

---

<a id="-repository-structure"></a>
## 📁 Estructura del repositorio

```
├── models/
│   ├── 3mf/                 # Proyectos de la rebanadora: brazo robot líder, brazo robot seguidor, pinza y caja del tablero
│   ├── stl/                 # Mallas listas para imprimir
│   │   ├── common/          # Piezas comunes, incluidas las cajas de los controladores
│   │   ├── follower/        # Pinza paralela y soporte de cámara
│   │   └── leader/          # Mango, gatillo y giro de muñeca
│   └── step/                # CAD fuentes, mismo diseño que stl/
├── docs/
│   ├── printing.md          # Material, ajustes de la rebanadora, cantidades
│   ├── bom.md               # Lista de materiales
│   ├── assembly-guide.md    # Lista de pasos con piezas y sujetadores
│   ├── specifications.md    # Geometría, servomotores, resultados medidos vs SO-ARM 101
│   └── SO-ARM102_assembly_A5_v0.7.pdf
├── assets/
│   ├── images/              # Fotos, renders, páginas de folletos, fotos de prueba
│   └── video/               # Vista previa de vídeo y GIF
├── LICENSING.md             # Qué licencia cubre qué archivo
└── NOTICE                   # Atribución a terceros
```

---

<a id="-known-issues"></a>
## Problemas conocidos

Notas de montaje de pruebas independientes; revíselas al montar.

1. **Use el folleto v0.7.** Los anteriores muestran el controlador HAT y piezas antiguas de la pinza. La v0.7 instala un Bus Servo Adapter en ambos brazos.
2. **M2 tornillos son difíciles de alcanzar en varios lugares.** Espere luchar contra algunos de ellos.
3. **Las abrazaderas de la pinza funcionan bien en varillas de carbono.** Los orificios de las abrazaderas tienen un tamaño para 6.1 mm.Los diámetros de las varillas varían entre los proveedores, así que compruebe el ajuste antes del montaje.
4. **Compruebe las longitudes de cable del servomotor** antes de cerrar cada junta, especialmente desde la base hasta el hombro.
5. **El orden de montaje es incómodo en dos lugares** del folleto.Lea dos pasos antes de fijar.
6. **Las juntas de los brazos del robot líder pueden sentirse sueltas.** Al agregar 8 × 2 mm juntas tóricas de goma entre cada servomotor y su bocina, el brazo del robot líder obtiene una fricción suave y silenciosa. Utilice dos por servomotor en las juntas 1–4 y una en las juntas 5–6.

Por favor, [abre un problema](https://github.com/roboninecom/SO-ARM-102/issues).

---

<a id="-star-history"></a>
## ⭐ Historial de estrellas

[![Historial de estrellas — SO-ARM 102](https://api.star-history.com/svg?repos=roboninecom/so-arm-102&type=date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm-102&type=date&legend=top-left)

---

<a id="-related-projects"></a>
## Proyectos relacionados

- [SO-ARM100/101 Pinza paralela](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper), la pinza de la que creció la SO-ARM 102 pinza
- [SO-ARM101](https://github.com/TheRobotStudio/SO-ARM100) por TheRobotStudio, el brazo robótico este diseño tiene éxito
- [Comparación práctica de servomotores inteligentes en serie](https://robonine.com/smart-serial-servo-motor-comparison-robotics/), las pruebas detrás de la elección del servomotor
- [Elegir un filamento para brazos robóticos](https://robonine.com/choosing-filament-for-robotic-arm-applications/), las pruebas detrás de PET-CF

---

<a id="-license"></a>
## 📄 Licencia de uso

Copyright (c) 2026 Robonine. Diferentes tipos de material llevan diferentes licencias:

| Material | Licencia |
|---|---|
| Diseños de hardware en `models/` | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| Software y configuración | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| Documentación e imágenes en `docs/`, `assets/`, todos `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

Vea [LICENSING.md](LICENSING.md) y [REUSE.toml](../../../REUSE.toml) para el mapa archivo por archivo.

---

<a id="-team"></a>
## 👥 Team

| Nombre | Función | Contacto |
|------|------|---------|
| **Alan Subin** | Ingeniero de diseño: diseño mecánico, CAD, folleto de montaje | [LinkedIn](https://www.linkedin.com/in/alan-subin/) |
| **Boris Kotov** | Ingeniero de software y pruebas: prototipos, impresión, bancos de prueba | [Telegram](https://t.me/bkotov) |
| **Nikita Bragin** | Gerente de proyecto | [LinkedIn](https://www.linkedin.com/in/nikita-bragin-82296b29/) |
| **Mikhail Chistiakov** | Diseñador industrial: aspecto y forma del brazo robot | [Telegram](https://t.me/brrryska) |
| **Mikhail Zhmaylo** | Ingeniero estructural: modelos de rigidez, cambios de diseño para reducir la desviación | [Telegram](https://t.me/mikhail_zhmaylo) |
| **Vladislav Eremenko** | Ingeniero estructural: análisis de resistencia y térmico, optimización topológica | [Telegram](https://t.me/v1ad_eremenko) |
| **Vladimir Osipov** | Tester y Consultor: construcción independiente de pruebas | [LinkedIn](https://www.linkedin.com/in/vladimirosipov/) |

<div align="center">

** Construido para la comunidad de robótica por [Robonine](https://robonine.com)** 🤖

</div>
<!-- /translated-content -->
