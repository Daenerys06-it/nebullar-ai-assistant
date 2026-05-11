 2. Overview ................................................................................................................................ 7

  2.1 Introduction ............................................................................................................................. 7
  2.2 Android version and IDE version supported by the SDK ................................................................. 7
  2.3 Feature Introduction ..................................................................................................................7
  2.3.1 Terminal Management Module ................................................................................................. 7
  2.3.2 Certificate Management Module ............................................................................................... 7
  2.3.3 Device Management Module .................................................................................................... 7
  2.3.4 Device Information Management Module ................................................................................... 7
  2.3.5 Location Management Module ..................................................................................................8
  2.3.6 Network Management Module .................................................................................................. 8
  2.3.7 Resource Management Module .................................................................................................8
  2.4 Importing the TerminalManagerService SDK .................................................................................8
  2.5 Initializing the TerminalManagerService SDK ............................................................................... 9
 3. API Interface Introduction ........................................................................................................ 9
   3.1 Terminal manager SDK initialization ................................................................................... 10
  3.1.1 Initialize the TerminalManagerService instance ........................................................................ 10
  -- TerminalManagerService instance callback - InitCallBack -- ....................................................... 10
  3.1.2 Initialization results ..............................................................................................................10
   3.2 Certification module ..........................................................................................................10
  -- Get Certification module - getCertificationManager-- ..................................................................10
  3.2.1 Updates the application's signature certificate .......................................................................... 10
  3.2.2 Deletes the application's signature certificate ........................................................................... 11
  3.2.3 Get the application's signature certificate information ................................................................11
   3.3 Device information module ................................................................................................ 11
  -- Get device information module - getDeviceInfoManager-- ........................................................... 11
  3.3.1 Get the SDK service version number ....................................................................................... 12
  3.3.2 Get Terminal serial number ................................................................................................... 12
  3.3.3 Get the IMSI number ............................................................................................................ 12
  3.3.4 Get the IMEI number ............................................................................................................ 12
  3.3.5 Get the equipment supplier name (XC, Kozen) ..........................................................................12
  3.3.6 Get the device model ............................................................................................................ 13
  3.3.7 Get the OS version number .................................................................................................... 13
  3.3.8 Get the Linux kernel version number .......................................................................................13
  3.3.9 Get the MCU version number ................................................................................................. 13
  3.3.10 Get the hardware version number ..........................................................................................13
  3.3.11 Get the EMV kernel version number ......................................................................................14
  3.3.12 Get TUSN (Only for the China region) ....................................................................................14
  3.3.13 Get customer serial number ..................................................................................................14
   3.4 Device module ................................................................................................................. 14
  -- Get device module - getDeviceManager-- ..................................................................................14
  3.4.1 Sets the system time ............................................................................................................. 15

                                                                                             2
3.4.3 Sets the time zone .................................................................................................................15
3.4.4 Get the current time zone .......................................................................................................15
3.4.5 Reboots the device ............................................................................................................... 16
3.4.6 Shuts down the device ...........................................................................................................16
3.4.7 Schedules a timed reboot .......................................................................................................16
3.4.8 Cancels the scheduled reboot ................................................................................................. 16
3.4.9 Enable or disable silent installation ........................................................................................ 16
3.4.10 Enforce runtime permission checks ....................................................................................... 17
3.4.11 Enforce runtime permission checks ....................................................................................... 17
3.4.12 Turn off the screen (sleep mode) ........................................................................................... 17
3.4.13 Enable or disable various device wake-up methods .................................................................17
 3. API Interface Introduction

void init(Context context,                       Terminal manager SDK initialization
InitCallBack callBack)
ICertificationManager getCertificationManager()  Certification module
IDeviceInfoManager getDeviceInfoManager()        Device information module
IDeviceManager getDeviceManager()                Device module
ILocationManager getLocationManager()            Location module
INetworkManager getNetworkManager()              Network module
IResourceManager getResourceManager()            Resource module

                                                 9
IPerceptionInfoManager getPerceptionInfoManager()        Perception Info module

 3.1 Terminal manager SDK initialization

3.1.1 Initialize the TerminalManagerService instance

Prototype     void init(Context context,
Function      InitCallBack callBack)
Parameters    Initialize the TerminalManagerService instance
              Parameters:
Return value  context - android context
Notes         callback - initialization callback

-- TerminalManagerService instance callback - InitCallBack --

void onInitResult(boolean result, String error)                                  Initialization results

3.1.2 Initialization results

Prototype     void onInitResult(boolean result,
Function      String error)
Parameters    Initialization results
              Parameters:
Return value  result - Initialization result (true or false)
Notes         error - error message

