---
title: "kozen-component-keyboard"
source: "KOZEN Component SDK Development Documentation _260129.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - keyboard
summary: "Defines Kozen Component SDK Keyboard module APIs for physical key input handling including start/stop keyboard listening, key press sound control, and InputCallback event notification."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-component-overview"
  - "kozen-component-errors"
  - "kozen-component-entities"
---

## Overview

Keyboard operation module providing physical key input event handling via IKeyboard obtained via ComponentEngine.INSTANCE.getKeyboardManager() or ComponentEngine.keyboardManager.

### Keyboard Interface Declaration

The keyboard is designed solely for general input and interaction purposes. It functions as a non-secure module and is not intended for sensitive data input.

To ensure user data security and comply with information security standards and regulatory requirements, it is strictly prohibited to use this module for processing or entering sensitive personal or financial information.

## Function List

| Function Name | Description |
|----|----|
| int startPhysicalKeyboard(InputCallback callback) | Start listening to physical keys |
| int stopPhysicalKeyboard() | Stop listening to physical keys |
| int switchKeyButtonVoiceEnable(boolean enable) | Enable or disable physical key press sound |
| int isKeyButtonVoiceEnable() | Get physical key press sound status |

## Details

### startPhysicalKeyboard

| Prototype    | int startPhysicalKeyboard(InputCallback callback) |
| ------------ | --- |
| Function     | Start listening to physical keys and return key values |
| Parameters   | callback - InputCallback listener for key events |
| Return Value | int result code |
| Notes        | — |

### stopPhysicalKeyboard

| Prototype    | int stopPhysicalKeyboard() |
| ------------ | --- |
| Function     | Stop listening to physical keys |
| Parameters   | — |
| Return Value | int result code |
| Notes        | — |

### switchKeyButtonVoiceEnable

| Prototype    | int switchKeyButtonVoiceEnable(boolean enable) |
| ------------ | --- |
| Function     | Enable or disable physical key press sound |
| Parameters   | enable - true to enable, false to disable |
| Return Value | int result code |
| Notes        | — |

### isKeyButtonVoiceEnable

| Prototype    | int isKeyButtonVoiceEnable() |
| ------------ | --- |
| Function     | Get physical key press sound status |
| Parameters   | — |
| Return Value | int result code |
| Notes        | — |

### Keyboard Listener (InputCallback)

| Prototype    | void onKey(KeyboardConstant.KeyCode keyCode, KeyboardConstant.KeyAction action) |
| ------------ | --- |
| Function     | Keyboard callback for key press events |
| Parameters   | keyCode - the code of the pressed key; action - the key action type |
| Return Value | — |
| Notes        | — |

## Notes

- See [[kozen-component-entities]] for KeyboardConstant.KeyCode and KeyAction enum definitions.
- The keyboard module is non-secure and should not be used for sensitive data input.

## Related Links

- [[kozen-component-overview]]
- [[kozen-component-errors]]
- [[kozen-component-entities]]
