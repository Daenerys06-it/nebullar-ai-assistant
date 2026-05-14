---
title: "kozen-financial-entities-3"
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
summary: "Defines EMV terminal configuration and transaction data constants used by setTerminal, getTerminal, and startTransaction APIs in the Kozen Financial SDK."
related:
  - "kozen-financial-emv-1"
  - "kozen-financial-emv-2"
  - "kozen-financial-entities-1"
  - "kozen-financial-entities-2"
---

## Overview

Defines EMV terminal configuration and transaction data constants used by setTerminal, getTerminal, and startTransaction APIs in the Kozen Financial SDK.

## Entity Class Definition

### ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints

| Constant Name | Type | Value |
| --- | --- | --- |
| BYPASS_PIN_ENTRY | String | "BypassPINEntry" |
| CARD_HOLDER_CONFIRM | String | "CardHolderConfirm" |
| CONFIG | String | "Config" |
| DEFAULT_DDOL | String | "DefaultDDOL" |
| DEFAULT_TDOL | String | "DefaultTDOL" |
| EXCEPTION_FILE | String | "ExceptionFile" |
| FLOOR_LIMIT_CHECKING | String | "FloorLimitChecking" |
| FORCED_ACCEPT | String | "ForcedAccept" |
| FORCED_ONLINE | String | "ForcedOnline" |
| GET_DATA_FOR_PIN_COUNTER | String | "GetDataForPINCounter" |
| IFD_SERIAL_NUMBER | String | "IfdSerialNumber" |
| ISSUER_REFERRAL | String | "IssuerReferral" |
| LANGUAGE_SELECT | String | "LanguageSelect" |
| MERCHANT_CATEGORY_CODE | String | "MerchantCategoryCode" |
| MERCHANT_ID | String | "MerchantId" |
| MERCHANT_NAME | String | "MerchantName" |
| PSE | String | "Pse" |
| RANDOM_TRANSACTION_SELECTION | String | "RandomTransactionSelection" |
| REVOCATION_ISSUER_PUBLIC_KEY | String | "RevocationIssuerPublicKey" |
| SETTINGS_AMEX | int | 24 |
| SETTINGS_DISCOVER | int | 23 |
| SETTINGS_EFTPOS | int | 30 |
| SETTINGS_INTERAC | int | 29 |
| SETTINGS_JCB | int | 25 |
| SETTINGS_MASTERCARD | int | 22 |
| SETTINGS_MIR | int | 26 |
| SETTINGS_PURE | int | 28 |
| SETTINGS_RUPAY | int | 27 |
| SETTINGS_UNIONPAY | int | 21 |
| SETTINGS_VISA | int | 20 |
| SUBSEQUENT_BYPASS_PIN_ENTRY | String | "SubsequentBypassPINEntry" |
| TAG_AMEX_SET_ENTRY_POINT | String | "DF30" |
| TAG_AMEX_SET_KERNEL_CONFIG | String | "DF1B" |
| TAG_AMEX_SET_QUALIFIERS | String | "9F6E" |
| TAG_AMEX_SET_STATUS_ZERO_AMOUNT | String | "DF32" |
| TAG_CARD_DATA_INPUT_CAPABILITY | String | "DF8117" |
| TAG_DISCOVER_SET_ENTRY_POINT | String | "DF30" |
| TAG_DISCOVER_SET_QUALIFIERS | String | "9F66" |
| TAG_DISCOVER_SET_STATUS_ZERO_AMOUNT | String | "DF32" |
| TAG_EFTPOS_SET_ENTRY_POINT | String | "DF30" |
| TAG_EFTPOS_SET_KERNEL_CONFIG | String | "DF1B" |
| TAG_EFTPOS_SET_QUALIFIERS | String | "9F66" |
| TAG_EFTPOS_SET_STATUS | String | "DF31" |
| TAG_EFTPOS_SET_ZERO_AMOUNT | String | "DF32" |
| TAG_JCB_SET_ENTRY_POINT | String | "DF30" |
| TAG_JCB_SET_KERNEL_CONFIG | String | "DF1B" |
| TAG_JCB_SET_QUALIFIERS | String | "9F53" |
| TAG_JCB_SET_STATUS | String | "DF31" |
| TAG_JCB_SET_ZERO_AMOUNT | String | "DF32" |
| TAG_MASTERCARD_SET_CVM_CAPABILITIES | String | "DF8118" |
| TAG_MASTERCARD_SET_DEFAULT_UDOL | String | "DF811A" |
| TAG_MASTERCARD_SET_KERNEL_CONFIG | String | "DF811B" |
| TAG_MASTERCARD_SET_KERNEL_ID | String | "DF810C" |
| TAG_MASTERCARD_SET_MAGSTRIPE_APP_VERSION | String | "9F6D" |
| TAG_MASTERCARD_SET_MAGSTRIPE_CVM_CAPABILITIES | String | "DF811E" |
| TAG_MASTERCARD_SET_MAGSTRIPE_NO_CVM_CAPABILITIES | String | "DF812C" |
| TAG_MASTERCARD_SET_MOBILE_SUPPORT_INDICATOR | String | "9F7E" |
| TAG_MASTERCARD_SET_NO_CVM_CAPABILITIES | String | "DF8119" |
| TAG_MASTERCARD_SET_RRP_ACCURACY_THRESHOLD | String | "DF8136" |
| TAG_MASTERCARD_SET_RRP_CAPDU_EXPECTED | String | "DF8134" |
| TAG_MASTERCARD_SET_RRP_MAX_GRACE | String | "DF8133" |
| TAG_MASTERCARD_SET_RRP_MIN_GRACE | String | "DF8132" |
| TAG_MASTERCARD_SET_RRP_MISMATCH_THRESHOLD | String | "DF8137" |
| TAG_MASTERCARD_SET_RRP_RAPDU_EXPECTED | String | "DF8135" |
| TAG_MIR_SET_ENTRY_POINT | String | "DF30" |
| TAG_MIR_SET_QUALIFIERS | String | "9F66" |
| TAG_MIR_SET_STATUS_ZERO_AMOUNT | String | "DF32" |
| TAG_PURE_SET_ENTRY_POINT | String | "DF30" |
| TAG_PURE_SET_KERNEL_CONFIG | String | "DF1B" |
| TAG_PURE_SET_QUALIFIERS | String | "C7" |
| TAG_PURE_SET_STATUS | String | "DF31" |
| TAG_PURE_SET_ZERO_AMOUNT | String | "DF32" |
| TAG_SECURITY_CAPABILITY | String | "DF811F" |
| TAG_UNIONPAY_SET_ENTRY_POINT | String | "DF30" |
| TAG_UNIONPAY_SET_QUALIFIERS | String | "9F66" |
| TAG_UNIONPAY_SET_STATUS_ZERO_AMOUNT | String | "DF32" |
| TAG_VISA_SET_ENTRY_POINT | String | "DF30" |
| TAG_VISA_SET_KERNEL_CONFIG | String | "DF1B" |
| TAG_VISA_SET_QUALIFIERS | String | "9F66" |
| TAG_VISA_SET_STATUS_ZERO_AMOUNT | String | "DF32" |
| TERMINAL_CAPABILITY | String | "TerminalCapability" |
| TERMINAL_COUNTRY_CODE | String | "TerminalCountryCode" |
| TERMINAL_ENTRY_MODE | String | "TerminalEntryMode" |
| TERMINAL_EX_CAPABILITY | String | "TerminalExCapability" |
| TERMINAL_ID | String | "TerminalId" |
| TERMINAL_TYPE | String | "TerminalType" |
| TRANS_CURRENCY_CODE | String | "TransCurrencyCode" |
| TRANS_CURRENCY_EXP | String | "TransCurrencyExp" |
| TRANS_REFER_CURRENCY_CODE | String | "TransReferCurrencyCode" |
| TRANS_REFER_CURRENCY_EXP | String | "TransReferCurrencyExp" |
| TYPE_AMEX | int | 7 |
| TYPE_CONFIG | int | 2 |
| TYPE_DISCOVER | int | 6 |
| TYPE_INTERAC | int | 10 |
| TYPE_MASTERCARD | int | 5 |
| TYPE_MIR | int | 8 |
| TYPE_RUPAY | int | 9 |
| TYPE_TERMINAL | int | 1 |
| TYPE_UNIONPAY | int | 4 |
| TYPE_VISA | int | 3 |
| UNABLE_TO_GO_ONLINE | String | "UnableToGoOnline" |
| VELOCITY_CHECKING | String | "VelocityChecking" |

### ConstantEmv.POIEmvCoreManager.EmvTransDataConstraints

| Constant Name | Type | Value |
| --- | --- | --- |
| ACCOUNT_MASK_HEAD | String | "accountMaskHead" |
| ACCOUNT_MASK_TAIL | String | "accountMaskTail" |
| ACCOUNT_TYPE | String | "accountType" |
| AMOUNT_CONFIG | String | "amountConfig" |
| APPLE_VAS | String | "appleVas" |
| CL_SPECIAL_TYPE | String | "clSpecialType" |
| CT_SPECIAL_TYPE | String | "ctSpecialType" |
| ENCRYPT_BASE64 | String | "encryptBase64" |
| ENCRYPT_CONTACT | String | "encryptContact" |
| ENCRYPT_CONTACTLESS | String | "encryptContactless" |
| ENCRYPT_EMV_DATA | String | "encryptEmvData" |
| ENCRYPT_KEY_INDEX | String | "encryptKeyIndex" |
| ENCRYPT_KEY_MODE | String | "encryptKeyMode" |
| ENCRYPT_KEY_MODE_TRANS_ARMOR | int | 1 |
| ENCRYPT_MAGSTRIPE | String | "encryptMagstripe" |
| ENCRYPT_MODE | String | "encryptMode" |
| ENCRYPT_MODE_CBC | int | 2 |
| ENCRYPT_MODE_ECB | int | 1 |
| ENCRYPT_OPEN_CONTACT | int | 1 |
| ENCRYPT_OPEN_CONTACTLESS | int | 2 |
| ENCRYPT_OPEN_MAGSTRIPE | int | 4 |
| ENCRYPT_PADDING | String | "encryptPadding" |
| ENCRYPT_SHA1 | String | "encryptSHA1" |
| ENCRYPT_TYPE | String | "encryptType" |
| ENCRYPT_TYPE_DUKPT_DATA_REQUEST | int | 3 |
| ENCRYPT_TYPE_DUKPT_DATA_RESPONSE | int | 4 |
| ENCRYPT_TYPE_DUKPT_MAC | int | 2 |
| ENCRYPT_TYPE_DUKPT_PIN | int | 5 |
| ENCRYPT_TYPE_RSA | int | 6 |
| ENCRYPT_TYPE_TDK | int | 1 |
| ENCRYPT_TYPE_TTK | int | 7 |
| ENCRYPT_VECTOR | String | "encryptVector" |
| GOOGLE_SMART_TAP | String | "googleSmartTap" |
| OPEN_ENCRYPT | String | "openEncrypt" |
| RSA_TRANS_ARMOR_KEY_ID | String | "rsaTransArmorKeyId" |
| RSA_TRANS_ARMOR_POS_ID | String | "rsaTransArmorPosId" |
| SPECIAL_CONTACT | String | "specialContact" |
| SPECIAL_CONTACT_TIME | String | "specialContactTime" |
| SPECIAL_MAGSTRIPE | String | "specialMagstripe" |
| SPECIAL_MAGSTRIPE_TIME | String | "specialMagstripeTime" |
| SPECIAL_START_MODE | String | "specialStartMode" |
| SPECIAL_TYPE | String | "specialType" |
| START_A | int | 0 |
| START_B | int | 1 |
| START_C | int | 2 |
| START_D | int | 3 |
| TARNS_COUNTER | String | "tarnsCounter" |
| TRANS_AMOUNT | String | "transAmount" |
| TRANS_AMOUNT_OTHER | String | "transAmountOther" |
| TRANS_DATE | String | "transDate" |
| TRANS_FALLBACK | String | "transFallback" |
| TRANS_MODE | String | "transMode" |
| TRANS_TIME | String | "transTime" |
| TRANS_TIMEOUT | String | "transTimeout" |
| TRANS_TYPE | String | "transType" |
| USE_ABECS | String | "useABECS" |
| USE_CARD_READ_SUCCESS | String | "useCardReadSuccess" |
| USE_CT_RUPAY | String | "useCTRupay" |
| USE_DELAY_PIN | String | "useDelayPIN" |
| USE_ENCRYPT_AMEX_TRACK | String | "useEncryptAmexTrack" |
| USE_FILTER | String | "useFilter" |
| USE_FORCED_AID_SELECTION | String | "useForcedAIDSelection" |
| USE_FORCED_ICC_AID_SELECTION | String | "useForcedIccAIDSelection" |
| USE_FORCED_RETURN_OF_CARD | String | "useForcedReturnOfCard" |
| USE_GAC1_FILTER | String | "useGac1Filter" |
| USE_GAC2_FILTER | String | "useGac2Filter" |
| USE_GPO_BEFORE_FILTER | String | "useGpoBeforeFilter" |
| USE_LOG | String | "log" |
| USE_MAGSTRIPE_FILTER | String | "useMagstripeFilter" |
| USE_PPSE_FAIL_SEND_AIDS_OPTION | String | "usePPSEFailSendAidsOption" |
| USE_SELECT_AFTER_FILTER | String | "useSelectAfterFilter" |
| USE_SELECT_KERNEL | String | "useSelectKernel" |
| USE_SPECIAL_AID_SELECTION | String | "useSpecialAIDSelection" |
| USE_USA_VISA | String | "useUSAVisa" |
| ENCRYPT_TRACK_USE_BCD | String | "encryptTrackUseBCD" |
| DOUBLE_BCD | String | "doubleBCD" |
| ENCRYPT_TRACK2_EXPIRATION_DATE | String | "encryptTrack2ExpirationData" |

## Related Links

- [[kozen-financial-emv-1]]
- [[kozen-financial-emv-2]]
- [[kozen-financial-entities-1]]
- [[kozen-financial-entities-2]]
