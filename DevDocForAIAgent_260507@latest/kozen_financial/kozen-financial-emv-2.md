---
title: "kozen-financial-emv-2"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - emv
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines Kozen Financial SDK EMV transaction lifecycle APIs, runtime response APIs, EMV tag access APIs, and IEmvListener callback APIs used during payment transaction processing."
related:
  - "kozen-financial-emv-1"
  - "kozen-financial-entities-1"
  - "kozen-financial-entities-2"
  - "kozen-financial-entities-3"
  - "kozen-financial-overview"
  - "kozen-financial-init"
---

## Overview

Defines Kozen Financial SDK EMV transaction lifecycle APIs, runtime response APIs, EMV tag access APIs, and IEmvListener callback APIs used during payment transaction processing.

## Function List

| Function Name | Description |
|--            |-----------|
| int startTransaction(android.os.Bundle bundle, IEmvListener callback) | Start EMV transaction |
| int stopTransaction() | Stop EMV transaction |
| int setKernel(byte[] tlv) | Set EMV Tag/Object parameters |
| byte[] getKernel(String[] tags) | Retrieve EMV Tag/Object parameters |
| int setSelectApplicationResponse(int position) | Set the result of multiple application selection |
| int setCardInfoResponse(android.os.Bundle bundle) | Set card information confirmation result |
| int setPinResponse(android.os.Bundle bundle) | Set Pin input result |
| int setOnlineResponse(android.os.Bundle bundle) | Set the online result |
| void onConfirmCardInfo(int mode,  android.os.Bundle info) Callback for card information confirmation | void onEmvProcess(int type,  android.os.Bundle info) Callback when a card is detected |
| void onEmvProcess(int type,  android.os.Bundle info) | Detect card |
| void onSelectApplication(List<String> appList,  boolean isFirstSelect) | Multiple application selection callback |
| void onConfirmCardInfo(int mode,  android.os.Bundle info) | Card information confirmation callback |
| void onKernelType(int type) | Kernel card scheme type callback |
| void onSecondTapCard() | Second tap card callback |
| void onRequestInputPin(android.os.Bundle info) | Request PIN input callback |
| void onRequestOnlineProcess(android.os.Bundle info) | Request online process callback |
| void onTransactionResult(int resultCode,  android.os.Bundle info) | Transaction result callback |

## Details

### startTransaction

| Prototype    | Prototype int startTransaction(android.os.Bundle bundle, IEmvListener callback) |
| ------------ | --- |
| Function     | Function Start EMV transaction |
| Parameters   | Parameters bundle: Transaction parameters. For details, refer to ConstantEmv.POIEmvCoreManager.EmvTransDataConstraints. callback: EMV process callback. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### stopTransaction

| Prototype    | Prototype int stopTransaction() |
| ------------ | --- |
| Function     | Function Stop EMV transaction |
| Parameters   | Parameters None |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### setKernel

| Prototype    | Prototype int setKernel(byte[] tlv) |
| ------------ | --- |
| Function     | Function Set EMV Tag/Object parameters |
| Parameters   | Parameters tlv: TAG in TLV format. Example: HexUtil.parseHex("9F02060000000000119F0306000000000011"). |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes After setting, this method is only used to change TAG values during the EMV transaction process. The set TAG values cannot be retrieved using getKernel. |

### getKernel

| Prototype    | Prototype byte[] getKernel(String[] tags) |
| ------------ | --- |
| Function     | Function Retrieve EMV Tag/Object parameters |
| Parameters   | Parameters tags: Array of TAGs. Example: new String[]{"4F", "50", "87", "9F12"}. |
| Return Value | Return value TAG values in TLV format. |
| Notes        | Notes  |

### setSelectApplicationResponse

| Prototype    | Prototype int setSelectApplicationResponse(int position) |
| ------------ | --- |
| Function     | Function Set the result of multiple application selection |
| Parameters   | Parameters position: The selected position in the multiple application selection callback data. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### setCardInfoResponse

| Prototype    | Prototype int setCardInfoResponse(android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Set card information confirmation result |
| Parameters   | Parameters bundle - parameter value For details, see ConstantEmv.POIEmvCoreManager.EmvCardInfoConstraints |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### setPinResponse

| Prototype    | Prototype int setPinResponse(android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Set Pin input result |
| Parameters   | Parameters bundle - parameter value For details, see ConstantEmv.POIEmvCoreManager.EmvPinConstraints |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### setOnlineResponse

| Prototype    | Prototype int setOnlineResponse(android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Set the online result |
| Parameters   | Parameters bundle - parameter value For details, see ConstantEmv.POIEmvCoreManager.EmvOnlineConstraints |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### onConfirmCardInfo (card info)

| Prototype    | void onConfirmCardInfo(int mode,  android.os.Bundle info) Callback for card information confirmation |
| ------------ | --- |
| Function     | void onEmvProcess(int type,  android.os.Bundle info) Callback when a card is detected |
| Parameters   | void onKernelType(int type) Callback for kernel card scheme type |
| Return Value | void onRequestInputPin(android.os.Bundle info) Callback to request PIN input |
| Notes        | void onRequestOnlineProcess(android.os.Bundle info) Callback to request online processing |

### onEmvProcess

| Prototype    | Prototype void onEmvProcess(int type,  android.os.Bundle info) |
| ------------ | --- |
| Function     | Function Detect card |
| Parameters   | Parameters Parameter: type: Card type. Enumerated values are as follows: ConstantEmv.POIEmvCoreManager.DEVICE_CONTACT ConstantEmv.POIEmvCoreManager.DEVICE_CONTACTLESS ConstantEmv.POIEmvCoreManager.DEVICE_MAGSTRIPE ConstantEmv.POIEmvCoreManager.DEVICE_MIFARE_CLASSIC ConstantEmv.POIEmvCoreManager.DEVICE_MIFARE_ULTRALIGHT ConstantEmv.POIEmvCoreManager.DEVICE_MIFARE_PLUS ConstantEmv.POIEmvCoreManager.DEVICE_MIFARE_DESFIRE info: Card information parameters.  |
| Return Value | Return value  |
| Notes        | Notes If the transaction card type is a magnetic stripe card,  the card data will be returned in this Bundle. For specific parameter constants, refer to  ConstantEmv.POIEmvCoreManager.EmvCardInfoConstraints. |

### onSelectApplication

| Prototype    | Prototype void onSelectApplication(List<String> appList,  boolean isFirstSelect) |
| ------------ | --- |
| Function     | Function Multiple application selection callback |
| Parameters   | Parameters Parameter: appList: Application selection list. isFirstSelect: Whether it is the first selection. |
| Return Value | Return value  |
| Notes        | Notes  |

### onConfirmCardInfo

| Prototype    | Prototype void onConfirmCardInfo(int mode,  android.os.Bundle info) |
| ------------ | --- |
| Function     | Function Card information confirmation callback |
| Parameters   | Parameters Parameter: mode: Current mode. Enumerated values are as follows: ConstantEmv.POIEmvCoreManager.CMD_TRY_OTHER_APPLICATION ConstantEmv.POIEmvCoreManager.CMD_AMOUNT_CONFIG ConstantEmv.POIEmvCoreManager.CMD_ISSUER_REFERRAL ConstantEmv.POIEmvCoreManager.CMD_GPO_FILTER ConstantEmv.POIEmvCoreManager.CMD_READ_RECORD_FILTER ConstantEmv.POIEmvCoreManager.CMD_SELECT_APPLICATION ConstantEmv.POIEmvCoreManager.CMD_READ_RECORD ConstantEmv.POIEmvCoreManager.CMD_GAC1 ConstantEmv.POIEmvCoreManager.CMD_GAC2 ConstantEmv.POIEmvCoreManager.CMD_SELECT_KERNEL ConstantEmv.POIEmvCoreManager.CMD_SELECT_AFTER ConstantEmv.POIEmvCoreManager.CMD_GPO_BEFORE ConstantEmv.POIEmvCoreManager.CMD_CARD_READ_SUCCESS  info: Card information data. For specific parameter constants, refer to ConstantEmv.POIEmvCoreManager.EmvCardInfoConstraints. |
| Return Value | Return value  |
| Notes        | Notes  |

### onKernelType

| Prototype    | Prototype void onKernelType(int type) |
| ------------ | --- |
| Function     | Function Kernel card scheme type callback |
| Parameters   | Parameters Parameter: type: Kernel card scheme type. Enumerated values are as follows: ConstantEmv.POIEmvCoreManager.EMV_CARD_NOT ConstantEmv.POIEmvCoreManager.EMV_CARD_VISA ConstantEmv.POIEmvCoreManager.EMV_CARD_UNIONPAY ConstantEmv.POIEmvCoreManager.EMV_CARD_MASTERCARD ConstantEmv.POIEmvCoreManager.EMV_CARD_DISCOVER ConstantEmv.POIEmvCoreManager.EMV_CARD_AMEX ConstantEmv.POIEmvCoreManager.EMV_CARD_JCB ConstantEmv.POIEmvCoreManager.EMV_CARD_MIR ConstantEmv.POIEmvCoreManager.EMV_CARD_RUPAY ConstantEmv.POIEmvCoreManager.EMV_CARD_PURE ConstantEmv.POIEmvCoreManager.EMV_CARD_INTERAC ConstantEmv.POIEmvCoreManager.EMV_CARD_EFTPOS |
| Return Value | Return value  |
| Notes        | Notes 1. This parameter is only returned for contactless card types. 2. For contact transactions and magnetic stripe transactions, this parameter will not be returned. |

### onSecondTapCard

| Prototype    | Prototype void onSecondTapCard() |
| ------------ | --- |
| Function     | Function Second tap card callback |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Note  |

### onRequestInputPin

| Prototype    | Prototype void onRequestInputPin(android.os.Bundle info) |
| ------------ | --- |
| Function     | Function Request PIN input callback |
| Parameters   | Parameters Parameter: info: PIN parameters.  For details, refer to ConstantEmv.POIEmvCoreManager.EmvPinConstraints. |
| Return Value | Return value  |
| Notes        | Notes  |

### onRequestOnlineProcess

| Prototype    | Prototype void onRequestOnlineProcess(android.os.Bundle info) |
| ------------ | --- |
| Function     | Function Request online process callback |
| Parameters   | Parameters Parameter: info: Online parameters.  For details, refer to ConstantEmv.POIEmvCoreManager.EmvOnlineConstraints. |
| Return Value | Return value  |
| Notes        | Notes  |

### onTransactionResult

| Prototype    | Prototype void onTransactionResult(int resultCode,  android.os.Bundle info) |
| ------------ | --- |
| Function     | Function Transaction result callback |
| Parameters   | Parameters Parameter: resultCode: Transaction result code. 0: Success Others: Failure.  Refer to ConstantEmv.PosEmvErrorCode/EmvError. info: Transaction data.  For details, refer to ConstantEmv.POIEmvCoreManager.EmvResultConstraints. |
| Return Value | Return value  |
| Notes        | Notes  |

## Notes

This page is split from kozen-financial-emv and covers only the functions listed above. See related pages for complementary EMV APIs and entity constants.

## Related Links

- [[kozen-financial-emv-1]]
- [[kozen-financial-entities-1]]
- [[kozen-financial-entities-2]]
- [[kozen-financial-entities-3]]
- [[kozen-financial-overview]]
- [[kozen-financial-init]]
