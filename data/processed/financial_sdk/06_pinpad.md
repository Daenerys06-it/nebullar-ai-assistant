 3.6 PINPAD Operation module ................................................................................................ 46
-- Get pinpad module - getPinpadManager -- ................................................................................ 46
3.6.1 Start Input PIN by provided view ............................................................................................ 46
3.6.2 Start Input PIN by default view ...............................................................................................47
3.6.3 Cancel PIN entry ..................................................................................................................47
3.6.4 Check if blind keyboard mode is enabled .................................................................................47
3.6.5 Toggle between blind and normal keyboard modes .................................................................... 48
3.6.6 Check whether the PINPAD is virtual or physical ..................................................................... 48
-- PIN input callback - PinpadInputCallback -- ............................................................................ 48

                                                                                         4
3.6.8 Error callback ......................................................................................................................49
3.6.9 Return when confirm PIN input ..............................................................................................49
3.6.10 Screen rotation callback when use PINPAD ............................................................................49
 3.6 PINPAD Operation module                  Cancel PIN entry
                                              Start Input PIN, take over TP according to the
-- Get pinpad module - getPinpadManager --    default view
                                              Start Input PIN, take over TP according to the
void cancelInputPin()                         incoming view
void startInputPin(android.os.Bundle params,
PinpadInputCallback callback)                 Check if blind keyboard mode is enabled
void startInputPin(android.os.Bundle params,  Toggle between blind keyboard mode and normal
Map<String,android.view.View> keyViews,       keyboard mode
PinpadInputCallback callback)                 Get the keyboard type
boolean isBlindModeEnable()
int switchBlindMode()

int getPinpadType()

3.6.1 Start Input PIN by provided view

Prototype     void startInputPin(android.os.Bundle params,
              Map<String,android.view.View> keyViews,
Function      PinpadInputCallback callback)
Parameters    Start PIN entry and take over touch processing based on the provided views
              Parameters:
              params - PIN configuration parameters. See
              ConstantEmv.POIEmvCoreManager.EmvPinConstraints for details

              keyViews -- View map for PIN keys. Example:
              Map<String, View> keyViews = new HashMap<>();
              keyViews.put(PinViewEnum.BUTTON0.getType(), button0);

                                                                             46
              keyViews.put(PinViewEnum.BUTTON2.getType(), button2);
              keyViews.put(PinViewEnum.BUTTON3.getType(), button3);
              keyViews.put(PinViewEnum.BUTTON4.getType(), button4);
              keyViews.put(PinViewEnum.BUTTON5.getType(), button5);
              keyViews.put(PinViewEnum.BUTTON6.getType(), button6);
              keyViews.put(PinViewEnum.BUTTON7.getType(), button7);
              keyViews.put(PinViewEnum.BUTTON8.getType(), button8);
              keyViews.put(PinViewEnum.BUTTON9.getType(), button9);
              keyViews.put(PinViewEnum.BUTTON_ENTER.getType(), buttonEnter);
              keyViews.put(PinViewEnum.BUTTON_CLEAR.getType(), buttonBackspace);
              keyViews.put(PinViewEnum.BUTTON_ESC.getType(), buttonEsc);

Return value  callback - the PIN input callback
Notes         take over TP according to the provided view

3.6.2 Start Input PIN by default view

Prototype     void startInputPin(android.os.Bundle params,
Function      PinpadInputCallback callback)
Parameters    Start input PIN and take over TP according to the default view
              Parameters:
Return value  params - PIN configuration parameters
Notes         Detail information refer to ConstantEmv.POIEmvCoreManager.EmvPinConstraints
              callback - the PIN input callback

              take over TP according to the default view

3.6.3 Cancel PIN entry

Prototype     void cancelInputPin()
Function      Cancel PIN entry
Parameters
Return value
Notes

3.6.4 Check if blind keyboard mode is enabled

Prototype     boolean isBlindModeEnable()
Function      Check if blind keyboard mode is enabled
Parameters
Return Value  Return:
              true - Blind keyboard mode is enabled
Notes         false - Normal keyboard mode
              This method returns the current state of the keyboard mode.

                                                                             47

Prototype     int switchBlindMode()
Function      Toggle between blind and normal keyboard modes
Parameters
Return Value  Return:
              0 - Success
Notes         Others - Failure. See PinpadError for details
              This method switches the keyboard mode.
              Typically used to assist visually impaired users.

3.6.6 Check whether the PINPAD is virtual or physical

Prototype     int getPinpadType()
Function      Check whether the PINPAD is virtual or physical
Parameters
Return Value  Return:
              0 - Virtual PINPAD
Notes         1 - Physical PINPAD
              Others - Failure (see PinpadError)

-- PIN input callback - PinpadInputCallback --

void onInput(int len,                                                 Key press event
int key)                                                              Callback on error
void onPinError(int verifyResult,                                     Invoked when the user confirms PIN entry
int pinTryCntOut)
void onPinSuccess(int verifyResult,                                   Screen rotation callback
byte[] pinBlock,
String ksn)
void onScreenRotation()

3.6.7 Key press event

Prototype     void onInput(int len,
Function      int key)
Parameters    Key press event
              Parameters:
Return value  len - The length of the password that has been entered
Notes         key - The current key value, uniformly returns *

                                                       48

Prototype             void onPinError(int verifyResult,
Function              int pinTryCntOut)
Parameters            Error callback
                      Parameters:
Return value          verifyResult - Error code, refer to ConstantEmv.POIEmvCoreManager.EmvPinConstraints
Notes                 pinTryCntOut - Number of PIN retry attempts

3.6.9 Return when confirm PIN input

Prototype             void onPinSuccess(int verifyResult, byte[] pinBlock, String ksn)
Function              Return when confirm PIN input
Parameters            Parameters:
                      verifyResult - The result of the PIN confirmation, 0 means successful PIN confirmation.
Return value          pinBlock - The ciphertext of the password calculated by PINPAD.
Notes                 ksn - Will returned when DUKPT type

3.6.10 Screen rotation callback when use PINPAD

Prototype             void onScreenRotation()
Function              Screen rotation callback when use PINPAD
Parameters
Return Value          This method is triggered when the screen orientation changes.
Notes

