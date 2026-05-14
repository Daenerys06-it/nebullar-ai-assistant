---
title: "kozen-financial-pinpad"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - pinpad
summary: "Defines Kozen Financial SDK PINPAD module APIs for PIN entry including start/cancel input (with custom or default view), blind mode toggle, type check, and PinpadInputCallback (onInput, onPinError, onPinSuccess, onScreenRotation)."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-financial-overview"
  - "kozen-financial-init"
---

## Overview

PINPAD operation module providing secure PIN entry via IPinpadManager from FinancialEngine.INSTANCE.getPinpadManager() or FinancialEngine.pinpadManager().

## Function List

| Function Name | Description |
|--            |-----------|
| void startInputPin(android.os.Bundle params,  Map<String,android.view.View> keyViews,  PinpadInputCallback callback) | Start PIN entry and take over touch processing based on the provided views |
| void startInputPin(android.os.Bundle params,  PinpadInputCallback callback) | Start input PIN and take over TP according to the default view |
| void cancelInputPin() | Cancel PIN entry |
| boolean isBlindModeEnable() | Check if blind keyboard mode is enabled |
| int switchBlindMode() | Toggle between blind and normal keyboard modes |
| int getPinpadType() | Check whether the PINPAD is virtual or physical |
| void onScreenRotation() | Screen rotation callback when use PINPAD |

## Details

### startInputPin (custom view)

| Prototype    | Prototype void startInputPin(android.os.Bundle params,  Map<String,android.view.View> keyViews,  PinpadInputCallback callback) |
| ------------ | --- |
| Function     | Function Start PIN entry and take over touch processing based on the provided views |
| Parameters   | Parameters Parameters: params - PIN configuration parameters. See ConstantEmv.POIEmvCoreManager.EmvPinConstraints for details  keyViews -- View map for PIN keys. Example: Map<String, View> keyViews = new HashMap<>(); keyViews.put(PinViewEnum.BUTTON0.getType(), button0); keyViews.put(PinViewEnum.BUTTON1.getType(), button1); keyViews.put(PinViewEnum.BUTTON2.getType(), button2); keyViews.put(PinViewEnum.BUTTON3.getType(), button3); keyViews.put(PinViewEnum.BUTTON4.getType(), button4); keyViews.put(PinViewEnum.BUTTON5.getType(), button5); keyViews.put(PinViewEnum.BUTTON6.getType(), button6); keyViews.put(PinViewEnum.BUTTON7.getType(), button7); keyViews.put(PinViewEnum.BUTTON8.getType(), button8); keyViews.put(PinViewEnum.BUTTON9.getType(), button9); keyViews.put(PinViewEnum.BUTTON_ENTER.getType(), buttonEnter); keyViews.put(PinViewEnum.BUTTON_CLEAR.getType(), buttonBackspace); keyViews.put(PinViewEnum.BUTTON_ESC.getType(), buttonEsc);  callback - the PIN input callback |
| Return Value | Return value  |
| Notes        | Notes take over TP according to the provided view |

### startInputPin (default)

| Prototype    | Prototype void startInputPin(android.os.Bundle params,  PinpadInputCallback callback) |
| ------------ | --- |
| Function     | Function Start input PIN and take over TP according to the default view |
| Parameters   | Parameters Parameters: params - PIN configuration parameters Detail information refer to ConstantEmv.POIEmvCoreManager.EmvPinConstraints callback - the PIN input callback |
| Return Value | Return value  |
| Notes        | Notes take over TP according to the default view |

### cancelInputPin

| Prototype    | Prototype void cancelInputPin() |
| ------------ | --- |
| Function     | Function Cancel PIN entry |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes  |

### isBlindModeEnable

| Prototype    | Prototype boolean isBlindModeEnable() |
| ------------ | --- |
| Function     | Function Check if blind keyboard mode is enabled |
| Parameters   | Parameters  |
| Return Value | Return Value Return: true - Blind keyboard mode is enabled false - Normal keyboard mode |
| Notes        | Notes This method returns the current state of the keyboard mode. |

### switchBlindMode

| Prototype    | Prototype int switchBlindMode() |
| ------------ | --- |
| Function     | Function Toggle between blind and normal keyboard modes |
| Parameters   | Parameters  |
| Return Value | Return Value Return: 0 - Success Others - Failure. See PinpadError for details |
| Notes        | Notes This method switches the keyboard mode.  Typically used to assist visually impaired users. |

### getPinpadType

| Prototype    | Prototype int getPinpadType() |
| ------------ | --- |
| Function     | Function Check whether the PINPAD is virtual or physical |
| Parameters   | Parameters  |
| Return Value | Return Value Return: 0 - Virtual PINPAD 1 - Physical PINPAD Others - Failure (see PinpadError) |
| Notes        | Notes  |

### PinpadInputCallback


#### onInput (Key press)

| Prototype    | Prototype void onInput(int len, int key) |
| ------------ | --- |
| Function     | Function Key press event |
| Parameters   | Parameters Parameters: len - The length of the password that has been entered key - The current key value, uniformly returns * |
| Return Value | Return value  |
| Notes        | Notes  |


#### onPinError

| Prototype    | Prototype void onPinError(int verifyResult,  int pinTryCntOut) |
| ------------ | --- |
| Function     | Function Error callback |
| Parameters   | Parameters Parameters: verifyResult - Error code, refer to ConstantEmv.POIEmvCoreManager.EmvPinConstraints pinTryCntOut - Number of PIN retry attempts |
| Return Value | Return value  |
| Notes        | Notes  |


#### onPinSuccess

| Prototype    | Prototype void onPinSuccess(int verifyResult, byte[] pinBlock, String ksn) |
| ------------ | --- |
| Function     | Function Return when confirm PIN input |
| Parameters   | Parameters Parameters: verifyResult - The result of the PIN confirmation, 0 means successful PIN confirmation. pinBlock - The ciphertext of the password calculated by PINPAD. ksn - Will returned when DUKPT type |
| Return Value | Return value  |
| Notes        | Notes  |


#### onScreenRotation

| Prototype    | Prototype void onScreenRotation() |
| ------------ | --- |
| Function     | Function Screen rotation callback when use PINPAD |
| Parameters   | Parameters  |
| Return Value | Return Value  |
| Notes        | Notes This method is triggered when the screen orientation changes. |

## Notes

No additional notes.

## Related Links

- [[kozen-financial-overview]]
- [[kozen-financial-init]]
