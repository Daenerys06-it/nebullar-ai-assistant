---
title: "kozen-financial-cardreader"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - cardreader
summary: "Defines Kozen Financial SDK CardReader module APIs for card power on/off, check card, APDU transmission, HCE read/write, and detection (contact, contactless, magstripe, Felica) via ICardReaderManager."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-financial-overview"
  - "kozen-financial-init"
---

## Overview

Card reader module providing smart card/NFC operations via ICardReaderManager from FinancialEngine.INSTANCE.getCardReaderManager() or FinancialEngine.cardReaderManager().

## Function List

| Function Name | Description |
|--            |-----------|
| int powerOn(int cardType) | Card reader powered on |
| int powerOff(int cardType) | Power off the card |
| int checkCard(int cardType,  int timeout,  ICheckCardListener callback) | Start checking card |
| int stopCheck() | Stop checking card |
| int getCardExistStatus(int cardType) | Check whether the card is in the card reader slot |
| int transmitApdu(int cardType,  byte[] sendBuff,  CustomByteArray rspBuf,  CustomByteArray swBuf) | Transmit APDU command to card |
| int hceWrite(android.nfc.NdefMessage msg,  int timeout) | Write NDEF data via HCE |
| byte[] hceRead(int timeout) | Read NDEF data using HCE (Host Card Emulation) in blocking mode |
| int detectCard(int cardType,  IDetectCardListener callback) | Detect a single card (synchronously) |
| int detectFelicaCard(byte[] systemCode,  byte[] requestCode,  byte[] timeSlot,  android.os.Bundle bundle) | Detect a Felica card (single detection) |
| int detectContactlessCard(String mode,  android.os.Bundle bundle) | Detect a contactless card (single detection) |
| void onTimeout() | Card detection timeout |

## Details

### powerOn

| Prototype    | Prototype int powerOn(int cardType) |
| ------------ | --- |
| Function     | Function Card reader powered on |
| Parameters   | Parameters Parameters: cardType - card type Supports single card and multiple card types. If input ConstantCardReader.CardType.ALL, can detect all card types. Multiple card types are detected such as follows: ConstantCardReader.CardType.CONTACT | ConstantCardReader.CardType.MAGNETIC 3. More card type details in ConstantCardReader.CardType |
| Return Value | Return value Returns: 0: Success Non-0: Failure - see CardReaderError |
| Notes        | Notes Note: 1. Due to protocol conflicts, Felica cards cannot be powered on simultaneously with other contactless cards. 2. When powering on cards, if the parameter ConstantCardReader.CardType.ALL is passed, only other contactless cards will be powered on by default, excluding Felica cards. 3. When powering on other contactless cards, Felica cards will be powered off; likewise, when powering on Felica cards, other contactless cards will be powered off. |

### powerOff

| Prototype    | Prototype int powerOff(int cardType) |
| ------------ | --- |
| Function     | Function Power off the card |
| Parameters   | Parameters Parameters: cardType - card type Supports single card and multiple card types. If input ConstantCardReader.CardType.ALL, can detect all card types. Multiple card types are detected such as follows: ConstantCardReader.CardType.CONTACT | ConstantCardReader.CardType.MAGNETIC 3. More card type details in ConstantCardReader.CardType |
| Return Value | Return value Returns: 0: Success Non-0: Failure - see CardReaderError |
| Notes        | Notes  |

### checkCard

| Prototype    | Prototype int checkCard(int cardType,  int timeout,  ICheckCardListener callback) |
| ------------ | --- |
| Function     | Function Start checking card |
| Parameters   | Parameters Parameters: cardType - card type Supports single card and multiple card types. If input ConstantCardReader.CardType.ALL, can detect all card types. Multiple card types are detected such as follows: ConstantCardReader.CardType.CONTACT | ConstantCardReader.CardType.MAGNETIC If both CardType.ALL and specific card types are passed, the specific card types take precedence. Example: ConstantCardReader.CardType.ALL | ConstantCardReader.CardType.CONTACT  will only detect contact cards during card detection. More card type details in ConstantCardReader.CardType timeout - timeout, in seconds callback - card check callback |
| Return Value | Return value Returns:  0: Success Non-0: Failure - see CardReaderError |
| Notes        | Notes Note: 1. The card will not be powered off automatically after the card checking is completed. Please note that the card must be powered off manually after the checking is completed; 2. During the card checking process, a card checking error will not terminate the process, but the onError callback will be called; 3. The checking process will continue until one type of card is detected or checking time out. 4.There is a protocol conflict between contactless cards and Felica cards; they cannot be detected simultaneously. If the card type is set to detect all cards (ConstantCardReader.CardType.ALL), felica cards will not be detected by default. |

### stopCheck

| Prototype    | Prototype int stopCheck() |
| ------------ | --- |
| Function     | Function Stop checking card |
| Parameters   | Parameters  |
| Return Value | Return value Returns:  0: Success Non-0: Failure - see CardReaderError |
| Notes        | Notes Note: If you want to interrupt checking manually during the card checking process, please call this method to end the card inspection 2. In the normal process, such as card is found or timeout occurs, the process will automatically stop 3. Stop the card checking process will not power off card; 4. After this function, please use the poweroff function to avoid affecting the power consumption of the machine. |

### getCardExistStatus

| Prototype    | Prototype int getCardExistStatus(int cardType) |
| ------------ | --- |
| Function     | Function Check whether the card is in the card reader slot |
| Parameters   | Parameters cardType - card type 1. Only supports single card 2. Supported card types: 2.1 ConstantCardReader.CardType.CONTACT - contact card 2.2 ConstantCardReader.CardType.CONTACTLESS - contactless card 2.3  ConstantCardReader.CardType.FELICA - felica card |
| Return Value | Return value Return: 0: Card present -1: Card not present Other: Failure – see CardReaderError for details |
| Notes        | Notes Note: 1. This function does not support composite cards; it only supports a single card type; 2. This function will not automatically power on the card being checked; 3. The function must be called when the card is already powered on; otherwise, it will return an error code indicating the card is powered off. |

### transmitApdu

| Prototype    | Prototype int transmitApdu(int cardType,  byte[] sendBuff,  CustomByteArray rspBuf,  CustomByteArray swBuf) |
| ------------ | --- |
| Function     | Function Transmit APDU command to card |
| Parameters   | Parameters Parameters: cardType - card type 1. Only supports single card 2. Supported card types: 2.1 ConstantCardReader.CardType.CONTACT - contact card 2.2 ConstantCardReader.CardType.CONTACTLESS - contactless card 2.3  ConstantCardReader.CardType.FELICA - felica card sendBuff - data to be transparently transmitted to the card, maximum 1929B rspBuf - card response data swBuf - card response data - software version number |
| Return Value | Return value Return: 0: Card is in the slot Others: Card is not in slot, see CardReaderError |
| Notes        | Notes Note: 1. This function does not support multiple cards, only single card types; 2. This function will power on the checked card automatically , but will not power off card after the detection is completed; 3. After this function, please use the poweroff function to avoid affecting the power consumption of the machine. 4. APDU command transmission is allowed only after successful card check; this method will fail if the card is powered on without card check |

### hceWrite

| Prototype    | Prototype int hceWrite(android.nfc.NdefMessage msg,  int timeout) |
| ------------ | --- |
| Function     | Function Write NDEF data via HCE |
| Parameters   | Parameters Parameters: msg - Data of type NdefMessage , max 255 bytes timeout - Timeout in seconds (timeout <= 0 means no timeout) |
| Return Value | Return Value Return: 0 - Success;  Others - Failure. Refer to CardReaderError for details |
| Notes        | Notes This method writes NDEF data using Host Card Emulation. |

### hceRead

| Prototype    | Prototype byte[] hceRead(int timeout) |
| ------------ | --- |
| Function     | Function Read NDEF data using HCE (Host Card Emulation) in blocking mode |
| Parameters   | Parameters Parameters: timeout - Read timeout in seconds |
| Return Value | Return Value Return: Byte array containing the read NDEF data |
| Notes        | Notes This is a blocking method;  use with caution on UI or main threads to avoid freezing |

### detectCard

| Prototype    | Prototype int detectCard(int cardType,  IDetectCardListener callback) |
| ------------ | --- |
| Function     | Function Detect a single card (synchronously) |
| Parameters   | Parameters Parameters: cardType - Type of card to detect. Only a single card type is supported.  See ConstantCardReader.DetectCardType callback - Callback triggered upon detection |
| Return Value | Return Value Return: 0 - Success Others - Failure. See CardReaderError for details |
| Notes        | Notes This method does not power on the card. Only supports single card types, not composite cards. You must power on the card before calling this method. |

### detectFelicaCard

| Prototype    | Prototype int detectFelicaCard(byte[] systemCode,  byte[] requestCode,  byte[] timeSlot,  android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Detect a Felica card (single detection) |
| Parameters   | Parameters Parameters: systemCode - System code (default: 0xFFFF) requestCode - Request code (default: 0x00) values can be:     ConstantCardReader.DetectFelicaRequestCode.NO_REQUEST ConstantCardReader.DetectFelicaRequestCode.SYSTEM_CODE_REQUEST ConstantCardReader.DetectFelicaRequestCode.COMMUNICATION_PERFORMANCE_REQUEST TtimeSlot - Maximum number of time slots (default: 0x03) bundle - Returned data on success, includes:     ConstantCardReader.ID_FOR_MANUFACTURER ConstantCardReader.PARAMETER_FOR_MANUFACTURER ConstantCardReader.REQUEST_DATA |
| Return Value | Return Value Return: 0 - Success Others - Failure. See CardReaderError for details |
| Notes        | Notes Used specifically for detecting Felica cards with custom system/request settings. |

### detectContactlessCard

| Prototype    | Prototype int detectContactlessCard(String mode,  android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Detect a contactless card (single detection) |
| Parameters   | Parameters Parameters: mode - Card type list string (e.g. "1,A,B")  Value options include: NULL ConstantCardReader.DetectContactlessMode.CARD_READER_DETECT_MODE_ISO14443 ConstantCardReader.DetectContactlessMode.CARD_READER_DETECT_MODE_EMV ConstantCardReader.DetectContactlessMode.CARD_READER_DETECT_MODE_A ConstantCardReader.DetectContactlessMode.CARD_READER_DETECT_MODE_B  bundle - Returned data on success, includes: ConstantCardReader.CARD_CHANNEL  ConstantCardReader.CARD_SERIAL_NUM ConstantCardReader.CARD_ATTRIBUTE  |
| Return Value | Return Value Return: 0 - Success Others - Failure. See CardReaderError for details |
| Notes        | Notes This method detects a non-contact (contactless) card by type list, returns card info in the bundle. |

### ICheckCardListener


#### findMagstripeCard

| Prototype    | Prototype void findMagstripeCard(android.os.Bundle info) |
| ------------ | --- |
| Function     | Function Magstripe card found successfully |
| Parameters   | Parameters Parameters: info - return data |
| Return Value | Return value  |
| Notes        | Notes Parameter constant value The following data will be returned during the card detection process ConstantCardReader.CARD_CHANNEL - logical channel number ConstantCardReader.CARD_SERIAL_NUM - Card serial number ConstantCardReader.CARD_ATTRIBUTE - ATR ConstantCardReader.TRACK1 - Track 1 data ConstantCardReader.TRACK2 - Track 2 data ConstantCardReader.TRACK3 - Track 3 data |


#### findContactCard

| Prototype    | Prototype void findContactCard(android.os.Bundle info) |
| ------------ | --- |
| Function     | Function Contact card found successfully |
| Parameters   | Parameters Parameters: info - return data |
| Return Value | Return value  |
| Notes        | Notes Parameter constant value The following data will be returned during the card detection process ConstantCardReader.CARD_CHANNEL - logical channel number ConstantCardReader.CARD_SERIAL_NUM - Card serial number ConstantCardReader.CARD_ATTRIBUTE - ATR |


#### findContactlessCard

| Prototype    | Prototype void findContactlessCard(android.os.Bundle info) |
| ------------ | --- |
| Function     | Function Contactless card found successfully |
| Parameters   | Parameters Parameters: info - return data |
| Return Value | Return value  |
| Notes        | Notes Parameter constant value The following data will be returned during the card detection process ConstantCardReader.CARD_CHANNEL - logical channel number ConstantCardReader.CARD_SERIAL_NUM - Card serial number ConstantCardReader.CARD_ATTRIBUTE - ATR |


#### findFelicaCard

| Prototype    | Prototype void findFelicaCard(android.os.Bundle info) |
| ------------ | --- |
| Function     | Function Felica card found successfully |
| Parameters   | Parameters Parameters: info - return data  |
| Return Value | Return Value  |
| Notes        | Notes Parameter constant value The following data will be returned during the card detection process ConstantCardReader.ID_FOR_MANUFACTURER - Unique card ConstantCardReader.PARAMETER_FOR_MANUFACTURER - Card parameters ConstantCardReader.REQUEST_DATA - Command response |


#### onError

| Prototype    | Prototype void onError(int code,  String message) |
| ------------ | --- |
| Function     | Function Card detection error |
| Parameters   | Parameters Parameters: code - error code, more details to see CardReaderError message - error description |
| Return Value | Return value  |
| Notes        | Notes  |


#### onTimeout

| Prototype    | Prototype void onTimeout() |
| ------------ | --- |
| Function     | Function Card detection timeout |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes  |

## Notes

No additional notes.

## Related Links

- [[kozen-financial-overview]]
- [[kozen-financial-init]]
