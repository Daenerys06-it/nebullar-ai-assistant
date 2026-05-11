 3.4 Device module

-- Get device module - getDeviceManager--

int cancelPCIReboot()                                     Cancel scheduled reboot
long getSystemTime()                                      Return the timestamp of the current system
                                                          time
String getTimeZone()                                      Get the current time zone
void reboot()                                             Reboot the device
int setPCIReboot(long time)                               Schedule a reboot
int setSystemTime(long time)                              Set the system time
int setTimeZone(String timeZone)                          Set the time zone
void shutdown()                                           Shut down the device
void forcePermission(boolean isOpen)                      Forced permission request
Void setSilentInstall(boolean isOpen)                     Silent app installation

                                                  14
int sleep(boolean isConfirm)                                   Turn off (sleep) the screen
int wakeUp(WakeUpType type, boolean enable)                    Enable or disable various device wake-up

3.4.1 Sets the system time

Prototype     int setSystemTime(long time)
Function      Sets the system time.
Parameters    time - Timestamp.
              Return:
Return value  0: Success,
              Others: Failure (refer to DeviceError).
Notes

3.4.2 Returns the current system time as a timestamp

Prototype     long getSystemTime()
Function      Returns the current system time as a timestamp.
Parameters
              Return:
Return value  The timestamp.

Notes

3.4.3 Sets the time zone

Prototype     int setTimeZone(String timeZone)
Function      Sets the time zone.
Parameters    timeZone - Time zone ID, supports two formats:
              1. Region/City (e.g., Europe/Moscow)
Return value  2. GMT (e.g., GMT+9).
Notes         Return:
              0: Success,
              Others: Failure (refer to DeviceError).

3.4.4 Get the current time zone

Prototype     String getTimeZone()
Function      Retrieves the current time zone.
Parameters
              Return:
Return value  The time zone.

Notes

                                                       15

Prototype     void reboot()
Function      Reboots the device
Parameters
Return value
Notes

3.4.6 Shuts down the device

Prototype     void shutdown()
Function      Shuts down the device.
Parameters
Return value
Notes

3.4.7 Schedules a timed reboot

Prototype     int setPCIReboot(long time)
Function      Schedules a timed reboot.
Parameters    time - Device will reboot after running for this duration (e.g., 1000 * 60 * 60 for 1 hour).
Return value  Return:
              0: Success, Others: Failure (refer to DeviceError).
Notes         1. The policy will automatically run after reboot unless canceled by cancelPCIReboot.
              2. A reboot prompt will be shown before rebooting.
              3. It is recommended not to exceed 24 hours.
              4. If the set time is less than the device's uptime, it will reboot immediately.

3.4.8 Cancels the scheduled reboot

Prototype     int cancelPCIReboot()
Function      Cancels the scheduled reboot.
Parameters
              Return:
Return value  0: Success, Others: Failure (refer to DeviceError).

Notes

3.4.9 Enable or disable silent installation

Prototype     void setSilentInstall(boolean isOpen)
Function      Enable or disable silent installation
Parameters    Parameters:
              isOpen -
Return Value  true: Do not show app installation prompt (silent install)
              false: Show installation prompt

                                                                             16

3.4.10 Enforce runtime permission checks

Prototype     void forcePermission(boolean isOpen)
Function      Enforce runtime permission checks
Parameters    Parameters:
              isOpen -
Return Value  true: The app must request permission to access a module
Notes         false: No permission enforcement

              When enabled, modules cannot be accessed unless the app has explicitly been granted the
              required permissions.

3.4.11 Enforce runtime permission checks

Prototype     int setScreenTimeOut(long timeOut)
Function      Set the screen timeout duration in seconds
Parameters    Parameters:
              timeOut -
Return Value  0: Always on
              1800: Maximum value (30 minutes)
Notes         Return:
              0 - Success
              1 - FailureOthers , See DeviceError for details
              This method sets how long the screen stays on before turning off due to inactivity.

3.4.12 Turn off the screen (sleep mode)

Prototype     int sleep(boolean isConfirm)
Function      Turn off the screen (sleep mode)
Parameters    Parameters:
              isConfirm - Whether to show a confirmation dialog before sleeping
Return Value  true - Show confirmation dialog
              false - Enter sleep directly
Notes         Return:
              0 - Success
              1 - Failure
              After calling this method, the screen will enter sleep mode in 5 seconds. The user can tap the
              screen to wake it up.This setting only takes effect for the next sleep.

3.4.13 Enable or disable various device wake-up methods

Prototype     int wakeUp(WakeUpType type, boolean enable)
Function      Enable or disable various device wake-up methods
Parameters    Parameters:

                                                                             17
Notes         true: Enable the wake-up method
              false: Disable the wake-up method
              Return:
              0 - Success
              1 - FailureOthers , See DeviceError for details
              This method configures whether a specific device wake-up method is enabled or disabled.

