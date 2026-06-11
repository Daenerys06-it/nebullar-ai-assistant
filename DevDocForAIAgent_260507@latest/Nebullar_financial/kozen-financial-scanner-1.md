---
title: "kozen-financial-scanner-1"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - scanner
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines Kozen Financial SDK scanner module 3.2 APIs for opening and closing the scanner, registering result callbacks, starting and stopping scans, barcode enablement, and scanner connection/result callbacks."
related:
  - "kozen-financial-scanner-2"
  - "kozen-financial-entities-5"
  - "kozen-financial-overview"
---

## Overview

Defines Kozen Financial SDK scanner module 3.2 APIs for opening and closing the scanner, registering result callbacks, starting and stopping scans, barcode enablement, and scanner connection/result callbacks.

## Function List

| Function Name | Description |
|--            |-----------|
| void open(IConnectionStatusListener callback) | Open the barcode scanning module Initialize the barcode scanning module. Only after successful called, other interfaces can be available. |
| void close() | Close the barcode scanning module. When the barcode scanning module is no longer needed, use this interface to release the resources |
| int registerResultCallback(IScannerResultCallback callback) | Register the callback listener for the scan result. After successful scanning, the barcode type and scan result will be returned through this callback. It needs to be called after OPEN API. |
| int startScan() | Trigger the barcode scanning action and start scanning. It needs to be called after OPEN API. |
| int stopScan() | Stop scanning. It needs to be called after OPEN API. |
| int setBarcodeEnable(List<ConstantScanner.BarcodeFormat> types,  boolean enable) | Enable/disable support for the specified type of barcode. When support is enabled, the scanner can recognize the barcode. Otherwise, it is disabled. This function needs to be called after the OPEN API is called. |
| int setBarcodeEnable(boolean enable) | Enable/Disable all supported barcode types. This function needs to be called after the OPEN API is called. |
| boolean isBarcodeEnabled(ConstantScanner.BarcodeFormat type) | Check whether a certain barcode type can be recognized. This function needs to be called after the OPEN API is called. |
| IConnectionStatusListener | IConnectionStatusListener |
| void onConnected() | Monitoring barcode scanning service is connected |
| void onDisconnected() | Monitoring barcode scanning service is disconnected |
| void onError(int error,  String msg) | Monitoring barcode scanning service error messages |
| IScannerResultCallback | IScannerResultCallback |
| void onResult(String sym, String barcode) | Get the scan result and code type |

## Details

### open

| Prototype    | Prototype void open(IConnectionStatusListener callback) |
| ------------ | --- |
| Function     | Function Open the barcode scanning module Initialize the barcode scanning module. Only after successful called, other interfaces can be available. |
| Parameters   | Parameters Parameters: callback - connection status callback |
| Return Value | Return value  |
| Notes        | Notes  |



### close

| Prototype    | Prototype void close() |
| ------------ | --- |
| Function     | Function Close the barcode scanning module. When the barcode scanning module is no longer needed, use this interface to release the resources |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes  |



### registerResultCallback

| Prototype    | Prototype int registerResultCallback(IScannerResultCallback callback) |
| ------------ | --- |
| Function     | Function Register the callback listener for the scan result. After successful scanning, the barcode type and scan result will be returned through this callback. It needs to be called after OPEN API. |
| Parameters   | Parameters Parameters: callback - callback for scanning result |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in ScannerError and CommonError |
| Notes        | Notes  |



### startScan

| Prototype    | Prototype int startScan() |
| ------------ | --- |
| Function     | Function Trigger the barcode scanning action and start scanning. It needs to be called after OPEN API. |
| Parameters   | Parameters  |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in ScannerError and CommonError |
| Notes        | Notes  |



### stopScan

| Prototype    | Prototype int stopScan() |
| ------------ | --- |
| Function     | Function Stop scanning. It needs to be called after OPEN API. |
| Parameters   | Parameters  |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in ScannerError and CommonError |
| Notes        | Notes  |



### setBarcodeEnable (multi)

| Prototype    | Prototype int setBarcodeEnable(List<ConstantScanner.BarcodeFormat> types,  boolean enable) |
| ------------ | --- |
| Function     | Function Enable/disable support for the specified type of barcode. When support is enabled, the scanner can recognize the barcode. Otherwise, it is disabled. This function needs to be called after the OPEN API is called. |
| Parameters   | Parameters Parameters: types - An array of ConstantScanner.BarcodeFormat enumeration types, used to specify the barcode types to be enabled or disabled. enable - true: enable support; false: disable support. |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in ScannerError and CommonError |
| Notes        | Notes  |



### setBarcodeEnable (all)

| Prototype    | Prototype int setBarcodeEnable(boolean enable) |
| ------------ | --- |
| Function     | Function Enable/Disable all supported barcode types. This function needs to be called after the OPEN API is called. |
| Parameters   | Parameters Parameters: enable - true: Enable all code system support; false: Disable all code system support. The scan button will light up at this time, but no barcode can be recognized |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in ScannerError and CommonError |
| Notes        | Notes  |



### isBarcodeEnabled

| Prototype    | Prototype boolean isBarcodeEnabled(ConstantScanner.BarcodeFormat type) |
| ------------ | --- |
| Function     | Function Check whether a certain barcode type can be recognized. This function needs to be called after the OPEN API is called. |
| Parameters   | Parameters Parameters: type - code type |
| Return Value | Return value Return: true: The scanner can recognize the barcode type; false: The scanner cannot recognize the barcode type. Please note that false will also be returned if the SDK status is abnormal. |
| Notes        | Notes  |



### IConnectionStatusListener



### onConnected

| Prototype    | Prototype void onConnected() |
| ------------ | --- |
| Function     | Function Monitoring barcode scanning service is connected |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes Will be called when a connection is established with the code scanning service, indicating that the code scanning module has been initialized successfully |



### onDisconnected

| Prototype    | Prototype void onDisconnected() |
| ------------ | --- |
| Function     | Function Monitoring barcode scanning service is disconnected |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes Will be called when the connection with the code scanning service is lost |



### onError

| Prototype    | Prototype void onError(int error,  String msg) |
| ------------ | --- |
| Function     | Function Monitoring barcode scanning service error messages |
| Parameters   | Parameters Parameters: error - error code. For the specific meaning of the error code, please refer to the definitions in the ScannerError and CommonError msg - error description |
| Return Value | Return value  |
| Notes        | Notes  |



### IScannerResultCallback



### onResult

| Prototype    | Prototype void onResult(String sym, String barcode) |
| ------------ | --- |
| Function     | Function Get the scan result and code type |
| Parameters   | Parameters Parameters: sym - code type barcode - scan result |
| Return Value | Return value  |
| Notes        | Notes  |

## Notes

This page covers Scanner Module (3.2). See related scanner pages for complementary scanner APIs.

## Related Links

- [[kozen-financial-scanner-2]]
- [[kozen-financial-entities-5]]
- [[kozen-financial-overview]]
