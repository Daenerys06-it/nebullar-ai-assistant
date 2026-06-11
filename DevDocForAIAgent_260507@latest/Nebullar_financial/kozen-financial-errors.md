---
title: "kozen-financial-errors"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - error_code
summary: "Defines all error codes for the Kozen Financial SDK across 10 modules: CardReaderError, CommonError, GeneralError, PinpadError, PrinterError, ScannerError, SecurityError, EmvError, PosEmvErrorCode, and EcrError."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-financial-overview"
  - "kozen-financial-cardreader"
  - "kozen-financial-general"
  - "kozen-financial-pinpad"
  - "kozen-financial-printer"
  - "kozen-financial-scanner-1"
  - "kozen-financial-security"
  - "kozen-financial-emv"
  - "kozen-financial-ecr"
---

## Overview

Error codes defined across all Kozen Financial SDK modules.

## Error Code List

### CardReaderError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| CARD_APDU_OTHER_ERROR | APDU Error | -70004 |
| CARD_CHECK_OTHER_ERROR | Card Check Other Error | -70003 |
| CARD_CONTACT_ATR_ERROR | Contact Card ATR Data Error | -72001 |
| CARD_CONTACT_NO_SUPPORT | IC Card Not Supported | -72000 |
| CARD_CONTACT_OTHERS_ERROR | Contact Card Insertion Failed | -72002 |
| CARD_CONTACTLESS_ATS_ERROR | Contactless Card ATS Data Error | -73001 |
| CARD_CONTACTLESS_NO_SUPPORT | IC Card Not Supported | -73000 |
| CARD_CONTACTLESS_OTHERS_ERROR | Contactless Card Other Error | -73002 |
| CARD_EXIST_STATUS_OTHER_ERROR | Card Present Status Other Error | -70005 |
| CARD_FELICA_ATS_ERROR | Contactless Card ATS Data Error | -74001 |
| CARD_FELICA_NO_SUPPORT | IC Card Not Supported | -74000 |
| CARD_FELICA_OTHERS_ERROR | Contactless Card Other Error | -74002 |
| CARD_MAG_INVALID_ERROR | Magnetic Track or Data Verification Failed | -71003 |
| CARD_MAG_NEED_RETRY_ERROR | Magnetic Card Swipe Failed, Please Retry | -71002 |
| CARD_MAG_NO_DATA_ERROR | No Data in Magnetic Track | -71001 |
| CARD_MAG_NO_SUPPORT | Magnetic Card Not Supported | -71000 |
| CARD_MAG_OTHERS_ERROR | Magnetic Card Swipe Failed | -71004 |
| CARD_READER_CONTACT_ALREADY_CLOSE | IC Card Already Powered Off | -72006 |
| CARD_READER_CONTACT_CHECK_ERROR | Contact Card Check Failed | -72004 |
| CARD_READER_CONTACT_OFF_ERROR | Contact Card Power-Off Failed | -72005 |
| CARD_READER_CONTACT_OPEN_ERROR | Magnetic Card Check Open Failed | -72003 |
| CARD_READER_CONTACTLESS_ALREADY_CLOSE | Contactless Card Already Powered Off | -73006 |
| CARD_READER_CONTACTLESS_CHECK_ERROR | Contactless Card Check Failed | -73004 |
| CARD_READER_CONTACTLESS_MULTI_CARD | Multiple Contactless Cards Detected | -73007 |
| CARD_READER_CONTACTLESS_OFF_ERROR | Contactless Card Power-Off Failed | -73005 |
| CARD_READER_CONTACTLESS_OPEN_ERROR | Magnetic Card Check Open Failed | -73003 |
| CARD_READER_FELICA_ALREADY_CLOSE | Contactless Card Already Powered Off | -74006 |
| CARD_READER_FELICA_CHECK_ERROR | Contactless Card Check Failed | -74004 |
| CARD_READER_FELICA_OFF_ERROR | Contactless Card Power-Off Failed | -74005 |
| CARD_READER_FELICA_OPEN_ERROR | Magnetic Card Check Open Failed | -74003 |
| CARD_READER_MAG_CHECK_ERROR | Magnetic Card Check Failed | -71006 |
| CARD_READER_MAG_OFF_ERROR | Magnetic Card Power-Off Failed | -71007 |
| CARD_READER_MAG_OPEN_ERROR | Magnetic Card Check Open Failed | -71005 |
| CARD_READER_OFF_OTHER_ERROR | Card Power-Off Other Error | -70002 |
| CARD_TYPE_ERROR | Card Type Error | -70001 |
| NFC_TAG_ALREADY_CLOSE | NFC TAG already closed | -75006 |
| NFC_TAG_NDEF_MESSAGE_ERROR | NFC TAG data error | -75004 |
| NFC_TAG_NDEF_MESSAGE_LENGTH_ERROR | NDEFMessage data length exceeds limit (max: 255 bytes) | -75005 |
| NFC_TAG_NO_SUPPORT | NFC TAG not supported | -75000 |
| NFC_TAG_OFF_ERROR | NFC TAG close failed | -75002 |
| NFC_TAG_OPEN_ERROR | NFC TAG open failed | -75001 |
| NFC_TAG_OTHERS_ERROR | Other NFC TAG error | -75007 |
| NFC_TAG_WRITE_MESSAGE_ERROR | NFC TAG write failed | -75003 |
| NOT_SUPPORT_CHECK_CONTACTLESS_AND_FELICA_SIMULTANEOUS | Simultaneous contactless and Felica card check not supported | -73008 |
| NOT_SUPPORT_OPEN_CONTACTLESS_AND_FELICA_SIMULTANEOUS | Simultaneous contactless and Felica card power-on not supported | -73009 |

### CommonError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| FINANCIAL_PARAMETERS_INVALID | Illegal parameters | -10002  |
| FINANCIAL_SERVICE_DISCONNECT   | Financial services are not connected, please initialize financial services | -10001 |
| FINANCIAL_VERSION_NOT_MATCH  | Financial Services SDK version mismatch | -10000 |
| FEATURE_NOPERMISSION | Permission not granted | -10010 |
| FEATURE_UNSUPPORTED | Feature unsupported | -10011 |

### GeneralError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| GENERAL_ERROR_INIT | General module initialization error | -20000 |
| GENERAL_OTHER_ERROR | Other general error | -20001 |
| GENERAL_PARAMETERS_INVALID | Invalid parameters | -20002 |
| GENERAL_NAVIGATION_BUTTON_TYPE_INVALID | Invalid navigation button type | -20003 |
| GENERAL_SCREEN_ROTATION_ERROR | Screen rotation error | -20004 |
| GENERAL_SET_BEEP_ERROR | Failed to set beep | -20005 |
| GENERAL_INDICATOR_TYPE_ERROR | Indicator type error | -20100 |
| GENERAL_INDICATOR_TYPE_PINPAD_CAPACITIVE_ERROR | Capacitive PINPAD indicator type error | -20101 |

### PinpadError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| PINPAD_OTHER_ERROR | Other PINPAD error | -60000 |
| PINPAD_START_ERROR | Failed to start PINPAD | -60001 |
| PINPAD_CANCEL_ERROR | PINPAD operation canceled | -60002 |
| PINPAD_SCREEN_ORIENTATION_CHANGED | Screen orientation changed during PINPAD operation | -60003 |
| PIN_KEY_COORDINATE_CALCULATION_ERROR | PIN key coordinate calculation error | -60004 |
| PIN_SWITCH_BLIND_MODE_ERROR | Failed to switch to blind PIN mode | -60005 |
| SP_ERROR_PHYSICAL_PINPAD_CALCULATE_KEY_POSITION_ERROR | Failed to calculate physical PINPAD key position | -60006 |
| CURRENT_SP_NOT_SUPPORT_GET_PINPAD_TYPE_ERROR | Current service provider does not support getting PINPAD type | -60007 |
| CURRENT_SP_NOT_SUPPORT_PHYSICAL_PINPAD_ERROR | Current service provider does not support physical PINPAD | -60008 |
| PHYSICAL_PINPAD_NOT_SUPPORT_KEY_POSITION_PARAM_ERROR | Physical PINPAD does not support key position parameters | -60009 |
| PINPAD_KEY_VIEW_POSITION_PARAM_ERROR | Invalid key view position parameters | -60010 |
| DEFAULT_PINPAD_START_ERROR | Failed to start default PINPAD | -60011 |
| CUSTOM_PINPAD_START_ERROR | Failed to start custom PINPAD | -60012 |
| BLIND_PINPAD_START_ERROR | Failed to start blind PINPAD | -60013 |

### PrinterError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| PRINTER_ERROR_INIT | Printer not initialized or initialization failed | -50000 |
| PRINTER_ERROR_NO_PRINTER | No printer device | -50001 |
| PRINTER_ERROR_NOT_OPENED | Printer not opened | -50002 |
| PRINTER_ERROR_PRINT | Print failed | -50003 |
| PRINTER_ERROR_OVERHEAT | Printer overheating | -50004 |
| PRINTER_ERROR_NO_PAPER | Printer out of paper | -50005 |
| PRINTER_ERROR_LOW_POWER | Printing is not possible when the battery level is low | -50006 |
| PRINTER_ERROR_NO_CONTENT | No content to print | -50007 |
| PRINTER_ERROR_OTHER | Other unknown error | -50008 |
| PRINTER_ERROR_QUEUE_OVER_FLOW | Print queue overflow | -50009 |
| PRINTER_ERROR_SCREEN_OFF | Screen off, unable to print | -50010 |
| PRINTER_ERROR_NOT_SUPPORT | Feature or parameter not supported | -50011 |
| PRINTER_ERROR_PRINTING | Configuration not allowed during printing | -50012 |

### ScannerError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| SCANNER_SERVICE_NOT_FIND | Scanner service not found | -30000 |
| SCANNER_SERVICE_UNAVAILABLE | Scanner service unavailable | -30001 |
| SCANNER_SERVICE_CONNECT_FAILED | Failed to connect to scanner service | -30002 |
| SCANNER_SERVICE_DISCONNECT | Scanner service not connected, please call open to initialize | -30003 |
| SCANNER_OTHER_ERROR | Other unknown error | -30004 |
| CAMERA_OCCUPIED | Camera is occupied, please call close to release resources first | -30005 |
| CAMERA_UNKNOWN | Current device does not support this camera type | -30006 |
| GET_CAMERA_INFO_ERROR | Failed to get camera information, please rebind Financial SDK | -30007 |
| INIT_CAMERA_ERROR | Camera initialization failed, try close then open again | -30008 |
| NOT_SUPPORT_LIGHT_CONTROL | Camera does not support light control | -30009 |
| OPEN_LIGHT_FAILED | Failed to turn on fill light, must be called after scan UI is started | -30010 |
| NO_SCAN_TYPE_SET | No decode type set, please set scan type first | -30011 |
| SET_SCAN_TYPE_FAILED | Failed to enable or disable decode type, please check parameters | -30012 |
| PARAMETER_EXCEPTION | Parameter exception | -30013 |
| NOT_SUPPORTED_FEATURE | Current camera type does not support this feature | -30014 |
| PREVIEW_MODE_EXCEPTION | Preview mode exception | -30015 |
| CAMERA_SESSION_ERROR | Camera session error | -30016 |
| CAMERA_CLOSED_ERROR | Camera was unexpectedly closed | -30017 |

### SecurityError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| SECURITY_ERROR_INIT | Security module not initialized | -40000 |
| SECURITY_OTHER_ERROR | Other error (e.g. system interface call exception) | -40001 |
| SECURITY_PARAMETERS_INVALID | Invalid parameters (null or illegal format) | -40002 |
| SECURITY_KEY_TYPE_OUT_OF_RANGE | Key type out of range | -40003 |
| SECURITY_KEY_INDEX_OUT_OF_RANGE | Key index out of range | -40004 |
| SECURITY_DATA_INDEX_OUT_OF_RANGE | Data index out of range | -40005 |
| SECURITY_TLK_INDEX_OUT_OF_RANGE | TLK index out of range | -40006 |
| SECURITY_KEY_IN_EMPTY_ERROR | Key input data is empty | -40007 |
| SECURITY_DATA_IN_EMPTY_ERROR | Input data is empty | -40008 |
| SECURITY_DATA_OUT_NULL_ERROR | Output data is null | -40009 |
| SECURITY_DATA_OUT_LENGTH_ERROR | Output buffer length insufficient | -40010 |
| SECURITY_KCV_MODE_ERROR | KCV mode error | -40011 |
| SECURITY_KCV_ERROR | KCV parameter error | -40012 |
| SECURITY_RANDOM_KEY_OUT_OF_RANGE | Random key output length out of range | -40013 |
| SECURITY_KCV_VALUE_OUT_OF_RANGE | KCV output value out of range | -40014 |
| SECURITY_MKSK_KEY_TYPE_ERROR | MK/SK key type out of range | -40100 |
| SECURITY_MKSK_SRC_KEY_TYPE_ERROR | MK/SK source key type error | -40101 |
| SECURITY_MKSK_KEY_INDEX_ERROR | MK/SK key index error | -40102 |
| SECURITY_MKSK_SRC_KEY_INDEX_ERROR | MK/SK source key index error | -40103 |
| SECURITY_MKSK_KEY_LENGTH_ERROR | MK/SK key length error | -40104 |
| SECURITY_MKSK_ENCRYPTION_ALGORITHM_ERROR | MK/SK encryption algorithm error | -40105 |
| SECURITY_MKSK_CALC_MODE_ERROR | MK/SK calculation mode error | -40106 |
| SECURITY_MKSK_MAC_MODE_ERROR | MK/SK MAC mode error | -40107 |
| SECURITY_MKSK_MAC_OUT_OF_RANGE | MK/SK MAC output length out of range | -40108 |
| SECURITY_MKSK_CALC_OUT_OF_RANGE | MK/SK calculation output length out of range | -40109 |
| SECURITY_SM4_CALC_MODE_ERROR | SM4 calculation mode error | -40110 |
| SECURITY_SM4_CALC_OUT_OF_RANGE | SM4 calculation output length out of range | -40111 |
| SECURITY_DUKPT_TIK_INDEX_ERROR | DUKPT TIK key index error | -40200 |
| SECURITY_DUKPT_SRC_KEY_INDEX_ERROR | DUKPT source key index error | -40201 |
| SECURITY_DUKPT_KEY_USAGE_ERROR | DUKPT key usage parameter error | -40202 |
| SECURITY_DUKPT_KEY_ALG_TYPE_ERROR | DUKPT key algorithm type error | -40203 |
| SECURITY_DUKPT_MAC_ALG_TYPE_ERROR | DUKPT MAC algorithm type error | -40204 |
| SECURITY_DUKPT_INIT_VECTOR_ERROR | DUKPT init vector parameter error | -40205 |
| SECURITY_DUKPT_AES_VECTOR_ERROR | DUKPT AES init vector parameter error | -40206 |
| SECURITY_DUKPT_KEY_TYPE_ERROR | DUKPT key type parameter error | -40207 |
| SECURITY_DUKPT_OPERATION_MODE_ERROR | DUKPT operation mode error | -40208 |
| SECURITY_DUKPT_OPERATION_DIRECTION_ERROR | DUKPT operation direction error | -40209 |
| SECURITY_DUKPT_KSN_MODE_ERROR | DUKPT KSN mode error | -40210 |
| SECURITY_DUKPT_KEY_LENGTH_ERROR | DUKPT key length error | -40211 |
| SECURITY_DUKPT_CALC_OUT_OF_RANGE | DUKPT calculation output length out of range | -40212 |
| SECURITY_DUKPT_MAC_OUT_OF_RANGE | DUKPT MAC output length out of range | -40213 |
| SECURITY_DUKPT_KSN_OUT_OF_RANGE | DUKPT KSN output length out of range | -40214 |
| SECURITY_RSA_KEY_INDEX_OUT_OF_RANGE | RSA key index out of range | -40300 |
| SECURITY_RSA_PADDING_MODE_ERROR | RSA padding mode error | -40301 |
| SECURITY_RSA_RESPONSE_DATA_EMPTY | RSA response data is empty | -40302 |
| SECURITY_RSA_OUT_DATA_LENGTH_OUT_OF_RANGE | RSA output data length out of range | -40303 |
| SECURITY_TR31_SRC_KEY_TYPE_ERROR | TR31 source key type error | -40401 |
| SECURITY_TR31_SRC_KEY_INDEX_ERROR | TR31 source key index error | -40402 |
| SECURITY_TR31_KEY_TYPE_ERROR | TR31 key type error | -40403 |
| SECURITY_TR31_KEY_INDEX_ERROR | TR31 key index error | -40404 |
| SECURITY_TR31_KEY_BLOCK_EMPTY_ERROR | TR31 key block is empty | -40405 |
| SECURITY_TR31_KEY_ALGORITHM_ERROR | TR31 key algorithm type error | -40406 |

### EmvError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| EMV_AID_OTHER_ERROR | Other AID parameter error | -80100 |
| EMV_APPLE_TERMINAL_OTHER_ERROR | Other Apple Terminal configuration error | -80400 |
| EMV_CAPK_OTHER_ERROR | Other CAPK error | -80200 |
| EMV_DELETE_AID_ERROR | Error deleting AID parameter | -80109 |
| EMV_DELETE_APPLE_MERCHANT_ERROR | Error deleting Apple Merchant | -80405 |
| EMV_DELETE_APPLE_TERMINAL_ERROR | Error deleting Apple Terminal | -80402 |
| EMV_DELETE_CAPK_ERROR | Error deleting CAPK | -80209 |
| EMV_DELETE_DRL_ERROR | Error deleting DRL configuration | -80310 |
| EMV_DELETE_EXCEPTION_FILE_ERROR | Error deleting ExceptionFile | -80305 |
| EMV_DELETE_REVOCATION_IPK_ERROR | Error deleting RevocationIPK | -80308 |
| EMV_DELETE_SERVICE_ERROR | Error deleting RuPay Service | -80314 |
| EMV_DRL_OTHER_ERROR | Other DRL configuration error | -80309 |
| EMV_GET_APPLE_MERCHANT_ERROR | Error retrieving Apple Merchant | -80404 |
| EMV_GET_DRL_ERROR | Error retrieving DRL configuration | -80311 |
| EMV_GET_KERNEL_VERSION_ERROR | Error retrieving Kernel version | -80316 |
| EMV_GET_SERVICE_ERROR | Error retrieving RuPay Service | -80315 |
| EMV_GET_TERMINAL_ERROR | Error retrieving terminal parameters | -80302 |
| EMV_OTHER_ERROR | Other EMV error | -80001 |
| EMV_SERVICE_OTHER_ERROR | Other RuPay Service error | -80312 |
| EMV_SET_AID_ERROR | Error setting AID parameter | -80108 |
| EMV_SET_AID_ERROR_AID_NULL | Error loading AID parameter, AID is null | -80101 |
| EMV_SET_AID_ERROR_DDOL_NULL | Error loading AID parameter, DDOL is null | -80103 |
| EMV_SET_AID_ERROR_TACDEFAULT_NULL | Error loading AID parameter, TACDefault is null | -80107 |
| EMV_SET_AID_ERROR_TACDENIAL_NULL | Error loading AID parameter, TACDenial is null | -80105 |
| EMV_SET_AID_ERROR_TACONLINE_NULL | Error loading AID parameter, TACOnline is null | -80106 |
| EMV_SET_AID_ERROR_TDOL_NULL | Error loading AID parameter, TDOL is null | -80104 |
| EMV_SET_AID_ERROR_VERSION_NULL | Error loading AID parameter, Version is null | -80102 |
| EMV_SET_APPLE_MERCHANT_ERROR | Error setting Apple Merchant | -80403 |
| EMV_SET_APPLE_TERMINAL_ERROR | Error setting Apple Terminal | -80401 |
| EMV_SET_CAPK_ERROR | Error setting CAPK | -80208 |
| EMV_SET_CAPK_ERROR_ALGORITHM_IND_NULL | Error loading CAPK parameter, AlgorithmInd is null | -80206 |
| EMV_SET_CAPK_ERROR_CAPK_INDEX_NULL | Error loading CAPK parameter, CapkIndex is null | -80202 |
| EMV_SET_CAPK_ERROR_CHECK_SUM_NULL | Error loading CAPK parameter, Checksum is null | -80205 |
| EMV_SET_CAPK_ERROR_Exponent_NULL | Error loading CAPK parameter, Exponent is null | -80204 |
| EMV_SET_CAPK_ERROR_HASH_IND_NULL | Error loading CAPK parameter, HashInd is null | -80207 |
| EMV_SET_CAPK_ERROR_MODULE_NULL | Error loading CAPK parameter, Module is null | -80203 |
| EMV_SET_CAPK_ERROR_RID_NULL | Error loading CAPK parameter, RID is null | -80201 |
| EMV_SET_CARD_INFO_RESPONSE_ERROR | Error setting card confirmation result | -81004 |
| EMV_SET_DRL_ERROR | Error setting DRL configuration | -80309 |
| EMV_SET_EXCEPTION_FILE_ERROR | Error setting ExceptionFile | -80304 |
| EMV_SET_KERNEL_ERROR | Error setting KernelTag | -80317 |
| EMV_SET_ONLINE_RESPONSE_ERROR | Error setting online result | -81006 |
| EMV_SET_PIN_RESPONSE_ERROR | Error setting PIN result | -81005 |
| EMV_SET_REVOCATION_IPK_ERROR | Error setting RevocationIPK | -80307 |
| EMV_SET_SELECT_RESPONSE_ERROR | Error setting multi-application selection result | -81003 |
| EMV_SET_SELECT_RESPONSE_POSITION_ERROR | Error confirming position in multi-application selection result | -81007 |
| EMV_SET_SERVICE_ERROR | Error setting RuPay Service | -80313 |
| EMV_SET_TERMINAL_ERROR | Error loading terminal parameters | -80301 |
| EMV_START_TRANSACTION_ERROR | Error starting transaction | -81001 |
| EMV_STOP_TRANSACTION_ERROR | Error stopping transaction | -81002 |
| EMV_SUCCESS | Success | 0 |
| EMV_TERMINAL_EXCEPTION_FILE_OTHER_ERROR | Other ExceptionFile error | -80303 |
| EMV_TERMINAL_OTHER_ERROR | Other terminal parameter error | -80300 |
| EMV_TERMINAL_REVOCATION_IPK_OTHER_ERROR | Other RevocationIPK error | -80306 |

### PosEmvErrorCode

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| APPLE_VAS_APPROVED | Apple Vas Approved. | 6 |
| APPLE_VAS_FAILED | Apple Vas Failed. | -41 |
| APPLE_VAS_UNTREATED | Apple Vas Untreated. | -40 |
| APPLE_VAS_WAITING_ACTIVATION | Apple Vas Waiting Activation. | -43 |
| APPLE_VAS_WAITING_INTERVENTION | Apple Vas Waiting Intervention. | -42 |
| EMV_APP_BLOCKED | Application Blocked. | -7 |
| EMV_APP_EMPTY | No Application. | -9 |
| EMV_APPROVED | Transaction Approved. | 1 |
| EMV_APPROVED_ONLINE | Transaction Online Approved. | 2 |
| EMV_CANCEL | Trans Cancel. | -1 |
| EMV_CARD_BLOCKED | Card Locked. | -8 |
| EMV_CARD_ERROR | Abecs Fallback. | -40 |
| EMV_COMMAND_FAIL | Read the Card Fail. | -3 |
| EMV_DATA_ERROR | Card Data Error. | -81 |
| EMV_DECLINED | Transaction Declined. | 3 |
| EMV_DELAYED_APPROVED | Transaction Delayed Approved. | 5 |
| EMV_ENCRYPT_ERROR | Trade Encrypt Error. | -30 |
| EMV_FALLBACK | Fallback. | -4 |
| EMV_FORCE_APPROVED | Transaction Force Approved. | 4 |
| EMV_GPO_6985 | Command GPO 6985. | -50 |
| EMV_MULTI_CONTACTLESS | Read Multi Contactless. | -5 |
| EMV_NOT_ACCEPTED | Not Accepted. | -11 |
| EMV_NOT_ALLOWED | Not Allowed. | -10 |
| EMV_OK | Handle OK. | 0 |
| EMV_OTHER_ERROR | Other Error Exceptions. | -999 |
| EMV_OTHER_ICC_INTERFACE | Not Pure Magnetic Strip. | -6 |
| EMV_OTHER_INTERFACE | Try Another Interface. | -14 |
| EMV_READ_RECORD_ERROR | Command Read Record Error. | -80 |
| EMV_SEE_PHONE | See Phone. | -13 |
| EMV_TERMINATED | Terminated. | -12 |
| EMV_TERMINATED_ON_MCCS | Terminated On MCCS. | -44 |
| EMV_TIMEOUT | Trans Timeout. | -2 |
| EMV_UNENCRYPTED | Trade Unencrypted. | -31 |
| EXCEPTION_ERROR | Exception Error. | 255 |
| PARAMETER_ERROR | Parameter Error. | 254 |

### EcrError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| ECR_CONNECT_CLOSE_FAILED | Failed to close connection | -90006 |
| ECR_CONNECT_FAILED | Connection failed | -90003 |
| ECR_CONNECT_INFO_EMPTY | Connection parameter info is empty | -90001 |
| ECR_CONNECT_INFO_FORMAT_EXCEPTION | Connection parameter format exception | -90002 |
| ECR_ERROR_INIT | ECR module not initialized | -90000 |
| ECR_FD_EMPTY | File handle is null | -90004 |
| ECR_FD_FORMAT_EXCEPTION | File handle format exception | -90005 |
| ECR_WRITE_DATA_EMPTY | Write data is empty | -90007 |
| ECR_WRITE_DATA_FAILED | Write data exception | -90008 |


## Related Links

- [[kozen-financial-overview]]
- [[kozen-financial-cardreader]]
- [[kozen-financial-emv-1]]
- [[kozen-financial-general]]
- [[kozen-financial-pinpad]]
- [[kozen-financial-printer]]
- [[kozen-financial-scanner-1]]
- [[kozen-financial-security]]
- [[kozen-financial-ecr]]
