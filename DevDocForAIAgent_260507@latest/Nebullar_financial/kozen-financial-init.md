---
title: "kozen-financial-init"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - init
summary: "Defines Kozen Financial SDK initialization APIs including init, deInit, getScannerManager, and InitListener callback."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-financial-overview"
  - "kozen-financial-scanner-1"
---

## Overview

SDK initialization API providing FinancialService instance creation and module manager access.

## Function List

| Function Name | Description |
|--            |-----------|
| void init(android.content.Context application,  InitListener callback) | Initialize the FinancialService instance |
| deInit | deInit |
| void onResult(int result,  String errorMsg) | Initialization results |
| void close() Close the scanner module. | boolean isBarcodeEnabled(ConstantScanner.BarcodeFormat type) Check whether a certain barcode type can be recognized. |
| void onResult(int result, String errorMsg) | Initialization results |

## Details
### init

| Prototype    | Prototype void init(android.content.Context application,  InitListener callback) |
| ------------ | --- |
| Function     | Function Initialize the FinancialService instance |
| Parameters   | Parameters Parameters: application - context callback - initialization callback |
| Return Value | Return value   |
| Notes        | Notes  |

### deInit

| void onResult(int result, String errorMsg) | Initialization results |
| --- | --- |

### getScannerManager

| Prototype    | Prototype void onResult(int result,  String errorMsg) |
| ------------ | --- |
| Function     | Function Initialization results |
| Parameters   | Parameters Parameters: result - initialization result  0: success  Others: failure - more details to see CommonError errorMsg - error message |
| Return Value | Return value  |
| Notes        | Notes  |

### getCardReaderManager

| Prototype    | void close() Close the scanner module. |
| ------------ | --- |
| Function     | boolean isBarcodeEnabled(ConstantScanner.BarcodeFormat type) Check whether a certain barcode type can be recognized. |
| Parameters   | void open(IConnectionStatusListener callback) Open the scanner module. |
| Return Value | int registerResultCallback(IScannerResultCallback callback) Register the callback listener for the barcode scanning result. |
| Notes        | int setBarcodeEnable(boolean enable) Enable/Disable all supported barcode types. |

### InitListener Callback

| Prototype    | void onResult(int result, String errorMsg) |
| ------------ | --- |
| Function     | Initialization results |
| Parameters   | result - 0 success/-1 failure; errorMsg - error details |
| Return Value | — |
| Notes        | — |

## Notes

- Initialize in Application class.
- result == 0 means success, -1 means failure.
- On service disconnect, reinitialize.
- Error code -10001 means service not connected - reinitialize.

## Related Links

- [[kozen-financial-overview]]
- [[kozen-financial-scanner-1]]
