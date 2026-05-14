---
title: "kozen-terminal-device-info"
source: "KOZEN Terminal manager SDK Development Documentation_260422.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - device_info
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines Kozen Terminal Manager Device Info module APIs for retrieving device identification and version information including SN, IMEI, IMSI, OS version, MCU version, EMV kernel version, TUSN, and CSN via IDeviceInfoManager."
---

## Overview

Device information module providing read-only access to device identification, version, and hardware information via IDeviceInfoManager obtained via TerminalManager.INSTANCE.getDeviceInfoManager() or TerminalManager.deviceInfoManager().

## Function List

| Function Name | Description |
|---------------|-------------|
| String getHardwareVersion() | Get hardware version number |
| String[] getImei() | Get IMEI number; if multiple exist, return multiple |
| String[] getImsi() | Get IMSI number; if multiple exist, return multiple |
| String getKernelVersion() | Get Linux kernel version number |
| String getMcuVersion() | Get MCU version number |
| String getOsVersion() | Get Android version number |
| String getSdkServiceVersion() | Get SDK service version number |
| String getSerialNo() | Get device serial number |
| String getDeviceModel() | Get device model |
| String getVendorName() | Get vendor name(XC, Kozen) |
| String getCSN() | Get customer serial number |
| String getTUSN() | Get TUSN(Only for the China region) |

## Details

### getSdkServiceVersion

| Prototype    | Prototype String getSdkServiceVersion() |
| ------------ | --- |
| Function     | Function Get the SDK service version number. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  The SDK service version number. |
| Notes        | Notes  |

### getSerialNo

| Prototype    | Prototype String getSerialNo() |
| ------------ | --- |
| Function     | Function Get Terminal serial number |
| Parameters   | Parameters  |
| Return Value | Return value Return:  The device serial number. |
| Notes        | Notes  |

### getImsi

| Prototype    | Prototype String[] getImsi() |
| ------------ | --- |
| Function     | Function Retrieves the IMSI number; if multiple exist, returns multiple. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  The IMSI number(s). |
| Notes        | Notes  |

### getImei

| Prototype    | Prototype String[] getImei() |
| ------------ | --- |
| Function     | Function Retrieves the IMEI number; if multiple exist, returns multiple. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  The IMEI number(s). |
| Notes        | Notes  |

### getVendorName

| Prototype    | Prototype String getVendorName() |
| ------------ | --- |
| Function     | Function Get the equipment supplier name (XC, Kozen) |
| Parameters   | Parameters  |
| Return Value | Return value Return:  Equipment supplier name |
| Notes        | Notes  |

### getDeviceModel

| Prototype    | Prototype String getDeviceModel() |
| ------------ | --- |
| Function     | Function Get the device model. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  The device model. |
| Notes        | Notes  |

### getOsVersion

| Prototype    | Prototype String getOsVersion() |
| ------------ | --- |
| Function     | Function Get the OS version number. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  If KozenOS is supported, return the KozenOS version number; if it is not supported, return the Android version number. |
| Notes        | Notes  |

### getKernelVersion

| Prototype    | Prototype String getKernelVersion() |
| ------------ | --- |
| Function     | Function Get the Linux kernel version number. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  The kernel version number. |
| Notes        | Notes  |

### getMcuVersion

| Prototype    | Prototype String getMcuVersion() |
| ------------ | --- |
| Function     | Function Retrieves the MCU version number. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  The MCU version number. |
| Notes        | Notes  |

### getHardwareVersion

| Prototype    | Prototype String getHardwareVersion() |
| ------------ | --- |
| Function     | Function Get the hardware version number. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  The hardware version number. |
| Notes        | Notes  |

### getEmvKernelVersion

| Prototype    | Prototype String getEmvKernelVersion() |
| ------------ | --- |
| Function     | Function Get the EMV kernel version number. |
| Parameters   | Parameters  |
| Return Value | Return value Return:  The EMV kernel version number. |
| Notes        | Notes  |

### getTUSN

| Prototype    | Prototype String getTUSN() |
| ------------ | --- |
| Function     | Function Get TUSN (Only for the China region) |
| Parameters   | Parameters  |
| Return Value | Return Value Return:TUSN |
| Notes        | Notes Returns the unique terminal serial number. |

### getCSN

| Prototype    | Prototype String getCSN() |
| ------------ | --- |
| Function     | Function Get customer serial number |
| Parameters   | Parameters  |
| Return Value | Return Value Return:CSN |
| Notes        | Notes Returns the customer serial number |


## Notes

- getImsi() and getImei() may return arrays for devices with multiple SIM slots.
- getTUSN() is only applicable in the China region.

## Related Links

- [[kozen-terminal-overview]]
- [[kozen-terminal-device]]
