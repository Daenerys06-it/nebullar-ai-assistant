 3.3 Device information module                                                                       EMV kernel version number
                                                                                                     Get hardware version number
-- Get device information module - getDeviceInfoManager--                                            Get IMEI number; if multiple exist, return
                                                                                                     multiple
String getEmvKernelVersion()                                                                         Get IMSI number; if multiple exist, return
String getHardwareVersion()                                                                          multiple
String[] getImei()                                                                                   Get Linux kernel version number
                                                                                                     Get MCU version number
String[] getImsi()                                                                                   Get Android version number
                                                                                                     Get SDK service version number
String getKernelVersion()                                                                            Get device serial number
String getMcuVersion()                                                                               Get device model
String getOsVersion()
String getSdkServiceVersion()
String getSerialNo()
String getDeviceModel()

                                                                                                 11
String getCSN()                                                                  Get customer serial number
String getTUSN()                                                                 Get TUSN(Only for the China region)

3.3.1 Get the SDK service version number

Prototype     String getSdkServiceVersion()
Function      Get the SDK service version number.
Parameters
              Return:
Return value  The SDK service version number.

Notes

3.3.2 Get Terminal serial number

Prototype     String getSerialNo()
Function      Get Terminal serial number
Parameters
              Return:
Return value  The device serial number.

Notes

3.3.3 Get the IMSI number

Prototype     String[] getImsi()
Function      Retrieves the IMSI number; if multiple exist, returns multiple.
Parameters
              Return:
Return value  The IMSI number(s).

Notes

3.3.4 Get the IMEI number

Prototype     String[] getImei()
Function      Retrieves the IMEI number; if multiple exist, returns multiple.
Parameters
              Return:
Return value  The IMEI number(s).

Notes

3.3.5 Get the equipment supplier name (XC, Kozen)

Prototype     String getVendorName()
Function      Get the equipment supplier name (XC, Kozen)
Parameters
Return value  Return:

                                                                             12

Notes

3.3.6 Get the device model

Prototype     String getDeviceModel()
Function      Get the device model.
Parameters
              Return:
Return value  The device model.

Notes

3.3.7 Get the OS version number

Prototype     String getOsVersion()
Function      Get the OS version number.
Parameters
              Return:
Return value  If KozenOS is supported, return the KozenOS version number; if it is not supported, return the
              Android version number.
Notes

3.3.8 Get the Linux kernel version number

Prototype     String getKernelVersion()
Function      Get the Linux kernel version number.
Parameters
              Return:
Return value  The kernel version number.

Notes

3.3.9 Get the MCU version number

Prototype     String getMcuVersion()
Function      Retrieves the MCU version number.
Parameters
              Return:
Return value  The MCU version number.

Notes

3.3.10 Get the hardware version number

Prototype     String getHardwareVersion()
Function      Get the hardware version number.
Parameters
Return value  Return:

                                                                             13

Notes

3.3.11 Get the EMV kernel version number

Prototype     String getEmvKernelVersion()
Function      Get the EMV kernel version number.
Parameters
              Return:
Return value  The EMV kernel version number.

Notes

3.3.12 Get TUSN (Only for the China region)

Prototype     String getTUSN()
Function      Get TUSN (Only for the China region)
Parameters
Return Value  Return:TUSN
Notes         Returns the unique terminal serial number.

3.3.13 Get customer serial number

Prototype     String getCSN()
Function      Get customer serial number
Parameters
Return Value  Return:CSN
Notes         Returns the customer serial number

