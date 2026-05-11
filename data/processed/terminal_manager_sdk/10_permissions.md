 6. Access permission ................................................................................................................. 35

                                                                                             5

Version  Release     Modify Record                                  Adapted SDK version           Author
1.4      2026/04/22   Adjust wakeupType to add support for          TerminalManagerService 1.3.x  Johnny
1.3      2026/01/30                                                 TerminalManagerService 1.2.x
                           double tap to wake and lift to wake                                    Johnny
1.2      2025/09/18   Add an information collection module.         TerminalManagerService 1.1.x
                      Add support for returning OTA upgrade                                       Johnny
1.1      2025/03/31                                                 TerminalManagerService 1.0.x
                           progress monitoring callbacks.                                         Yue.Cui
                      Add a main screen brightness timeout                                        Tong.Liu
                                                                                                  Johnny
                           duration.                                                              Yao.zhang
                      Add a screen-off reminder setting.                                          Sunan
                      Add log retrieval.                                                          Johnny
                      Adjust compatibility for retrieving the                                     Johnny

                           OS version number.
                      Adjust the SDK icon
                      Add forcePermission API for mandatory

                           permission check
                      Add silentInstall API for silent

                           installation
                      Add CSN API
                      Add TUSN reading
                      Extend getLocationManager with 2 open

                           interfaces to specify location provider
                      Add application install API with listener
                      Add OTA install API with compatibility

                           support
                      Add resource install API with listener
                      Add module permission
                      Add a security statement for location
                      Positioning module constants

                           supplement;
                      Enhance the resource module with

                           extended error codes and implement

                           upgrade listener for the MCU

1.0      2025/03/19  Version verification and release               TerminalManagerService 1.0.x

0.2      2025/03/15   Update LocationManager module, add            TerminalManagerService 1.0.x

                     LocationError

0.1      2025/03/14  Initial version                                TerminalManagerService 1.0.x Johnny

                                      6

2.1 Introduction

      This document is interfaces for TMS and AppStore clients, with broader OS operation permissions compared to
the Financial SDK. Main functionalities include installing/uninstalling apps on the OS, retrieving system information,
location data, consumable status, and performing operations such as shutting down or rebooting the OS. After client
integration, the cloud can be used to manage applications and information on terminals in bulk.

      This document serves as the KozenTerminalManagerService API Reference.

2.2 Android version and IDE version supported by the SDK

System environment        Platform      Compile environment
Android 6.0 and above     ARM 64ARM 32  Android Studio, Intellij

2.3 Feature Introduction

2.3.1 Terminal Management Module

 This class handles SDK initialization and provides access to operation classes for each module.
 The operation class object is: TerminalManager.

2.3.2 Certificate Management Module

 This module provides certificate management functionalities.
 The operation class object is: ICertificationManager.
 Example to obtain the operation class:
JAVA: TerminalManager.INSTANCE.getCertificationManager()
Kotlin: TerminalManager.certificationManager()

2.3.3 Device Management Module

 This module handles device-related functionalities.
 The operation class object is: IDeviceManager.
 Example to obtain the operation class:
JAVA: TerminalManager.INSTANCE.getDeviceManager()
Kotlin: TerminalManager.deviceManager()

2.3.4 Device Information Management Module

 This module provides functionalities for retrieving device information.
 The operation class object is: IDeviceInfoManager.
 Example to obtain the operation class:

                                                                                                  7
Kotlin: TerminalManager.deviceInfoManager()
2.3.5 Location Management Module
 This module handles location-related functionalities.
 The operation class object is: ILocationManager.
 Example to obtain the operation class:
JAVA: TerminalManager.INSTANCE.getLocationManager()
Kotlin: TerminalManager.locationManager()
2.3.6 Network Management Module
 This module handles network-related functionalities.
 The operation class object is: INetworkManager.
 Example to obtain the operation class:
JAVA: TerminalManager.INSTANCE.getNetworkManager()
Kotlin: TerminalManager.networkManager()
2.3.7 Resource Management Module
 This module handles resource management functionalities.
 The operation class object is: IResourceManager.
 Example to obtain the operation class:
JAVA: TerminalManager.INSTANCE.getResourceManager()
Kotlin: TerminalManager.resourceManager()

2.4 Importing the TerminalManagerService SDK

Local Dependency: Place the TerminalManagerLib-release-x.x.x.aar file in the libs directory of your Android Studio
project.
Add the following code to the build.gradle file:

After importing the .aar file, sync and rebuild the project.

                                                                                                  8

Please initialize the TerminalManagerService SDK in your Application. Example:

If the initialization is successful, the callback will return result=true; if it fails, the callback will return result=false.
After the Terminal Management SDK is successfully initialized, use TerminalManager to obtain the operation objects
for each module.

If the Terminal Management service is disconnected during use, the InitCallBack will also be triggered,
with result=false. Upon receiving this callback, reinitialize the Terminal Management SDK.

 6. Access permission

Permission Name                           Related Module   Tooltips

                                                       35
EVICE                                   ResourceManager    other system settings
android.permission.SUPER_PERMISSIONS_R  LocationManager    Install or update resource packages (e.g.,
ESOURCE                                 DeviceInfoManager  fonts, images, applications)
android.permission.SUPER_PERMISSIONS_L  NetworkManager     Get device location (GPS / Cell tower)
OCATION
android.permission.SUPER_PERMISSIONS_D                     Collect device info (SN, IMEI, hardware)
EVICE_INFO
android.permission.SUPER_PERMISSIONS_N                     Manage network access and firewall rules
ETWORK

                                        36
