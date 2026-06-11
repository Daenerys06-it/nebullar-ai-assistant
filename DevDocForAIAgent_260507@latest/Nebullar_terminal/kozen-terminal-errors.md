---
title: "kozen-terminal-errors"
source: "KOZEN Terminal manager SDK Development Documentation_260422.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - error_code
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines all error codes for the Kozen Terminal Manager SDK across five modules: CertificationError (-10xxx to -19999), DeviceError (-20xxx), LocationError (-30xxx), NetworkError (-40xxx), and ResourceError (-50xxx)."
---

## Overview

Error codes defined across all Kozen Terminal Manager SDK modules. All error codes use negative integer values.

## Error Code List

### CertificationError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| CERTIFICATION_ERROR_INIT | Certification manager service initialization exception | -10000 |
| CERTIFICATION_ERR_PARA_ERROR | Parameter exception | -10001 |
| CERTIFICATION_CERT_LIST_CHECK_FAIL_ERROR | Certificate chain validation exception | -10002 |
| CERTIFICATION_OTHER_ERROR | Other exceptions | -19999 |


### DeviceError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| DEVICE_ERROR_INIT | Device manager service initialization exception | -20000 |
| DEVICE_OTHER_ERROR | Other exceptions | -20001 |
| DEVICE_PARAMETERS_INVALID | Invalid parameters | -20002 |


### LocationError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| MANAGER_SERVICE_DISCONNECT | Device management service is not connected, please initialize the device management service first. | -30001 |
| ERROR_INIT | Positioning module is not open or initialized. | -30002 |
| ERROR_POSITIONING_PROGRESS | Positioning is in progress. If positioning is in progress, repeated positioning is prohibited. Stop positioning first and then restart it. | -30003 |
| ERROR_UNKNOWN | Unknown error. | -30004 |
| ERROR_PARAMETERS_INVALID | Invalid parameters. | -30005 |
| ERROR_MISS_PERMISSIONS | Missing location permissions. | -30006 |
| ERROR_CODE_INVALID_PARAMETER | Some important parameters are empty. | -31001 |
| ERROR_CODE_FAILURE_WIFI_INFO | Positioning failed because the device only scanned a single WiFi, and the location information cannot be accurately calculated. | -31002 |
| ERROR_CODE_FAILURE_LOCATION_PARAMETER | The obtained request parameters are empty, possibly due to an exception during the process. | -31003 |
| ERROR_CODE_FAILURE_CONNECTION | Network connection exception. Detailed information can be obtained through AMapLocation.getLocationDetail(). | -31004 |
| ERROR_CODE_FAILURE_PARSER | XML parsing error. | -31005 |
| ERROR_CODE_FAILURE_LOCATION | Positioning result error. | -31006 |
| ERROR_CODE_FAILURE_AUTH | KEY error. | -31007 |
| ERROR_CODE_UNKNOWN | Other errors. | -31008 |
| ERROR_CODE_FAILURE_INIT | Initialization exception. | -31009 |
| ERROR_CODE_SERVICE_FAIL | Positioning service startup failed. Please check if the service is configured and if the service tag in the manifest is placed inside the application tag. | -31010 |
| ERROR_CODE_FAILURE_CELL | Incorrect base station information. Please check if the SIM card is installed. | -31011 |
| ERROR_CODE_FAILURE_LOCATION_PERMISSION | Missing location permissions. Please check if location permissions are configured and enable location permissions in security software and settings. | -31012 |
| ERROR_CODE_FAILURE_NOWIFIANDAP | Network positioning failed. Please check if the device has a SIM card inserted, mobile network is enabled, or the WiFi module is turned on. | -31013 |
| ERROR_CODE_FAILURE_NOENOUGHSATELLITES | Satellite positioning failed due to insufficient available satellites. | -31014 |
| ERROR_CODE_FAILURE_SIMULATION_LOCATION | The location may be simulated. | -31015 |
| ERROR_CODE_AIRPLANEMODE_WIFIOFF | Positioning failed. Airplane mode is on and the WiFi switch is off. Please turn off airplane mode or turn on the WiFi switch. | -31018 |
| ERROR_CODE_NOCGI_WIFIOFF | Positioning failed. No SIM card detected and the WiFi switch is off. Please turn on the WiFi switch or insert a SIM card. | -31019 |
| ERROR_CODE_FAILURE_COARSE_LOCATION | Positioning failed due to an exception under coarse permissions. | -31020 |
| GEO_ERROR_CODE_INVALID_PARAMETER | Parameter error. | -32001 |
| GEO_ERROR_CODE_FAILURE_CONNECTION | Network connection exception. | -32004 |
| GEO_ERROR_CODE_FAILURE_PARSER | Data parsing failed (possibly due to connecting to a network that requires login but not logged in). | -32005 |
| GEO_ERROR_CODE_FAILURE_AUTH | Authentication failed. | -32007 |
| GEO_ERROR_CODE_UNKNOWN | Other unknown errors. | -32008 |
| GEO_ERROR_NO_VALIDFENCE | No valid geofence available. | -32016 |
| GEO_ERROR_CODE_EXISTS | The same fence already exists and does not need to be added again. Applies when the geofence's customID is the same. | -32017 |


### NetworkError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| NETWORK_ERROR_INIT | Network module initialization error | -40000 |
| NETWORK_OTHER_ERROR | Other exceptions | -40001 |
| NETWORK_PARAMETERS_INVALID | Invalid parameters | -40002 |


### ResourceError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| RESOURCE_ERROR_INIT | Resource module initialization error | -50000 |
| RESOURCE_OTHER_ERROR | Other error | -50001 |
| RESOURCE_REGISTER_UPGRADE_LISTENER_ERROR | Failed to register MCU upgrade listener | -50002 |
| RESOURCE_MCU_UPGRADE_FILE_PATH_ERROR | MCU upgrade file path error | -50003 |
| RESOURCE_MCU_UPGRADE_FILE_ERROR | MCU upgrade file error | -50004 |
| RESOURCE_MCU_UPGRADE_ERROR | MCU upgrade error | -50005 |
| RESOURCE_APP_UPGRADE_ERROR | App upgrade error | -50006 |
| RESOURCE_APP_UPGRADE_ERROR_ABORTED | App upgrade error — aborted | -50007 |
| RESOURCE_APP_UPGRADE_ERROR_BLOCKED | App upgrade error — blocked | -50008 |
| RESOURCE_APP_UPGRADE_ERROR_CONFLICT | App upgrade error — conflict | -50009 |
| RESOURCE_APP_UPGRADE_ERROR_INCOMPATIBLE | App upgrade error — incompatible | -50010 |
| RESOURCE_APP_UPGRADE_ERROR_INVALID | App upgrade error — invalid | -50011 |
| RESOURCE_APP_UPGRADE_ERROR_STORAGE | App upgrade error — storage error | -50012 |
| RESOURCE_ERROR_INIT | Resource module initialization error | -50000 |

## Related Links

- [[kozen-terminal-overview]]
- [[kozen-terminal-certification]]
- [[kozen-terminal-device]]
- [[kozen-terminal-location]]
- [[kozen-terminal-network]]
- [[kozen-terminal-resource]]
- [[kozen-terminal-entities]]
