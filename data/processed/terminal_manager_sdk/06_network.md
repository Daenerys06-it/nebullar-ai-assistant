 3.6 Network module ............................................................................................................... 24
-- Get network module - getNetworkManager-- ..............................................................................24

                                                                                         3
  3.6.2 Enables an APN configuration ................................................................................................24
   3.7 Resource module .............................................................................................................. 24
  -- Get resource module - getResourceManager-- ............................................................................24
  3.7.1 Installs or updates an app ...................................................................................................... 25
  3.7.2 Uninstalls an app ................................................................................................................. 25
  3.7.3 Updates the device system version or MCU firmware version ...................................................... 25
  3.7.4 Updates the resource package ................................................................................................ 25
  3.7.5 Install or update an app with listner ........................................................................................ 26
  3.7.6 Update the resource package with listener ............................................................................... 26
  3.7.7 Update the device system version / MCU firmware version with listener ....................................... 26
  -- Upgrade listener - OnAppUpgradeListener-- ............................................................................. 26
  3.7.8 Upgrade error/failure ............................................................................................................ 27
  3.7.9 Upgrade successful ...............................................................................................................27
  -- Upgrade listener - OnUpdateCustomResListener -- .................................................................... 27
  3.7.10 Upgrade error/failure ...........................................................................................................27
  3.7.11 Upgrade successful ............................................................................................................. 27
  -- Upgrade listener - OnUpdateOTAListener -- ............................................................................. 27
  3.7.12 Upgrade error/failure ...........................................................................................................28
  3.7.13 Upgrade successful ............................................................................................................. 28
  3.7.14 Callback for upgrade progress .............................................................................................. 28
   3.8 Device Log module ........................................................................................................... 28
  -- Get device log module - getDeviceLogsManager-- ...................................................................... 28
  3.8.1 Get the device log file path .................................................................................................... 28
   3.9 Perception Info module ......................................................................................................29
  -- Get Certification module - getCertificationManager-- ..................................................................29
  3.9.1 Get perception data as a file stream .........................................................................................29
  3.9.2 Get large battery cycle count list .............................................................................................29
  3.9.3 Get large battery design capacity list ....................................................................................... 29
  3.9.4 Get current max capacity of large battery ................................................................................. 29
  3.9.5 Get battery health percentage list ............................................................................................30
  3.9.6 Get battery health status list ...................................................................................................30
  3.9.7 Get small battery voltage list .................................................................................................. 30
  3.9.8 Get print distance history list ................................................................................................. 30
 3.6 Network module

-- Get network module - getNetworkManager--

int addApn(ApnConfiguration config)                                                                  Add an APN
int enableApn(String name)                                                                           Enable an APN

3.6.1 Adds an APN configuration

Prototype     int addApn(ApnConfiguration config)
Function      Adds an APN configuration.
Parameters    config - The APN configuration to add.
              Return:
Return value  0: Success
              Others: Failure (refer to NetworkError).
Notes

3.6.2 Enables an APN configuration

Prototype     int enableApn(String name)
Function      Enables an APN configuration.
Parameters    name - The name of the APN. Pass null to disable the currently used APN.
              Return:
Return value  0: Success
              Others: Failure (refer to NetworkError).
Notes

