---
title: "kozen-terminal-overview"
source: "KOZEN Terminal manager SDK Development Documentation_260422.docx"
type: "index"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - index
  - overview
created: "2026-04-30"
updated: "2026-04-30"
summary: "Index and overview of the Kozen Terminal Manager SDK API, including revision history, system environment, module summary, integration instructions, and SDK initialization guide for integrating terminal management capabilities into Android applications."
related:
  - kozen-terminal-certification
  - kozen-terminal-device-info
  - kozen-terminal-device
  - kozen-terminal-location
  - kozen-terminal-network
  - kozen-terminal-resource
  - kozen-terminal-perception
  - kozen-terminal-log
  - kozen-terminal-errors
  - kozen-terminal-entities
  - kozen-terminal-permission
---

## Overview

### Revision History

| Version | Release | Modify Record | Adapted SDK version | Author |
| --- | --- | --- | --- | --- |
| 1.4 | 2026/04/22 | Adjust wakeupType to add support for double tap to wake and lift to wake | TerminalManagerService 1.3.x | Johnny |
| 1.3 | 2026/01/30 | Add an information collection module. Add support for returning OTA upgrade progress monitoring callbacks. Add a main screen brightness timeout duration. Add a screen-off reminder setting. Add log retrieval. Adjust compatibility for retrieving the OS version number. Adjust the SDK icon | TerminalManagerService 1.2.x | Johnny |
| 1.2 | 2025/09/18 | Add forcePermission API for mandatory permission check Add silentInstall API for silent installation Add CSN API Add TUSN reading Extend getLocationManager with 2 open interfaces to specify location provider Add application install API with listener Add OTA install API with compatibility support Add resource install API with listener Add module permission Add a security statement for location | TerminalManagerService 1.1.x | Johnny |
| 1.1 | 2025/03/31 | Positioning module constants supplement; Enhance the resource module with extended error codes and implement upgrade listener for the MCU | TerminalManagerService 1.0.x | Yue.Cui Tong.Liu Johnny |
| 1.0 | 2025/03/19 | Version verification and release | TerminalManagerService 1.0.x | Yao.zhang Sunan Johnny |
| 0.2 | 2025/03/15 | Update LocationManager module, add LocationError | TerminalManagerService 1.0.x | Johnny |
| 0.1 | 2025/03/14 | Initial version | TerminalManagerService 1.0.x | Johnny |

### System Environment

| System environment | Platform | Compile environment |
| --- | --- | --- |
| Android 6.0 and above | ARM 64，ARM 32 | Android Studio, Intellij |

### Module Summary

| Function Name | Description |
|---------------|-------------|
| ICertificationManager getCertificationManager() | Certification module |
| IDeviceInfoManager getDeviceInfoManager() | Device information module |
| IDeviceManager getDeviceManager() | Device module |
| ILocationManager getLocationManager() | Location module |
| INetworkManager getNetworkManager() | Network module |
| IResourceManager getResourceManager() | Resource module |
| ILogManager getLogManager() | Log module |
| IPerceptionInfoManager getPerceptionInfoManager() | Perception Info module |

### Introduction

2.1 Introduction

This document is interfaces for TMS and AppStore clients, with broader OS operation permissions compared to the Financial SDK. Main functionalities include installing/uninstalling apps on the OS, retrieving system information, location data, consumable status, and performing operations such as shutting down or rebooting the OS. After client integration, the cloud can be used to manage applications and information on terminals in bulk.

### Feature Introduction

2.2 Android version and IDE version supported by the SDK

#### Terminal Management Module

2.3.1 Terminal Management Module

This class handles SDK initialization and provides access to operation classes for each module. 



#### Certificate Management Module

The operation class object is: TerminalManager.

2.3.2 Certificate Management Module

This module provides certificate management functionalities. 

The operation class object is: ICertificationManager.



#### Device Management Module

Kotlin: TerminalManager.certificationManager()

2.3.3 Device Management Module

This module handles device-related functionalities. 

The operation class object is: IDeviceManager.

Example to obtain the operation class: 



#### Device Information Management Module

Example to obtain the operation class: 

JAVA: TerminalManager.INSTANCE.getDeviceManager()

Kotlin: TerminalManager.deviceManager()

2.3.4 Device Information Management Module

This module provides functionalities for retrieving device information. 



#### Location Management Module

This module provides functionalities for retrieving device information. 

The operation class object is: IDeviceInfoManager.

Example to obtain the operation class: 

JAVA: TerminalManager.INSTANCE.getDeviceInfoManager()

Kotlin: TerminalManager.deviceInfoManager()



#### Network Management Module

This module handles location-related functionalities. 

The operation class object is: ILocationManager.

Example to obtain the operation class: 

JAVA: TerminalManager.INSTANCE.getLocationManager()

Kotlin: TerminalManager.locationManager()



#### Resource Management Module

Kotlin: TerminalManager.locationManager()

2.3.6 Network Management Module

This module handles network-related functionalities. 

The operation class object is: INetworkManager.

Example to obtain the operation class: 



### SDK Integration

Kotlin: TerminalManager.resourceManager()

2.4 Importing the TerminalManagerService SDK

Local Dependency: Place the TerminalManagerLib-release-x.x.x.aar file in the libs directory of your Android Studio project.
Add the following code to the build.gradle file:



### SDK Initialization

2.5 Initializing the TerminalManagerService SDK

Please initialize the TerminalManagerService SDK in your Application. Example:

If the initialization is successful, the callback will return result=true; if it fails, the callback will return result=false.

After the Terminal Management SDK is successfully initialized, use TerminalManager to obtain the operation objects for each module.

If the Terminal Management service is disconnected during use, the InitCallBack will also be triggered, with result=false. Upon receiving this callback, reinitialize the Terminal Management SDK.


## Related Links

- [[kozen-terminal-certification]]
- [[kozen-terminal-device-info]]
- [[kozen-terminal-device]]
- [[kozen-terminal-location]]
- [[kozen-terminal-network]]
- [[kozen-terminal-resource]]
- [[kozen-terminal-perception]]
- [[kozen-terminal-log]]
- [[kozen-terminal-errors]]
- [[kozen-terminal-entities]]
- [[kozen-terminal-permission]]
