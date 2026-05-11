 3.9 ECR module .................................................................................................................... 75
-- Get ECR module - getEcrManager -- ........................................................................................ 75
3.9.1 Create a connection to a device .............................................................................................. 75
3.9.2 Close connection(s) ...............................................................................................................76
3.9.3 Enumerate and return available ports ...................................................................................... 76
3.9.4 Hide all displayed pages ....................................................................................................... 76
3.9.5 Register a connection listener ................................................................................................ 76
3.9.6 Unregister the connection listener ...........................................................................................77
3.9.7 Get local BT/HOST information and display as QR code ............................................................ 77
3.9.8 Display QR scanning interface and obtain showHostByQR result ................................................ 77
3.9.9 Check whether the device is connected to the specified port ....................................................... 77
3.9.10 Display the device's BT/HOST information via NFC HCE tap .................................................78
3.9.11 Display the UI via NFC HCE tap to receive information from showHostByNFC ............................78
3.9.12 Retrieve the default printer set in Settings ..............................................................................78
3.9.13 Enable or disable virtual COM port ....................................................................................... 78
-- ECR connector object- EcrConnector -- ....................................................................................78
3.9.14 Read data ..........................................................................................................................79
3.9.15 Write data ......................................................................................................................... 79
3.9.16 Get connection information .................................................................................................. 79
-- ECR connection listener - ConnectionListener-- ........................................................................ 79
3.9.17 Connection state callback .................................................................................................... 79
3.9.18 Called when a connection is established ................................................................................ 80
 3.9 ECR module

-- Get ECR module - getEcrManager --

int close(String port)                                        Close the connection on the specified port;
                                                              pass 'null' to close all ports
ArrayList<String> getLocal()                                  Enumerate and return available port numbers
EcrConnector openOrConnect(String connection)                 Create a connection;
                                                              Supported types: Serial, USB-to-Serial, Cash Drawer
void hideHost()                                               Hide all displayed pages
void registerConnectionListener(ConnectionListener listener)  Register a connection listener
void unregisterConnectionListener()                           Unregister the connection listener
String showClientByQR(int timeout,                            Display the interface using QR scan,
ConstantScanner.ScannerCameraType cameraType)                 and get the result by showHostByQR
String showHostByQR(ConstantEcr.ConnectType type)             Show the host info as a QR code though BT/HOST
EcrConnector getPrinterMaster()                               Get the default printer added in the "Settings"
boolean isOpenOrConnect(String connection)                    Return the connection status of the specified port
String showClientByNFC(int timeout)                           Display the interface via NFC HCE tap to prepare for
                                                              receiving data from showHostByNFC
String showHostByNFC(ConstantEcr.ConnectType type)            Retrieve the device's BT/HOST info and display it
                                                              via NFC HCE tap interface
void enableVirtualCom(boolean enable)                         Enable the virtual serial port. After turning it on, the
                                                              device will operate in slave mode.

3.9.1 Create a connection to a device

Prototype     EcrConnector openOrConnect(String connection)
Function      Create a connection
Parameters    Parameters:
              connection - Connection parameter information. Supported formats:
              · Serial: SERIAL:port:baudrate
              · USB to serial: SERIAL:port:baudrate

                                                                             75
Notes         · BT: BT:0:deviceName:UUID or BT:1:UUID
              · NET: NET:0:IP:port or NET:1:port
              · USB device: USB:VIDxxxx:PIDxxxx
              Return:
              EcrConnector operation object
              Supports serial, USB to serial, cash drawer port, Bluetooth, NET, and USB device connections.

3.9.2 Close connection(s)

Prototype     int close(String port)
Function      Close connection(s)
Parameters    Parameters:
Return Value  port - Port name to close, or 'null' to close all ports
              Return:
Notes         0 - Success;
              Others - Failure
              Closes the specified port or all connections.

3.9.3 Enumerate and return available ports

Prototype     ArrayList<String> getLocal()
Function      Enumerate and return available ports
Parameters
Return Value  Return:
              List of local port names (e.g., "tty0" for /dev/ttySx)
Notes         Used to detect available local communication ports.

3.9.4 Hide all displayed pages

Prototype     void hideHost()
Function      Hide all displayed pages
Parameters
Return Value  Cancels or clears all currently displayed pages from the host screen.
Notes

3.9.5 Register a connection listener

Prototype     void registerConnectionListener(ConnectionListener listener)
Function      Register a connection listener
Parameters    Parameters:
              listener - Listener for connection events
Return Value
Notes         Registers a listener to receive callbacks when a connection is established.

                                            76

Prototype     void unregisterConnectionListener()
Function      Unregister the connection listener
Parameters
Return Value  Used to detect available local communication ports.
Notes

3.9.7 Get local BT/HOST information and display as QR code

Prototype     String showHostByQR(ConstantEcr.ConnectType type)
Function      Get local BT/HOST information and display as QR code
Parameters    Parameters:
              type - Connection type:
Return Value
Notes           · ConstantEcr.ConnectType.BT - Bluetooth
                · ConstantEcr.ConnectType.HOST - Local network
              Return:
              Local BT or HOST information string
              This method returns the device's Bluetooth or network info in a format suitable for QR code
              display.

3.9.8 Display QR scanning interface and obtain showHostByQR result

Prototype     String showClientByQR(int timeout,
Function      ConstantScanner.ScannerCameraType cameraType)
Parameters    Display QR scanning interface and obtain showHostByQR result
              Parameters:
Return Value  timeout - Timeout for reading (in seconds)
Notes         cameraType - Camera used for scanning:

                · CAMERA_REAR - Rear camera
                · CAMERA_FRONT - Front camera
                · SCANNER - Dedicated scan engine
              Return:
              Result string from showHostByQR
              Opens a QR code scanning UI to retrieve host information broadcast by showHostByQR.

3.9.9 Check whether the device is connected to the specified port

Prototype     boolean isOpenOrConnect(String connection)
Function      Check whether the device is connected to the specified port
Parameters    Parameters:
Return Value  connection - Connection information
              Return:
Notes         true: Connected
              false: Not connected

                                                                            77

Prototype     String showHostByNFC(ConstantEcr.ConnectType type)
Function      Display the device's BT/HOST information via NFC HCE tap
Parameters    Parameters:
              type - Connection type:
Return Value  · ConstantEcr.ConnectType.BT: Bluetooth
Notes         · ConstantEcr.ConnectType.HOST: Local network
              Return:
              BT or HOST information of the device

3.9.11 Display the UI via NFC HCE tap to receive information from showHostByNFC

Prototype     String showClientByNFC(int timeout)
Function      Display the UI via NFC HCE tap to receive information from showHostByNFC
Parameters    Parameters:
              timeout - Timeout in seconds
Return Value  Return:
              Result from showHostByNFC
Notes

3.9.12 Retrieve the default printer set in Settings

Prototype     EcrConnector getPrinterMaster()
Function      Retrieve the default printer set in Settings
Parameters
Return Value  Return:
              Printer object, or null if not set
Notes

3.9.13 Enable or disable virtual COM port

Prototype     void enableVirtualCom(boolean enable)
Function      Enable or disable virtual COM port
Parameters    enable -
              true: Enable virtual COM (device enters slave mode, ttyGSx appears on terminal and VCOM
Return Value  appears on PC)
Notes         false: Disable virtual COM

              When enabled, the device operates in slave mode and exposes a virtual serial interface to the PC.

-- ECR connector object- EcrConnector --

String getConnectInfo()                                     Return connection information
byte[] read()                                               Read data

                                                     78

3.9.14 Read data

Prototype          byte[] read()
Function           Read data
Parameters
                   Return:
Return Value       Byte array containing the read data
                   Reads data from the scanner module or connected device.
Notes

3.9.15 Write data

Prototype          void write(byte[] commands)
Function           Write data
                   Parameters:
Parameters         commands - Command data to write (max 4096 bytes)

Return Value       Sends command data to the connected device or module.
Notes

3.9.16 Get connection information

Prototype          String getConnectInfo()
Function           Get connection information
Parameters
                   Return:
Return Value       Connection information string
                   Returns current connection details of the scanner or related module.
Notes

-- ECR connection listener - ConnectionListener--

void onConnected(String connectionInfo)            Will be called when a connection is established
void onState(int state,                            Will be callback for connection state changes
String msg,
String connectionInfo)

3.9.17 Connection state callback

Prototype          void onState(int state,
                   String msg,
Function           String connectionInfo)
Parameters         Connection state callback
                   Parameters:
                   state - Connection state value. See ConstantEcr.ConnectState for constants
                   msg - Detailed description of the state

                                                                                  79
Notes         This method is triggered to notify the current connection state and a descriptive message.

3.9.18 Called when a connection is established

Prototype     void onConnected(String connectionInfo)
Function      Called when a connection is established
Parameters    Parameters:
              connectionInfo - Device connection information
Return Value
Notes         This method is invoked when the device has successfully connected.

