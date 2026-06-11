---
title: "kozen-financial-ecr"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - ecr
summary: "Defines Kozen Financial SDK ECR module APIs for ECR/secondary display connection including open/close connect, QR/NFC display, port enumeration, connection management, and EcrConnector operations (read/write/getInfo)."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-financial-overview"
  - "kozen-financial-init"
---

## Overview

ECR operation module providing ECR/secondary display connectivity via IEcrManager from FinancialEngine.INSTANCE.getEcrManager() or FinancialEngine.ecrManager().

## Function List

| Function Name | Description |
|--            |-----------|
| EcrConnector openOrConnect(String connection) | Create a connection |
| int close(String port) | Close connection(s) |
| ArrayList<String> getLocal() | Enumerate and return available ports |
| void hideHost() | Hide all displayed pages |
| void registerConnectionListener(ConnectionListener listener) | Register a connection listener |
| void unregisterConnectionListener() | Unregister the connection listener |
| String showHostByQR(ConstantEcr.ConnectType type) | Get local BT/HOST information and display as QR code |
| String showClientByQR(int timeout,  ConstantScanner.ScannerCameraType cameraType) | Display QR scanning interface and obtain showHostByQR result |
| boolean isOpenOrConnect(String connection) | Check whether the device is connected to the specified port |
| String showHostByNFC(ConstantEcr.ConnectType type) | Display the device’s BT/HOST information via NFC HCE tap |
| String showClientByNFC(int timeout) | Display the UI via NFC HCE tap to receive information from showHostByNFC |
| EcrConnector getPrinterMaster() | Retrieve the default printer set in Settings |
| void enableVirtualCom(boolean enable) | Enable or disable virtual COM port |
| EcrConnector | EcrConnector |
| byte[] read() | Read data |
| void write(byte[] commands) | Write data |
| String getConnectInfo() | Get connection information |
| ConnectionListener | ConnectionListener |
| void onConnected(String connectionInfo) | Called when a connection is established |
| void onState(int state,  String msg, String connectionInfo) | Connection state callback |

## Details

### openOrConnect

| Prototype    | Prototype EcrConnector openOrConnect(String connection) |
| ------------ | --- |
| Function     | Function Create a connection |
| Parameters   | Parameters Parameters: connection - Connection parameter information. Supported formats: • Serial: SERIAL:port:baudrate • USB to serial: SERIAL:port:baudrate • Cash drawer port: SERIAL:port:baudrate • BT: BT:0:deviceName:UUID or BT:1:UUID • NET: NET:0:IP:port or NET:1:port • USB device: USB:VIDxxxx:PIDxxxx |
| Return Value | Return Value Return: EcrConnector operation object |
| Notes        | Notes Supports serial, USB to serial, cash drawer port, Bluetooth, NET, and USB device connections. |

### close

| Prototype    | Prototype int close(String port) |
| ------------ | --- |
| Function     | Function Close connection(s) |
| Parameters   | Parameters Parameters: port - Port name to close, or 'null' to close all ports |
| Return Value | Return Value Return: 0 - Success;  Others - Failure |
| Notes        | Notes Closes the specified port or all connections. |

### getLocal

| Prototype    | Prototype ArrayList<String> getLocal() |
| ------------ | --- |
| Function     | Function Enumerate and return available ports |
| Parameters   | Parameters  |
| Return Value | Return Value Return: List of local port names (e.g., "tty0" for /dev/ttySx) |
| Notes        | Notes Used to detect available local communication ports. |

### hideHost

| Prototype    | Prototype void hideHost() |
| ------------ | --- |
| Function     | Function Hide all displayed pages |
| Parameters   | Parameters  |
| Return Value | Return Value  |
| Notes        | Notes Cancels or clears all currently displayed pages from the host screen. |

### registerConnectionListener

| Prototype    | Prototype void registerConnectionListener(ConnectionListener listener) |
| ------------ | --- |
| Function     | Function Register a connection listener |
| Parameters   | Parameters Parameters: listener - Listener for connection events |
| Return Value | Return Value  |
| Notes        | Notes Registers a listener to receive callbacks when a connection is established. |

### unregisterConnectionListener

| Prototype    | Prototype void unregisterConnectionListener() |
| ------------ | --- |
| Function     | Function Unregister the connection listener |
| Parameters   | Parameters  |
| Return Value | Return Value  |
| Notes        | Notes Used to detect available local communication ports. |

### showHostByQR

| Prototype    | Prototype String showHostByQR(ConstantEcr.ConnectType type) |
| ------------ | --- |
| Function     | Function Get local BT/HOST information and display as QR code |
| Parameters   | Parameters Parameters: type - Connection type: • ConstantEcr.ConnectType.BT - Bluetooth     • ConstantEcr.ConnectType.HOST - Local network |
| Return Value | Return Value Return: Local BT or HOST information string |
| Notes        | Notes This method returns the device’s Bluetooth or network info in a format suitable for QR code display. |

### showClientByQR

| Prototype    | Prototype String showClientByQR(int timeout,  ConstantScanner.ScannerCameraType cameraType) |
| ------------ | --- |
| Function     | Function Display QR scanning interface and obtain showHostByQR result |
| Parameters   | Parameters Parameters: timeout - Timeout for reading (in seconds) cameraType - Camera used for scanning: • CAMERA_REAR - Rear camera     • CAMERA_FRONT - Front camera     • SCANNER - Dedicated scan engine |
| Return Value | Return Value Return: Result string from showHostByQR |
| Notes        | Notes Opens a QR code scanning UI to retrieve host information broadcast by showHostByQR. |

### isOpenOrConnect

| Prototype    | Prototype boolean isOpenOrConnect(String connection) |
| ------------ | --- |
| Function     | Function Check whether the device is connected to the specified port |
| Parameters   | Parameters Parameters: connection - Connection information |
| Return Value | Return Value Return:   true: Connected   false: Not connected |
| Notes        | Notes  |

### showHostByNFC

| Prototype    | Prototype String showHostByNFC(ConstantEcr.ConnectType type) |
| ------------ | --- |
| Function     | Function Display the device’s BT/HOST information via NFC HCE tap |
| Parameters   | Parameters Parameters: type - Connection type: • ConstantEcr.ConnectType.BT: Bluetooth   • ConstantEcr.ConnectType.HOST: Local network |
| Return Value | Return Value Return:    BT or HOST information of the device |
| Notes        | Notes  |

### showClientByNFC

| Prototype    | Prototype String showClientByNFC(int timeout) |
| ------------ | --- |
| Function     | Function Display the UI via NFC HCE tap to receive information from showHostByNFC |
| Parameters   | Parameters Parameters: timeout - Timeout in seconds |
| Return Value | Return Value Return: Result from showHostByNFC |
| Notes        | Notes  |

### getPrinterMaster

| Prototype    | Prototype EcrConnector getPrinterMaster() |
| ------------ | --- |
| Function     | Function Retrieve the default printer set in Settings |
| Parameters   | Parameters  |
| Return Value | Return Value Return:    Printer object, or null if not set |
| Notes        | Notes  |

### enableVirtualCom

| Prototype    | Prototype void enableVirtualCom(boolean enable) |
| ------------ | --- |
| Function     | Function Enable or disable virtual COM port |
| Parameters   | Parameters enable -  true: Enable virtual COM (device enters slave mode, ttyGSx appears on terminal and VCOM appears on PC) false: Disable virtual COM |
| Return Value | Return Value  |
| Notes        | Notes When enabled, the device operates in slave mode and exposes a virtual serial interface to the PC. |

### EcrConnector

### read

| Prototype    | Prototype byte[] read() |
| ------------ | --- |
| Function     | Function Read data |
| Parameters   | Parameters  |
| Return Value | Return Value Return: Byte array containing the read data |
| Notes        | Notes Reads data from the scanner module or connected device. |

### write

| Prototype    | Prototype void write(byte[] commands) |
| ------------ | --- |
| Function     | Function Write data |
| Parameters   | Parameters Parameters: commands - Command data to write (max 4096 bytes) |
| Return Value | Return Value  |
| Notes        | Notes Sends command data to the connected device or module. |

### getConnectInfo

| Prototype    | Prototype String getConnectInfo() |
| ------------ | --- |
| Function     | Function Get connection information |
| Parameters   | Parameters  |
| Return Value | Return Value Return: Connection information string |
| Notes        | Notes Returns current connection details of the scanner or related module. |

### ConnectionListener

### onConnected

| Prototype    | Prototype void onConnected(String connectionInfo) |
| ------------ | --- |
| Function     | Function Called when a connection is established |
| Parameters   | Parameters Parameters: connectionInfo - Device connection information |
| Return Value | Return Value  |
| Notes        | Notes This method is invoked when the device has successfully connected. |

### onState

| Prototype    | Prototype void onState(int state,  String msg, String connectionInfo) |
| ------------ | --- |
| Function     | Function Connection state callback |
| Parameters   | Parameters Parameters: state - Connection state value. See ConstantEcr.ConnectState for constants msg - Detailed description of the state connectionInfo - Device connection information |
| Return Value | Return Value  |
| Notes        | Notes This method is triggered to notify the current connection state and a descriptive message. |

## Notes

No additional notes.

## Related Links

- [[kozen-financial-overview]]
- [[kozen-financial-init]]
