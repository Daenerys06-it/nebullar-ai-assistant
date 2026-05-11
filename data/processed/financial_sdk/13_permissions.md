 6. Access permission ............................................................................................................... 114

                                                                                             8

Version Release  Modify Record                                      Adapted SDK version                  Author
                                                                                                         Johnny
                  Add single-frame image parsing for scanning
                  Detect keyboard type; devices with physical                                            Johnny

                      keyboards can no longer use the on-screen

                       keyboard by default
                  Add physical keyboard support to

                      startPInputPin

                  Add physical backlit silk-screen NFC logo

1.8  2026/04/28  Add device indicator light control interface       FinnancialService1.5.x

                  Significantly improve scanning performance

                  Add zoom ratio control interface during

                       scanning
                  Add support for ITF barcode format in

                       scanning
                  Add virtual port enable/disable functionality in

                      ECR module

                  Add support to retrieve the AID and CAPK

                       lists.
                  Add a Mydebit card OPT-IN mode switch

                       during transactions.
                  Add standalone card checking.
                  Add RSA encryption and decryption

                       interfaces.
                  Use BCD format to encrypt track data and PAN

                       data.
                  Add TR31 key writing.
                  Add kcvMode when writing MK/SK keys.
                  Add parameters tlkIndex and kcvMode when

1.7  2026/02/03       writing DUKPT_AES keys.
                                                                                 FinnancialService1.4.x
                      Add kcvMode when writing DUKPT_DES

                       keys.
                  Add a Bundle parameter when reading RSA

                       keys.
                  Add ksnMode to the DUKPT_AES

                       encryption/decryption interface.
                  Add ksnMode to the DUKPT_AES MAC

                       calculation interface.
                  Add SM4 encryption and decryption interfaces.
                  Set print density based on the input percentage

                       value.
                  Get the printer density percentage.
                  Set the global font size.

                                               9
                  Add printer line spacing information.
                  Add support to retrieve printer line spacing

                       information.
                  Modify the style of the print error popup.
                  Adjust returning the out-of-paper status

                       before printing.
                  Add switching for blind keyboard mode.
                  Add support to get whether the current mode is

                       blind keyboard mode.
                  Add disabling camera auto-focus during

                       scanning.
                  Add a custom camera scanning UI.
                  Add camera scan decoding.
                  Add stopping camera decoding.
                  Modify the default preview scanning UI style.
                  Support LED light on/off control.
                  Support NFC tag reading.
                  Add NFC HCE data reading.
                  Return the device connection status of a

                       specified port.
                  Get the system default printer.
                  Add printer cache-clearing settings
                  Add RSA public/private key encryption and

                   decryption support

                  Add option to show/hide dropdown menus

1.6  2025/11/14  Add setting for displaying the NFC logo mode FinnancialService1.3.2+ Johnny

                  Add TR31 support

                  Supplement the input parameter descriptions

                       for EMV CAPK and AID
                  Bug fix

1.5  2025/09/24   Fix the problem of getCardExistStatus           FinnancialService1.2.x Johnny

                   description

                  Fix documentation regarding EMVListener

                       errors
                  Add key-value enumeration description for

                   PinViewEnum

                  Add ECR pairing

     2025/09/15   Add LED display
1.4                                                                           FinnancialService1.2.x  Johnny
                   Add interface to obtain library dependency

                       versions
                  Add PINPAD screen rotation support
                  Add scanner default interface
                  Add default PICC logo
                  Add printer pop-up reminders for high/low

                                             10
                  Add voice notifications for high/low

                       temperature and paper shortage in the printer.
                  Add support for SM4 (Only for the China

                       region)
                  Add permission control for each module

                  Add explanations for three DEKPT_DES

                   functions

1.3  2025/08/22  Include instructions for MK/SK writing                FinnancialService1.1.x Johnny

                  Fix the issue with ConstantSecurity in the

                   previous version of the document.

                  Add NFC TAG, ECR (only includes serial port

                   & USB-to-serial), Felica card support, front

                   and rear camera scanning

     2025/07/24   Support for separate updates of the Kozen SDK                                       Johnny
1.2                                                                           FinnancialService1.1.x
                   Fix the API level of the system environment to

                       23.
                  getCardExistStatus adds a return value for card

                   presence.

                  Supplemental printing & barcode module error                                        Yue.Cui
                                                                                                      Yao.Zhang
1.1                         codes/constants                            FinnancialService1.0.x
     2025/03/31  Remove duplicate error messages in EMV                                               Tong.Liu

                   module                                                                             Johnny

                   Add Pinpad rotation support

                  Add error code definition, entity definition,                                       Yao.zhang

1.0                access permission                                   FinnancialService1.0.x         Sunan
     2025/03/10  Add EMV module                                                                       Johnny

                  Add SDK integration description

0.5  2025/03/03   Add a description of the financial SDK engine        FinnancialService1.0.x         Sunan

                   module                                                                             Johnny

0.4  2025/02/27   Update card reader, password keyboard, and           FinnancialService1.0.x Johnny

                   some interfaces for general operations

                  Add EMV module, printer module, scanner

                       module, and security module
                  Update the API description for card reader,

0.3  2025/1/24     PINPAD, and general operation                       FinnancialService1.0.x Johnny

                  Add card detection and card positioning

                   functions; Add PINPAD parameter

                   configuration

0.2  2025/1/2  Add object description                                  FinnancialService1.0.x Johnny

0.1  2024/11/12  Initial version                                       FinnancialService1.0.x Johnny

                                                11

2.1 Introduction

      KozenFinancialService is a hardware firmware-based API SDK provided by KOZEN. Designed specifically for
Java and Android developers. This SDK enables developers to quickly access hardware operation interfaces for
KOZEN financial terminal, facilitating efficient business logic implementation.

      The SDK primarily includes the following modules: Basic Device Information, Card Operations, PIN Pad, EMV,
and Security mode.

      This document serves as the KozenFinancialService API Reference.

2.2 Android version and IDE version supported by the SDK

System environment     Platform                           Compile environment
Android 6.0 and above  ARM 64ARM 32                       Android Studio, Intellij

2.3 Feature Introduction

2.3.1 Financial SDK Engine Module

 This module handles SDK initialization and provides access to various module operation classes.
 Operation class object: FinancialEngine

2.3.2 Cardreader Module

 This module handles card reader functionality.
 Operation class object: ICardReaderManager
 Example to get the module operation class:
JAVA: FinancialEngine.INSTANCE.getCardReaderManager()
Kotlin: FinancialEngine.cardReaderManager()

2.3.3 EMV Module

 This module handles EMV functionality.
 Operation class object: IEmvManager
 Example to get the module operation class:
JAVA: FinancialEngine.INSTANCE.getEmvManager()
Kotlin: FinancialEngine.emvManager()

2.3.4. General Module

 This module handles basic device control functionalities.
 Operation class object: IGeneralManager

                                                                                                 12
JAVA: FinancialEngine.INSTANCE.getGeneralManager()
Kotlin: FinancialEngine.generalManager()

2.3.5. Pinpad Module

 This module handles Pinpad functionality.
 Operation class object: IPinpadManager
 Example to get the module operation class:
JAVA: FinancialEngine.INSTANCE.getPinpadManager()
Kotlin: FinancialEngine.pinpadManager()

2.3.6. Printer Module

 This module handles printing functionality.
 Operation class object: IPrinterManager
 Example to get the module operation class:
JAVA: FinancialEngine.INSTANCE.getPrinterManager()
Kotlin: FinancialEngine.printerManager()

2.3.7. Scanner Module

 This module handles scanning functionality.
 Operation class object: IScannerManager
 Example to get the module operation class:
JAVA: FinancialEngine.INSTANCE.getScannerManager()
Kotlin: FinancialEngine.scannerManager()

2.3.8. Security Module

 This module handles encryption/decryption algorithms and key-related functionalities.
 Operation class object: ISecurityManager
 Example to get the module operation class:
JAVA: FinancialEngine.INSTANCE.getSecurityManager()
Kotlin: FinancialEngine.securityManager()

2.3.9. ECR Module

 This module handles Kiosk functionalities.
 Operation class object: IEcrManager
 Example to get the module operation class:
JAVA: FinancialEngine.INSTANCE.getEcrManager()
Kotlin: FinancialEngine.ecrManager()

                                                                                                 13
Local Dependency: Place the FinancialLib-x.x.x-release.aar file in the libs directory of your Android Studio project.
Add the following code to the build.gradle file:
After importing the .aar file, sync and rebuild the project.

2.5 Initializing the Financial SDK
Please initialize the Financial SDK in your Application. Example:

If initialization is successful, the callback will return result == 0.
If initialization fails, the callback will return result == -1.

                                                                                                 14
module. Otherwise, an error code -10001 (Financial service not connected) will be thrown.
If the financial service is disconnected during use, the InitListener will be called again with result == -1. Upon
receiving this callback, reinitialize the Financial SDK.
If an interface throws the error code -10001 (Financial service not connected) during use, reinitialize the Financial
SDK.

                                                                                                 15

void init(android.content.Context application,           Financial SDK initialization
InitListener callback)
ICardReaderManager getCardReaderManager()                Card Reader Operation module
IEmvManager getEmvManager()                              EMV Operation module
IGeneralManager getGeneralManager()                      Device Basic Operation function
IPinpadManager getPinpadManager()                        PINPAD Operation module
IPrinterManager getPrinterManager()                      Printing Operation module
ISecurityManager getSecurityManager()                    Security module
IEcrManager getEcrManager()                              ECR Operation module
IScannerManager getScannerManager()                      Scanner Operation module

 6. Access permission

Permission Name                         Related Module     Tooltips
android.permission.SUPER_PERMISSIONS_P  PrinterManager     Control and use built-in printer
RINTER                                  PinpadManager
android.permission.SUPER_PERMISSIONS_P  ScannerManager     Access encrypted pinpad for input
INPAD                                   CardReaderManager
android.permission.SUPER_PERMISSIONS_S  EmvManager         Scan barcodes and QR codes
CANNER                                  GeneralManager
android.permission.SUPER_PERMISSIONS_C  SecurityManager    Access magstripe, IC, and contactless cards
ARD_READER                              EcrManager
android.permission.SUPER_PERMISSIONS_E                     Perform EMV card transactions
MV
android.permission.SUPER_PERMISSIONS_G                     Access general device functions (buzzer,
ENERAL                                                     LED)
android.permission.SUPER_PERMISSIONS_S                     Use security module (key management,
ERURITY                                                    encryption)
android.permission.SUPER_PERMISSIONS_E                     Interact with external ECR system
CR

                                        114
