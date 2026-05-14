---
title: "kozen-component-overview"
source: "KOZEN Component SDK Development Documentation _260129.docx"
type: "index"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - index
  - overview
summary: "Index and overview of the Kozen Component SDK API, including revision history, system environment, module summary, integration and initialization guide for the Component SDK supporting SecondaryScreen and Keyboard modules."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-component-keyboard"
  - "kozen-component-secondary-screen"
  - "kozen-component-errors"
  - "kozen-component-entities"
---
## Overview

### Revision History

| Version | Release | Modify Record | Adapted SDK version | Author |
| --- | --- | --- | --- | --- |
| 1.5 | 2026/01/29 | Add default wallpaper display on the secondary screen. Add support for application paths for displaying images, videos, and logos. Add support to get the secondary screen power-on status. Add support to get the secondary screen brightness. Save the secondary screen brightness after reboot. | ComponentService1.3.x | Johnny |
| 1.4 | 2025/09/09 | Add PCI Statement | ComponentService1.2.x | Johnny |
| 1.3 | 2025/08/12 | Add keyboard voice broadcast Fixed documentation errors regarding CommonError issues | ComponentService1.2.x | Johnny |
| 1.2 | 2025/07/03 | Secondary screen image display with GIF support | ComponentService1.1.x | Johnny |
| 1.1 | 2025/04/25 | Switch to English version | ComponentService1.0.x | Johnny |
| 1.0 | 2025/04/24 | Renamed setDefaultBackground to setBootLogo | ComponentService1.0.x | Yanan.Zhu |
| 0.4 | 2025/04/24 | Updated key definitions in Key Module | ComponentService1.0.x | Yue.Cui |
| 0.3 | 2025/04/22 | Functionality adjustments and optimizations | ComponentService1.0.x | Yanan.Zhu |
| 0.2 | 2025/04/21 | Add Key Module | ComponentService1.0.x | Yue.Cui |
| 0.1 | 2025/04/15 | Added Secondary Screen Module | ComponentService1.0.x | Yue.Cui |

### System Environment

| System environment | Platform | Compile environment |
| --- | --- | --- |
| Android 6.0 and above | ARM 64，ARM 32 | Android Studio, Intellij |

### Module Summary

| Function Name | Description |
|---------------|-------------|
| IKeyboard getKeyboardManager() | Get the keyboard module |
| ISecondaryScreen getSecondaryScreenManager() | Get the secondary screen module |
| void init(android.content.Context application, InitListener callback) | Initialize the SDK |

### Introduction

2. Overview

2.1 Introduction

### Feature Introduction

#### Component SDK Engine Module

2.3.1 Component SDK Engine Module

This module handles SDK initialization and provides access to various module operation classes.

#### SecondaryScreen Module

2.3.2 SecondaryScreen Module

This module handles functions related to the secondary screen.

Operation class object: ISecondaryScreen
Example to get the module operation class:

#### Keyboard Module

Kotlin: ComponentEngine.secondaryScreenManager

2.3.3 Keyboard Module

This module handles functions related to the keyboard.
Operation class object: IKeyboard


### SDK Integration

Kotlin: ComponentEngine.keyboardManager

2.4 Importing the SDK


### SDK Initialization

Local Dependency: Place the ComponentLib_xxx_release.aar file in the libs directory of your Android Studio project.
Add the following code to the build.gradle file:

After importing the .aar file, sync and rebuild the project.
2.5 Initializing the SDK
Please initialize the Component SDK in your Application. Example:
If initialization is successful, the callback will return result == 0.
If initialization fails, the callback will return result == -1.
After the Component SDK is successfully initialized, use ComponentEngine to obtain the operation objects for each module. Otherwise, an error code -10001 (service not connected) will be thrown.

## Related Links

- [[kozen-component-keyboard]]
- [[kozen-component-secondary-screen]]
- [[kozen-component-errors]]
- [[kozen-component-entities]]
