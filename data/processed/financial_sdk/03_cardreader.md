 3.3 Card Reader Operation module

-- Get card reader operation module - getCardReaderManager --

int powerOff(int cardType)                            Power off the card
int powerOn(int cardType)                             Power on the card
int checkCard(int cardType,                           Start checking card
int timeout,
ICheckCardListener callback)                          Check whether the card is in the card reader slot
int getCardExistStatus(int cardType)                  Stop checking card
int stopCheck()                                       Transmit APDU command to card
Int transmitApdu(int cardType,
byte[] sendBuff,                           20
CustomByteArray rspBuf,
int hceWrite(android.nfc.NdefMessage msg,      Read NDEF data via HCE
int timeout)                                   Perform a single card detection
byte[] hceRead(int timeout)                    Perform a single detection of a contactless card
int detectCard(int cardType,                   Perform a single detection of a Felica card
IDetectCardListener callback)
int detectContactlessCard(String mode,
android.os.Bundle bundle)
int detectFelicaCard(byte[] systemCode,
byte[] requestCode,
byte[] timeSlot,
android.os.Bundle bundle)

3.3.1 Power on the card

Prototype     int powerOn(int cardType)
Function      Card reader powered on
Parameters    Parameters:
              cardType - card type
Return value  1. Supports single card and multiple card types. If input ConstantCardReader.CardType.ALL, can
Notes         detect all card types.
              2. Multiple card types are detected such as follows:
              ConstantCardReader.CardType.CONTACT | ConstantCardReader.CardType.MAGNETIC
              3. More card type details in ConstantCardReader.CardType
              Returns:
              0: Success
              Non-0: Failure - see CardReaderError
              Note:
              1. Due to protocol conflicts, Felica cards cannot be powered on simultaneously with other
              contactless cards.
              2. When powering on cards, if the parameter ConstantCardReader.CardType.ALL is passed, only
              other contactless cards will be powered on by default, excluding Felica cards.
              3. When powering on other contactless cards, Felica cards will be powered off; likewise, when
              powering on Felica cards, other contactless cards will be powered off.

3.3.2 Power off the card

Prototype     int powerOff(int cardType)
Function      Power off the card
Parameters    Parameters:
              cardType - card type
              1. Supports single card and multiple card types. If input ConstantCardReader.CardType.ALL, can
              detect all card types.
              2. Multiple card types are detected such as follows:
              ConstantCardReader.CardType.CONTACT | ConstantCardReader.CardType.MAGNETIC

                                           21
Notes         Returns:
              0: Success
              Non-0: Failure - see CardReaderError

3.3.3 Start checking card

Prototype     int checkCard(int cardType,
Function      int timeout,
Parameters    ICheckCardListener callback)
              Start checking card
Return value  Parameters:
Notes         cardType - card type
              1. Supports single card and multiple card types. If input ConstantCardReader.CardType.ALL,
              can detect all card types.
              2. Multiple card types are detected such as follows:
              ConstantCardReader.CardType.CONTACT | ConstantCardReader.CardType.MAGNETIC
              3. If both CardType.ALL and specific card types are passed, the specific card types take
              precedence.
              Example: ConstantCardReader.CardType.ALL | ConstantCardReader.CardType.CONTACT
              will only detect contact cards during card detection.
              4. More card type details in ConstantCardReader.CardType
              timeout - timeout, in seconds
              callback - card check callback
              Returns:
              0: Success
              Non-0: Failure - see CardReaderError
              Note:
              1. The card will not be powered off automatically after the card checking is completed. Please
              note that the card must be powered off manually after the checking is completed;
              2. During the card checking process, a card checking error will not terminate the process, but
              the onError callback will be called;
              3. The checking process will continue until one type of card is detected or checking time out.
              4.There is a protocol conflict between contactless cards and Felica cards; they cannot be
              detected simultaneously.
              5. If the card type is set to detect all cards (ConstantCardReader.CardType.ALL), felica cards
              will not be detected by default.

3.3.4 Stop checking card

Prototype     int stopCheck()
Function      Stop checking card
Parameters
Return value  Returns:

                                  22
              Non-0: Failure - see CardReaderError
              Note:
              1. If you want to interrupt checking manually during the card checking process, please call this
              method to end the card inspection
              2. In the normal process, such as card is found or timeout occurs, the process will automatically
              stop
              3. Stop the card checking process will not power off card;
              4. After this function, please use the poweroff function to avoid affecting the power consumption of
              the machine.

3.3.5 Check whether the card is in the card reader slot

Prototype     int getCardExistStatus(int cardType)
Function      Check whether the card is in the card reader slot
Parameters    cardType - card type
              1. Only supports single card
Return value  2. Supported card types:
              2.1 ConstantCardReader.CardType.CONTACT - contact card
Notes         2.2 ConstantCardReader.CardType.CONTACTLESS - contactless card
              2.3 ConstantCardReader.CardType.FELICA - felica card
              Return:
              0: Card present
              -1: Card not present
              Other: Failure ­ see CardReaderError for details
              Note:
              1. This function does not support composite cards; it only supports a single card type;
              2. This function will not automatically power on the card being checked;
              3. The function must be called when the card is already powered on; otherwise, it will return an
              error code indicating the card is powered off.

3.3.6 Transmit APDU command to card

Prototype     int transmitApdu(int cardType,
              byte[] sendBuff,
Function      CustomByteArray rspBuf,
Parameters    CustomByteArray swBuf)
              Transmit APDU command to card
              Parameters:
              cardType - card type
              1. Only supports single card
              2. Supported card types:
              2.1 ConstantCardReader.CardType.CONTACT - contact card
              2.2 ConstantCardReader.CardType.CONTACTLESS - contactless card
              2.3 ConstantCardReader.CardType.FELICA - felica card

                                                         23
Notes         rspBuf - card response data
              swBuf - card response data - software version number
              Return:
              0: Card is in the slot
              Others: Card is not in slot, see CardReaderError
              Note:
              1. This function does not support multiple cards, only single card types;
              2. This function will power on the checked card automatically , but will not power off card after the
              detection is completed;
              3. After this function, please use the poweroff function to avoid affecting the power consumption of
              the machine.
              4. APDU command transmission is allowed only after successful card check; this method will fail
              if the card is powered on without card check

3.3.7 write HCE data via NFC tag

Prototype     int hceWrite(android.nfc.NdefMessage msg,
Function      int timeout)
Parameters    Write NDEF data via HCE
              Parameters:
Return Value  msg - Data of type NdefMessage , max 255 bytes
Notes         timeout - Timeout in seconds (timeout <= 0 means no timeout)
              Return:
              0 - Success;
              Others - Failure. Refer to CardReaderError for details
              This method writes NDEF data using Host Card Emulation.

3.3.8 Read NDEF data using HCE (Host Card Emulation) in blocking mode

Prototype     byte[] hceRead(int timeout)
Function      Read NDEF data using HCE (Host Card Emulation) in blocking mode
Parameters    Parameters:
              timeout - Read timeout in seconds
Return Value  Return:
              Byte array containing the read NDEF data
Notes         This is a blocking method;
              use with caution on UI or main threads to avoid freezing

3.3.9 Detect a single card (synchronously)

Prototype     int detectCard(int cardType,
              IDetectCardListener callback)
Function      Detect a single card (synchronously)
Parameters    Parameters:
              cardType - Type of card to detect. Only a single card type is supported.

                                                                             24
Notes         callback - Callback triggered upon detection
              Return:
              0 - Success
              Others - Failure. See CardReaderError for details
              This method does not power on the card.
              Only supports single card types, not composite cards.
              You must power on the card before calling this method.

3.3.10 Detect a Felica card (single detection)

Prototype     int detectFelicaCard(byte[] systemCode,
Function      byte[] requestCode,
Parameters    byte[] timeSlot,
              android.os.Bundle bundle)
Return Value  Detect a Felica card (single detection)
Notes         Parameters:
              systemCode - System code (default: 0xFFFF)
              requestCode - Request code (default: 0x00)
              values can be:
              ConstantCardReader.DetectFelicaRequestCode.NO_REQUEST
              ConstantCardReader.DetectFelicaRequestCode.SYSTEM_CODE_REQUEST
              ConstantCardReader.DetectFelicaRequestCode.COMMUNICATION_PERFORMANCE_REQUEST
              TtimeSlot - Maximum number of time slots (default: 0x03)
              bundle - Returned data on success, includes:
              ConstantCardReader.ID_FOR_MANUFACTURER
              ConstantCardReader.PARAMETER_FOR_MANUFACTURER
              ConstantCardReader.REQUEST_DATA
              Return:
              0 - Success
              Others - Failure. See CardReaderError for details
              Used specifically for detecting Felica cards with custom system/request settings.

3.3.11 Detect a contactless card (single detection)

Prototype     int detectContactlessCard(String mode,
              android.os.Bundle bundle)
Function      Detect a contactless card (single detection)
Parameters    Parameters:
              mode - Card type list string (e.g. "1,A,B")

              Value options include:
              NULL
              ConstantCardReader.DetectContactlessMode.CARD_READER_DETECT_MODE_ISO14443
              ConstantCardReader.DetectContactlessMode.CARD_READER_DETECT_MODE_EMV

                                                     25
              ConstantCardReader.DetectContactlessMode.CARD_READER_DETECT_MODE_B

Return Value  bundle - Returned data on success, includes:
Notes         ConstantCardReader.CARD_CHANNEL
              ConstantCardReader.CARD_SERIAL_NUM
              ConstantCardReader.CARD_ATTRIBUTE
              Return:
              0 - Success
              Others - Failure. See CardReaderError for details
              This method detects a non-contact (contactless) card by type list, returns card info in the bundle.

-- Card check listener - ICheckCardListener --

void findContactCard(android.os.Bundle info)                Contact card found successfully
void findMagstripeCard(android.os.Bundle info)              Magstripe card found successfully
void findContactlessCard(android.os.Bundle info)            Contactless card found successfully
void findFelicaCard(android.os.Bundle info)                 Felica card found successfully
void onError(int code, String message)                      Card detection error
void onTimeout()                                            Card detection timeout

3.3.12 Magstripe card found successfully

Prototype     void findMagstripeCard(android.os.Bundle info)
Function      Magstripe card found successfully
Parameters    Parameters:
              info - return data
Return value
Notes         Parameter constant value
              The following data will be returned during the card detection process
              ConstantCardReader.CARD_CHANNEL - logical channel number
              ConstantCardReader.CARD_SERIAL_NUM - Card serial number
              ConstantCardReader.CARD_ATTRIBUTE - ATR
              ConstantCardReader.TRACK1 - Track 1 data
              ConstantCardReader.TRACK2 - Track 2 data
              ConstantCardReader.TRACK3 - Track 3 data

3.3.13 Contact card found successfully

Prototype     void findContactCard(android.os.Bundle info)
Function      Contact card found successfully
Parameters    Parameters:
              info - return data
Return value
Notes         Parameter constant value

                                                  26
              ConstantCardReader.CARD_CHANNEL - logical channel number
              ConstantCardReader.CARD_SERIAL_NUM - Card serial number
              ConstantCardReader.CARD_ATTRIBUTE - ATR

3.3.14 Contactless card found successfully

Prototype     void findContactlessCard(android.os.Bundle info)
Function      Contactless card found successfully
Parameters    Parameters:
              info - return data
Return value
Notes         Parameter constant value
              The following data will be returned during the card detection process
              ConstantCardReader.CARD_CHANNEL - logical channel number
              ConstantCardReader.CARD_SERIAL_NUM - Card serial number
              ConstantCardReader.CARD_ATTRIBUTE - ATR

3.3.15 Felica card found successfully

Prototype     void findFelicaCard(android.os.Bundle info)
Function      Felica card found successfully
Parameters    Parameters:
Return Value  info - return data

Notes         Parameter constant value
              The following data will be returned during the card detection process
              ConstantCardReader.ID_FOR_MANUFACTURER - Unique card
              ConstantCardReader.PARAMETER_FOR_MANUFACTURER - Card parameters
              ConstantCardReader.REQUEST_DATA - Command response

3.3.16 Card detection error

Prototype     void onError(int code,
Function      String message)
Parameters    Card detection error
              Parameters:
Return value  code - error code, more details to see CardReaderError
Notes         message - error description

3.3.17 Card detection timeout

Prototype     void onTimeout()
Function      Card detection timeout

                                            27
Return value
Notes

