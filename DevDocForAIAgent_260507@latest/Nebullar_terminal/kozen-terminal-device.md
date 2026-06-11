---
title: "kozen-terminal-device"
source: "KOZEN Terminal manager SDK Development Documentation_260422.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - device
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines Kozen Terminal Manager Device module APIs for device control operations including system time, timezone, reboot, shutdown, scheduled reboot, silent installation, runtime permission enforcement, screen timeout, sleep mode, and wake-up methods via IDeviceManager."
---

## Overview

Device management module providing device control operations including system time management, reboot/shutdown, silent installation, wake-up control etc. via IDeviceManager obtained via TerminalManager.INSTANCE.getDeviceManager() or TerminalManager.deviceManager().

## Function List

| Function Name | Description |
|---------------|-------------|
| long getSystemTime() | Return the timestamp of the current system time |
| String getTimeZone() | Get the current time zone |
| void reboot() | Reboot the device |
| int setPCIReboot(long time) | Schedule a reboot |
| int setSystemTime(long time) | Set the system time |
| int setTimeZone(String timeZone) | Set the time zone |
| void shutdown() | Shut down the device |
| void forcePermission(boolean isOpen) | Forced permission request |
| Void setSilentInstall(boolean isOpen) | Silent app installation |
| int setScreenTimeOut(long timeOut) | Set screen timeout duration |
| int sleep(boolean isConfirm) | Turn off (sleep) the screen |
| int wakeUp(WakeUpType type, boolean enable) | Enable or disable various device wake-up |

## Details

### setSystemTime

| Prototype    | Prototype int setSystemTime(long time) |
| ------------ | --- |
| Function     | Function Sets the system time. |
| Parameters   | Parameters time - Timestamp. |
| Return Value | Return value Return:  0: Success,  Others: Failure (refer to DeviceError). |
| Notes        | Notes  |

### getSystemTime

| Prototype    | Prototype long getSystemTime() |
| ------------ | --- |
| Function     | Function Returns the current system time as a timestamp. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  The timestamp. |
| Notes        | Notes  |

### setTimeZone

| Prototype    | Prototype int setTimeZone(String timeZone) |
| ------------ | --- |
| Function     | Function Sets the time zone. |
| Parameters   | Parameters timeZone - Time zone ID, supports two formats:  1. Region/City (e.g., Europe/Moscow)  2. GMT (e.g., GMT+9). |
| Return Value | Return value Return:  0: Success,  Others: Failure (refer to DeviceError). |
| Notes        | Notes  |

### getTimeZone

| Prototype    | Prototype String getTimeZone() |
| ------------ | --- |
| Function     | Function Retrieves the current time zone. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  The time zone. |
| Notes        | Notes  |

### reboot

| Prototype    | Prototype void reboot() |
| ------------ | --- |
| Function     | Function Reboots the device |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes  |

### shutdown

| Prototype    | Prototype void shutdown() |
| ------------ | --- |
| Function     | Function Shuts down the device. |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes  |

### setPCIReboot

| Prototype    | Prototype int setPCIReboot(long time) |
| ------------ | --- |
| Function     | Function Schedules a timed reboot. |
| Parameters   | Parameters time - Device will reboot after running for this duration (e.g., 1000 * 60 * 60 for 1 hour). |
| Return Value | Return value Return:  0: Success, Others: Failure (refer to DeviceError). |
| Notes        | Notes 1. The policy will automatically run after reboot unless canceled by cancelPCIReboot.  2. A reboot prompt will be shown before rebooting.  3. It is recommended not to exceed 24 hours.  4. If the set time is less than the device's uptime, it will reboot immediately. |

### cancelPCIReboot

| Prototype    | Prototype int cancelPCIReboot() |
| ------------ | --- |
| Function     | Function Cancels the scheduled reboot. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  0: Success, Others: Failure (refer to DeviceError). |
| Notes        | Notes  |

### setSilentInstall

| Prototype    | Prototype void setSilentInstall(boolean isOpen) |
| ------------ | --- |
| Function     | Function Enable or disable silent installation |
| Parameters   | Parameters Parameters: isOpen -  true: Do not show app installation prompt (silent install)         false: Show installation prompt |
| Return Value | Return Value  |
| Notes        | Notes When enabled, applications can be installed silently without prompting the user. |

### forcePermission

| Prototype    | Prototype void forcePermission(boolean isOpen) |
| ------------ | --- |
| Function     | Function Enforce runtime permission checks |
| Parameters   | Parameters Parameters: isOpen -  true: The app must request permission to access a module         false: No permission enforcement |
| Return Value | Return Value  |
| Notes        | Notes When enabled, modules cannot be accessed unless the app has explicitly been granted the required permissions. |

### setScreenTimeOut

| Prototype    | Prototype int setScreenTimeOut(long timeOut) |
| ------------ | --- |
| Function     | Function Set the screen timeout duration in seconds |
| Parameters   | Parameters Parameters: timeOut -      0: Always on     1800: Maximum value (30 minutes) |
| Return Value | Return Value Return: 0 - Success 1 - FailureOthers , See DeviceError for details |
| Notes        | Notes This method sets how long the screen stays on before turning off due to inactivity. |

### sleep

| Prototype    | Prototype int sleep(boolean isConfirm) |
| ------------ | --- |
| Function     | Function Turn off the screen (sleep mode) |
| Parameters   | Parameters Parameters: isConfirm - Whether to show a confirmation dialog before sleeping     true - Show confirmation dialog     false - Enter sleep directly |
| Return Value | Return Value Return: 0 - Success 1 - Failure |
| Notes        | Notes After calling this method, the screen will enter sleep mode in 5 seconds. The user can tap the screen to wake it up.This setting only takes effect for the next sleep. |

### wakeUp

| Prototype    | Prototype int wakeUp(WakeUpType type, boolean enable) |
| ------------ | --- |
| Function     | Function Enable or disable various device wake-up methods |
| Parameters   | Parameters Parameters: type - Wake-up method enum value (see WakeUpType)enable  true: Enable the wake-up method         false: Disable the wake-up method |
| Return Value | Return Value Return: 0 - Success 1 - FailureOthers , See DeviceError for details |
| Notes        | Notes This method configures whether a specific device wake-up method is enabled or disabled. |


## Notes

- Wake-up methods are controlled via the WakeUpType enum. See [[kozen-terminal-entities]] for enum values.
- Screen timeout default is 0 (always on).

## Related Links

- [[kozen-terminal-overview]]
- [[kozen-terminal-entities]]
