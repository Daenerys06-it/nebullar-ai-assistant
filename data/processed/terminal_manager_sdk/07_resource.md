 3.7 Resource module                                                                                 Install or update an app
                                                                                                     Uninstall an app
-- Get resource module - getResourceManager--                                                        Update the resource package
int installOrUpdate(String path)                                                                     Update the device system version / MCU
int unInstall(String pkgName)                                                                        firmware version
int updateCustomRes(String path)
int updateOTA(String path)

                                                                                                 24
OnAppUpdateListener listener)
int updateCustomResWithListener(String path,                     Update the resource package with listener
OnUpdateCustomResListener listener)
int updateOTAWithListener(String path,                           Update the device system version / MCU
OnUpdateOTAListener listener)                                    firmware version with listener

3.7.1 Installs or updates an app

Prototype     int installOrUpdate(String path)
Function      Installs or updates an app.
Parameters    path - The path of the app installation package.
              Return:
Return value  0: Success
              Others: Failure (refer to ResourceError).
Notes

3.7.2 Uninstalls an app

Prototype     int unInstall(String pkgName)
Function      Uninstalls an app.
Parameters    pkgName - The package name of the app to uninstall.
              Return:
Return value  0: Success, Others: Failure (refer to ResourceError).

Notes

3.7.3 Updates the device system version or MCU firmware version

Prototype     int updateOTA(String path)
Function      Updates the device system version or MCU firmware version.
Parameters    path - The path of the update package (supports /storage/emulated/0/ or /sdcard/).
              - .zip: Recognized as a system version package.
Return value  - .bin: Recognized as an MCU firmware package.
Notes         Return:
              0: Package verification successful, starting upgrade.
              Others: Failure (refer to ResourceError).

3.7.4 Updates the resource package

Prototype     int updateCustomRes(String path)
Function      Updates the resource package.
Parameters    path - The path of the resource package.
              Return:
Return value  0: Package verification successful, starting resource update.
              Others: Failure (refer to ResourceError).

                                                                             25

3.7.5 Install or update an app with listner

Prototype     int installOrUpdateWithListener(String path,
Function      OnAppUpdateListener listener)
Parameters    Install or update an app with listner
              Parameters:
Return Value  path - Path to the app package (either a file URI string or absolute accessible file path)
              listener - Callback for app installation result (see OnAppUpdateListener)
Notes         Return:
              0 - API call successful
              Others - API call failed (see CommonError for details)

3.7.6 Update the resource package with listener

Prototype     int updateCustomResWithListener(String path,
Function      OnUpdateCustomResListener listener)
Parameters    Update the resource package with listener
              Parameters:
Return Value  path - Path to the resource package (either a file URI string or absolute accessible file path)
              listener - Callback for update result (see OnUpdateCustomResListener )
Notes         Return:
              0 - API call successful
              Others - API call failed (see CommonError for details)

3.7.7 Update the device system version / MCU firmware version with listener

Prototype     int updateOTAWithListener(String path,
Function      OnUpdateOTAListener listener)
Parameters    Update the device system version / MCU firmware version with listener
              Parameters:
Return Value  path - Path to the OTA package (either a file URI string or absolute accessible file path)
              listener - Callback for update result (see OnUpdateOTAListener )
Notes         Return:
              0 - API call successful
              Others - API call failed (see CommonError for details)

-- Upgrade listener - OnAppUpgradeListener--

void onError(String msg, int code)                   Upgrade error/failure
void onSuccess()                                     Upgrade successful

                                                 26

Prototype     void onError(String msg, int code)
Function      Upgrade failed
              msg - Error message
Parameters    code - Error code (refer to ResourceError)

Return value
Notes

3.7.9 Upgrade successful

Prototype     void onSuccess()
Function      Upgrade successful
Parameters
Return value
Notes

-- Upgrade listener - OnUpdateCustomResListener --

void onError(String msg, int code)                        Upgrade error/failure
void onSuccess(String resultPath)                         Upgrade successful

3.7.10 Upgrade error/failure                              Upgrade error/failure
                                                          Upgrade successful
Prototype     void onError(String msg, int code)          Callback for upgrade progress
Function      Upgrade failed
              msg - Error message
Parameters    code - Error code (refer to ResourceError)

Return value
Notes

3.7.11 Upgrade successful

Prototype     void onSuccess()
Function      Upgrade successful
Parameters
Return value
Notes

-- Upgrade listener - OnUpdateOTAListener --

void onError(String msg, int code)
void onSuccess()
void onUpdateInProgress(int percent)

                                                    27

Prototype     void onError(String msg, int code)
Function      Upgrade failed
              msg - Error message
Parameters    code - Error code (refer to ResourceError)

Return value
Notes

3.7.13 Upgrade successful

Prototype     void onSuccess()
Function      Upgrade successful
Parameters
Return value
Notes

3.7.14 Callback for upgrade progress

Prototype     void onUpdateInProgress(int percent)
Function      Firmware or application update progress callback
Parameters    Parameters:
              percent - Update progress percentage (0­100)
Return Value
Notes         This method is called to report the current progress of an ongoing update.

 3.8 Device Log module                                    Get the device logs directory path

-- Get device log module - getDeviceLogsManager--
String getDeviceLogsPath()

3.8.1 Get the device log file path

Prototype     String getDeviceLogsPath()
Function      Get the device log file path
Parameters
Return Value  Return:
              Log file path as a String
Notes         This method returns the file system path where device logs are stored

                                                   28

-- Get Certification module - getCertificationManager--

android.os.ParcelFileDescriptor collectPerceptionData()  Get perception data in file stream format
ArrayList<String> getBatteryCurrentMaxCapacity()         Get the current max capacity list of the main battery
ArrayList<String> getBatteryCycleCount()                 Get the cycle count list of the main battery
ArrayList<String> getBatteryDesignCapacity()             Get the factory design capacity list of the main battery
ArrayList<String> getBatteryHealthPercent()              Get the battery health percentage list
ArrayList<String> getBatteryHealthStatus()               Get the battery health status list
ArrayList<String> getPrintDistance()                     Get the print distance list
ArrayList<String> getSmallBatteryVoltage()               Get the small battery voltage list

3.9.1 Get perception data as a file stream

Prototype     android.os.ParcelFileDescriptor collectPerceptionData()
Function      Get perception data as a file stream
Parameters
Return Value  Return:
              File descriptor for perception data;
Notes         null if no data (file size < 2MB or not found)
              Returns a file descriptor containing buried point (analytics) data.

3.9.2 Get large battery cycle count list

Prototype     ArrayList<String> getBatteryCycleCount()
Function      Get large battery cycle count list
Parameters
Return Value  Return:
              List of cycle counts in the format: "yyyyMMdd,count" (e.g., "20250630,100")
Notes         Each item represents the total charge cycle count on a specific date.

3.9.3 Get large battery design capacity list

Prototype     ArrayList<String> getBatteryDesignCapacity()
Function      Get large battery design capacity list
Parameters
Return Value  Return:
              List in the format: "yyyyMMdd,capacity" (e.g., "20250630,2800")
Notes         Represents the designed capacity of the battery on a given date.

3.9.4 Get current max capacity of large battery

Prototype     ArrayList<String> getBatteryCurrentMaxCapacity()
Function      Get current max capacity of large battery

                                                                             29
Return Value  List in the format: "yyyyMMdd,capacity" (e.g., "20250630,2750")
              Indicates the actual current maximum charge capacity over time.
Notes

3.9.5 Get battery health percentage list

Prototype     ArrayList<String> getBatteryHealthPercent()
Function      Get battery health percentage list
Parameters
Return Value  Return:
              List in the format: "yyyyMMdd,healthPercent" (e.g., "20250630,100")
Notes         Battery health percentage over time.

3.9.6 Get battery health status list

Prototype     ArrayList<String> getBatteryHealthStatus()
Function      Get battery health status list
Parameters
Return Value  Return:
              List in the format: "yyyyMMdd,status" (e.g., "20250630,0")
Notes         Health status values may refer to different health categories

3.9.7 Get small battery voltage list

Prototype     ArrayList<String> getSmallBatteryVoltage()
Function      Get small battery voltage list
Parameters
Return Value  Return:
              List in the format: "yyyyMMdd,voltage" (e.g., "20250630,24")
Notes         Voltage data for the small/internal battery.

3.9.8 Get print distance history list

Prototype     ArrayList<String> getPrintDistance()
Function      Get print distance history list
Parameters
Return Value  Return:List in the format: "yyyyMMdd,distance" (e.g., "20250630,45000")
Notes         Represents cumulative printing distance (in meters) by date.

                                          30

4.1 CertificationError

Error Code                                    Error Description                           Error Value
CERTIFICATION_ERROR_INIT                      Certification manager service               -10000
                                              initialization exception
CERTIFICATION_ERR_PARA_ERROR                  Parameter exception                         -10001
CERTIFICATION_CERT_LIST_CHECK_FAIL_ERROR      Certificate chain validation exception      -10002
CERTIFICATION_OTHER_ERROR                     Other exceptions                            -19999

4.2 DeviceError

Error Code                                    Error Description                           Error Value
DEVICE_ERROR_INIT                             Device manager service initialization       -20000
                                              exception
DEVICE_OTHER_ERROR                            Other exceptions                            -20001
DEVICE_PARAMETERS_INVALID                     Invalid parameters                          -20002

4.3 LocationError

Error Code                                    Error Description                           Error Value
MANAGER_SERVICE_DISCONNECT                    Device management service is not            -30001
                                              connected, please initialize the device
ERROR_INIT                                    management service first.                   -30002
ERROR_POSITIONING_PROGRESS                    Positioning module is not open or           -30003
                                              initialized.
ERROR_UNKNOWN                                 Positioning is in progress. If positioning  -30004
ERROR_PARAMETERS_INVALID                      is in progress, repeated positioning is     -30005
ERROR_MISS_PERMISSIONS                        prohibited. Stop positioning first and      -30006
ERROR_CODE_INVALID_PARAMETER                  then restart it.                            -31001
ERROR_CODE_FAILURE_WIFI_INFO                  Unknown error.                              -31002
                                              Invalid parameters.
ERROR_CODE_FAILURE_LOCATION_PARAMETER         Missing location permissions.               -31003
                                              Some important parameters are empty.
ERROR_CODE_FAILURE_CONNECTION                 Positioning failed because the device       -31004
                                              only scanned a single WiFi, and the
                                              location information cannot be
                                              accurately calculated.
                                              The obtained request parameters are
                                              empty, possibly due to an exception
                                              during the process.
                                              Network connection exception.
                                              Detailed information can be obtained

                                          31
ERROR_CODE_FAILURE_LOCATION                                                                          AMapLocation.getLocationDetail().         -31006
ERROR_CODE_FAILURE_AUTH                                                                              XML parsing error.                        -31007
ERROR_CODE_UNKNOWN                                                                                   Positioning result error.                 -31008
ERROR_CODE_FAILURE_INIT                                                                              KEY error.                                -31009
ERROR_CODE_SERVICE_FAIL                                                                              Other errors.                             -31010
                                                                                                     Initialization exception.
ERROR_CODE_FAILURE_CELL                                                                              Positioning service startup failed.       -31011
                                                                                                     Please check if the service is
ERROR_CODE_FAILURE_LOCATION_PERMISSION                                                               configured and if the service tag in the  -31012
                                                                                                     manifest is placed inside the
ERROR_CODE_FAILURE_NOWIFIANDAP                                                                       application tag.                          -31013
                                                                                                     Incorrect base station information.
ERROR_CODE_FAILURE_NOENOUGHSATELLITES                                                                Please check if the SIM card is           -31014
ERROR_CODE_FAILURE_SIMULATION_LOCATION                                                               installed.                                -31015
ERROR_CODE_AIRPLANEMODE_WIFIOFF                                                                      Missing location permissions. Please      -31018
                                                                                                     check if location permissions are
ERROR_CODE_NOCGI_WIFIOFF                                                                             configured and enable location            -31019
                                                                                                     permissions in security software and
ERROR_CODE_FAILURE_COARSE_LOCATION                                                                   settings.                                 -31020
GEO_ERROR_CODE_INVALID_PARAMETER                                                                     Network positioning failed. Please        -32001
GEO_ERROR_CODE_FAILURE_CONNECTION                                                                    check if the device has a SIM card        -32004
GEO_ERROR_CODE_FAILURE_PARSER                                                                        inserted, mobile network is enabled, or   -32005
                                                                                                     the WiFi module is turned on.
GEO_ERROR_CODE_FAILURE_AUTH                                                                          Satellite positioning failed due to       -32007
GEO_ERROR_CODE_UNKNOWN                                                                               insufficient available satellites.        -32008
GEO_ERROR_NO_VALIDFENCE                                                                              The location may be simulated.            -32016
                                                                                                     Positioning failed. Airplane mode is on
                                                                                                 32  and the WiFi switch is off. Please turn
                                                                                                     off airplane mode or turn on the WiFi
                                                                                                     switch.
                                                                                                     Positioning failed. No SIM card
                                                                                                     detected and the WiFi switch is off.
                                                                                                     Please turn on the WiFi switch or
                                                                                                     insert a SIM card.
                                                                                                     Positioning failed due to an exception
                                                                                                     under coarse permissions.
                                                                                                     Parameter error.
                                                                                                     Network connection exception.
                                                                                                     Data parsing failed (possibly due to
                                                                                                     connecting to a network that requires
                                                                                                     login but not logged in).
                                                                                                     Authentication failed.
                                                                                                     Other unknown errors.
                                                                                                     No valid geofence available.
                                             not need to be added again. Applies
                                             when the geofence's customID is the
                                             same.

4.4 NetworkError

Error Code                                   Error Description                       Error Value
NETWORK_ERROR_INIT                           Network module initialization error     -40000
NETWORK_OTHER_ERROR                          Other exceptions                        -40001
NETWORK_PARAMETERS_INVALID                   Invalid parameters                      -40002

4.5 ResourceError

Error Code                                   Error Description                       Error Value
RESOURCE_ERROR_INIT                          Resource module initialization error    -50000
RESOURCE_OTHER_ERROR                         Other error                             -50001
RESOURCE_REGISTER_UPGRADE_LISTENER_ERROR     Failed to register MCU upgrade          -50002
                                             listener
RESOURCE_MCU_UPGRADE_FILE_PATH_ERROR         MCU upgrade file path error             -50003
RESOURCE_MCU_UPGRADE_FILE_ERROR              MCU upgrade file error                  -50004
RESOURCE_MCU_UPGRADE_ERROR                   MCU upgrade error                       -50005
RESOURCE_APP_UPGRADE_ERROR                   App upgrade error                       -50006
RESOURCE_APP_UPGRADE_ERROR_ABORTED           App upgrade error -- aborted            -50007
RESOURCE_APP_UPGRADE_ERROR_BLOCKED           App upgrade error -- blocked            -50008
RESOURCE_APP_UPGRADE_ERROR_CONFLICT          App upgrade error -- conflict           -50009
RESOURCE_APP_UPGRADE_ERROR_INCOMPATIBLE      App upgrade error -- incompatible       -50010
RESOURCE_APP_UPGRADE_ERROR_INVALID           App upgrade error -- invalid            -50011
RESOURCE_APP_UPGRADE_ERROR_STORAGE           App upgrade error -- storage error      -50012
RESOURCE_ERROR_INIT                          Resource module initialization error    -50000

