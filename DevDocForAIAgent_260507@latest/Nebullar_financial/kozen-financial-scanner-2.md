---
title: "kozen-financial-scanner-2"
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
summary: "Defines Kozen Financial SDK scanner camera module 3.10 APIs for camera-based scanning, preview initialization, barcode decoding, light and autofocus control, zoom, bitmap decoding, and camera scanner callbacks."
related:
  - "kozen-financial-scanner-1"
  - "kozen-financial-entities-5"
  - "kozen-financial-overview"
---

## Overview

Defines Kozen Financial SDK scanner camera module 3.10 APIs for camera-based scanning, preview initialization, barcode decoding, light and autofocus control, zoom, bitmap decoding, and camera scanner callbacks.

## Function List

| Function Name | Description |
|--            |-----------|
| void open(IConnectionStatusListener callback) | Open the scanner module |
| void open(ConstantScanner.ScannerCameraType cameraType,  IConnectionStatusListener callback) | Open the scanner module with a specific camera |
| void close() | Close the scanner module |
| int registerResultCallback(IScannerResultCallback callback) | Register a scanner result callback |
| int startScan() | Start scanning |
| int stopScan() | Stop scanning |
| int setBarcodeEnable(List<ConstantScanner.BarcodeFormat> types,  boolean enable) | Enable or disable specific barcode types |
| int setBarcodeEnable(boolean enable) | Enable or disable all barcode types |
| boolean isBarcodeEnabled(ConstantScanner.BarcodeFormat type) | Check if a barcode type is enabled |
| int switchLight() | Toggle the flashlight |
| void setAFModeEnable(boolean open,  int fixDistanceCM) | Enable or disable auto-focus (AF) mode and set fixed focus distance |
| int startScan(android.graphics.SurfaceTexture surface,  ICamScanInitStatusListener listener) | Start camera scan and preview rendering to a SurfaceTexture |
| int startDecoding() | Trigger the decode action |
| int stopDecoding() | Stop the decode action (camera and preview remain active) |
| int decodeWithBitmap(android.graphics.Bitmap bitmap) | Decode an image |
| int setZoom(float zoomScale) | Set zoom scale |
| IScannerResultCallback | IScannerResultCallback |
| void onResult(String sym,  String barcode) | Receive scan result and symbology type |
| IConnectionStatusListener | IConnectionStatusListener |
| void onConnected() | Called when the connection to the scanner service is established |
| void onError(int error,  String msg) | Called when the connection to the scanner service fails |
| void onDisconnected() | Called when the connection to the scanner service is lost |
| ICamScanInitStatusListener | ICamScanInitStatusListener |
| void updatePreviewSize(int previewWidth,  int previewHeight) | Preview size change callback |
| void onInitSuccess() | Initialization success callback |
| void onInitFailed(int errCode) | Initialization failure callback |

## Details

### open (with listener)

| Prototype    | Prototype void open(IConnectionStatusListener callback) |
| ------------ | --- |
| Function     | Function Open the scanner module |
| Parameters   | Parameters Parameters: callback - Connection status callback |
| Return Value | Return Value  |
| Notes        | Notes Initializes the scanner module. Other scanner interfaces should only be used after a successful initialization. |



### open (with camera)

| Prototype    | Prototype void open(ConstantScanner.ScannerCameraType cameraType,  IConnectionStatusListener callback) |
| ------------ | --- |
| Function     | Function Open the scanner module with a specific camera |
| Parameters   | Parameters Parameters: cameraType - Camera type for scanning: CAMERA_REAR,  2. CAMERA_FRONT,  3. SCANNER callback - Connection status callback |
| Return Value | Return Value  |
| Notes        | Notes Initializes the scanner with the selected camera. Other interfaces should only be used after successful initialization. |



### close

| Prototype    | Prototype void close() |
| ------------ | --- |
| Function     | Function Close the scanner module |
| Parameters   | Parameters  |
| Return Value | Return Value  |
| Notes        | Notes Unbinds from the scanner service and releases related resources. |



### registerResultCallback

| Prototype    | Prototype int registerResultCallback(IScannerResultCallback callback) |
| ------------ | --- |
| Function     | Function Register a scanner result callback |
| Parameters   | Parameters Parameters: callback - Callback for scan results including type and data |
| Return Value | Return Value Return: 0 - Success;  Others - Failure. See ScannerError and CommonError for details |
| Notes        | Notes Must be called after open() is successfully executed. |



### startScan

| Prototype    | Prototype int startScan() |
| ------------ | --- |
| Function     | Function Start scanning |
| Parameters   | Parameters  |
| Return Value | Return Value Return:0 - Success;  Others - Failure. See ScannerError and CommonError for details |
| Notes        | Notes Triggers a scan. Must be called after open() is successfully executed. |



### stopScan

| Prototype    | Prototype int stopScan() |
| ------------ | --- |
| Function     | Function Stop scanning |
| Parameters   | Parameters  |
| Return Value | Return Value Return:0 - Success;  Others - Failure. See ScannerError and CommonError for details |
| Notes        | Notes Stops the current scan. Must be called after open() is successfully executed. |



### setBarcodeEnable (multi)

| Prototype    | Prototype int setBarcodeEnable(List<ConstantScanner.BarcodeFormat> types,  boolean enable) |
| ------------ | --- |
| Function     | Function Enable or disable specific barcode types |
| Parameters   | Parameters Parameters: types - List of barcode formats to enable/disable enable - true to enable, false to disable |
| Return Value | Return Value Return: 0 - Success;  Others - Failure. See ScannerError and CommonError for details |
| Notes        | Notes Must be called after open() is successfully executed. |



### setBarcodeEnable (all)

| Prototype    | Prototype int setBarcodeEnable(boolean enable) |
| ------------ | --- |
| Function     | Function Enable or disable all barcode types |
| Parameters   | Parameters Parameters: Enable - true to enable all types; false to disable all types |
| Return Value | Return Value Return: 0 - Success;  Others - Failure. See ScannerError and CommonError for details |
| Notes        | Notes Enable or disable all supported code types. This method must be called after a successful open(). |



### isBarcodeEnabled

| Prototype    | Prototype boolean isBarcodeEnabled(ConstantScanner.BarcodeFormat type) |
| ------------ | --- |
| Function     | Function Check if a barcode type is enabled |
| Parameters   | Parameters Parameters: type - The barcode format to check |
| Return Value | Return Value Return: true to enabled; false to disabled or SDK error |
| Notes        | Notes Must be called after open() is successfully executed. |



### switchLight

| Prototype    | Prototype int switchLight() |
| ------------ | --- |
| Function     | Function Toggle the flashlight |
| Parameters   | Parameters  |
| Return Value | Return Value Return: 0 - Success;  Others - Failure. See ScannerError and CommonError for details |
| Notes        | Notes Requires hardware support; Not supported by SCANNER Must be called after open() is successfully executed. |



### setAFModeEnable

| Prototype    | Prototype void setAFModeEnable(boolean open,  int fixDistanceCM) |
| ------------ | --- |
| Function     | Function Enable or disable auto-focus (AF) mode and set fixed focus distance |
| Parameters   | Parameters Parameters: open -  true: Enable AF mode;  false: Disable AF and use fixed  focusfixDistanceCM -  Fixed focus distance in cm. Must be ≥ 0 0 means use the minimum supported focus distance. |
| Return Value | Return Value  |
| Notes        | Notes Applicable only if the hardware supports AF mode.  When disabled, default focus is ~15cm (hardware-dependent). |



### startScan (surface)

| Prototype    | Prototype int startScan(android.graphics.SurfaceTexture surface,  ICamScanInitStatusListener listener) |
| ------------ | --- |
| Function     | Function Start camera scan and preview rendering to a SurfaceTexture |
| Parameters   | Parameters Parameters: surface -  Target SurfaceTexture for preview listener - Initialization status callback for camera and decoder |
| Return Value | Return Value Return: 0 - Success Others - Failure (see ScannerError / CommonError) |
| Notes        | Notes Must be called after a successful camera open operation. |



### startDecoding

| Prototype    | Prototype int startDecoding() |
| ------------ | --- |
| Function     | Function Trigger the decode action |
| Parameters   | Parameters  |
| Return Value | Return Value Return: 0 - Success Others - Failure (see ScannerError / CommonError) |
| Notes        | Notes Only effective after successful startScan(...) initialization. |



### stopDecoding

| Prototype    | Prototype int stopDecoding() |
| ------------ | --- |
| Function     | Function Stop the decode action (camera and preview remain active) |
| Parameters   | Parameters  |
| Return Value | Return Value Return: 0 - Success Others - Failure (see ScannerError / CommonError) |
| Notes        | Notes Only effective after successful startScan(...) initialization. |



### decodeWithBitmap

| Prototype    | Prototype int decodeWithBitmap(android.graphics.Bitmap bitmap) |
| ------------ | --- |
| Function     | Function Decode an image |
| Parameters   | Parameters Parameter: bitmap - Image to be decoded. Recommended resolution: 960px × 540px to 1920px × 1080px. Image size should not exceed 20 MB. |
| Return Value | Return Value Return: 0 - Operation succeeded Others - Operation failed (see ScannerError and CommonError) |
| Notes        | Notes  |



### setZoom

| Prototype    | Prototype int setZoom(float zoomScale) |
| ------------ | --- |
| Function     | Function Set zoom scale |
| Parameters   | Parameters Parameter: zoomScale - Zoom factor (must be a float ≥ 1.0) |
| Return Value | Return Value Return: 0 - Operation succeeded Others - Operation failed (see ScannerError and CommonError) |
| Notes        | Notes  |



### IScannerResultCallback



### onResult

| Prototype    | Prototype void onResult(String sym,  String barcode) |
| ------------ | --- |
| Function     | Function Receive scan result and symbology type |
| Parameters   | Parameters Parameters: sym - Barcode symbology type barcode - Scanned barcode result |
| Return Value | Return Value  |
| Notes        | Notes This method is triggered upon a successful scan, returning the barcode data and type. |



### IConnectionStatusListener



### onConnected

| Prototype    | Prototype void onConnected() |
| ------------ | --- |
| Function     | Function Called when the connection to the scanner service is established |
| Parameters   | Parameters  |
| Return Value | Return Value  |
| Notes        | Notes Indicates that the scanner module has been successfully initialized. |



### onError

| Prototype    | Prototype void onError(int error,  String msg) |
| ------------ | --- |
| Function     | Function Called when the connection to the scanner service fails |
| Parameters   | Parameters Parameters: error - Error code. See ScannerError and CommonError for definitions msg - Error description |
| Return Value | Return Value  |
| Notes        | Notes Triggered upon failure to establish a connection with the scanner service. |



### onDisconnected

| Prototype    | Prototype void onDisconnected() |
| ------------ | --- |
| Function     | Function Called when the connection to the scanner service is lost |
| Parameters   | Parameters  |
| Return Value | Return Value  |
| Notes        | Notes Indicates that the scanner service is no longer connected. |



### ICamScanInitStatusListener



### updatePreviewSize

| Prototype    | Prototype void updatePreviewSize(int previewWidth,  int previewHeight) |
| ------------ | --- |
| Function     | Function Preview size change callback |
| Parameters   | Parameters Parameter: previewWidth - Preview width previewHeight - Preview height |
| Return Value | Return Value  |
| Notes        | Notes Adjust the preview UI size and aspect ratio when the preview size changes. |



### onInitSuccess

| Prototype    | Prototype void onInitSuccess() |
| ------------ | --- |
| Function     | Function Initialization success callback |
| Parameters   | Parameters  |
| Return Value | Return Value  |
| Notes        | Notes  |



### onInitFailed

| Prototype    | Prototype void onInitFailed(int errCode) |
| ------------ | --- |
| Function     | Function Initialization failure callback |
| Parameters   | Parameters errCode - Failure error code. See ScannerError for details |
| Return Value | Return Value  |
| Notes        | Notes  |

## Notes

This page covers Scanner Module (3.10 — Camera). See related scanner pages for complementary scanner APIs.

## Related Links

- [[kozen-financial-scanner-1]]
- [[kozen-financial-entities-5]]
- [[kozen-financial-overview]]
