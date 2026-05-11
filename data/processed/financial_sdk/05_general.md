 3.5 General Operation function ................................................................................................ 40
-- Get general operation module - getGeneralManager -- ................................................................ 40
3.5.1 Set buzzer ........................................................................................................................... 41
3.5.2 Set system navigation bar ...................................................................................................... 41
3.5.3 Set system status bar .............................................................................................................41
3.5.4 Wake up device ................................................................................................................... 42
3.5.5 Set system time .................................................................................................................... 42
3.5.6 Get time from system ............................................................................................................ 42
3.5.7 Get time zone .......................................................................................................................42
3.5.8 Set time zone ....................................................................................................................... 43
3.5.9 Reboot device ...................................................................................................................... 43
3.5.10 Shut down device ................................................................................................................43
3.5.11 Set system property value .................................................................................................... 43
3.5.12 Get system property value .................................................................................................... 44
3.5.13 Configures screen rotation function ....................................................................................... 44
3.5.14 Toggle LED light on/off ....................................................................................................... 44
3.5.15 Show or hide the LED view .................................................................................................. 44
3.5.16 Checks the version of dependency library .............................................................................. 45
3.5.17 Show or hide the notification quick settings panel ................................................................... 45
3.5.18 Set default visibility of the NFC logo ..................................................................................... 45
3.5.19 Control the device indicator light .......................................................................................... 46
 3.5 General Operation function                                                                      Set time
                                                                                                     Get time
-- Get general operation module - getGeneralManager --                                               Set time zone
                                                                                                     Get time zone
int setTime(long time)                                                                               Set Beep
long getTime()
int setTimeZone(String timeZone)                                                                     Set navigation bar
String getTimeZone()
int setBeep(boolean enable,                                                                          Set status bar
int times,                                                                                           Wake up device
int freq)                                                                                            Shut down device
int setNavigationBar(int type,                                                                       Get system property value
boolean isHide)                                                                                      Set system property value
int setStatusBar(boolean isHide)
int wakeUp()
int shutdown()
string getSystemProperty(String key)
setSystemProperty(String key,
String value)

                                                                                                 40
int setScreenRotation(boolean enable)                     Configure screen rotation functionality
void led(int type,                                        Switches the LED light between ON and OFF states
int status)
void setLedVisible(boolean visible)                       Sets the visibility of the LedView
String checkDependencyVersion(int type)                   Checks the version of dependency library
int setNotificationShade(boolean isEnable)                Set the Quick Settings dropdown menu to show/hide
int setNfcLogoVisible(boolean visiable)                   Default to hiding or showing the NFC logo
int setDeviceIndicator(int type,                          Device operation indicator light
int brightness,
boolean enable)

3.5.1 Set buzzer

Prototype         int setBeep(boolean enable,
Function          int times,
Parameters        int freq)
                  Set Beep
Return value      Parameters:
Notes             enable - begin or close buzzer
                  times - buzzer duration
                  freq - buzzer frequency
                  Return:
                  0: success
                  Others: failure - see GeneralError

3.5.2 Set system navigation bar

Prototype         int setNavigationBar(int type,
Function          boolean isHide)
Parameters        Set system navigation bar
                  Parameters:
Return value      type - the type of navigation bar to be operated
Notes             1: back 2: home 3: recent
                  isHide - the state of the navigation bar to be operated
                  true: hidden false: displayed
                  Return:
                  0: success
                  Others: failure - see GeneralError

3.5.3 Set system status bar

Prototype         int setStatusBar(boolean isHide)

                                                      41
Parameters           isHide - the state of the navigation bar to be operated
Return value         true: hidden false: displayed
                     Return:
Notes                0: success
                     Others: failure - see GeneralError

3.5.4 Wake up device

Prototype            int wakeUp()
Function             Wake up device
Parameters
Return value         Return:
                     0: success
Notes                Others: failure - see GeneralError

3.5.5 Set system time

Prototype            int setTime(long time)
Function             Set system time
Parameters
Return value         Return:
                     0: success
Notes                Others: failure - see GeneralError

3.5.6 Get time from system

Prototype            int getTime()
Function             Get time from system
Parameters
Return value         Return:
                     0: success
Notes                Others: failure - see GeneralError

3.5.7 Get time zone

Prototype            String getTimeZone()

Function             Get time zone

Parameters

Return value         Returns:

                     Time zone

Notes

                                                         42

Prototype            int setTimeZone(String timeZone)
Function             Set time zone
Parameters           Parameters:
                     timeZone - time zone id, supports two formats:
Return value         1. Region/City 2. GMT
                     Example 1: setTimeZone("Europe/Moscow")
Notes                Example 2: setTimeZone("GMT+9")
                     Return:
                     0: success
                     Others: failure - see GeneralError

3.5.9 Reboot device

Prototype            int reboot()
Function             Reboot device
Parameters
Return value         Return:
                     0: success
Notes                Others: failure - see GeneralError

3.5.10 Shut down device

Prototype            int shutdown()
Function             Shut down device
Parameters
Return value         Return:
                     0: success
Notes                Others: failure - see GeneralError

3.5.11 Set system property value

Prototype            int setSystemProperty(String key, String value)
Function             Set system property value
Parameters           Parameters:
                     key - the key of the system property(ro.product.model)
Return value         value - the value of the system property
                     Return:
Notes                0: success
                     Others: failure - see GeneralError

                                                         43

Prototype     String getSystemProperty(String key)
Function      Get system property value
Parameters    Parameters:
              key - the key of the system property (ro.product.model)
Return value  Return:
              Return the value of the system property by string form, or null if it cannot be read
Notes

3.5.13 Configures screen rotation function

Prototype     int setScreenRotation(boolean enable)
Function      Configures screen rotation function
              Parameters:
Parameters    enable
              - true: Enable screen rotation
Return value  - false: Disable screen rotation
Notes         0: Success
              Others: failure - see GeneralError

3.5.14 Toggle LED light on/off

Prototype     void led(int type,
Function      int status)
Parameters    Toggle LED light on/off
              Parameters:
Return Value  type - LED light type (range: 1­4):
Notes         1 - Blue
              2 - Yellow
              3 - Green
              4 - Red
              status- Switch state:
              1 - Turn on
              0 - Turn off

              This method is used to control the on/off state of different colored LED lights.

3.5.15 Show or hide the LED view

Prototype     void setLedVisible(boolean visible)
Function      Show or hide the LED view
              Parameters:
Parameters    visible
              true: show the LED view

                                                                             44
Notes         Controls the visibility of the on-screen LED view component.

3.5.16 Checks the version of dependency library

Prototype     String checkDependencyVersion(int type)
Function      Checks the version of dependency library
Parameters    Parameters:
              type - Dependency type:
Return Value  0 - EMV kernel
Notes         1 - POI
              2 - UART
              3 - Scanner box
              Return:
              Version string of the specified dependency
              This method returns the version number of the selected module by type.

3.5.17 Show or hide the notification quick settings panel

Prototype     int setNotificationShade(boolean isEnable)
Function      Show or hide the notification quick settings panel
Parameters    Parameters:
              isEnable -
Return Value  true: Show the quick settings dropdown (default)
Notes         false: Hide the quick settings dropdown
              Return:
              0 - Operation succeeded
              Others - Operation failed (see CommonError for details)
              Controls the visibility of the Android notification shade's quick settings panel.

3.5.18 Set default visibility of the NFC logo

Prototype     int setNfcLogoVisible(boolean visible)
Function      Set default visibility of the NFC logo
Parameters    Parameters:
              visible -
Return Value  true: Show NFC logo
Notes         false: Hide NFC logo
              Return:
              0 - Operation succeeded
              Others - Operation failed (see CommonError for details)
              Sets whether the NFC logo is shown by default.
              This setting persists after reboot until changed again.

                                                           45

Prototype     int setDeviceIndicator(int type,
Function      int brightness,
Parameters    boolean enable)
              Control the device indicator light
Return Value  Parameters:
Notes         type - Indicator type:
              ConstantGeneral.IndicatorType.PINPAD_PHYSICAL
              ConstantGeneral.IndicatorType.PINPAD_CAPACITIVE
              brightness - Brightness level (range: 0­255, 0 turns off the indicator)
              enable - Indicator switch: true to enable, false to disable
              Return:
              0 - Success
              Others - Failure (see GeneralError)
              Controls brightness and on/off state of the specified device indicator light.

