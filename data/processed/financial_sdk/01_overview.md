 2. Overview .............................................................................................................................. 12

  2.1 Introduction ........................................................................................................................... 12
  2.2 Android version and IDE version supported by the SDK ............................................................... 12
  2.3 Feature Introduction ................................................................................................................12
  2.3.1 Financial SDK Engine Module ............................................................................................... 12
  2.3.2 Cardreader Module ...............................................................................................................12
  2.3.3 EMV Module ....................................................................................................................... 12
  2.3.4. General Module .................................................................................................................. 12
  2.3.5. Pinpad Module ....................................................................................................................13
  2.3.6. Printer Module ....................................................................................................................13
  2.3.7. Scanner Module .................................................................................................................. 13
  2.3.8. Security Module .................................................................................................................. 13
  2.3.9. ECR Module .......................................................................................................................13
  2.4 Importing the Financial SDK .................................................................................................... 14
  2.5 Initializing the Financial SDK ...................................................................................................14
 3.1 Financial SDK initialization

3.1.1 Initialize the FinancialService instance

Prototype     void init(android.content.Context application,
Function       InitListener callback)
Parameters
              Initialize the FinancialService instance
Return value  Parameters:
Notes         application - context
              callback - initialization callback

-- FinancialService instance callback - InitListener --

void onResult(int result, String errorMsg)                       Initialization results

3.1.2 Initialization results

Prototype     void onResult(int result,
Function      String errorMsg)
Parameters    Initialization results
              Parameters:
Return value  result - initialization result
Notes
               0: success
              Others: failure - more details to see CommonError
              errorMsg - error message

                                                         16

-- Get scanner operation module - getScannerManager --

void close()                                                       Close the scanner module.
boolean isBarcodeEnabled(ConstantScanner.BarcodeFormat type)       Check whether a certain barcode type can be
                                                                   recognized.
void open(IConnectionStatusListener callback)                      Open the scanner module.
int registerResultCallback(IScannerResultCallback callback)        Register the callback listener for the barcode
                                                                   scanning result.
int setBarcodeEnable(boolean enable)                               Enable/Disable all supported barcode types.
int setBarcodeEnable(List<ConstantScanner.BarcodeFormat> types,    Enable/Disable specified barcode type to be
boolean enable)                                                    recognized.
int startScan()                                                    Trigger the barcode scanning action and start
                                                                   scanning.
int stopScan()                                                     Stop scanning.

3.2.1 Open the scanner module.

Prototype     void open(IConnectionStatusListener callback)
Function      Open the barcode scanning module
              Initialize the barcode scanning module. Only after successful called, other interfaces can be
Parameters    available.
Return value  Parameters:
Notes         callback - connection status callback

3.2.2 Close the scanner module

Prototype     void close()
Function      Close the barcode scanning module.
              When the barcode scanning module is no longer needed, use this interface to release the resources
Parameters
Return value
Notes

3.2.3 Register the callback listener for the code scanning result

Prototype     int registerResultCallback(IScannerResultCallback callback)
Function      Register the callback listener for the scan result. After successful scanning, the barcode type and
              scan result will be returned through this callback. It needs to be called after OPEN API.
Parameters    Parameters:
              callback - callback for scanning result
Return value  Return:
              0: The operation is successfully executed;

                                                                             17
                     For the specific meaning of the error code, please refer to the definitions in ScannerError and
                     CommonError

Notes

3.2.4 Trigger the barcode scanning action and start scanning

Prototype            int startScan()
Function             Trigger the barcode scanning action and start scanning. It needs to be called after OPEN API.
Parameters
Return value         Return:
                     0: The operation is successfully executed;
Notes                Others: The operation fails.
                     For the specific meaning of the error code, please refer to the definitions in ScannerError and
                     CommonError

3.2.5 Stop scanning

Prototype            int stopScan()
Function             Stop scanning. It needs to be called after OPEN API.
Parameters
Return value         Return:
                     0: The operation is successfully executed;
Notes                Others: The operation fails.
                     For the specific meaning of the error code, please refer to the definitions in ScannerError and
                     CommonError

3.2.6 Enable/Disable specified barcode type to be recognized

Prototype            int setBarcodeEnable(List<ConstantScanner.BarcodeFormat> types,
Function              boolean enable)
Parameters
Return value         Enable/disable support for the specified type of barcode. When support is enabled, the scanner
                     can recognize the barcode. Otherwise, it is disabled. This function needs to be called after the
Notes                OPEN API is called.
                     Parameters:
                     types - An array of ConstantScanner.BarcodeFormat enumeration types, used to specify the
                     barcode types to be enabled or disabled.
                     enable - true: enable support; false: disable support.
                     Return:
                     0: The operation is successfully executed;
                     Others: The operation fails.
                     For the specific meaning of the error code, please refer to the definitions in ScannerError and
                     CommonError

                                                                                    18

Prototype     int setBarcodeEnable(boolean enable)
Function      Enable/Disable all supported barcode types. This function needs to be called after the OPEN API
Parameters    is called.
Return value  Parameters:
              enable - true: Enable all code system support; false: Disable all code system support. The scan
Notes         button will light up at this time, but no barcode can be recognized
              Return:
              0: The operation is successfully executed;
              Others: The operation fails.
              For the specific meaning of the error code, please refer to the definitions in ScannerError and
              CommonError

3.2.8 Check whether a certain barcode type can be recognized.

Prototype     boolean isBarcodeEnabled(ConstantScanner.BarcodeFormat type)
Function      Check whether a certain barcode type can be recognized. This function needs to be called after the
Parameters    OPEN API is called.
Return value  Parameters:
              type - code type
Notes         Return:
              true: The scanner can recognize the barcode type; false: The scanner cannot recognize the barcode
              type. Please note that false will also be returned if the SDK status is abnormal.

-- Scanner connection status listener - IConnectionStatusListener --

void onConnected()                                 Monitoring barcode scanning service is connected
void onDisconnected()                              Monitoring barcode scanning service is disconnected
void onError(int error,                            Monitoring barcode scanning service error messages
String msg)

3.2.9 Monitoring barcode scanning service is connected

Prototype     void onConnected()
Function      Monitoring barcode scanning service is connected
Parameters
Return value  Will be called when a connection is established with the code scanning service, indicating that the
Notes         code scanning module has been initialized successfully

3.2.10 Monitoring barcode scanning service is disconnected

Prototype     void onDisconnected()

                                                        19
Parameters    Will be called when the connection with the code scanning service is lost
Return value
Notes

3.2.11 Monitoring barcode scanning service error messages

Prototype     void onError(int error,
Function      String msg)
Parameters    Monitoring barcode scanning service error messages
              Parameters:
Return value  error - error code. For the specific meaning of the error code, please refer to the definitions in the
Notes         ScannerError and CommonError
              msg - error description

-- Scanner Result Callback - IScannerResultCallback --

void onResult(String sym, String barcode)                      Get the scan result and code type

3.2.12 Get the scan result and code type

Prototype     void onResult(String sym, String barcode)
Function      Get the scan result and code type
Parameters    Parameters:
              sym - code type
Return value  barcode - scan result
Notes

