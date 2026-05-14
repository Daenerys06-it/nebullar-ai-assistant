---
title: "kozen-financial-general"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - general
summary: "Defines Kozen Financial SDK General module APIs for system-level functions including beep, navigation/status bar control, wake, time, timezone, reboot/shutdown, system property, screen rotation, LED control, notification shade, NFC logo, and device indicator."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-financial-overview"
  - "kozen-financial-init"
---

## Overview

General operation module providing device system-level control via IGeneralManager from FinancialEngine.INSTANCE.getGeneralManager() or FinancialEngine.generalManager().

## Function List

| Function Name | Description |
|--            |-----------|
| int setBeep(boolean enable,  int times,  int freq) | Set Beep |
| int setNavigationBar(int type,  boolean isHide) | Set system navigation bar |
| int setStatusBar(boolean isHide) | Set system status bar |
| int wakeUp() | Wake up device |
| int setTime(long time) | Set system time |
| int getTime() | Get time from system |
| String getTimeZone() | Get time zone |
| int setTimeZone(String timeZone) | Set time zone |
| int reboot() | Reboot device |
| int shutdown() | Shut down device |
| int setSystemProperty(String key, String value) | Set system property value |
| String getSystemProperty(String key) | Get system property value |
| int setScreenRotation(boolean enable) | Configures screen rotation function |
| void led(int type,  int status) | Toggle LED light on/off |
| void setLedVisible(boolean visible) | Show or hide the LED view |
| String checkDependencyVersion(int type) | Checks the version of dependency library |
| int setNotificationShade(boolean isEnable) | Show or hide the notification quick settings panel |
| int setNfcLogoVisible(boolean visible) | Set default visibility of the NFC logo |
| int setDeviceIndicator(int type,  int brightness,  boolean enable) | Control the device indicator light |

## Details

### setBeep

| Prototype    | Prototype int setBeep(boolean enable,  int times,  int freq) |
| ------------ | --- |
| Function     | Function Set Beep |
| Parameters   | Parameters Parameters: enable - begin or close buzzer times - buzzer duration freq - buzzer frequency |
| Return Value | Return value Return: 0: success Others: failure - see GeneralError |
| Notes        | Notes  |

### setNavigationBar

| Prototype    | Prototype int setNavigationBar(int type,  boolean isHide) |
| ------------ | --- |
| Function     | Function Set system navigation bar |
| Parameters   | Parameters Parameters: type - the type of navigation bar to be operated 1: back 2: home 3: recent isHide - the state of the navigation bar to be operated true: hidden false: displayed |
| Return Value | Return value Return: 0: success Others: failure - see GeneralError |
| Notes        | Notes  |

### setStatusBar

| Prototype    | Prototype int setStatusBar(boolean isHide) |
| ------------ | --- |
| Function     | Function Set system status bar |
| Parameters   | Parameters isHide - the state of the navigation bar to be operated true: hidden false: displayed |
| Return Value | Return value Return: 0: success Others: failure - see GeneralError |
| Notes        | Notes  |

### wakeUp

| Prototype    | Prototype int wakeUp() |
| ------------ | --- |
| Function     | Function Wake up device |
| Parameters   | Parameters  |
| Return Value | Return value Return: 0: success Others: failure - see GeneralError |
| Notes        | Notes  |

### setTime

| Prototype    | Prototype int setTime(long time) |
| ------------ | --- |
| Function     | Function Set system time |
| Parameters   | Parameters  |
| Return Value | Return value Return: 0: success Others: failure - see GeneralError |
| Notes        | Notes  |

### getTime

| Prototype    | Prototype int getTime() |
| ------------ | --- |
| Function     | Function Get time from system |
| Parameters   | Parameters  |
| Return Value | Return value Return: 0: success Others: failure - see GeneralError |
| Notes        | Notes  |

### getTimeZone

| Prototype    | Prototype String getTimeZone() |
| ------------ | --- |
| Function     | Function Get time zone |
| Parameters   | Parameters  |
| Return Value | Return value Returns: Time zone |
| Notes        | Notes  |

### setTimeZone

| Prototype    | Prototype int setTimeZone(String timeZone) |
| ------------ | --- |
| Function     | Function Set time zone |
| Parameters   | Parameters Parameters: timeZone - time zone id, supports two formats:  Region/City  2. GMT Example 1: setTimeZone("Europe/Moscow")  Example 2: setTimeZone("GMT+9") |
| Return Value | Return value Return: 0: success Others: failure - see GeneralError |
| Notes        | Notes  |

### reboot

| Prototype    | Prototype int reboot() |
| ------------ | --- |
| Function     | Function Reboot device |
| Parameters   | Parameters  |
| Return Value | Return value Return: 0: success Others: failure - see GeneralError |
| Notes        | Notes  |

### shutdown

| Prototype    | Prototype int shutdown() |
| ------------ | --- |
| Function     | Function Shut down device |
| Parameters   | Parameters  |
| Return Value | Return value Return: 0: success Others: failure - see GeneralError |
| Notes        | Notes  |

### setSystemProperty

| Prototype    | Prototype int setSystemProperty(String key, String value) |
| ------------ | --- |
| Function     | Function Set system property value |
| Parameters   | Parameters Parameters: key - the key of the system property(ro.product.model) value - the value of the system property |
| Return Value | Return value Return: 0: success Others: failure - see GeneralError |
| Notes        | Notes  |

### getSystemProperty

| Prototype    | Prototype String getSystemProperty(String key) |
| ------------ | --- |
| Function     | Function Get system property value |
| Parameters   | Parameters Parameters: key - the key of the system property (ro.product.model) |
| Return Value | Return value Return: Return the value of the system property by string form, or null if it cannot be read |
| Notes        | Notes  |

### setScreenRotation

| Prototype    | Prototype int setScreenRotation(boolean enable) |
| ------------ | --- |
| Function     | Function Configures screen rotation function |
| Parameters   | Parameters Parameters: enable  - true: Enable screen rotation - false: Disable screen rotation |
| Return Value | Return value 0: Success Others: failure - see GeneralError |
| Notes        | Notes  |

### led

| Prototype    | Prototype void led(int type,  int status) |
| ------------ | --- |
| Function     | Function Toggle LED light on/off |
| Parameters   | Parameters Parameters: type - LED light type (range: 1–4):     1 - Blue     2 - Yellow     3 - Green     4 - Red status- Switch state:     1 - Turn on     0 - Turn off |
| Return Value | Return Value  |
| Notes        | Notes This method is used to control the on/off state of different colored LED lights. |

### setLedVisible

| Prototype    | Prototype void setLedVisible(boolean visible) |
| ------------ | --- |
| Function     | Function Show or hide the LED view |
| Parameters   | Parameters Parameters: visible  true: show the LED view false: hide the LED view |
| Return Value | Return Value  |
| Notes        | Notes Controls the visibility of the on-screen LED view component. |

### checkDependencyVersion

| Prototype    | Prototype String checkDependencyVersion(int type) |
| ------------ | --- |
| Function     | Function Checks the version of dependency library |
| Parameters   | Parameters Parameters: type - Dependency type:     0 - EMV kernel     1 - POI     2 - UART     3 - Scanner box |
| Return Value | Return Value Return: Version string of the specified dependency |
| Notes        | Notes This method returns the version number of the selected module by type. |

### setNotificationShade

| Prototype    | Prototype int setNotificationShade(boolean isEnable) |
| ------------ | --- |
| Function     | Function Show or hide the notification quick settings panel |
| Parameters   | Parameters Parameters: isEnable -  true: Show the quick settings dropdown (default)            false: Hide the quick settings dropdown |
| Return Value | Return Value Return: 0 - Operation succeeded Others - Operation failed (see CommonError for details) |
| Notes        | Notes Controls the visibility of the Android notification shade's quick settings panel. |

### setNfcLogoVisible

| Prototype    | Prototype int setNfcLogoVisible(boolean visible) |
| ------------ | --- |
| Function     | Function Set default visibility of the NFC logo |
| Parameters   | Parameters Parameters: visible -  true: Show NFC logo            false: Hide NFC logo |
| Return Value | Return Value Return: 0 - Operation succeeded Others - Operation failed (see CommonError for details) |
| Notes        | Notes Sets whether the NFC logo is shown by default.  This setting persists after reboot until changed again. |

### setDeviceIndicator

| Prototype    | Prototype int setDeviceIndicator(int type,  int brightness,  boolean enable) |
| ------------ | --- |
| Function     | Function Control the device indicator light |
| Parameters   | Parameters Parameters: type - Indicator type: ConstantGeneral.IndicatorType.PINPAD_PHYSICAL ConstantGeneral.IndicatorType.PINPAD_CAPACITIVE brightness - Brightness level (range: 0–255, 0 turns off the indicator) enable - Indicator switch: true to enable, false to disable |
| Return Value | Return Value Return: 0 - Success Others - Failure (see GeneralError) |
| Notes        | Notes Controls brightness and on/off state of the specified device indicator light. |

## Notes

No additional notes.

## Related Links

- [[kozen-financial-overview]]
- [[kozen-financial-init]]
