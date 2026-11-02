<!-- translation-navigation -->
[English](../../en/docs/bom.md) · [Русский](bom.md) · [Español](../../es/docs/bom.md) · [Français](../../fr/docs/bom.md) · [Deutsch](../../de/docs/bom.md) · [Português (Brasil)](../../pt-BR/docs/bom.md) · [简体中文](../../zh-CN/docs/bom.md) · [日本語](../../ja/docs/bom.md) · [हिन्दी](../../hi/docs/bom.md) · [العربية](../../ar/docs/bom.md)

[Английский оригинал](../../../bom.md)

[Документация](../README.md) · [Печать](printing.md) · [Комплектующие](bom.md) · [Сборка](assembly-guide.md) · [Характеристики](specifications.md) · [Модели](../models/README.md) · [Участие](../CONTRIBUTING.md) · [Лицензирование](../LICENSING.md) · [Переводы](translations.md)

> Полный перевод документа. Изображения и исходный PDF-буклет общие для всех языков. Перевод подготовлен с помощью ИИ; проверка носителями языка ещё не проведена.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="bill-of-materials"></a>
# Спецификация комплектующих

Количество рассчитано на один полный комплект: одну ведомую и одну ведущую руку. Печатные детали отдельно перечислены в [printing.md](printing.md).

<a id="estimated-kit-cost"></a>
## Расчётная стоимость комплекта

**Одна ведущая и одна ведомая рука: $340 на комплектующие или $374 с материалом для печати.**

| Категория | Стоимость использованного количества (USD) | Закупка полных упаковок / катушек (USD) |
|---|---:|---:|
| Сервоприводы (12 pcs) | $240.72 | $240.72 |
| Электроника, камера и блоки питания | $50.50 | $50.50 |
| Подшипники, стальные направляющие и струбцины | $37.76 | $49.70 |
| Крепёж | $11.24 | $28.60 |
| **Итого комплектующие** | **$340.22** | **$368.82** |
| Материал для печати: 0.4 kg PET-CF17 + 0.75 kg PETG | $33.75 | $66.0 |
| **Итого с материалом для печати** | **$373.97** | **$434.82** |

В столбце **Итого (USD)** указана стоимость нужного для комплекта количества по справочному предложению, использованному в расчёте строки, а не сумма предложений разных поставщиков. Включённые винты стоят $0; альтернативные карбоновые трубки в итог не входят. Используются указанные ниже справочные цены с округлением каждой строки до центов. Это не новые предложения поставщиков: перед заказом проверьте варианты, минимальные партии и цены. Доставка, налоги, инструменты, компьютер, принтер, электричество и работа по сборке не включены.

Столбец полных упаковок включает неиспользованные остатки, катушку PET-CF17 массой 0.5 kg и катушку PETG массой 1 kg. Расход пластика — расчётное допущение: заново нарежьте проекты 3MF для своих настроек. В расчёте направляющих использована сталь; карбоновые трубки — альтернатива.

![Комплектующие](../../../../assets/images/assembly/hardware.jpg)

<a id="servos"></a>
## Сервоприводы

| Сустав | ID | Ведомая рука | Ведущая рука |
|---|:-:|---|---|
| Поворот основания | 1 | ST-3235-С001 | ST-3215-C066, 1:191 |
| Подъём плеча | 2 | ST-3250-С002 | ST-3215-C066, 1:191 |
| Сгибание локтя | 3 | ST-3250-С002 | ST-3215-C066, 1:191 |
| Сгибание запястья | 4 | ST-3235-С001 | ST-3215-C066, 1:191 |
| Вращение запястья | 5 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |
| Захват / курок | 6 | ST-3215-C049, 1:191 | ST-3215-C066, 1:191 |

Итого: 6 × STS3215 7.4V, 2 × STS3215 12V, 2 × STS3235 12V, 2 × STS3250 12V. Все — сервоприводы Feetech с последовательной шиной TTL.

| Сервопривод | Кол-во | Выбор варианта | Ссылка Aliexpress | Цена за единицу (USD) | Ссылка Alibaba | Цена за единицу (USD) | Итого (USD) |
|---|---|---|---|---|---|---|---|
| STS3215 | 6 | Вариант 7.4V TTL для ведущей руки. Выберите ST-3215-C066 (7.4V). | [Aliexpress](https://www.aliexpress.us/item/3256811860804361.html) | $32.8 | [Alibaba](https://www.alibaba.com/product-detail/Feetech-SO-ARM101-LeRobot-Open-Source_1601636174153.html) | $6.74 | $40.44 |
| STS3215 | 2 | Вариант 12V TTL для суставов ведомой руки 5 и 6. Выберите ST-3215-C049 (12V30KG). | [Aliexpress](https://www.aliexpress.us/item/3256811832699316.html) | $55.8 за 2pcs | [Alibaba](https://www.alibaba.com/product-detail/6pcs-12V-30KG-1-345-STS3215_1601900233170.html) | $14.70 | $29.40 |
| STS3235 | 2 | Вариант 12V TTL для суставов ведомой руки 1 и 4. | [Aliexpress](https://www.aliexpress.us/item/3256810213842277.html) | $63 | [Alibaba](https://www.alibaba.com/product-detail/FEETECH-STS3235-12V-30KG-TTL-Dual_1601910640629.html) | $40.79 | $81.58 |
| STS3250 | 2 | Вариант 12V TTL для суставов ведомой руки 2 и 3. | [Aliexpress](https://www.aliexpress.us/item/3256811995148799.html) | $126.4 за 2pcs | [Alibaba](https://www.alibaba.com/product-detail/Feetech-STS3250-12V-50kg-Servo-High_1601711893549.html) | $44.65 | $89.30 |
| **Итого** |  |  |  |  |  |  | **$240.72** |

- **Ведомая рука, 12V.** STS3250 — бесщёточный сервопривод 50 kg·cm со скоростью 75 RPM. Он приводит два наиболее нагруженных сустава. STS3235 — сервопривод 30 kg·cm с меньшим люфтом, чем STS3215.
- **Ведущая рука, 5V.**С её сервоприводов только считываются показания; нагрузка не прикладывается. Пассивный ST-3215-C066 без мотора и редуктора подходит**только** для ведущей руки.
- Качалки и винты их крепления M3 × 6 входят в комплект сервоприводов.

<a id="electronics"></a>
## Электроника

| Позиция | Кол-во | Примечания | Купить в США | Цена за единицу (США) | Купить в США | Цена за единицу (США) | Купить в ЕС | Цена за единицу (ЕС) | Итого (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Waveshare Bus Servo Adapter | 2 | Контроллер сервоприводов | [Amazon](https://www.amazon.com/Waveshare-Integrates-Control-Applicable-Integrate/dp/B0CJ6TP3TP/) | $13.00 | [Aliexpress](https://www.aliexpress.us/item/3256810343532716.html) | $7.40 | [Amazon EU](https://www.amazon.fr/-/en/Serial-Integrates-Control-Circuit-Support/dp/B0CJBKQ8LJ/) | €11.90 | $14.80 |
| Блок питания 12V постоянного тока (12V 5A, разъём 5.5 2.1mm) | 1 | Ведомая рука. Рекомендуется не менее 60W / 5A. Пиковый ток руки под нагрузкой 300g — 3.3A. Подберите разъём для Adapter (5.5x2.1mm). | [Amazon](https://www.amazon.com/Power-Supply-Adapter-5-5x2-1-2-5mm/dp/B0C3CJF313/) | $10.00 | [Aliexpress](https://www.aliexpress.us/item/3256812113231032.html) | $6.60 | [Amazon EU](https://www.amazon.fr/-/en/zstg-Universal-Power-Supply-Connector/dp/B0GTLSRM91/) | €12.00 | $6.60 |
| Блок питания 5V постоянного тока (5V 2A, разъём 5.5 2.1mm) | 1 | Ведущая рука. Подберите разъём для адаптера (5.5x2.1mm). | [Amazon](https://www.amazon.com/MTDZKJG-Adapter-100V-240V-Transformer-Security/dp/B0BZP65GRW/) | $6.20 | [Aliexpress](https://www.aliexpress.us/item/3256812479558626.html) | $4.10 | [Amazon EU](https://www.amazon.fr/5V-2A-Supply-DC-Adapter/dp/B0GDXFRYJS/) | €11.00 | $4.10 |
| Кабель USB-C, 1.5 м (USB A — USB C, передача данных, 1.5m) | 2 | По одному на контроллер. Нужен кабель передачи данных, не только зарядки. | [Amazon](https://www.amazon.com/Data-Cable-1-5ft-10Gbps-Transfer/dp/B0FMJTHRCM/) | $6.00 | [Aliexpress](https://www.aliexpress.us/item/3256812299430938.html) | $3.00 | [Amazon EU](https://www.amazon.fr/-/en/10Gbps-Transfer-Charging-Samsung-External/dp/B0DHZ1R8FQ/) | €7.00 | $6.00 |
| USB-камера (OV2735, модуль 1080P, 2MP 1920x1080, UVC, объектив 2.8 или 3.0 mm) | 1 | Камера на запястье ведомой руки. В прототипе использован модуль OV2735. Сверьте размеры модуля и крепёжные отверстия с держателем камеры. | [Amazon](https://www.amazon.com/innomaker-Computer-Raspberry-Support-Windows/dp/B0CNCSFQC1/) | $19.00 | [Aliexpress](https://www.aliexpress.us/item/3256804452094739.html) | $26.10 | [Amazon EU](https://www.amazon.fr/InnoMaker-Raspberry-Compatible-Windows-Android/dp/B0CNCSFQC1/) | €21.00 | $19.00 |
| **Итого** |  |  |  |  |  |  |  |  | **$50.50** |

<a id="mechanical-parts"></a>
## Механические детали

| Позиция | Размер | Кол-во | Расположение | Купить в США | Цена за единицу (США) | Купить в США | Цена за единицу (США) | Купить в ЕС | Цена за единицу (ЕС) | Итого (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Шарикоподшипник 6812 | 60 × 78 × 10 mm | 2 | Поворот основания, по одному на руку | [Amazon](https://www.amazon.com/Othmro-6812-2RS-60x78x10mm-Accuracy-Bearing/dp/B081W9QL2Z/) | $5.90 | [Aliexpress](https://www.aliexpress.us/item/3256812369319030.html) | $39.60 / 2 | [Amazon EU](https://www.amazon.fr/-/en/XYWHPGV-6812-2RS-Groove-Bearings-Chrome/dp/B0CQLT6J6D/) | €7.40 / 2 | $11.80 |
| Фланцевый подшипник MF106ZZ | 6 × 10 × 3 mm | 2 | Основная рама захвата | [Amazon](https://www.amazon.com/METERXITY-Shielded-Bearings-Wheelbarrow-Machines/dp/B0F4QXJSRQ/) | $6.60 / 4 | [Aliexpress](https://www.aliexpress.us/item/3256807821523719.html) | $6.00 / 10 | [Amazon EU](https://www.amazon.fr/-/en/PRECISCRY-DE-SGQ-FLZC-11-MF128ZZ-8x12x3-5-5Pcs/dp/B0GQK9BGWK/) | €11.60 / 5 | $1.20 |
| Направляющая (круглый стержень из нержавеющей стали, диаметр 6mm, длина 125mm) | Ø6 × 125 mm, карбон или сталь | 2 | Направляющие захвата | [Amazon](https://www.amazon.com/SKYPRO-Stainless-Diameter-Industry-Working/dp/B0CLCSWSJ9?th=1) | $11.90 / 5 | [Aliexpress](https://www.aliexpress.us/item/3256805290944526.html) | $2.80 | [Amazon EU](https://www.amazon.fr/-/en/SKYPRO-Stainless-Diameter-Industry-Metalworking/dp/B0CLCSWSJ9/) | €14.40 / 5 | $4.76 |
| Алюминиевая направляющая трубка, альтернатива | Ø6 × 4 × 125 mm; из 1 × 300 mm отрезать 2 × 125 mm; снять заусенцы | 2 | Альтернатива стальным направляющим захвата | [Amazon](https://www.amazon.com/dp/B0DRG94GJB/) | $9.99 / 3 шт. | [Aliexpress](https://www.aliexpress.us/item/3256804988048256.html) | $4.05 / 1 шт. | [Amazon EU](https://www.amazon.de/dp/B0D266J2NF/) | €14.89 / 3 шт. | $3.33 (альтернатива) |
| Карбоновая трубка (6mm x 4mm x 125mm), альтернатива | Ø6 × 4 × 125 mm | 2 | Альтернатива стальным направляющим захвата | [Amazon](https://www.amazon.com/MECCANIXITY-Carbon-Pultruded-Airplane-Quadcopter/dp/B0CZDCW2NL/) | $5.60 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256812851232051.html) | $5.90 / 2 | [Amazon EU](https://www.amazon.fr/-/en/QUARKZMAN-Carbon-Fiber-Tubes-Aircraft/dp/B0CZQVN7JB/) | €8.10 / 2 | $5.60 (альтернатива) |
| Струбцина | 3 дюйма, раскрытие 0–75 mm | 4 | По две на руку для крепления основания к столу | [Amazon](https://www.amazon.com/Inch-Clamp-Woodworking-Precision-Carpentry/dp/B0FLHZVM7G/) | $10.00 / 2 | [Aliexpress](https://www.aliexpress.us/item/3256813098676278.html) | $9.70 | [Amazon EU](https://www.amazon.fr/Performance-75mm-Adjustable-Stainless-Metalworking/dp/B0GSQL9BCN/) | €17.40 / 2 | $20.00 |
| **Итого** |  |  |  |  |  |  |  |  |  | **$37.76** |

<a id="fasteners"></a>
## Крепёж

Количество соответствует комплекту в буклете сборки.

Используйте разборный фиксатор резьбы, совместимый с пластиком деталей, например [Vibra-Tite VC-3](https://www.vibra-tite.com/faq/if-vc-3-has-mek-how-can-it-be-plastic-compatible/). Нанесите VC-3 на резьбу металлического винта и полностью высушите до сборки (не менее 30 минут по [техническому описанию](https://www.vibra-tite.com/wp-content/uploads/213_tds.pdf)); не наносите жидкий состав на пластик. Сначала проверьте совместимость с вашим филаментом на пробной детали.

| Крепёж | Стандарт | Кол-во | Купить в США | Цена за единицу (США) | Купить в США | Цена за единицу (США) | Купить в ЕС | Цена за единицу (ЕС) | Итого (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M2 × 6, цилиндрическая головка | DIN 912 | 28 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY8XHB1/) | $6.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZP1XT/) | €6.60 / 60 | $1.04 |
| M2 × 8, цилиндрическая головка | DIN 912 | 12 | [Amazon](https://www.amazon.com/Socket-Stainless-Threaded-Furniture-Printing/dp/B0DKY7L8YJ/) | $6.60 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/THFJWJ-M2-Allen-Cylinder-Screws/dp/B0FP8ZKVDN/) | €7.00 / 60 | $0.49 |
| M3 × 10, потайная головка | DIN 7991 | 64 | [Amazon](https://www.amazon.com/M3-0-5-Socket-Screws-Alloy-Threaded/dp/B08HNF3J3D/) | $9.00 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $3.70 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY12R93P/) | €8.00 / 60 | $4.59 |
| M3 × 16, потайная головка | DIN 7991 | 36 | [Amazon](https://www.amazon.com/Skweawert-40-Pcs-M3x16mm-countersunk/dp/B0D7MY32JZ/) | $6.20 / 40 | [Aliexpress](https://www.aliexpress.us/item/3256812583382995.html) | $4.10 / 50 | [Amazon EU](https://www.amazon.fr/-/en/Mbsomnus-Countersunk-Stainless-Mechanical-Furniture/dp/B0DY138MGY/) | €8.00 / 60 | $2.95 |
| M3 × 4, установочный винт | DIN 913 | 4 | [Amazon](https://www.amazon.com/Generic-Bathroom-Fixtures-Furniture-Project/dp/B0H8DPZJPQ/) | $4.60 / 60 | [Aliexpress](https://www.aliexpress.us/item/3256805653005840.html) | $2.10 / 10 | [Amazon EU](https://www.amazon.fr/-/en/MIETONG-Hex-Socket-Grub-Screws/dp/B0FSKLJR93/) | €6.00 / 20 | $0.31 |
| Гайка M2 | DIN 934 | 12 | [Amazon](https://www.amazon.com/1-10Pcs-M1-M20-Stainless-Steel-Loose/dp/B0GVMQ3VD5/) | $3.50 / 100 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.10 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC5QKH9/) | €6.00 / 20 | $0.42 |
| Гайка M3 | DIN 934 | 36 | [Amazon](https://www.amazon.com/FOCMKEAS-Stainless-Hexagon-Fasteners-Hardware/dp/B0CR7WL4D6/) | $3.70 / 50 | [Aliexpress](https://www.aliexpress.us/item/3256812621986317.html) | $4.00 / 100 | [Amazon EU](https://www.amazon.fr/-/en/PRORAJE-Stainless-Steel-Hexagonal-Diameter/dp/B0GVC7PD4Q/) | €6.30 / 50 | $1.44 |
| M3 × 6, винт под крестовую отвёртку | Из комплекта сервопривода | 16 | Входят в комплект сервоприводов. | — | — | — | — | — | — |
| Саморез 2 × 6 | Из комплекта сервопривода | 20 | Входят в комплект сервоприводов. | — | — | — | — | — | — |
| **Итого** |  |  |  |  |  |  |  |  | **$11.24** |

Чёрный крепёж соответствует рендерам, но не обязателен.

<a id="printing-materials"></a>
## Материалы для печати

| Материал | Назначение | Ссылка закупки | Цена / бюджет (USD) | Итого (USD) |
|---|---|---|---|---:|
| Fiberon PET-CF17 | Звенья руки и держатели сервоприводов | [Polymaker](https://shop.polymaker.com/products/fiberon-pet-cf17) | $44.99 / 1 kg | $18.00 (0.4 kg) |
| PETG или PET-CF | Губки захвата, крышки, рукоятка и курок ведущей руки | [Amazon](https://www.amazon.com/Bambu-Printer-Filament-1-75mm-Spool/dp/B0GS568LQ1/) | PETG: $21.00 / 1 kg | $15.75 (0.75 kg) |
| **Итого** |  |  |  | **$33.75** |

Используйте [руководство по печати](printing.md) и заново нарежьте проекты 3MF, чтобы определить расход пластика для вашего принтера и настроек.

<a id="tools"></a>
## Инструменты

Если инструментов ещё нет, заложите около **$10.00** на небольшой набор шестигранников и отвёрток.

- Шестигранник 1.5 mm для винтов M2: [Amazon search](https://www.amazon.com/s?k=1.5mm+hex+key)
- Шестигранник 2 mm для винтов M3: [Amazon search](https://www.amazon.com/s?k=2mm+hex+key)
- Крестовая отвёртка PH1 для винтов качалок: [Amazon search](https://www.amazon.com/s?k=PH1+Phillips+screwdriver)
<!-- /translated-content -->
