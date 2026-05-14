---
title: "kozen-component-errors"
source: "KOZEN Component SDK Development Documentation _260129.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - error_code
summary: "Defines all error codes for the Kozen Component SDK: CommonError, KeyboardError, and SecondaryScreenError."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-component-overview"
  - "kozen-component-keyboard"
  - "kozen-component-secondary-screen"
---

## Overview

Error codes defined across all Kozen Component SDK modules.

## Error Code List

### CommonError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| FEATURE_NOPERMISSION | Feature no-permission | -10011 |
| DEVICE_BUSY | Device is busy | -10005 |
| FEATURE_UNSUPPORTED | Feature unsupported | -10003 |
| PARAMETERS_INVALID | Parameters invalid | -10002 |
| SERVICE_DISCONNECT | Services are not connected, please initialize financial services | -10001 |
| VERSION_NOT_MATCH | Version mismatch | -10004 |


### KeyboardError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| KEYBOARD_UNKNOWN | Unknown error | -30001 |
| KEYCODE_UNDEFINED | Key not defined | -30002 |


### SecondaryScreenError

| Error Code | Error Description | Error Value |
| --- | --- | --- |
| VICE_SCREEN_CANCELED | Operation terminated | -20005 |
| VICE_SCREEN_DECODE_FAILED | Decoding failed | -20003 |
| VICE_SCREEN_INVALID_DATA | Invalid data | -20002 |
| VICE_SCREEN_TIMEOUT | Interface call timeout | -20001 |
| VICE_SCREEN_UNKNOWN | Unknown error | -20004 |

## Related Links

- [[kozen-component-overview]]
- [[kozen-component-keyboard]]
- [[kozen-component-secondary-screen]]
- [[kozen-component-entities]]
