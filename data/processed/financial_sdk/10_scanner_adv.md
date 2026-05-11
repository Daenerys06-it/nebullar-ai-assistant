 3.10 Scanner module ..............................................................................................................80
-- Get scanner module - getScannerManager -- ............................................................................. 80
3.10.1 Open the scanner module .................................................................................................... 80
3.10.2 Open the scanner module with a specific camera .....................................................................81
3.10.3 Close the scanner module .................................................................................................... 81
3.10.4 Register a scanner result callback .........................................................................................81
3.10.5 Start scanning .................................................................................................................... 81
3.10.6 Stop scanning .....................................................................................................................82

                                                                                         6
  3.10.8 Enable or disable all barcode types ....................................................................................... 82
  3.10.9 Check if a barcode type is enabled ........................................................................................ 82
  3.10.10 Toggle the flashlight ..........................................................................................................83
  3.10.11 Enable or disable auto-focus (AF) mode and set fixed focus distance ....................................... 83
  3.10.12 Start camera scan and preview rendering to a SurfaceTexture .................................................. 83
  3.10.13 Trigger the decode action ................................................................................................... 83
  3.10.14 Stop the decode action .......................................................................................................84
  3.10.15 Decode an image .............................................................................................................. 84
  3.10.16 Set zoom scale .................................................................................................................. 84
  -- Scanner result callback - ScannerResultCallback -- ................................................................... 84
  3.10.17 Receive scan result and symbology type ............................................................................... 84
  -- Connection Status Listener- IConnectionStatusListener-- ............................................................ 85
  3.10.18 Called when the connection to the scanner service is established ............................................. 85
  3.10.19 Called when the connection to the scanner service fails .......................................................... 85
  3.10.20 Called when the connection to the scanner service is lost ........................................................85
  -- ScanInit Status Listener- ICamScanInitStatusListener-- .............................................................. 86
  3.10.21 Preview size change callback ..............................................................................................86
  3.10.22 Initialization success callback ............................................................................................ 86
  3.10.23 Initialization failure callback ..............................................................................................86
 3.10 Scanner module

-- Get scanner module - getScannerManager --

void close()                                                     Close the scanner module
boolean isBarcodeEnabled(ConstantScanner.BarcodeFormat type)     Check whether a specific barcode format is
                                                                 enabled
void open(ConstantScanner.ScannerCameraType cameraType,          Open the scanner module with a specific
 IConnectionStatusListener callback)                             camera type
void open(IConnectionStatusListener callback)                    Open the scanner module
int registerResultCallback(IScannerResultCallback callback)      Register a callback to receive scan results
int setBarcodeEnable(boolean enable)                             Enable/disable all supported barcode formats
int setBarcodeEnable(List<ConstantScanner.BarcodeFormat> types,  Enable/disable specified barcode formats
 boolean enable)
int startScan()                                                  Start scanning
int stopScan()                                                   Stop scanning
int switchLight()                                                Toggle the fill light on or off
void setAFModeEnable(boolean open, int fixDistanceCM)            Enable or disable auto-focus mode, and set
                                                                 fixed focus distance (in cm) when disabled
int startScan(android.graphics.SurfaceTexture surface,           Start scanning with camera preview on the
ICamScanInitStatusListener listener)                             given surface
int startDecoding()                                              Trigger the decoding action for scanning
int stopDecoding()                                               Stop the decoding action without closing
                                                                 preview or camera
int decodeWithBitmap(android.graphics.Bitmap bitmap)             Image decoding
int setZoom(float zoomScale)                                     Set the scaling factor

3.10.1 Open the scanner module

Prototype     void open(IConnectionStatusListener callback)
Function      Open the scanner module

                                                80
              callback - Connection status callback
Return Value
Notes         Initializes the scanner module. Other scanner interfaces should only be used after a successful
              initialization.

3.10.2 Open the scanner module with a specific camera

Prototype     void open(ConstantScanner.ScannerCameraType cameraType,
Function      IConnectionStatusListener callback)
Parameters    Open the scanner module with a specific camera
              Parameters:
Return Value  cameraType - Camera type for scanning:
Notes         1. CAMERA_REAR,
              2. CAMERA_FRONT,
              3. SCANNER
              callback - Connection status callback

              Initializes the scanner with the selected camera. Other interfaces should only be used after
              successful initialization.

3.10.3 Close the scanner module

Prototype     void close()
Function      Close the scanner module
Parameters
Return Value  Unbinds from the scanner service and releases related resources.
Notes

3.10.4 Register a scanner result callback

Prototype     int registerResultCallback(IScannerResultCallback callback)
Function      Register a scanner result callback
Parameters    Parameters:
Return Value  callback - Callback for scan results including type and data
              Return:
Notes         0 - Success;
              Others - Failure. See ScannerError and CommonError for details
              Must be called after open() is successfully executed.

3.10.5 Start scanning

Prototype     int startScan()

Function      Start scanning

Parameters

Return Value  Return:0 - Success;

                                                       81
              Triggers a scan. Must be called after open() is successfully executed.

3.10.6 Stop scanning

Prototype     int stopScan()
Function      Stop scanning
Parameters
Return Value  Return:0 - Success;
              Others - Failure. See ScannerError and CommonError for details
Notes         Stops the current scan. Must be called after open() is successfully executed.

3.10.7 Enable or disable specific barcode types

Prototype     int setBarcodeEnable(List<ConstantScanner.BarcodeFormat> types,
Function      boolean enable)
Parameters    Enable or disable specific barcode types
              Parameters:
Return Value  types - List of barcode formats to enable/disable
              enable - true to enable, false to disable
Notes         Return:
              0 - Success;
              Others - Failure. See ScannerError and CommonError for details
              Must be called after open() is successfully executed.

3.10.8 Enable or disable all barcode types

Prototype     int setBarcodeEnable(boolean enable)
Function      Enable or disable all barcode types
Parameters    Parameters:
Return Value  Enable - true to enable all types; false to disable all types
              Return:
Notes         0 - Success;
              Others - Failure. See ScannerError and CommonError for details
              Enable or disable all supported code types. This method must be called after a successful open().

3.10.9 Check if a barcode type is enabled

Prototype     boolean isBarcodeEnabled(ConstantScanner.BarcodeFormat type)
Function      Check if a barcode type is enabled
Parameters    Parameters:
              type - The barcode format to check
Return Value  Return:
              true to enabled; false to disabled or SDK error
Notes         Must be called after open() is successfully executed.

                                                 82

Prototype     int switchLight()
Function      Toggle the flashlight
Parameters
Return Value  Return:
              0 - Success;
Notes         Others - Failure. See ScannerError and CommonError for details
              Requires hardware support; Not supported by SCANNER
              Must be called after open() is successfully executed.

3.10.11 Enable or disable auto-focus (AF) mode and set fixed focus distance

Prototype     void setAFModeEnable(boolean open,
Function      int fixDistanceCM)
Parameters    Enable or disable auto-focus (AF) mode and set fixed focus distance
              Parameters:
Return Value  open -
Notes         true: Enable AF mode;
              false: Disable AF and use fixed
              focusfixDistanceCM -
              Fixed focus distance in cm. Must be  0
              0 means use the minimum supported focus distance.

              Applicable only if the hardware supports AF mode.
              When disabled, default focus is ~15cm (hardware-dependent).

3.10.12 Start camera scan and preview rendering to a SurfaceTexture

Prototype     int startScan(android.graphics.SurfaceTexture surface,
Function      ICamScanInitStatusListener listener)
Parameters    Start camera scan and preview rendering to a SurfaceTexture
              Parameters:
Return Value  surface -
              Target SurfaceTexture for preview
Notes         listener - Initialization status callback for camera and decoder
              Return:
              0 - Success
              Others - Failure (see ScannerError / CommonError)
              Must be called after a successful camera open operation.

3.10.13 Trigger the decode action

Prototype     int startDecoding()

Function      Trigger the decode action

Parameters

                                         83
Notes         0 - Success
              Others - Failure (see ScannerError / CommonError)
              Only effective after successful startScan(...) initialization.

3.10.14 Stop the decode action

Prototype     int stopDecoding()
Function      Stop the decode action (camera and preview remain active)
Parameters
Return Value  Return:
              0 - Success
Notes         Others - Failure (see ScannerError / CommonError)
              Only effective after successful startScan(...) initialization.

3.10.15 Decode an image

Prototype     int decodeWithBitmap(android.graphics.Bitmap bitmap)
Function      Decode an image
Parameters    Parameter:
              bitmap - Image to be decoded. Recommended resolution: 960px × 540px to 1920px × 1080px.
Return Value  Image size should not exceed 20 MB.
              Return:
Notes         0 - Operation succeeded
              Others - Operation failed (see ScannerError and CommonError)

3.10.16 Set zoom scale

Prototype     int setZoom(float zoomScale)
Function      Set zoom scale
Parameters    Parameter:
Return Value  zoomScale - Zoom factor (must be a float  1.0)
              Return:
Notes         0 - Operation succeeded
              Others - Operation failed (see ScannerError and CommonError)

-- Scanner result callback - ScannerResultCallback --

void onResult(String sym,                                  Retrieve the scan result and the barcode
String barcode)                                            format

3.10.17 Receive scan result and symbology type

Prototype     void onResult(String sym,

                                                       84
              Receive scan result and symbology type
Parameters    Parameters:
              sym - Barcode symbology type
Return Value  barcode - Scanned barcode result
Notes
              This method is triggered upon a successful scan, returning the barcode data and type.

-- Connection Status Listener- IConnectionStatusListener--

void onConnected()       Called when the connection to the scanning service is established
void onDisconnected()    Called when the connection to the scanning service is lost
void onError(int error,  Called when the connection to the scanning service fails
String msg)

3.10.18 Called when the connection to the scanner service is established

Prototype     void onConnected()
Function      Called when the connection to the scanner service is established
Parameters
Return Value  Indicates that the scanner module has been successfully initialized.
Notes

3.10.19 Called when the connection to the scanner service fails

Prototype     void onError(int error,
Function      String msg)
              Called when the connection to the scanner service fails
Parameters    Parameters:
              error - Error code. See ScannerError and CommonError for definitions
Return Value  msg - Error description
Notes
              Triggered upon failure to establish a connection with the scanner service.

3.10.20 Called when the connection to the scanner service is lost

Prototype     void onDisconnected()
Function      Called when the connection to the scanner service is lost
Parameters
Return Value  Indicates that the scanner service is no longer connected.
Notes

                         85

void onInitFailed(int errCode)            Initialization failed
void onInitSuccess()                      Initialization successful
void updatePreviewSize(int previewWidth,  Callback triggered when the preview size changes;
int previewHeight)                        you can adjust the preview interface size and aspect ratio here.

3.10.21 Preview size change callback

Prototype     void updatePreviewSize(int previewWidth,
Function      int previewHeight)
Parameters    Preview size change callback
              Parameter:
Return Value  previewWidth - Preview width
Notes         previewHeight - Preview height

              Adjust the preview UI size and aspect ratio when the preview size changes.

3.10.22 Initialization success callback

Prototype     void onInitSuccess()
Function      Initialization success callback
Parameters
Return Value
Notes

3.10.23 Initialization failure callback

Prototype     void onInitFailed(int errCode)
Function      Initialization failure callback
Parameters    errCode - Failure error code. See ScannerError for details
Return Value
Notes

