---
title: "kozen-component-entities"
source: "KOZEN Component SDK Development Documentation _260129.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - entity_classes
summary: "Defines entity class constants and enums used in the Kozen Component SDK: KeyboardConstant.KeyCode and KeyboardConstant.KeyAction."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-component-overview"
  - "kozen-component-keyboard"
---

## Overview

Entity class definitions providing constants and enums used throughout the Kozen Component SDK.

## Entity Class Definition

### KeyboardConstant.KeyCode

| Constant Name | Description | Type | HexValue |
| --- | --- | --- | --- |
| BUTTON_0 | Number key 0 | ENUM | 0x30 |
| BUTTON_1 | Number key 1 | ENUM | 0x31 |
| BUTTON_2 | Number key 2 | ENUM | 0x32 |
| BUTTON_3 | Number key 3 | ENUM | 0x33 |
| BUTTON_4 | Number key 4 | ENUM | 0x34 |
| BUTTON_5 | Number key 5 | ENUM | 0x35 |
| BUTTON_6 | Number key 6 | ENUM | 0x36 |
| BUTTON_7 | Number key 7 | ENUM | 0x37 |
| BUTTON_8 | Number key 8 | ENUM | 0x38 |
| BUTTON_9 | Number key 9 | ENUM | 0x39 |
| BUTTON_ASTERISK | Asterisk key (*) or Multiply key (x) | ENUM | 0x2A |
| BUTTON_PLUS | Plus key (+) | ENUM | 0x2B |
| BUTTON_MINUS | Minus key (-) | ENUM | 0x2D |
| BUTTON_DIVIDE | Divide key (/) | ENUM | 0x2F |
| BUTTON_POUND | Pound key (#) | ENUM | 0x23 |
| BUTTON_DOT | Dot key (.) | ENUM | 0x2E |
| BUTTON_ENTER | Enter key | ENUM | 0x0D |
| BUTTON_BACKSPACE | Backspace key | ENUM | 0x08 |
| BUTTON_ESC | ESC key | ENUM | 0x1B |
| BUTTON_FN | FN key (keyboard extension) | ENUM | 0xE0 |
| BUTTON_HORN | Horn key (for communication) | ENUM | 0x98 |
| BUTTON_PAGEDOWN | Page Down key | ENUM | 0x22 |
| BUTTON_PAGEUP | Page Up key | ENUM | 0x21 |
| BUTTON_USER_DEFINED | User-defined key (custom key value, Kozen button) | ENUM | 0x99 |


### KeyboardConstant.KeyAction

| Constant Name | Description | Type | Value |
| --- | --- | --- | --- |
| ACTION_DOWN | Key press down | int | 0 |
| ACTION_UP | Key release | int | 1 |

## Related Links

- [[kozen-component-overview]]
- [[kozen-component-keyboard]]
- [[kozen-component-errors]]
