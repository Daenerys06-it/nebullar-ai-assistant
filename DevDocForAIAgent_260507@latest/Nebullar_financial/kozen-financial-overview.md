---
title: "kozen-financial-overview"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "index"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - index
  - overview
summary: "Index and overview of the Kozen Financial SDK API, including revision history, system environment, module summary, integration and initialization guide for the Financial SDK supporting Scanner, CardReader, EMV, General, PINPAD, Printer, Security, and ECR modules."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-financial-init"
  - "kozen-financial-scanner-1"
  - "kozen-financial-cardreader"
  - "kozen-financial-emv"
  - "kozen-financial-general"
  - "kozen-financial-pinpad"
  - "kozen-financial-printer"
  - "kozen-financial-security"
  - "kozen-financial-ecr"
  - "kozen-financial-errors"
  - "kozen-financial-entities"
  - "kozen-financial-permission"
---

## Overview

### Revision History

| Version | Release | Modify Record | Adapted SDK version | Author |
| --- | --- | --- | --- | --- |
| 1.8 | 2026/04/28 | Add single-frame image parsing for scanning Detect keyboard type; devices with physical keyboards can no longer use the on-screen keyboard by default Add physical keyboard support to startPInputPin Add physical backlit silk-screen NFC logo Add device indicator light control interface Significantly improve scanning performance Add zoom ratio control interface during scanning Add support for ITF barcode format in scanning Add virtual port enable/disable functionality in ECR module | FinnancialService1.5.x | Johnny |
| 1.7 | 2026/02/03 | Add support to retrieve the AID and CAPK lists. Add a Mydebit card OPT-IN mode switch during transactions. Add standalone card checking. Add RSA encryption and decryption interfaces. Use BCD format to encrypt track data and PAN data. Add TR31 key writing. Add kcvMode when writing MK/SK keys. Add parameters tlkIndex and kcvMode when writing DUKPT_AES keys. Add kcvMode when writing DUKPT_DES keys. Add a Bundle parameter when reading RSA keys. Add ksnMode to the DUKPT_AES encryption/decryption interface. Add ksnMode to the DUKPT_AES MAC calculation interface. Add SM4 encryption and decryption interfaces. Set print density based on the input percentage value. Get the printer density percentage. Set the global font size. Get the global font size. Add printer line spacing information. Add support to retrieve printer line spacing information. Modify the style of the print error popup. Adjust returning the out-of-paper status before printing. Add switching for blind keyboard mode. Add support to get whether the current mode is blind keyboard mode. Add disabling camera auto-focus during scanning. Add a custom camera scanning UI. Add camera scan decoding. Add stopping camera decoding. Modify the default preview scanning UI style. Support LED light on/off control. Support NFC tag reading. Add NFC HCE data reading. Return the device connection status of a specified port. Get the system default printer. | FinnancialService1.4.x | Johnny |
| 1.6 | 2025/11/14 | Add printer cache-clearing settings Add RSA public/private key encryption and decryption support Add option to show/hide dropdown menus Add setting for displaying the NFC logo mode Add TR31 support Supplement the input parameter descriptions for EMV CAPK and AID Bug fix | FinnancialService1.3.2+ | Johnny |
| 1.5 | 2025/09/24 | Fix the problem of getCardExistStatus     description  | FinnancialService1.2.x | Johnny |
| 1.4 | 2025/09/15 | Fix documentation regarding EMVListener errors Add key-value enumeration description for PinViewEnum Add ECR pairing Add LED display Add interface to obtain library dependency versions Add PINPAD screen rotation support Add scanner default interface Add default PICC logo Add printer pop-up reminders for high/low temperature and paper shortage Add voice notifications for high/low temperature and paper shortage in the printer. Add support for SM4 (Only for the China region) Add permission control for each module  | FinnancialService1.2.x | Johnny |
| 1.3 | 2025/08/22 | Add explanations for three DEKPT_DES functions Include instructions for MK/SK writing Fix the issue with ConstantSecurity in the previous version of the document. | FinnancialService1.1.x | Johnny |
| 1.2 | 2025/07/24 | Add NFC TAG, ECR (only includes serial port & USB-to-serial), Felica card support, front and rear camera scanning Support for separate updates of the Kozen SDK Fix the API level of the system environment to 23. getCardExistStatus adds a return value for card presence. | FinnancialService1.1.x | Johnny |
| 1.1 | 2025/03/31 | Supplemental printing & barcode module error codes/constants Remove duplicate error messages in EMV module Add Pinpad rotation support | FinnancialService1.0.x | Yue.Cui Yao.Zhang Tong.Liu Johnny |
| 1.0 | 2025/03/10 | Add error code definition, entity definition, access permission Add EMV module Add SDK integration description | FinnancialService1.0.x | Yao.zhang Sunan Johnny |
| 0.5 | 2025/03/03 | Add a description of the financial SDK engine module | FinnancialService1.0.x | Sunan Johnny |
| 0.4 | 2025/02/27 | Update card reader, password keyboard, and some interfaces for general operations | FinnancialService1.0.x | Johnny |
| 0.3 | 2025/1/24 | Add EMV module, printer module, scanner module, and security module Update the API description for card reader, PINPAD, and general operation Add card detection and card positioning functions; Add PINPAD parameter configuration  | FinnancialService1.0.x | Johnny |
| 0.2 | 2025/1/2 | Add object description | FinnancialService1.0.x | Johnny |
| 0.1 | 2024/11/12 | Initial version | FinnancialService1.0.x | Johnny |

### System Environment

| System environment | Platform | Compile environment |
| --- | --- | --- |
| Android 6.0 and above | ARM 64，ARM 32 | Android Studio, Intellij |

### Module Summary

| Function Name | Description |
|----|----|
| ICardReaderManager getCardReaderManager() | Card Reader Operation module |
| IEmvManager getEmvManager() | EMV Operation module |
| IGeneralManager getGeneralManager() | Device Basic Operation function |
| IPinpadManager getPinpadManager() | PINPAD Operation module |
| IPrinterManager getPrinterManager() | Printing Operation module |
| ISecurityManager getSecurityManager() | Security module |
| IEcrManager getEcrManager() | ECR Operation module |
| IScannerManager getScannerManager() | Scanner Operation module |

### Introduction

2. Overview

2.1 Introduction

### Feature Introduction

2.2 Android version and IDE version supported by the SDK

#### Scanner Operation Module

KozenFinancialService is a hardware firmware-based API SDK provided by KOZEN. Designed specifically for Java and Android developers. This SDK enables developers to quickly access hardware operation interfaces for KOZEN financial terminal, facilitating efficient business logic implementation.

The SDK primarily includes the following modules: Basic Device Information, Card Operations, PIN Pad, EMV, and Security mode.

This document serves as the KozenFinancialService API Reference.

2.2 Android version and IDE version supported by the SDK



#### Cardreader Module

2.3 Feature Introduction

2.3.1 Financial SDK Engine Module

This module handles SDK initialization and provides access to various module operation classes.

Operation class object: FinancialEngine 

2.3.2 Cardreader Module



#### EMV Module

This module handles card reader functionality.

Operation class object: ICardReaderManager

Example to get the module operation class:

JAVA: FinancialEngine.INSTANCE.getCardReaderManager()

Kotlin: FinancialEngine.cardReaderManager()

2.3.3 EMV Module



#### General Module

This module handles EMV functionality.

Operation class object: IEmvManager

Example to get the module operation class:

JAVA: FinancialEngine.INSTANCE.getEmvManager()

Kotlin: FinancialEngine.emvManager()

2.3.4. General Module



#### Pinpad Module

This module handles basic device control functionalities.

Operation class object: IGeneralManager

Example to get the module operation class:

JAVA: FinancialEngine.INSTANCE.getGeneralManager()

Kotlin: FinancialEngine.generalManager()

2.3.5. Pinpad Module



#### Printer Module

This module handles Pinpad functionality.

Operation class object: IPinpadManager

Example to get the module operation class:

JAVA: FinancialEngine.INSTANCE.getPinpadManager()

Kotlin: FinancialEngine.pinpadManager()

2.3.6. Printer Module



#### Scanner Module

This module handles printing functionality.

Operation class object: IPrinterManager

Example to get the module operation class: 

JAVA: FinancialEngine.INSTANCE.getPrinterManager()

Kotlin: FinancialEngine.printerManager()

2.3.7. Scanner Module



#### Security Module

This module handles scanning functionality.

Operation class object: IScannerManager

Example to get the module operation class: 

JAVA: FinancialEngine.INSTANCE.getScannerManager()

Kotlin: FinancialEngine.scannerManager()

2.3.8. Security Module



#### ECR Module

This module handles encryption/decryption algorithms and key-related functionalities.

Operation class object: ISecurityManager

Example to get the module operation class: 

JAVA: FinancialEngine.INSTANCE.getSecurityManager()

Kotlin: FinancialEngine.securityManager()

2.3.9. ECR Module


### Importing the Financial SDK

This module handles Kiosk functionalities.

Operation class object: IEcrManager

Example to get the module operation class: 


### Initializing the Financial SDK

JAVA: FinancialEngine.INSTANCE.getEcrManager()

Kotlin: FinancialEngine.ecrManager()

2.4 Importing the Financial SDK

Local Dependency: Place the FinancialLib-x.x.x-release.aar file in the libs directory of your Android Studio project.
Add the following code to the build.gradle file:

After importing the .aar file, sync and rebuild the project.

2.5 Initializing the Financial SDK


## Related Links

- [[kozen-financial-init]]
- [[kozen-financial-scanner-1]]
- [[kozen-financial-cardreader]]
- [[kozen-financial-emv-1]]
- [[kozen-financial-general]]
- [[kozen-financial-pinpad]]
- [[kozen-financial-printer]]
- [[kozen-financial-security]]
- [[kozen-financial-ecr]]
- [[kozen-financial-errors]]
- [[kozen-financial-entities-1]]
- [[kozen-financial-permission]]
