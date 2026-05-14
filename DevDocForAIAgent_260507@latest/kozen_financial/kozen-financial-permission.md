---
title: "kozen-financial-permission"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - permission
summary: "Defines required Android system permissions for the Kozen Financial SDK across all modules: Scanner, CardReader, EMV, General, PINPAD, Printer, Security, and ECR."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-financial-overview"
---

## Overview

Required Android system permissions for the Kozen Financial SDK.

## Permission List

| Permission Name | Related Module | Tooltips |
| --- | --- | --- |
| android.permission.SUPER_PERMISSIONS_PRINTER | PrinterManager | Control and use built-in printer |
| android.permission.SUPER_PERMISSIONS_PINPAD | PinpadManager | Access encrypted pinpad for input |
| android.permission.SUPER_PERMISSIONS_SCANNER | ScannerManager | Scan barcodes and QR codes |
| android.permission.SUPER_PERMISSIONS_CARD_READER | CardReaderManager | Access magstripe, IC, and contactless cards |
| android.permission.SUPER_PERMISSIONS_EMV | EmvManager | Perform EMV card transactions |
| android.permission.SUPER_PERMISSIONS_GENERAL | GeneralManager | Access general device functions (buzzer, LED) |
| android.permission.SUPER_PERMISSIONS_SERURITY | SecurityManager | Use security module (key management, encryption) |
| android.permission.SUPER_PERMISSIONS_ECR | EcrManager | Interact with external ECR system |

## Related Links

- [[kozen-financial-overview]]
- [[kozen-financial-init]]
