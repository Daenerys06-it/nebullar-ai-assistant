---
title: "kozen-terminal-entities"
source: "KOZEN Terminal manager SDK Development Documentation_260422.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - entity_classes
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines entity class constants, enum values, and configuration data structures used across the Kozen Terminal Manager SDK including Const, LocationConstant (GeoLanguage, LocationMode, SignalMode), ApnConfiguration, and WakeUpType."
---

## Overview

Entity class definitions providing constants, enums, and configuration structures used throughout the Kozen Terminal Manager SDK.

## Entity Class Definition

### com.kozen.terminalmanager.Const

| Constant Name | Type | Value |
| --- | --- | --- |
| FUN_ERROR | int | -1 |
| FUN_SUCC | int | 0 |
| TERMINAL_MANAGER_SERVICE_ACTION | String | "android.intent.action.XC_TERMINAL_MANAGER_SERVICE" |
| TERMINAL_MANAGER_SERVICE_CLASS | String | "com.kozen.terminalmanager.service.TerminalManagerService" |
| TERMINAL_MANAGER_SERVICE_PACKAGE | String | "com.kozen.terminalmanager.service" |


### com.kozen.terminalmanager.location.constant.LocationConstant

### GeoLanguage

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| DEFAULT | ENUM | Returns reverse geocoding info in local language  |
| EN | ENUM | Always returns reverse geocoding info in English |
| ZH | ENUM | Always returns reverse geocoding info in Chinese |

### LocationMode

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| Battery_Saving | ENUM | Low-power positioning mode |
| Device_Sensors | ENUM | Device-only positioning mode |
| Hight_Accuracy | ENUM | High-accuracy positioning mode |

### SignalMode

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| BEIDOU_FIRST | ENUM | In high-accuracy positioning mode, performs a single location operation and prioritizes returning BeiDou satellite positioning information. |
| DEFAULT | ENUM | In high-accuracy positioning mode, performs a single location operation, and the system returns the first available positioning result. |
| GPS_FIRST | ENUM | In high-accuracy positioning mode, performs a single location operation and prioritizes returning GPS satellite positioning information |

### Location Constants (GEO_*)

| Constant Name | Type | Value |
| --- | --- | --- |
| GEO_BUNDLE_KEY_CUSTOMID | String | "customId" |
| GEO_BUNDLE_KEY_FENCESTATUS | String | "event" |
| GEO_BUNDLE_KEY_LOCERRORCODE | String | "location_errorcode" |
| GEO_STATUS_IN | int | 1 |
| GEO_STATUS_LOCFAIL | int | 4 |
| GEO_STATUS_OUT | int | 2 |
| GPS_ACCURACY_BAD | int | 0 |
| GPS_ACCURACY_GOOD | int | 1 |
| GPS_ACCURACY_UNKNOWN | int | -1 |
| GPS_STATUS_MODE_SAVING | int | 3 |
| GPS_STATUS_NOGPSPERMISSION | int | 4 |
| GPS_STATUS_NOGPSPROVIDER | int | 1 |
| GPS_STATUS_OFF | int | 2 |
| GPS_STATUS_OK | int | 0 |
| LOCATION_PROVIDER_GPS | String | "gps" |
| LOCATION_PROVIDER_LBS | String | "lbs" |
| LOCATION_TYPE_CELL | int | 6 |
| LOCATION_TYPE_COARSE_LOCATION | int | 11 |
| LOCATION_TYPE_FIX_CACHE | int | 4 |
| LOCATION_TYPE_GPS | int | 1 |
| LOCATION_TYPE_LAST_LOCATION_CACHE | int | 9 |
| LOCATION_TYPE_OFFLINE | int | 8 |
| LOCATION_TYPE_SAME_REQ | int | 2 |
| LOCATION_TYPE_WIFI | int | 5 |
| TRUSTED_LEVEL_BAD | int | 4 |
| TRUSTED_LEVEL_HIGH | int | 1 |
| TRUSTED_LEVEL_LOW | int | 3 |
| TRUSTED_LEVEL_NORMAL | int | 2 |


### com.kozen.terminalmanager.device.constant.WakeUpType

| Enum Constant | TYPE | Description |
| --- | --- | --- |
| TAP_OR_INSERT_CARD | ENUM | Wake up by IC card insertion or NFC card tapping |
| SCREEN_DOUBLE_TAP | ENUM | Wake up by screen double tap |
| LIFT_TO_WAKE | ENUM | Lift to wake screen |


### ApnConfiguration

| Constant Name | Type | Description |
|---|-|-|
| apn | String | APN name. |
| authType | int | Authentication type. |
| current | boolean | Enable current APN. |
| mcc | String | Mobile Country Code (MCC). |
| mmsc | String | MMSC URL. |
| mmsPort | String | MMS proxy port. |
| mmsProxy | String | MMS proxy address. |
| mnc | String | MNC Mobile Network Code (MNC). |
| name | String | Entry name. |
| numeric | String | Operator Network Identification. |
| password | String | APN password. |
| port | String | Proxy port. |
| protocol | String | The protocol to use to connect to this APN. |
| proxy | String | Proxy address. |
| roaming_protocol | String | The protocol to use to connect to this APN when roaming. |
| server | String | Server address. |
| type | String | Comma-delimited list of APN types. |
| user | String | APN username. |

## Related Links

- [[kozen-terminal-overview]]
- [[kozen-terminal-device]]
- [[kozen-terminal-location]]
- [[kozen-terminal-network]]
- [[kozen-terminal-errors]]
