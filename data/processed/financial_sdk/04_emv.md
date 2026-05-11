 3.4 EMV Operation module ..................................................................................................... 28
-- Get EMV operation module - getEmvManager -- ........................................................................ 28
3.4.1 Set the terminal information for the EMV kernel ....................................................................... 29
3.4.2 Get the terminal information for the EMV kernel .......................................................................29
3.4.3 Set AID ...............................................................................................................................30
3.4.4 Delete AID ..........................................................................................................................30
3.4.5 Retrieve AID List ................................................................................................................. 30
3.4.6 Add CAPK .......................................................................................................................... 30
3.4.7 Delete CAPK ....................................................................................................................... 30
3.4.8 Retrieve the CAPK list ..........................................................................................................31
3.4.9 Set Exception File ................................................................................................................ 31
3.4.10 Delete Exception File ..........................................................................................................31
3.4.11 Retrieve the configured Exception File .................................................................................. 31
3.4.12 Set RevocationIPK ..............................................................................................................31
3.4.13 Delete RevocationIPK ......................................................................................................... 32
3.4.14 Retrieve the configured CAPK Revocation parameters ............................................................. 32
3.4.15 Set Dynamic Reader Limits (DRL) configuration parameters ..................................................... 32
3.4.16 Delete Dynamic Reader Limits (DRL) configuration parameters ................................................ 32
3.4.17 Retrieve Dynamic Reader Limits (DRL) configuration parameters ............................................. 33
3.4.18 Set RuPay terminal parameters .............................................................................................33
3.4.19 Delete RuPay terminal parameters ........................................................................................ 33
3.4.20 Retrieve RuPay terminal parameters ..................................................................................... 33
3.4.21 Set Apple VAS transaction parameters .................................................................................. 34
3.4.22 Retrieve Apple VAS transaction parameters ........................................................................... 34
3.4.23 Set Apple Merchant transaction parameters ............................................................................34
3.4.24 Delete Apple Merchant transaction parameters ....................................................................... 34
3.4.25 Retrieve Apple Merchant transaction parameters .................................................................... 34
3.4.26 Retrieve Kernel version information ...................................................................................... 35
3.4.27 Start EMV transaction ......................................................................................................... 35
3.4.28 Stop EMV transaction ......................................................................................................... 35
3.4.29 Set EMV Tag/Object parameters ........................................................................................... 35

                                                                                         3
3.4.31 Set the result of multiple application selection ........................................................................ 36
3.4.32 Set card information confirmation result .................................................................................36
3.4.33 Set Pin input result ............................................................................................................. 36
3.4.34 Set the online result ............................................................................................................ 36
3.4.35 Detect card ........................................................................................................................ 37
3.4.36 Multiple application selection callback ..................................................................................37
3.4.37 Card information confirmation callback ................................................................................. 38
3.4.38 Kernel card scheme type callback .........................................................................................38
3.4.39 Second tap card callback ..................................................................................................... 39
3.4.40 Request PIN input callback ................................................................................................. 39
3.4.41 Request online process callback ........................................................................................... 39
3.4.42 Transaction result callback .................................................................................................. 39
3.4.43 Get the list of CAPK ........................................................................................................... 40
3.4.44 Get the list of AID .............................................................................................................. 40
 3.4 EMV Operation module
-- Get EMV operation module - getEmvManager --

int deleteAid()                                           Delete AID
int deleteAppleMerchant()                                 Delete Apple Merchant transaction parameters
int deleteCapk()                                          Delete CAPK
int deleteDRL(int type)                                   Delete Dynamic Reader Limits (DRL) configuration
                                                          parameters
int deleteExceptionFile()                                 Delete Exception File
int deleteRevocationIPK()                                 Delete Revocation IPK
int deleteService()                                       Delete RuPay payment terminal parameters
List<EmvAid> getAid()                                     Get AID list
int getAppleMerchant(android.os.Bundle bundle)            Get Apple Merchant transaction parameters
int getAppleTerminal(android.os.Bundle bundle)            Get Apple VAS transaction parameters
List<EmvCapk> getCapk()                                   Get CAPK list
int getDRL(int type, android.os.Bundle bundle)            Get Dynamic Reader Limits (DRL) configuration
                                                          parameters
List<EmvExceptionFile> getExceptionFile()                 Get configured Exception File
byte[] getKernel(String[] tags)                           Get EMV Tag/Object parameters
List<EmvRevocationIPK> getRevocationIPK()                 Get configured CAPK Revocation parameters
int getService(android.os.Bundle bundle)                  Get RuPay payment terminal parameters
int getTerminal(int type, android.os.Bundle bundle)       Get EMV kernel terminal information
String getVersion(int type)                               Get Kernel version information
int setAid(EmvAid emvAid)                                 Load AID
int setAppleMerchant(android.os.Bundle bundle)            Set Apple Merchant transaction parameters
int setAppleTerminal(android.os.Bundle bundle)            Set Apple VAS transaction parameters
int setCapk(EmvCapk emvCapk)                              Add CAPK
int setCardInfoResponse(android.os.Bundle bundle)         Set card information confirmation result
int setDRL(int type, android.os.Bundle bundle)            Set Dynamic Reader Limits (DRL) configuration
                                                          parameters
int setExceptionFile(EmvExceptionFile exceptionFile)      Set Exception File
int setKernel(byte[] tlv)                                 Set EMV Tag/Object parameters
int setOnlineResponse(android.os.Bundle bundle)           Set online transaction result
int setPinResponse(android.os.Bundle bundle)              Set PIN input result
int setRevocationIPK(EmvRevocationIPK revocationIPK)      Set Revocation IPK
int setSelectApplicationResponse(int position)            Set multiple application selection result
int setService(android.os.Bundle bundle)                  Set RuPay terminal parameters
int setTerminal(int type, android.os.Bundle bundle)       Set EMV kernel terminal information

                                                      28
IEmvListener callback)
int stopTransaction()                                  Stop transaction
List<EmvAid> getAid()                                  Retrieve the list of AIDs
List<EmvCapk> getCapk()                                Retrieve the list of CAPKs

3.4.1 Set the terminal information for the EMV kernel

Prototype     int setTerminal(int type,
Function      android.os.Bundle bundle)
              Set the terminal information for the EMV kernel.
Parameters    type: Terminal type, with the following enumerated values:
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_TERMINAL
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_CONFIG
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_VISA
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_UNIONPAY
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_MASTERCARD
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_DISCOVER
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_AMEX
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_MIR
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_RUPAY
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_INTERAC

Return value  bundle: Terminal parameters. For constant details, refer
Notes         to ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.
              0: Success
              Others: Failure. Refer to EmvError for error codes.

3.4.2 Get the terminal information for the EMV kernel

Prototype     int getTerminal(int type,
Function      android.os.Bundle bundle)
              Get the terminal information for the EMV kernel.
Parameters    type: Terminal type, with the following enumerated values:
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_TERMINAL
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_CONFIG
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_VISA
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_UNIONPAY
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_MASTERCARD
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_DISCOVER
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_AMEX
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_MIR
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_RUPAY

                                                                             29

Return value       bundle: Terminal parameters. For details, refer to the class definition
Notes              of ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.
                   0: Success
                   Others: Failure. Refer to EmvError for error codes.

3.4.3 Set AID

Prototype          int setAid(EmvAid emvAid)
Function           Set AID
Parameters         emvAid: Parameter entity. For details, refer to EmvAid.
                   0: Success
Return value       Others: Failure. Refer to EmvError for error codes.

Notes

3.4.4 Delete AID

Prototype          int deleteAid()
Function           Delete AID
Parameters         None
                   0: Success
Return value       Others: Failure. Refer to EmvError for error codes.

Notes

3.4.5 Retrieve AID List

Prototype          List<EmvAid> getAid()
Function           Retrieve the AID list
Parameters         None
Return value       List of EmvAid. For details, refer to EmvAid.
Notes

3.4.6 Add CAPK

Prototype          int setCapk(EmvCapk emvCapk)
Function           Add CAPK
Parameters         emvCapk: Parameter entity. For details, refer to EmvCapk.
                   0: Success
Return value       Others: Failure. Refer to EmvError for error codes.

Notes

3.4.7 Delete CAPK

Prototype          int deleteCapk()

                                     30
Parameters    None
Return value  0: Success
Notes         Others: Failure. Refer to EmvError for error codes.

3.4.8 Retrieve the CAPK list

Prototype     List<EmvCapk> getCapk()
Function      Retrieve the CAPK list
Parameters    None
Return value  List of EmvCapk. For details, refer to EmvCapk.
Notes

3.4.9 Set Exception File

Prototype     int setExceptionFile(EmvExceptionFile exceptionFile)
Function      Set Exception File
Parameters    exceptionFile: Parameter entity. For details, refer to EmvExceptionFile.
              0: Success
Return value  Others: Failure. Refer to EmvError for error codes.

Notes

3.4.10 Delete Exception File

Prototype     int deleteExceptionFile()
Function      Delete Exception File
Parameters    None
              0: Success
Return value  Others: Failure. Refer to EmvError for error codes.

Notes

3.4.11 Retrieve the configured Exception File

Prototype     List<EmvExceptionFile> getExceptionFile()
Function      Retrieve the configured Exception File
Parameters    None
Return value  List of EmvExceptionFile. For details, refer to EmvExceptionFile.
Notes

3.4.12 Set RevocationIPK

Prototype     int setRevocationIPK(EmvRevocationIPK revocationIPK)
Function      Set RevocationIPK
Parameters    revocationIPK: Parameter entity. For details, refer to EmvRevocationIPK.
Return value  0: Success

                                                                             31

Notes

3.4.13 Delete RevocationIPK

Prototype     int deleteRevocationIPK()
Function      Delete RevocationIPK
Parameters    None
              0: Success
Return value  Others: Failure. Refer to EmvError for error codes.

Notes

3.4.14 Retrieve the configured CAPK Revocation parameters

Prototype     List<EmvRevocationIPK> getRevocationIPK()
Function      Retrieve the configured CAPK Revocation parameters
Parameters    None
Return value  List of EmvRevocationIPK. For details, refer to EmvRevocationIPK.
Notes

3.4.15 Set Dynamic Reader Limits (DRL) configuration parameters

Prototype     int setDRL(int type,
Function      android.os.Bundle bundle)
              Set Dynamic Reader Limits (DRL) configuration parameters
Parameters    type: DRL type. Supported card scheme types are as follows:
              ConstantEmv.POIEmvCoreManager.EmvDrlConstraints.TYPE_VISA
Return value  ConstantEmv.POIEmvCoreManager.EmvDrlConstraints.TYPE_AMEX
Notes
              bundle: Parameter values. For details, refer
              to ConstantEmv.POIEmvCoreManager.EmvDrlConstraints.
              0: Success
              Others: Failure. Refer to EmvError for error codes.

3.4.16 Delete Dynamic Reader Limits (DRL) configuration parameters

Prototype     int deleteDRL(int type)
Function      Delete Dynamic Reader Limits (DRL) configuration parameters
Parameters    type: DRL type. Supported card scheme types are as follows:
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_VISA
Return value  ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_AMEX
Notes         0: Success
              Others: Failure. Refer to EmvError for error codes.

                             32

Prototype     int getDRL(int type,
Function      android.os.Bundle bundle)
              Retrieve Dynamic Reader Limits (DRL) configuration parameters
Parameters    type: DRL type. Supported card scheme types are as follows:
              ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_VISA
Return value  ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints.TYPE_AMEX
Notes
              bundle: Parameter values. For details, refer
              to ConstantEmv.POIEmvCoreManager.EmvDrlConstraints.
              0: Success
              Others: Failure. Refer to EmvError for error codes.

3.4.18 Set RuPay terminal parameters

Prototype     int setService(android.os.Bundle bundle)
Function      Set RuPay terminal parameters
              bundle: Parameter values. Enumerated values are as follows:
Parameters    Bundle_Key: ConstantEmv.POIEmvCoreManager.EmvServiceConstraints.CONFIG
              Bundle_value: ByteArray in TLV format.
Return value  For specific parameter values, refer
Notes         to ConstantEmv.POIEmvCoreManager.EmvServiceConstraints.
              0: Success
              Others: Failure. Refer to EmvError for error codes.

3.4.19 Delete RuPay terminal parameters

Prototype     int deleteService()
Function      Delete RuPay payment terminal parameters
Parameters    None
              0: Success
Return value  Others: Failure. Refer to EmvError for error codes.

Notes

3.4.20 Retrieve RuPay terminal parameters

Prototype     int getService(android.os.Bundle bundle)
Function      Retrieve RuPay payment terminal parameters
Parameters    bundle: Parameter values. For details, refer
              to ConstantEmv.POIEmvCoreManager.EmvServiceConstraints.
Return value  0: Success
Notes         Others: Failure. Refer to EmvError for error codes.

                                                                             33

Prototype     int setAppleTerminal(android.os.Bundle bundle)
Function      Set Apple VAS transaction parameters
Parameters    bundle: Parameter values. For details, refer
              to ConstantEmv.POIEmvCoreManager.AppleTerminalConstraints.
Return value  0: Success
Notes         Others: Failure. Refer to EmvError for error codes.

3.4.22 Retrieve Apple VAS transaction parameters

Prototype     int getAppleTerminal(android.os.Bundle bundle)
Function      Retrieve Apple VAS transaction parameters
Parameters    bundle: Parameter values. For details, refer
              to ConstantEmv.POIEmvCoreManager.AppleTerminalConstraints.
Return value  0: Success
Notes         Others: Failure. Refer to EmvError for error codes.

3.4.23 Set Apple Merchant transaction parameters

Prototype     int setAppleMerchant(android.os.Bundle bundle)
Function      Set Apple Merchant transaction parameters
Parameters    bundle: Parameter values. For details, refer
              to ConstantEmv.POIEmvCoreManager.AppleTerminalConstraints.
Return value  0: Success
Notes         Others: Failure. Refer to EmvError for error codes.

3.4.24 Delete Apple Merchant transaction parameters

Prototype     int deleteAppleMerchant()
Function      Delete Apple Merchant transaction parameters
Parameters    None
              0: Success
Return value  Others: Failure. Refer to EmvError for error codes.

Notes

3.4.25 Retrieve Apple Merchant transaction parameters

Prototype     int getAppleMerchant(android.os.Bundle bundle)
Function      Retrieve Apple Merchant transaction parameters
Parameters    bundle: Parameter values. For details, refer
Return value  to ConstantEmv.POIEmvCoreManager.AppleTerminalConstraints.
              0: Success

                                                                             34

Notes

3.4.26 Retrieve Kernel version information

Prototype     String getVersion(int type)
Function      Retrieve Kernel version information
              type: Kernel type. Enumerated values are as follows:
Parameters    ConstantEmv.POIEmvCoreManager.GET_LIB_VERSION
              ConstantEmv.POIEmvCoreManager.GET_VERSION_EMV
Return value  ConstantEmv.POIEmvCoreManager.GET_VERSION_VISA
Notes         ConstantEmv.POIEmvCoreManager.GET_VERSION_MASTERCARD
              ConstantEmv.POIEmvCoreManager.GET_VERSION_DISCOVER
              ConstantEmv.POIEmvCoreManager.GET_VERSION_AMEX
              ConstantEmv.POIEmvCoreManager.GET_VERSION_MIR
              ConstantEmv.POIEmvCoreManager.GET_VERSION_RUPAY
              ConstantEmv.POIEmvCoreManager.GET_VERSION_INTERAC
              ConstantEmv.POIEmvCoreManager.GET_VERSION_APPLE
              Version information

3.4.27 Start EMV transaction

Prototype     int startTransaction(android.os.Bundle bundle, IEmvListener callback)
Function      Start EMV transaction
Parameters    bundle: Transaction parameters. For details, refer
              to ConstantEmv.POIEmvCoreManager.EmvTransDataConstraints.
Return value  callback: EMV process callback.
Notes         0: Success
              Others: Failure. Refer to EmvError for error codes.

3.4.28 Stop EMV transaction

Prototype     int stopTransaction()
Function      Stop EMV transaction
Parameters    None
              0: Success
Return value  Others: Failure. Refer to EmvError for error codes.

Notes

3.4.29 Set EMV Tag/Object parameters

Prototype     int setKernel(byte[] tlv)
Function      Set EMV Tag/Object parameters
Parameters    tlv: TAG in TLV format.

                                                                             35
Notes         0: Success
              Others: Failure. Refer to EmvError for error codes.
              After setting, this method is only used to change TAG values during the EMV transaction process.
              The set TAG values cannot be retrieved using getKernel.

3.4.30 Retrieve EMV Tag/Object parameters

Prototype     byte[] getKernel(String[] tags)
Function      Retrieve EMV Tag/Object parameters
Parameters    tags: Array of TAGs. Example: new String[]{"4F", "50", "87", "9F12"}.
Return value  TAG values in TLV format.
Notes

3.4.31 Set the result of multiple application selection

Prototype     int setSelectApplicationResponse(int position)
Function      Set the result of multiple application selection
Parameters    position: The selected position in the multiple application selection callback data.
              0: Success
Return value  Others: Failure. Refer to EmvError for error codes.

Notes

3.4.32 Set card information confirmation result

Prototype     int setCardInfoResponse(android.os.Bundle bundle)
Function      Set card information confirmation result
Parameters    bundle - parameter value
              For details, see ConstantEmv.POIEmvCoreManager.EmvCardInfoConstraints
Return value  0: Success
Notes         Others: Failure. Refer to EmvError for error codes.

3.4.33 Set Pin input result

Prototype     int setPinResponse(android.os.Bundle bundle)
Function      Set Pin input result
Parameters    bundle - parameter value
              For details, see ConstantEmv.POIEmvCoreManager.EmvPinConstraints
Return value  0: Success
Notes         Others: Failure. Refer to EmvError for error codes.

3.4.34 Set the online result

Prototype     int setOnlineResponse(android.os.Bundle bundle)

                                                                             36
Parameters          bundle - parameter value
                    For details, see ConstantEmv.POIEmvCoreManager.EmvOnlineConstraints
Return value        0: Success
Notes               Others: Failure. Refer to EmvError for error codes.

-- EMV Listener- IEmvListener--

void onConfirmCardInfo(int mode,                                                       Callback for card information confirmation
android.os.Bundle info)
void onEmvProcess(int type,                                                            Callback when a card is detected
android.os.Bundle info)
void onKernelType(int type)                                                            Callback for kernel card scheme type
void onRequestInputPin(android.os.Bundle info)                                         Callback to request PIN input
void onRequestOnlineProcess(android.os.Bundle info)                                    Callback to request online processing
void onSecondTapCard()                                                                 Callback for second card tap
void onSelectApplication(List<String> appList,                                         Callback for multiple application selection
boolean isFirstSelect)
void onTransactionResult(int resultCode,                                               Callback for transaction result
android.os.Bundle info)

3.4.35 Detect card

Prototype           void onEmvProcess(int type,
Function            android.os.Bundle info)
Parameters          Detect card
                    Parameter:
Return value        type: Card type. Enumerated values are as follows:
Notes               ConstantEmv.POIEmvCoreManager.DEVICE_CONTACT
                    ConstantEmv.POIEmvCoreManager.DEVICE_CONTACTLESS
                    ConstantEmv.POIEmvCoreManager.DEVICE_MAGSTRIPE
                    ConstantEmv.POIEmvCoreManager.DEVICE_MIFARE_CLASSIC
                    ConstantEmv.POIEmvCoreManager.DEVICE_MIFARE_ULTRALIGHT
                    ConstantEmv.POIEmvCoreManager.DEVICE_MIFARE_PLUS
                    ConstantEmv.POIEmvCoreManager.DEVICE_MIFARE_DESFIRE
                    info: Card information parameters.

                    If the transaction card type is a magnetic stripe card,
                    the card data will be returned in this Bundle. For specific parameter constants, refer to
                    ConstantEmv.POIEmvCoreManager.EmvCardInfoConstraints.

3.4.36 Multiple application selection callback

Prototype           void onSelectApplication(List<String> appList,

                                                                                   37
Parameters    Multiple application selection callback
              Parameter:
Return value  appList: Application selection list.
Notes         isFirstSelect: Whether it is the first selection.

3.4.37 Card information confirmation callback

Prototype     void onConfirmCardInfo(int mode,
              android.os.Bundle info)
Function      Card information confirmation callback
Parameters    Parameter:
              mode: Current mode. Enumerated values are as follows:
              ConstantEmv.POIEmvCoreManager.CMD_TRY_OTHER_APPLICATION
              ConstantEmv.POIEmvCoreManager.CMD_AMOUNT_CONFIG
              ConstantEmv.POIEmvCoreManager.CMD_ISSUER_REFERRAL
              ConstantEmv.POIEmvCoreManager.CMD_GPO_FILTER
              ConstantEmv.POIEmvCoreManager.CMD_READ_RECORD_FILTER
              ConstantEmv.POIEmvCoreManager.CMD_SELECT_APPLICATION
              ConstantEmv.POIEmvCoreManager.CMD_READ_RECORD
              ConstantEmv.POIEmvCoreManager.CMD_GAC1
              ConstantEmv.POIEmvCoreManager.CMD_GAC2
              ConstantEmv.POIEmvCoreManager.CMD_SELECT_KERNEL
              ConstantEmv.POIEmvCoreManager.CMD_SELECT_AFTER
              ConstantEmv.POIEmvCoreManager.CMD_GPO_BEFORE
              ConstantEmv.POIEmvCoreManager.CMD_CARD_READ_SUCCESS

              info: Card information data. For specific parameter constants, refer
              to ConstantEmv.POIEmvCoreManager.EmvCardInfoConstraints.

Return value
Notes

3.4.38 Kernel card scheme type callback

Prototype     void onKernelType(int type)
Function      Kernel card scheme type callback
Parameters    Parameter:
              type: Kernel card scheme type. Enumerated values are as follows:
              ConstantEmv.POIEmvCoreManager.EMV_CARD_NOT
              ConstantEmv.POIEmvCoreManager.EMV_CARD_VISA
              ConstantEmv.POIEmvCoreManager.EMV_CARD_UNIONPAY
              ConstantEmv.POIEmvCoreManager.EMV_CARD_MASTERCARD
              ConstantEmv.POIEmvCoreManager.EMV_CARD_DISCOVER

                                                                             38
Notes         ConstantEmv.POIEmvCoreManager.EMV_CARD_JCB
              ConstantEmv.POIEmvCoreManager.EMV_CARD_MIR
              ConstantEmv.POIEmvCoreManager.EMV_CARD_RUPAY
              ConstantEmv.POIEmvCoreManager.EMV_CARD_PURE
              ConstantEmv.POIEmvCoreManager.EMV_CARD_INTERAC
              ConstantEmv.POIEmvCoreManager.EMV_CARD_EFTPOS

              1. This parameter is only returned for contactless card types.
              2. For contact transactions and magnetic stripe transactions, this parameter will not be returned.

3.4.39 Second tap card callback

Prototype     void onSecondTapCard()
Function      Second tap card callback
Parameters
Return value
Note

3.4.40 Request PIN input callback

Prototype     void onRequestInputPin(android.os.Bundle info)
Function      Request PIN input callback
Parameters    Parameter:
              info: PIN parameters.
Return value  For details, refer to ConstantEmv.POIEmvCoreManager.EmvPinConstraints.
Notes

3.4.41 Request online process callback

Prototype     void onRequestOnlineProcess(android.os.Bundle info)
Function      Request online process callback
Parameters    Parameter:
              info: Online parameters.
Return value  For details, refer to ConstantEmv.POIEmvCoreManager.EmvOnlineConstraints.
Notes

3.4.42 Transaction result callback

Prototype     void onTransactionResult(int resultCode,
              android.os.Bundle info)
Function      Transaction result callback
Parameters    Parameter:
              resultCode: Transaction result code.

                                                                             39
              Others: Failure. Refer to ConstantEmv.PosEmvErrorCode/EmvError.
              info: Transaction data.
              For details, refer to ConstantEmv.POIEmvCoreManager.EmvResultConstraints.

Return value
Notes

3.4.43 Get the list of CAPK

Prototype     List<EmvCapk> getCapk()
Function      Get the list of CAPK (Certification Authority Public Keys)
Parameters
Return Value  Return:
              List of EmvCapk objects
Notes         See EmvCapk for structure details

3.4.44 Get the list of AID

Prototype     List<EmvAid> getAid()
Function      Get the list of AID (Application Identifier)
Parameters
Return Value  Return:
              List of EmvAid objects
Notes         See EmvAid for structure details

