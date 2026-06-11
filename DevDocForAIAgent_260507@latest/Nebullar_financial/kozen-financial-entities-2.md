---
title: "kozen-financial-entities-2"
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
summary: "Defines card reader and EMV core manager constants used for card detection, EMV callbacks, PIN input, online processing, result data, and service configuration in the Kozen Financial SDK."
related:
  - "kozen-financial-emv-1"
  - "kozen-financial-emv-2"
  - "kozen-financial-cardreader"
  - "kozen-financial-entities-1"
  - "kozen-financial-entities-3"
---

## Overview

Defines card reader and EMV core manager constants used for card detection, EMV callbacks, PIN input, online processing, result data, and service configuration in the Kozen Financial SDK.

## Entity Class Definition

### ConstantCardReader

| Constant Name | Type | Value |
| --- | --- | --- |
| ATR | String | "cardAtr" |
| ATS | String | "cardAs" |
| CARD_ATTRIBUTE | String | "cardAttribute" |
| CARD_CATEGORY | String | "cardCategory" |
| CARD_CHANNEL | String | "cardChannel" |
| CARD_SERIAL_NUM | String | "cardSerialNum" |
| CARD_TYPE | String | "cardType" |
| EXPIRED_DATE | String | "cardExpDate" |
| ID_FOR_MANUFACTURER | String | "IDm" |
| PAN | String | "cardPan" |
| PARAMETER_FOR_MANUFACTURER | String | "PMm" |
| REQUEST_DATA | String | "RequestData" |
| SERVICE_CODE | String | "cardServiceCode" |
| TIMEOUT | String | "cardTimeout" |
| TRACK1 | String | "cardTrack1" |
| TRACK2 | String | "cardTrack2" |
| TRACK3 | String | "cardTrack3" |

### ConstantCardReader.CardType

| Constant Name | Type | Value |
| --- | --- | --- |
| ALL | int | 0 |
| CONTACT | int | 2 |
| CONTACTLESS | int | 4 |
| FELICA | int | 32 |
| MAGNETIC | int | 1 |
| MIFARE | int | 8 |
| NFC_TAG | int | 64 |
| PSAM | int | 16 |

### ConstantEmv.POIEmvCoreManager

| Constant Name | Type | Value |
| --- | --- | --- |
| CMD_AMOUNT_CONFIG | int | 1 |
| CMD_CARD_READ_SUCCESS | int | 64 |
| CMD_GAC1 | int | 18 |
| CMD_GAC2 | int | 19 |
| CMD_GPO_BEFORE | int | 49 |
| CMD_GPO_FILTER | int | 16 |
| CMD_ISSUER_REFERRAL | int | 2 |
| CMD_READ_RECORD | int | 17 |
| CMD_READ_RECORD_FILTER | int | 17 |
| CMD_SELECT_AFTER | int | 48 |
| CMD_SELECT_APPLICATION | int | 16 |
| CMD_SELECT_KERNEL | int | 32 |
| CMD_TRY_OTHER_APPLICATION | int | 0 |
| DEVICE_CONTACT | int | 1 |
| DEVICE_CONTACTLESS | int | 2 |
| DEVICE_MAGSTRIPE | int | 4 |
| DEVICE_MIFARE_CLASSIC | int | 8 |
| DEVICE_MIFARE_DESFIRE | int | 64 |
| DEVICE_MIFARE_PLUS | int | 32 |
| DEVICE_MIFARE_ULTRALIGHT | int | 16 |
| DEVICE_VICC | int | 128 |
| EMV_ADMINISTRATIVE | int | 7 |
| EMV_BALANCE_ENQUIRY | int | 13 |
| EMV_BALANCE_UPDATE | int | 14 |
| EMV_CARD_AMEX | int | 5 |
| EMV_CARD_DISCOVER | int | 4 |
| EMV_CARD_EFTPOS | int | 11 |
| EMV_CARD_INTERAC | int | 10 |
| EMV_CARD_JCB | int | 6 |
| EMV_CARD_MASTERCARD | int | 3 |
| EMV_CARD_MIR | int | 7 |
| EMV_CARD_NOT | int | 0 |
| EMV_CARD_PURE | int | 9 |
| EMV_CARD_RUPAY | int | 8 |
| EMV_CARD_UNIONPAY | int | 2 |
| EMV_CARD_VISA | int | 1 |
| EMV_CASH | int | 3 |
| EMV_CASHBACK | int | 4 |
| EMV_DEPOSIT | int | 10 |
| EMV_DISBURSEMENT | int | 8 |
| EMV_GOODS | int | 1 |
| EMV_INQUIRY | int | 11 |
| EMV_MONEY_ADD | int | 12 |
| EMV_PAYMENT | int | 6 |
| EMV_REFUND | int | 9 |
| EMV_SERVICE | int | 2 |
| EMV_SERVICE_CREATION | int | 16 |
| EMV_TRANSFER | int | 5 |
| EMV_VOID | int | 15 |
| GET_LIB_VERSION | int | 0 |
| GET_VERSION_AMEX | int | 6 |
| GET_VERSION_APPLE | int | 16 |
| GET_VERSION_CL1 | int | 14 |
| GET_VERSION_DISCOVER | int | 5 |
| GET_VERSION_EFTPOS | int | 12 |
| GET_VERSION_EMV | int | 1 |
| GET_VERSION_INTERAC | int | 11 |
| GET_VERSION_JCB | int | 7 |
| GET_VERSION_L1 | int | 13 |
| GET_VERSION_MASTERCARD | int | 4 |
| GET_VERSION_MIR | int | 8 |
| GET_VERSION_PURE | int | 10 |
| GET_VERSION_RUPAY | int | 9 |
| GET_VERSION_UNIONPAY | int | 3 |
| GET_VERSION_VISA | int | 2 |
| PIN_ENCIPHER_PIN | int | 2 |
| PIN_ONLINE_PIN | int | 1 |
| PIN_PLAIN_PIN | int | 0 |

### ConstantEmv.POIEmvCoreManager.AppleTerminalConstraints

| Constant Name | Type | Value |
| --- | --- | --- |
| CAPABILITY | String | "capability" |
| CAPABILITY_DUAL_MODE | int | 1 |
| CAPABILITY_PAYMENT_ONLY | int | 3 |
| CAPABILITY_SINGLE_MODE | int | 0 |
| CAPABILITY_VAS_ONLY | int | 2 |
| DATA | String | "data" |
| PROTOCOL | String | "protocol" |
| PROTOCOL_FULL_VAS | int | 1 |
| PROTOCOL_URL_ONLY | int | 0 |
| TAG_APPLE_SET_DELIMITER | String | "DF01" |
| TAG_APPLE_SET_FILTER | String | "9F2B" |
| TAG_APPLE_SET_MERCHANT_ID | String | "9F25" |
| TAG_APPLE_SET_MERCHANT_URL | String | "9F29" |

### ConstantEmv.POIEmvCoreManager.EmvCardInfoConstraints

| Constant Name | Type | Value |
| --- | --- | --- |
| ATR | String | "atr" |
| CARD | String | "card" |
| DATA | String | "data" |
| OUT_AMOUNT | String | "amount" |
| OUT_AMOUNT_OTHER | String | "amountOther" |
| OUT_CONFIRM | String | "confirm" |
| OUT_TLV | String | "tlv" |
| OUT_TVR | String | "tvr" |
| TRACK1 | String | "track1" |
| TRACK2 | String | "track2" |
| TRACK3 | String | "track3" |

### ConstantEmv.POIEmvCoreManager.EmvDrlConstraints

| Constant Name | Type | Value |
| --- | --- | --- |
| CONFIG | String | "Config" |
| TAG_DRL_SET_CVM_REQUIRED_LIMIT | String | "DF24" |
| TAG_DRL_SET_DELIMITER | String | "DF01" |
| TAG_DRL_SET_ENTRY_POINT | String | "DF30" |
| TAG_DRL_SET_FLOOR_LIMIT | String | "DF25" |
| TAG_DRL_SET_PROGRAM_ID | String | "9F5A" |
| TAG_DRL_SET_STATUS_ZERO_AMOUNT | String | "DF32" |
| TAG_DRL_SET_TRANSACTION_LIMIT | String | "DF23" |
| TYPE_AMEX | int | 2 |
| TYPE_VISA | int | 1 |

### ConstantEmv.POIEmvCoreManager.EmvOnlineConstraints

| Constant Name | Type | Value |
| --- | --- | --- |
| APPLE_DATA | String | "appleData" |
| APPLE_MERCHANT | String | "appleMerchant" |
| APPLE_RESULT | String | "appleResult" |
| EMV_DATA | String | "emvData" |
| EMV_ONLINE_APPROVE | int | 0 |
| EMV_ONLINE_DENIAL | int | 2 |
| EMV_ONLINE_FAIL | int | 1 |
| EMV_ONLINE_REFER_TO_CARD_ISSUER | int | 3 |
| ENCRYPT_DATA | String | "encryptData" |
| ENCRYPT_RESULT | String | "encryptResult" |
| OUT_AUTH_CODE | String | "outAuthCode" |
| OUT_AUTH_DATA | String | "outAuthData" |
| OUT_AUTH_RESP_CODE | String | "outAuthRespCode" |
| OUT_ISSUER_SCRIPT | String | "outIssuerScript" |
| OUT_SPECIAL_AUTH_RESP_CODE | String | "outSpecialAuthRespCode" |

### ConstantEmv.POIEmvCoreManager.EmvPinConstraints

| Constant Name | Type | Value |
| --- | --- | --- |
| OUT_PIN_BLOCK | String | "outPinBlock" |
| OUT_PIN_TRY_COUNTER | String | "outPinTryCounter" |
| OUT_PIN_VERIFY_RESULT | String | "outPinVerifyResult" |
| PIN_BLOCK_FORMAT | String | "pinBlockFormat" |
| PIN_BYPASS | String | "pinBypass" |
| PIN_CARD | String | "pinCard" |
| PIN_CARD_RANDOM | String | "pinCardRandom" |
| PIN_COUNTER | String | "pinCounter" |
| PIN_DUKPT_KEY_LENGTH | String | "pinDukptKeyLength" |
| PIN_ENCRYPT | String | "pinEncrypt" |
| PIN_EXPONENT | String | "pinExponent" |
| PIN_IS_ORDER | String | "isOrder " |
| PIN_ISO_FMT0 | int | 0 |
| PIN_ISO_FMT1 | int | 1 |
| PIN_ISO_FMT1_SM4 | int | 5 |
| PIN_ISO_FMT2 | int | 2 |
| PIN_ISO_FMT2_SM4 | int | 6 |
| PIN_ISO_FMT3 | int | 3 |
| PIN_ISO_FMT3_SM4 | int | 7 |
| PIN_ISO_FMT4 | int | 4 |
| PIN_KEY_INDEX | String | "pinKeyId" |
| PIN_KEY_MODE | String | "pinKeyMode" |
| PIN_KEY_MODE_DUKPT | int | 3 |
| PIN_KEY_MODE_TPK | int | 1 |
| PIN_LENGTH_LIMIT | String | "lengthLimit" |
| PIN_MODULE | String | "pinModule" |
| PIN_TIMEOUT | String | "pinTimeout" |
| PIN_TYPE | String | "pinType" |
| VERIFY_CANCELED | int | 4 |
| VERIFY_ERROR | int | 3 |
| VERIFY_NO_PASSWORD | int | 1 |
| VERIFY_PIN_BLOCK | int | 2 |
| VERIFY_SUCCESS | int | 0 |
| VERIFY_TIMEOUT | int | 5 |

### ConstantEmv.POIEmvCoreManager.EmvResultConstraints

| Constant Name | Type | Value |
| --- | --- | --- |
| APPLE_DATA | String | "appleData" |
| APPLE_MERCHANT | String | "appleMerchant" |
| APPLE_RESULT | String | "appleResult" |
| CVM | String | "cvm" |
| CVM_CONFIRMATION_CODE_VERIFIED | int | 2 |
| CVM_NO_CVM | int | 0 |
| CVM_SIGNATURE | int | 1 |
| EMV_DATA | String | "emvData" |
| ENCRYPT_DATA | String | "encryptData" |
| ENCRYPT_RESULT | String | "encryptResult" |
| SCRIPT_RESULT | String | "scriptResult" |
| SECOND_TAP_CANCEL | int | 3 |
| SECOND_TAP_FAIL | int | 1 |
| SECOND_TAP_RESULT | String | "secondTapResult" |
| SECOND_TAP_SUCCESS | int | 0 |
| SECOND_TAP_TIMEOUT | int | 2 |

### ConstantEmv.POIEmvCoreManager.EmvServiceConstraints

| Constant Name | Type | Value |
| --- | --- | --- |
| CONFIG | String | "Config" |
| TAG_PRMACQ_SET_DELIMITER | String | "DF02" |
| TAG_PRMACQ_SET_INDEX | String | "DF30" |
| TAG_PRMACQ_SET_KCV | String | "DF32" |
| TAG_PRMACQ_SET_KEY | String | "DF31" |
| TAG_SERVICE_SET_DATA | String | "DF19" |
| TAG_SERVICE_SET_DELIMITER | String | "DF01" |
| TAG_SERVICE_SET_ID | String | "DF16" |
| TAG_SERVICE_SET_MANAGEMENT | String | "DF18" |
| TAG_SERVICE_SET_PRIORITY | String | "DF17" |
| TAG_SERVICE_SET_PRMACQ | String | "DF21" |
| TAG_SERVICE_SET_PRMISS | String | "DF20" |

## Related Links

- [[kozen-financial-emv-1]]
- [[kozen-financial-emv-2]]
- [[kozen-financial-cardreader]]
- [[kozen-financial-entities-1]]
- [[kozen-financial-entities-3]]
