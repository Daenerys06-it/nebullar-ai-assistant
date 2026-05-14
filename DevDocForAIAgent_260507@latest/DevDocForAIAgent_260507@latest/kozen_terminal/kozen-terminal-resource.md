---
title: "kozen-terminal-resource"
source: "KOZEN Terminal manager SDK Development Documentation_260422.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - resource
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines Kozen Terminal Manager Resource module APIs for application installation/uninstallation, firmware OTA updates, resource package updates, and progress/error callbacks via OnAppUpdateListener, OnUpdateCustomResListener, and OnUpdateOTAListener."
---

## Overview

Resource module providing application management, firmware/OTA upgrade, and resource package update functionality via IResourceManager obtained via TerminalManager.INSTANCE.getResourceManager() or TerminalManager.resourceManager().

## Function List

| Function Name | Description |
|---------------|-------------|
| int unInstall(String pkgName) | Uninstall an app |
| int updateCustomRes(String path) | Update the resource package |
| int updateOTA(String path) | Update the device system version / MCU firmware version |
| int installOrUpdateWithListener(String path,  OnAppUpdateListener listener) | Install or update an app with listener |
| int updateCustomResWithListener(String path,  OnUpdateCustomResListener listener) | Update the resource package with listener |
| int updateOTAWithListener(String path, OnUpdateOTAListener listener) | Update the device system version / MCU firmware version with listener |

## Details

### installOrUpdate

| Prototype    | Prototype int installOrUpdate(String path) |
| ------------ | --- |
| Function     | Function Installs or updates an app. |
| Parameters   | Parameters path - The path of the app installation package. |
| Return Value | Return value Return:  0: Success Others: Failure (refer to ResourceError). |
| Notes        | Notes  |

### unInstall

| Prototype    | Prototype int unInstall(String pkgName) |
| ------------ | --- |
| Function     | Function Uninstalls an app. |
| Parameters   | Parameters pkgName - The package name of the app to uninstall. |
| Return Value | Return value Return:  0: Success, Others: Failure (refer to ResourceError). |
| Notes        | Notes  |

### updateOTA

| Prototype    | Prototype int updateOTA(String path) |
| ------------ | --- |
| Function     | Function Updates the device system version or MCU firmware version. |
| Parameters   | Parameters path - The path of the update package (supports /storage/emulated/0/ or /sdcard/).  - .zip: Recognized as a system version package.  - .bin: Recognized as an MCU firmware package. |
| Return Value | Return value Return:  0: Package verification successful, starting upgrade.  Others: Failure (refer to ResourceError). |
| Notes        | Notes  |

### updateCustomRes

| Prototype    | Prototype int updateCustomRes(String path) |
| ------------ | --- |
| Function     | Function Updates the resource package. |
| Parameters   | Parameters path - The path of the resource package. |
| Return Value | Return value Return:  0: Package verification successful, starting resource update.  Others: Failure (refer to ResourceError). |
| Notes        | Notes  |

### installOrUpdateWithListener

| Prototype    | Prototype int installOrUpdateWithListener(String path,  OnAppUpdateListener listener) |
| ------------ | --- |
| Function     | Function Install or update an app with listner |
| Parameters   | Parameters Parameters: path - Path to the app package (either a file URI string or absolute accessible file path) listener - Callback for app installation result (see OnAppUpdateListener) |
| Return Value | Return Value Return: 0 - API call successful Others - API call failed (see CommonError for details) |
| Notes        | Notes  |

### updateCustomResWithListener

| Prototype    | Prototype int updateCustomResWithListener(String path,  OnUpdateCustomResListener listener) |
| ------------ | --- |
| Function     | Function Update the resource package with listener |
| Parameters   | Parameters Parameters: path - Path to the resource package (either a file URI string or absolute accessible file path) listener - Callback for update result (see OnUpdateCustomResListener ) |
| Return Value | Return Value Return: 0 - API call successful Others - API call failed (see CommonError for details) |
| Notes        | Notes  |

### updateOTAWithListener

| Prototype    | Prototype int updateOTAWithListener(String path, OnUpdateOTAListener listener) |
| ------------ | --- |
| Function     | Function Update the device system version / MCU firmware version with listener |
| Parameters   | Parameters Parameters: path - Path to the OTA package (either a file URI string or absolute accessible file path) listener - Callback for update result (see OnUpdateOTAListener ) |
| Return Value | Return Value Return: 0 - API call successful Others - API call failed (see CommonError for details) |
| Notes        | Notes  |


### OnAppUpdateListener

#### onError

| Prototype    | Prototype void onError(String msg, int code) |
| ------------ | --- |
| Function     | Function Upgrade failed |
| Parameters   | Parameters msg - Error message code - Error code (refer to ResourceError) |
| Return Value | Return value  |
| Notes        | Notes  |

#### onSuccess

| Prototype    | Prototype void onSuccess() |
| ------------ | --- |
| Function     | Function Upgrade successful |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes  |


### OnUpdateCustomResListener

#### onError

| Prototype    | Prototype void onError(String msg, int code) |
| ------------ | --- |
| Function     | Function Upgrade failed |
| Parameters   | Parameters msg - Error message code - Error code (refer to ResourceError) |
| Return Value | Return value  |
| Notes        | Notes  |

#### onSuccess

| Prototype    | Prototype void onSuccess() |
| ------------ | --- |
| Function     | Function Upgrade successful |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes  |


### OnUpdateOTAListener

#### onError

| Prototype    | Prototype void onError(String msg, int code) |
| ------------ | --- |
| Function     | Function Upgrade failed |
| Parameters   | Parameters msg - Error message code - Error code (refer to ResourceError) |
| Return Value | Return value  |
| Notes        | Notes  |

#### onSuccess

| Prototype    | Prototype void onSuccess() |
| ------------ | --- |
| Function     | Function Upgrade successful |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes  |

#### onUpdateInProgress

| Prototype    | Prototype void onUpdateInProgress(int percent) |
| ------------ | --- |
| Function     | Function Firmware or application update progress callback |
| Parameters   | Parameters Parameters: percent - Update progress percentage (0–100) |
| Return Value | Return Value  |
| Notes        | Notes This method is called to report the current progress of an ongoing update. |


## Notes

- Upgrade error codes refer to the ResourceError section in [[kozen-terminal-errors]].
- The progress callback onUpdateInProgress provides percentage-based progress updates.

## Related Links

- [[kozen-terminal-overview]]
- [[kozen-terminal-errors]]
