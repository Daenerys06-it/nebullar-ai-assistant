---
title: "kozen-financial-emv-1"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - emv
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines Kozen Financial SDK EMV configuration and parameter management APIs, including terminal setup, AID, CAPK, exception file, revocation IPK, DRL, service, Apple Pay, and kernel version operations."
related:
  - "kozen-financial-emv-2"
  - "kozen-financial-entities-1"
  - "kozen-financial-entities-2"
  - "kozen-financial-entities-3"
  - "kozen-financial-overview"
  - "kozen-financial-init"
---

## Overview

Defines Kozen Financial SDK EMV configuration and parameter management APIs, including terminal setup, AID, CAPK, exception file, revocation IPK, DRL, service, Apple Pay, and kernel version operations.

## Function List

| Function Name | Description |
|--            |-----------|
| int setTerminal(int type,  android.os.Bundle bundle) | Set the terminal information for the EMV kernel. |
| int getTerminal(int type,  android.os.Bundle bundle) | Get the terminal information for the EMV kernel. |
| int setAid(EmvAid emvAid) | Set AID |
| int deleteAid() | Delete AID |
| List<EmvAid> getAid() | Retrieve the AID list |
| int setCapk(EmvCapk emvCapk) | Add CAPK |
| int deleteCapk() | Delete CAPK |
| List<EmvCapk> getCapk() | Retrieve the CAPK list |
| int setExceptionFile(EmvExceptionFile exceptionFile) | Set Exception File |
| int deleteExceptionFile() | Delete Exception File |
| List<EmvExceptionFile> getExceptionFile() | Retrieve the configured Exception File |
| int setRevocationIPK(EmvRevocationIPK revocationIPK) | Set RevocationIPK |
| int deleteRevocationIPK() | Delete RevocationIPK |
| List<EmvRevocationIPK> getRevocationIPK() | Retrieve the configured CAPK Revocation parameters |
| int setDRL(int type,  android.os.Bundle bundle) | Set Dynamic Reader Limits (DRL) configuration parameters |
| int deleteDRL(int type) | Delete Dynamic Reader Limits (DRL) configuration parameters |
| int getDRL(int type, android.os.Bundle bundle) | Retrieve Dynamic Reader Limits (DRL) configuration parameters |
| int setService(android.os.Bundle bundle) | Set RuPay terminal parameters |
| int deleteService() | Delete RuPay payment terminal parameters |
| int getService(android.os.Bundle bundle) | Retrieve RuPay payment terminal parameters |
| int setAppleTerminal(android.os.Bundle bundle) | Set Apple VAS transaction parameters |
| int getAppleTerminal(android.os.Bundle bundle) | Retrieve Apple VAS transaction parameters |
| int setAppleMerchant(android.os.Bundle bundle) | Set Apple Merchant transaction parameters |
| int deleteAppleMerchant() | Delete Apple Merchant transaction parameters |
| int getAppleMerchant(android.os.Bundle bundle) | Retrieve Apple Merchant transaction parameters |
| String getVersion(int type) | Retrieve Kernel version information |

## Details

### setTerminal

| Prototype    | Prototype int setTerminal(int type,  android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Set the terminal information for the EMV kernel. |
| Parameters   | Parameters type: Terminal type, with the following enumerated values: ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_TERMINAL ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_CONFIG ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_VISA ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_UNIONPAY ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_MASTERCARD ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_DISCOVER ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_AMEX ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_MIR ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_RUPAY ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_INTERAC  bundle: Terminal parameters. For constant details, refer to ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### getTerminal

| Prototype    | Prototype int getTerminal(int type,  android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Get the terminal information for the EMV kernel. |
| Parameters   | Parameters type: Terminal type, with the following enumerated values: ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_TERMINAL ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_CONFIG ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_VISA ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_UNIONPAY ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_MASTERCARD ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_DISCOVER ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_AMEX ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_MIR ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_RUPAY ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_INTERAC  bundle: Terminal parameters. For details, refer to the class definition of ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### setAid

| Prototype    | Prototype int setAid(EmvAid emvAid) |
| ------------ | --- |
| Function     | Function Set AID |
| Parameters   | Parameters emvAid: Parameter entity. For details, refer to EmvAid. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### deleteAid

| Prototype    | Prototype int deleteAid() |
| ------------ | --- |
| Function     | Function Delete AID |
| Parameters   | Parameters None |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### getAid

| Prototype    | Prototype List<EmvAid> getAid() |
| ------------ | --- |
| Function     | Function Retrieve the AID list |
| Parameters   | Parameters None |
| Return Value | Return value List of EmvAid. For details, refer to EmvAid. |
| Notes        | Notes  |

### setCapk

| Prototype    | Prototype int setCapk(EmvCapk emvCapk) |
| ------------ | --- |
| Function     | Function Add CAPK |
| Parameters   | Parameters emvCapk: Parameter entity. For details, refer to EmvCapk. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### deleteCapk

| Prototype    | Prototype int deleteCapk() |
| ------------ | --- |
| Function     | Function Delete CAPK |
| Parameters   | Parameters None |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### getCapk

| Prototype    | Prototype List<EmvCapk> getCapk() |
| ------------ | --- |
| Function     | Function Retrieve the CAPK list |
| Parameters   | Parameters None |
| Return Value | Return value List of EmvCapk. For details, refer to EmvCapk. |
| Notes        | Notes  |

### setExceptionFile

| Prototype    | Prototype int setExceptionFile(EmvExceptionFile exceptionFile) |
| ------------ | --- |
| Function     | Function Set Exception File |
| Parameters   | Parameters exceptionFile: Parameter entity. For details, refer to EmvExceptionFile. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### deleteExceptionFile

| Prototype    | Prototype int deleteExceptionFile() |
| ------------ | --- |
| Function     | Function Delete Exception File |
| Parameters   | Parameters None |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### getExceptionFile

| Prototype    | Prototype List<EmvExceptionFile> getExceptionFile() |
| ------------ | --- |
| Function     | Function Retrieve the configured Exception File |
| Parameters   | Parameters None |
| Return Value | Return value List of EmvExceptionFile. For details, refer to EmvExceptionFile. |
| Notes        | Notes  |

### setRevocationIPK

| Prototype    | Prototype int setRevocationIPK(EmvRevocationIPK revocationIPK) |
| ------------ | --- |
| Function     | Function Set RevocationIPK |
| Parameters   | Parameters revocationIPK: Parameter entity. For details, refer to EmvRevocationIPK. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### deleteRevocationIPK

| Prototype    | Prototype int deleteRevocationIPK() |
| ------------ | --- |
| Function     | Function Delete RevocationIPK |
| Parameters   | Parameters None |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### getRevocationIPK

| Prototype    | Prototype List<EmvRevocationIPK> getRevocationIPK() |
| ------------ | --- |
| Function     | Function Retrieve the configured CAPK Revocation parameters |
| Parameters   | Parameters None |
| Return Value | Return value List of EmvRevocationIPK. For details, refer to EmvRevocationIPK. |
| Notes        | Notes  |

### setDRL

| Prototype    | Prototype int setDRL(int type,  android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Set Dynamic Reader Limits (DRL) configuration parameters |
| Parameters   | Parameters type: DRL type. Supported card scheme types are as follows: ConstantEmv.POIEmvCoreManager.EmvDrlConstraints.TYPE_VISA ConstantEmv.POIEmvCoreManager.EmvDrlConstraints.TYPE_AMEX  bundle: Parameter values. For details, refer to ConstantEmv.POIEmvCoreManager.EmvDrlConstraints. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### deleteDRL

| Prototype    | Prototype int deleteDRL(int type) |
| ------------ | --- |
| Function     | Function Delete Dynamic Reader Limits (DRL) configuration parameters |
| Parameters   | Parameters type: DRL type. Supported card scheme types are as follows: ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_VISA ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_AMEX |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### getDRL

| Prototype    | Prototype int getDRL(int type, android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Retrieve Dynamic Reader Limits (DRL) configuration parameters |
| Parameters   | Parameters type: DRL type. Supported card scheme types are as follows: ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_VISA ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_AMEX  bundle: Parameter values. For details, refer to ConstantEmv.POIEmvCoreManager.EmvDrlConstraints. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### setService

| Prototype    | Prototype int setService(android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Set RuPay terminal parameters |
| Parameters   | Parameters bundle: Parameter values. Enumerated values are as follows: Bundle_Key: ConstantEmv.POIEmvCoreManager.EmvServiceConstraints.CONFIG Bundle_value: ByteArray in TLV format. For specific parameter values, refer to ConstantEmv.POIEmvCoreManager.EmvServiceConstraints. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### deleteService

| Prototype    | Prototype int deleteService() |
| ------------ | --- |
| Function     | Function Delete RuPay payment terminal parameters |
| Parameters   | Parameters None |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### getService

| Prototype    | Prototype int getService(android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Retrieve RuPay payment terminal parameters |
| Parameters   | Parameters bundle: Parameter values. For details, refer to ConstantEmv.POIEmvCoreManager.EmvServiceConstraints. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### setAppleTerminal

| Prototype    | Prototype int setAppleTerminal(android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Set Apple VAS transaction parameters |
| Parameters   | Parameters bundle: Parameter values. For details, refer to ConstantEmv.POIEmvCoreManager.AppleTerminalConstraints. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### getAppleTerminal

| Prototype    | Prototype int getAppleTerminal(android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Retrieve Apple VAS transaction parameters |
| Parameters   | Parameters bundle: Parameter values. For details, refer to ConstantEmv.POIEmvCoreManager.AppleTerminalConstraints. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### setAppleMerchant

| Prototype    | Prototype int setAppleMerchant(android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Set Apple Merchant transaction parameters |
| Parameters   | Parameters bundle: Parameter values. For details, refer to ConstantEmv.POIEmvCoreManager.AppleTerminalConstraints. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### deleteAppleMerchant

| Prototype    | Prototype int deleteAppleMerchant() |
| ------------ | --- |
| Function     | Function Delete Apple Merchant transaction parameters |
| Parameters   | Parameters None |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### getAppleMerchant

| Prototype    | Prototype int getAppleMerchant(android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Retrieve Apple Merchant transaction parameters |
| Parameters   | Parameters bundle: Parameter values. For details, refer to ConstantEmv.POIEmvCoreManager.AppleTerminalConstraints. |
| Return Value | Return value 0: Success Others: Failure. Refer to EmvError for error codes. |
| Notes        | Notes  |

### getVersion

| Prototype    | Prototype String getVersion(int type) |
| ------------ | --- |
| Function     | Function Retrieve Kernel version information |
| Parameters   | Parameters type: Kernel type. Enumerated values are as follows: ConstantEmv.POIEmvCoreManager.GET_LIB_VERSION ConstantEmv.POIEmvCoreManager.GET_VERSION_EMV ConstantEmv.POIEmvCoreManager.GET_VERSION_VISA ConstantEmv.POIEmvCoreManager.GET_VERSION_MASTERCARD ConstantEmv.POIEmvCoreManager.GET_VERSION_DISCOVER ConstantEmv.POIEmvCoreManager.GET_VERSION_AMEX ConstantEmv.POIEmvCoreManager.GET_VERSION_MIR ConstantEmv.POIEmvCoreManager.GET_VERSION_RUPAY ConstantEmv.POIEmvCoreManager.GET_VERSION_INTERAC ConstantEmv.POIEmvCoreManager.GET_VERSION_APPLE |
| Return Value | Return value Version information |
| Notes        | Notes  |

## Notes

This page is split from kozen-financial-emv and covers only the functions listed above. See related pages for complementary EMV APIs and entity constants.

## Related Links

- [[kozen-financial-emv-2]]
- [[kozen-financial-entities-1]]
- [[kozen-financial-entities-2]]
- [[kozen-financial-entities-3]]
- [[kozen-financial-overview]]
- [[kozen-financial-init]]
