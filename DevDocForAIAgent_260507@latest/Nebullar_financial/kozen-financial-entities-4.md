---
title: "kozen-financial-entities-4"
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
summary: "Defines printer constants, printer formatting enums, print failure policies, font size enums, and security constants used by Kozen Financial SDK device modules."
related:
  - "kozen-financial-printer"
  - "kozen-financial-security"
  - "kozen-financial-entities-5"
---

## Overview

Defines printer constants, printer formatting enums, print failure policies, font size enums, and security constants used by Kozen Financial SDK device modules.

## Entity Class Definition

### ConstantPrinter

| Constant Name | Type | Value |
| --- | --- | --- |
| STATUS_IDLE | int | 0 |
| STATUS_NO_PAPER | int | 3 |
| STATUS_OVERHEAT | int | 2 |
| STATUS_PRINTING | int | 1 |

### ConstantPrinter.Align

| Enum Constant | Type | Description |
| --- | --- | --- |
| CENTER | ENUM | Center alignment |
| LEFT | ENUM | Left alignment |
| RIGHT | ENUM | Right alignment |

### ConstantPrinter.BarcodeFormat

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| CODABAR | ENUM | CODABAR 1D format. |
| CODE_128 | ENUM | Code 128 1D format. |
| CODE_39 | ENUM | Code 39 1D format. |
| CODE_93 | ENUM | Code 93 1D format. |
| DATA_MATRIX | ENUM | Data Matrix 2D barcode format. |
| EAN_8 | ENUM | EAN-8 1D format. |
| QR_CODE | ENUM | QR Code 2D barcode format. |
| UPC_E | ENUM | UPC-E 1D format. |

### ConstantPrinter.PrintFailurePolicy

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| ABORT_ALL | ENUM | Aborts all pending print jobs in the queue |
| IGNORE_AND_CONTINUE | ENUM | Ignores current error and continues next print |

### ConstantPrinter.FontSize

| Constant Name | Type | Value |
| --- | --- | --- |
| LARGE | float | 36.0f |
| NORMAL | float | 24.0f |
| SMALL | float | 16.0f |

### ConstantSecurity

| Constant Name | Type | Value |
| --- | --- | --- |
| AUTHENTICATION_BOTH | int | 2 |
| AUTHENTICATION_GENERATION | int | 0 |
| AUTHENTICATION_VERIFICATION | int | 1 |
| DUKPT_KEY_SELECT_DATA_REQUEST | int | 1 |
| DUKPT_KEY_SELECT_DATA_RESPONSE | int | 2 |
| DUKPT_KEY_SELECT_MAC_REQUEST_OR_RESPONSE | int | 0 |
| DUKPT_KEY_SELECT_PIN_ENCRYPTION | int | 3 |
| DUKPT_MAC_MODE_CBC | int | 2 |
| DUKPT_MAC_MODE_ECB | int | 0 |
| DUKPT_MODE_AES_MODE | int | 128 |
| ENCRYPTION_ALGORITHM_AES | int | 16 |
| ENCRYPTION_ALGORITHM_SM4 | int | 32 |
| ENCRYPTION_ALGORITHM_TDES | int | 0 |
| ENCRYPTION_MECHANISM_DUKPT | int | 2 |
| ENCRYPTION_MECHANISM_MK_SK | int | 1 |
| KCV_MODE_CHK_0 | int | 1 |
| KCV_MODE_CHK_EVEN | int | 3 |
| KCV_MODE_CHK_ODD | int | 2 |
| KCV_MODE_NO_VERIFY | int | 0 |
| KEY_ALG_TYPE_2TDEA | int | 0 |
| KEY_ALG_TYPE_3TDEA | int | 16 |
| KEY_ALG_TYPE_AES_128 | int | 32 |
| KEY_ALG_TYPE_AES_192 | int | 48 |
| KEY_ALG_TYPE_AES_256 | int | 64 |
| KSN_AUTO_INCREASING_BY_DUKPT_TDES_MAC_BOTH_KEY | int | 0 |
| KSN_NOT_AUTO_INCREASING_BY_DUKPT_TDES_MAC_BOTH_KEY | int | 20 |
| KSN_NOT_AUTO_INCREASING_BY_DUKPT_TDES_MAC_RSP_KEY | int | 40 |
| MAC_ALGORITHM_ANSI_X9_19 | int | 2 |
| MAC_ALGORITHM_ANSI_X9_9 | int | 3 |
| MAC_ALGORITHM_CBC | int | 0 |
| MAC_ALGORITHM_XOR_ECB_MAC | int | 1 |
| MAC_MODE_ANSI_X9_19 | int | 2 |
| MAC_MODE_ANSI_X9_9 | int | 3 |
| MAC_MODE_CBC | int | 0 |
| MAC_MODE_XOR_ECB_MAC | int | 1 |
| NOT_SELF_INCREASING | int | 0 |
| OPERATION_DIRECTION_DECRYPT | int | 0 |
| OPERATION_DIRECTION_ENCRYPT | int | 1 |
| OPERATION_MODE_CBC | int | 2 |
| OPERATION_MODE_ECB | int | 0 |
| PED_CALC_DES_MODE_CBC_DEC | int | 2 |
| PED_CALC_DES_MODE_CBC_ENC | int | 3 |
| PED_CALC_DES_MODE_ECB_DEC | int | 0 |
| PED_CALC_DES_MODE_ECB_ENC | int | 1 |
| PED_CALC_DUKPT_MODE_DEC | int | 0 |
| PED_CALC_DUKPT_MODE_ENC | int | 1 |
| PED_CALC_RSA_MODE_NO_PADDING | int | 0 |
| PED_CALC_RSA_MODE_OAEP_PADDING | int | 2 |
| PED_CALC_RSA_MODE_PKCS1_PADDING | int | 1 |
| PED_PROTECT_KEY_TYPE_DUKPT | int | 1 |
| PED_PROTECT_KEY_TYPE_MKSK | int | 0 |
| PED_PROTECT_KEY_TYPE_RSA | int | 2 |
| PED_PROTECT_TYPE_DEC | int | 1 |
| PED_PROTECT_TYPE_TR31 | int | 0 |
| PED_PROTECT_WRITE_TYPE_DUKPT | int | 2 |
| PED_PROTECT_WRITE_TYPE_TLK | int | 0 |
| PED_PROTECT_WRITE_TYPE_TMK | int | 1 |
| PED_TAK | int | 4 |
| PED_TDK | int | 5 |
| PED_TEK | int | 6 |
| PED_TIK | int | 7 |
| PED_TLK | int | 1 |
| PED_TMK | int | 2 |
| PED_TPK | int | 3 |
| PED_TTK | int | 9 |
| PINBLOCK_DUKPT_FMT_ISO9564_0 | int | 32 |
| PINBLOCK_DUKPT_FMT_ISO9564_0_KSN_INC | int | 0 |
| PINBLOCK_DUKPT_FMT_ISO9564_1 | int | 33 |
| PINBLOCK_DUKPT_FMT_ISO9564_1_KSN_INC | int | 1 |
| PINBLOCK_DUKPT_FMT_ISO9564_2 | int | 34 |
| PINBLOCK_DUKPT_FMT_ISO9564_2_KSN_INC | int | 2 |
| PINBLOCK_DUKPT_FMT_ISO9564_4 | int | 36 |
| PINBLOCK_DUKPT_FMT_ISO9564_4_KSN_INC | int | 4 |
| PINBLOCK_TPK_FMT_ISO9564_0 | int | 0 |
| PINBLOCK_TPK_FMT_ISO9564_1 | int | 1 |
| PINBLOCK_TPK_FMT_ISO9564_3 | int | 2 |
| PINBLOCK_TPK_FMT_ISO9564_4 | int | 4 |
| SELF_INCREASING | int | 64 |
| USE_BOTH_WAYS_KEY | int | 2 |
| USE_DATA_DECRYPT_KEY | int | 1 |
| USE_DATA_ENCRYPT_KEY | int | 0 |
| WRITE_DUKPT_WITH_TMK_ALG_TYPE_AES | int | 17 |
| WRITE_DUKPT_WITH_TMK_ALG_TYPE_TDES | int | 16 |

## Related Links

- [[kozen-financial-printer]]
- [[kozen-financial-security]]
- [[kozen-financial-entities-5]]
