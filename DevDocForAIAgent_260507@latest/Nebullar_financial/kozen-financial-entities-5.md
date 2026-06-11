---
title: "kozen-financial-entities-5"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - entity_classes
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines scanner constants, barcode format enums, scanner camera and support flags, PIN view enums, printer supplemental enums, ECR connection enums, and general indicator constants in the Kozen Financial SDK."
related:
  - "kozen-financial-scanner-1"
  - "kozen-financial-pinpad"
  - "kozen-financial-ecr"
  - "kozen-financial-general"
  - "kozen-financial-entities-4"
---

## Overview

Defines scanner constants, barcode format enums, scanner camera and support flags, PIN view enums, printer supplemental enums, ECR connection enums, and general indicator constants in the Kozen Financial SDK.

## Entity Class Definition

### ConstantScanner

| Constant Name | Type | Value |
| ------------- | ---- | ----- |
| ALL_BARCODES | ConstantScanner.BarcodeFormat[] | – |
| ONE_DIMENSIONAL_BARCODES | ConstantScanner.BarcodeFormat[] | – |
| TWO_DIMENSIONAL_BARCODES | ConstantScanner.BarcodeFormat[] | – |

### ConstantScanner.BarcodeFormat

| Enum Constant | Type | Description |
| --- | --- | --- |
| CODABAR | 1D | Used in blood banks and libraries, supports digits and some special characters |
| CODABLOCKF | 1D | Stacked barcode format used in logistics and industrial applications |
| CODE11 | 1D | Primarily for telecom equipment, supports digits and hyphens |
| CODE128 | 1D | High-density linear barcode supporting ASCII, widely used in logistics and retail |
| CODE39 | 1D | General-purpose alphanumeric barcode for industrial applications |
| CODE93 | 1D | Improved version of Code 39 with higher density character support |
| EAN13 | 1D | International standard retail barcode (13-digit) |
| EAN8 | 1D | Compact version of EAN-13 for small products (8-digit) |
| GS1_128 | 1D | Supply chain barcode based on Code 128 standard |
| GS1_DATABAR | 1D | Compact barcode for small retail items like produce |
| HK25 | 1D | Hong Kong variant of Interleaved 2 of 5 barcode |
| IATA25 | 1D | Air cargo specific barcode format |
| INDUSTRIAL25 | 1D | Industrial variant of 25 barcodes |
| ITF25 | 1D | High-density numeric barcode for carton labeling |
| MATRIX25 | 1D | Variant of 25 barcode format |
| MSI | 1D | Inventory management barcode (digits only) |
| TELEPEN | 1D | UK barcode standard supporting full ASCII |
| UPCA | 1D | North American retail product barcode (12-digit) |
| UPCE | 1D | Compressed version of UPC-A for small packages |
| USPS4ST | 1D | US Postal Service tracking barcode |
| AZTEC | 2D | Compact matrix barcode suitable for small spaces |
| DATAMATRIX | 2D | 2D barcode for product identification and marking |
| DOTCODE | 2D | Dot-based barcode for high-speed industrial printing |
| GRIDMATRIX | 2D | Chinese-developed 2D barcode for Chinese characters |
| GS1_DATAMATRIX | 2D | GS1-compliant version of Data Matrix |
| HANXIN | 2D | Chinese national standard 2D barcode |
| MAXICODE | 2D | Fixed-size matrix barcode used in logistics |
| MICROPDF | 2D | Compact PDF417 variant for ID documents |
| PDF417 | 2D | Stacked 2D barcode for transportation and ID cards |
| QRCODE | 2D | Popular matrix barcode for general-purpose use |

### ConstantScanner.ScannerCameraType

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| CAMERA_FRONT | ENUM | Front Camera |
| CAMERA_REAR | ENUM | Rear Camera |
| SCANNER | ENUM | E-Series Scanner |

### ConstantScanner.BarcodeSupport

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| ALL_SUPPORT | ENUM | This barcode type is supported by both cameras and scanner |
| CAMERA_SUPPORT | ENUM | This barcode type is only supported by front/rear cameras |
| SCANNER_SUPPORT | ENUM | This barcode type is only supported by scanner |

### PinViewEnum

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| BUTTON_BACKSPACE | ENUM | Backspace key |
| BUTTON_ENTER | ENUM | Enter key |
| BUTTON_ESC | ENUM | Escape key |
| BUTTON0 | ENUM | Number key 0 |
| BUTTON1 | ENUM | Number key 1 |
| BUTTON2 | ENUM | Number key 2 |
| BUTTON3 | ENUM | Number key 3 |
| BUTTON4 | ENUM | Number key 4 |
| BUTTON5 | ENUM | Number key 5 |
| BUTTON6 | ENUM | Number key 6 |
| BUTTON7 | ENUM | Number key 7 |
| BUTTON8 | ENUM | Number key 8 |
| BUTTON9 | ENUM | Number key 9 |

### ConstantPrinter.GrayPercent

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| GRAY_100 | ENUM | 100% gray level (fully opaque gray). |
| GRAY_70 | ENUM | 70% gray level. |
| GRAY_80 | ENUM | 80% gray level. |
| GRAY_90 | ENUM | 90% gray level |

### ConstantPrinter.GlobalFontSize

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| LARGE | ENUM | Large size. |
| NORMAL | ENUM | Normal size. |
| SMALL | ENUM | Small size. |

### ConstantPrinter.LineSpaceMultiplier

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| MULTIPLIER_05 | ENUM | Multiplier value of 0.5. |
| MULTIPLIER_10 | ENUM | Multiplier value of 1.0. |
| MULTIPLIER_15 | ENUM | Multiplier value of 1.5. |
| MULTIPLIER_20 | ENUM | Multiplier value of 2.0. |

### ConstantEcr.ConnectType

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| BT | ENUM | bluetooth |
| HOST | ENUM | localhost |

### ConstantEcr.ConnectState

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| CONNECT_TIMEOUT | ENUM | Connection timed out. |
| CONNECTED | ENUM | Connected. |
| CONNECTION_ERROR | ENUM | Connection error occurred. |
| DISCONNECTED | ENUM | Disconnected. |
| IDLE | ENUM | Initial state. |
| READ_ERROR | ENUM | Read error occurred. |
| SERVER_CREATE_ERROR | ENUM | Server creation error occurred. |
| SERVER_LISTENING | ENUM | Server is listening. |
| WRTE_ERROR | ENUM | Write error occurred. |

### ConstantGeneral.IndicatorType

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| PINPAD_CAPACITIVE | int | Capacitive pinpad |
| PINPAD_PHYSICAL | int | Physical pinpad |

## Related Links

- [[kozen-financial-scanner-1]]
- [[kozen-financial-pinpad]]
- [[kozen-financial-ecr]]
- [[kozen-financial-general]]
- [[kozen-financial-entities-4]]
