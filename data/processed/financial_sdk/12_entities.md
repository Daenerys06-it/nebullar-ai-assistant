 5. Entity Class Definition ............................................................................................................94
  5.1 com.kozen.financial.aidl.emv.EmvCapk ..................................................................................... 94
  5.2 com.kozen.financial.aidl.emv.EmvAid ........................................................................................95
  5.3 com.kozen.financial.aidl.emv.EmvExceptionFile ......................................................................... 98
  5.4 com.kozen.financial.aidl.emv.EmvCapk ..................................................................................... 98
  5.5 ConstantCardReader ............................................................................................................... 98
  5.6 ConstantCardReader.CardType ................................................................................................. 99
  5.7 ConstantEmv.POIEmvCoreManager ...........................................................................................99
  5.8 ConstantEmv.POIEmvCoreManager.AppleTerminalConstraints ................................................... 101
  5.9 ConstantEmv.POIEmvCoreManager.EmvCardInfoConstraints ......................................................101
  5.10 ConstantEmv.POIEmvCoreManager.EmvDrlConstraints ............................................................102
  5.11 ConstantEmv.POIEmvCoreManager.EmvOnlineConstraints .......................................................102
  5.12 ConstantEmv.POIEmvCoreManager.EmvPinConstraints ........................................................... 102
  5.13 ConstantEmv.POIEmvCoreManager.EmvResultConstraints ....................................................... 103

                                                                                             7
  5.15 ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints ....................................................104
  5.16 ConstantEmv.POIEmvCoreManager.EmvTransDataConstraints ..................................................107
  5.17 ConstantPrinter ...................................................................................................................108
  5.18 ConstantPrinter.Align .......................................................................................................... 109
  5.19 ConstantPrinter.BarcodeFormat .............................................................................................109
  5.20 ConstantPrinter.PrintFailurePolicy ........................................................................................ 109
  5.21 ConstantPrinter.FontSize ...................................................................................................... 109
  5.22 ConstantSecurity ................................................................................................................. 109
  5.23 ConstantScanner ................................................................................................................. 111
  5.24 ConstantScanner.BarcodeFormat ........................................................................................... 111
  5.25 ConstantScanner.ScannerCameraType ....................................................................................112
  5.26 ConstantScanner.BarcodeSupport .......................................................................................... 112
  5.27 com.kozen.financial.pinpad.PinViewEnum ............................................................................. 113
  5.28 ConstantPrinter.GrayPercent .................................................................................................113
  5.29 ConstantPrinter.GlobalFontSize .............................................................................................113
  5.30 ConstantPrinter.LineSpaceMultiplier ..................................................................................... 113
  5.31 ConstantEcr.ConnectType .................................................................................................... 113
  5.32 ConstantEcr.ConnectState .................................................................................................... 114
  5.33 ConstantGeneral.IndicatorType ............................................................................................. 114
 5. Entity Class Definition

5.1 com.kozen.financial.aidl.emv.EmvCapk

Constant Name  Type                           Value  Description
                                              1      ­
ALGO_IND_RSA   int                            4      ­
                                              ­      Algorithm Flag.
ALGO_IND_SM    int

AlgorithmInd   byte

                                          94
Checksum                                                      Checksum.
CREATOR             byte[]               ­                    ­
Exponent                                                      Exponent.
HASH_IND_NOT        android.os.Parcelable.Creator<EmvCapk> ­  ­
HASH_IND_SHA1                                                 ­
HashInd             byte[]               ­                    HASH Algorithm Flag.
Module                                                        Module.
RID                 int                  0                    Application Registration
                                                              Provider ID.
                    int                  1

                    byte                 ­

                    byte[]               ­

                    byte[]               ­                                              Service

5.2 com.kozen.financial.aidl.emv.EmvAid

Constant Name               Type         Description
AcquirerIdentifier          byte[]       Acquirer Identifier.
                                         Tag: 9F01.Value Type : byte[]. Required Field.
AdditionalTerminalCapabilities byte[]    Additional Terminal Capabilities.
                                         Tag: 9F40.Value Type : byte[].Required Field.
AID                         byte[]       Application Id.
                                         Tag: 9F06. Value Type: byte[]. Required Field.
CombinationData             byte[]       Combination Data.

                                         public byte[] CombinationData
                                         Combination Data. Set Parameters for AID Will Overwrite the Default Parameters. Not Related
                                         to CombinationType.
                                         eg. aid.CombinationData = getKernel(getLimit(999999999999L,

                                          999999999999L,
                                         999999999999L,
                                         999999999999L),
                                         HexUtil.parseHex("9F660436004000"), null, null, null, null);
                                         The getKernel Function is Defined to Set Parameters for Different Card Organizations
                                         Can Set EMV Standard Tag.
                                         "DF10", "DF11", "DF12", "DF13", "DF14", "DF17" in this Function are Custom Tags.
                                         Just Pass in the Tag and Value that Need to be Set as Parameters.
                                         eg. 9F660436004000.
                                         private static byte[] getKernel(byte[] kernel, byte[] visa, byte[] unionpay, byte[] mastercard,
                                         byte[] discover, byte[] mir) {

                                               BerTlvBuilder tlvBuilder = new BerTlvBuilder();
                                               if (kernel != null) {

                                                     tlvBuilder.addBytes(new BerTag("DF10"), kernel);
                                               }
                                               if (visa != null) {

                                                     tlvBuilder.addBytes(new BerTag("DF11"), visa);
                                               }
                                               if (unionpay != null) {

                                                     tlvBuilder.addBytes(new BerTag("DF12"), unionpay);

                                                     95
                                  if (mastercard != null) {
ContactlessCVMLimit   int
                                        tlvBuilder.addBytes(new BerTag("DF13"), mastercard);
ContactlessCVMLimitL  long        }
                                  if (discover != null) {

                                        tlvBuilder.addBytes(new BerTag("DF14"), discover);
                                  }
                                  if (mir != null) {

                                        tlvBuilder.addBytes(new BerTag("DF17"), mir);
                                  }
                                  return tlvBuilder.buildArray();
                            }
                            Set CVM Parameters.
                            "DF01", "DF02", "DF03", "DF04" in this Function are Custom Tags.
                            Just Pass in the Tag and Value that Need to be Set as Parameters. eg. 999999999999L,
                             999999999999L,
                            999999999999L,
                            999999999999L.
                            private static byte[] getLimit(long contactlessLimit, long contactlessCVMLimit, long
                            contactlessFloorLimit, long contactlessDynamicLimit) {
                                  BerTlvBuilder tlvBuilder = new BerTlvBuilder();
                                  tlvBuilder.addBytes(new BerTag("DF01"),
                                  getAmount(contactlessLimit));
                                  tlvBuilder.addBytes(new BerTag("DF02"),
                                  getAmount(contactlessCVMLimit));
                                  tlvBuilder.addBytes(new BerTag("DF03"),
                                  getAmount(contactlessFloorLimit));
                                  tlvBuilder.addBytes(new BerTag("DF04"),
                                  getAmount(contactlessDynamicLimit));
                                  return tlvBuilder.buildArray();
                            }
                            private static byte[] getAmount(long value) {
                                  StringBuilder builder = new StringBuilder(12);
                                  builder.append(value);
                                  while (builder.length() < 12) {

                                        builder.insert(0, '0');
                                  }
                                  return HexUtil.parseHex(builder.toString());
                            }

                            Combination Type.
                            Not Usage. Value Type : int.
                            Contactless CVM Required Limit.
                            Value Type : int. Optional Field.
                            Contactless CVM Required Limit.
                            Value Type : long. Optional Field.

                                        96
ContactlessFloorLimitL      long           Value Type : int. Optional Field.
ContactlessTransLimit       int            Contactless Floor Limit.
ContactlessTransLimitL      long           Value Type : long. Optional Field.
CREATOR                     static final   Contactless Transaction Limit.
                            android.os.Pa  Value Type : int. Optional Field.
dDOL                        rcelable.Crea  Contactless Transaction Limit.
DynamicTransLimit           tor            Value Type : long. Optional Field.
DynamicTransLimitL          byte[]         ­
FloorLimit                  int
MaxTargetPercentage         long           Default dDOL.
MerchantCategoryCode        int            Tag: 97. Value Type : byte[]. Required Field.
SelectIndicator             int            Dynamic Trans Limit.
                            byte[]         Value Type : int. Optional Field.
TACDefault                  boolean        Dynamic Trans Limit.
TACDenial                                  Value Type : long. Optional Field.
TACOnline                   byte[]         Floor Limit.
TargetPercentage            byte[]         Value Type : int. Optional Field.
tDOL                        byte[]         The Maximum Target Percentage of Offset Random Selection.
TerminalCapabilities        int            Value Type : int. Optional Field.
TerminalCountryCode         byte[]         Merchant Category Code.
TerminalRiskManagementData  byte[]         Tag: 9F15. Value Type : byte[].Required Field.
TerminalType                byte[]         Application Select Indicator:
                            byte[]         True: FULL_MATCH,
                            byte[]         False: PART_MATCH.
                                           Value Type : boolean. Optional Field.
                                           TAC-Default.
                                           Tag: DF8120.Value Type: byte[].Required Field.
                                           TAC-Denial.
                                           Tag : DF8121.Value Type : byte[].Required Field.
                                           TAC-Online.
                                           Tag : DF8122.Value Type : byte[].Required Field.
                                           Target Percentage of Random Selection.
                                           Value Type : int. Optional Field.
                                           Default tDOL.
                                           Tag : 9F49.Value Type : byte[].Required Field.
                                           Terminal Capability.
                                           Value Type : byte[]. Required Field.
                                           Terminal Country Code.
                                           Tag : 9F1A.Value Type : byte[].Required Field.
                                           Terminal Risk Management Data.
                                           Tag : 9F1D.Value Type : byte[].Required Field.
                                           Terminal Type.

                                                       97
TransCurrencyCode       byte[]            Threshold of Bias Random Selection.
TransCurrencyExp        byte[]            Value Type : int. Optional Field.
TypeIndicator           boolean           Trans Currency Code.
                                          Tag : 5F2A.Value Type : byte[]. Required Field.
Version                 byte[]            Trans Currency Exp.
                                          Tag : 5F36.Value Type : byte[]. Required Field.
                                          Application Type Indicator:
                                          True: Contactless,
                                          False: Both for Contact and Contactless.
                                          Value Type : boolean. Optional Field.
                                          Application Version.
                                          Tag : 9F09.Value Type : byte[]. Required Field.

5.3 com.kozen.financial.aidl.emv.EmvExceptionFile

Constant Name           Type              Description
CapkIndex               byte              Capk Index
CREATOR                                   Value Type : byte[]. Required Field.
                        static final      ­
RID                     android.os.Pa
SerialNo                rcelable.Crea     RID
                        tor<EmvRevo       Tag : 9F06.Value Type : byte[]. Required Field.
                        cationIPK>        SerialNumber
                        byte[]            Value Type : byte[]. Required Field.

                        byte[]

5.4 com.kozen.financial.aidl.emv.EmvCapk

Constant Name           Type              Description
CREATOR                 static final      ­
                        android.os.Pa
PAN                     rcelable.Crea     Primary Account Number. (PAN).
SerialNo                tor<EmvExce       Value Type : byte[]. Required Field.
                        ptionFile>        Serial Number.
                        byte[]            Value Type : byte[]. Required Field.

                        byte[]

5.5 ConstantCardReader

Constant Name                                      Type    Value
ATR                                                String  "cardAtr"

                                                     98
CARD_ATTRIBUTE                     String  "cardAttribute"
CARD_CATEGORY                      String  "cardCategory"
CARD_CHANNEL                       String  "cardChannel"
CARD_SERIAL_NUM                    String  "cardSerialNum"
CARD_TYPE                          String  "cardType"
EXPIRED_DATE                       String  "cardExpDate"
ID_FOR_MANUFACTURER                String  "IDm"
PAN                                String  "cardPan"
PARAMETER_FOR_MANUFACTURER         String  "PMm"
REQUEST_DATA                       String  "RequestData"
SERVICE_CODE                       String  "cardServiceCode"
TIMEOUT                            String  "cardTimeout"
TRACK1                             String  "cardTrack1"
TRACK2                             String  "cardTrack2"
TRACK3                             String  "cardTrack3"

5.6 ConstantCardReader.CardType    Type    Value
                                   int     0
Constant Name                      int     2
ALL                                int     4
CONTACT                            int     32
CONTACTLESS                        int     1
FELICA                             int     8
MAGNETIC                           int     64
MIFARE                             int     16
NFC_TAG
PSAM                               Type    Value
                                   int     1
5.7 ConstantEmv.POIEmvCoreManager  int     64
                                   int     18
Constant Name                      int     19
CMD_AMOUNT_CONFIG                  int     49
CMD_CARD_READ_SUCCESS              int     16
CMD_GAC1                           int     2
CMD_GAC2                           int     17
CMD_GPO_BEFORE                     int     17
CMD_GPO_FILTER                     int     48
CMD_ISSUER_REFERRAL                int     16
CMD_READ_RECORD                    int     32
CMD_READ_RECORD_FILTER             int     0
CMD_SELECT_AFTER
CMD_SELECT_APPLICATION               99
CMD_SELECT_KERNEL
CMD_TRY_OTHER_APPLICATION
DEVICE_CONTACTLESS
DEVICE_MAGSTRIPE          int  2
DEVICE_MIFARE_CLASSIC
DEVICE_MIFARE_DESFIRE     int  4
DEVICE_MIFARE_PLUS
DEVICE_MIFARE_ULTRALIGHT  int  8
DEVICE_VICC
EMV_ADMINISTRATIVE        int  64
EMV_BALANCE_ENQUIRY
EMV_BALANCE_UPDATE        int  32
EMV_CARD_AMEX
EMV_CARD_DISCOVER         int  16
EMV_CARD_EFTPOS
EMV_CARD_INTERAC          int  128
EMV_CARD_JCB
EMV_CARD_MASTERCARD       int  7
EMV_CARD_MIR
EMV_CARD_NOT              int  13
EMV_CARD_PURE
EMV_CARD_RUPAY            int  14
EMV_CARD_UNIONPAY
EMV_CARD_VISA             int  5
EMV_CASH
EMV_CASHBACK              int  4
EMV_DEPOSIT
EMV_DISBURSEMENT          int  11
EMV_GOODS
EMV_INQUIRY               int  10
EMV_MONEY_ADD
EMV_PAYMENT               int  6
EMV_REFUND
EMV_SERVICE               int  3
EMV_SERVICE_CREATION
EMV_TRANSFER              int  7
EMV_VOID
GET_LIB_VERSION           int  0
GET_VERSION_AMEX
GET_VERSION_APPLE         int  9
GET_VERSION_CL1
GET_VERSION_DISCOVER      int  8
GET_VERSION_EFTPOS
GET_VERSION_EMV           int  2
GET_VERSION_INTERAC
                          int  1

                          int  3

                          int  4

                          int  10

                          int  8

                          int  1

                          int  11

                          int  12

                          int  6

                          int  9

                          int  2

                          int  16

                          int  5

                          int  15

                          int  0

                          int  6

                          int  16

                          int  14

                          int  5

                          int  12

                          int  1

                          int  11

                          100
                                                            13
GET_VERSION_L1              int                             4
                                                            8
GET_VERSION_MASTERCARD      int                             10
                                                            9
GET_VERSION_MIR             int                             3
                                                            2
GET_VERSION_PURE            int                             2
                                                            1
GET_VERSION_RUPAY           int                             0

GET_VERSION_UNIONPAY        int                             Value
                                                            "capability"
GET_VERSION_VISA            int                             1
                                                            3
PIN_ENCIPHER_PIN            int                             0
                                                            2
PIN_ONLINE_PIN              int                             "data"
                                                            "protocol"
PIN_PLAIN_PIN               int                             1
                                                            0
5.8 ConstantEmv.POIEmvCoreManager.AppleTerminalConstraints  "DF01"
                                                            "9F2B"
Constant Name               Type                            "9F25"
CAPABILITY                  String                          "9F29"
CAPABILITY_DUAL_MODE        int
CAPABILITY_PAYMENT_ONLY     int                             Value
CAPABILITY_SINGLE_MODE      int                             "atr"
CAPABILITY_VAS_ONLY         int                             "card"
DATA                        String                          "data"
PROTOCOL                    String                          "amount"
PROTOCOL_FULL_VAS           int                             "amountOther"
PROTOCOL_URL_ONLY           int                             "confirm"
TAG_APPLE_SET_DELIMITER     String                          "tlv"
TAG_APPLE_SET_FILTER        String                          "tvr"
TAG_APPLE_SET_MERCHANT_ID   String                          "track1"
TAG_APPLE_SET_MERCHANT_URL  String                          "track2"
                                                            "track3"
5.9 ConstantEmv.POIEmvCoreManager.EmvCardInfoConstraints

Constant Name               Type
ATR                         String
CARD                        String
DATA                        String
OUT_AMOUNT                  String
OUT_AMOUNT_OTHER            String
OUT_CONFIRM                 String
OUT_TLV                     String
OUT_TVR                     String
TRACK1                      String
TRACK2                      String
TRACK3                      String

                            101

Constant Name                    Type                    Value
CONFIG                           String                  "Config"
TAG_DRL_SET_CVM_REQUIRED_LIMIT   String                  "DF24"
TAG_DRL_SET_DELIMITER            String                  "DF01"
TAG_DRL_SET_ENTRY_POINT          String                  "DF30"
TAG_DRL_SET_FLOOR_LIMIT          String                  "DF25"
TAG_DRL_SET_PROGRAM_ID           String                  "9F5A"
TAG_DRL_SET_STATUS_ZERO_AMOUNT   String                  "DF32"
TAG_DRL_SET_TRANSACTION_LIMIT    String                  "DF23"
TYPE_AMEX                        int                     2
TYPE_VISA                        int                     1

5.11 ConstantEmv.POIEmvCoreManager.EmvOnlineConstraints  Value
                                                         "appleData"
Constant Name                    Type                    "appleMerchant"
APPLE_DATA                       String                  "appleResult"
APPLE_MERCHANT                   String                  "emvData"
APPLE_RESULT                     String                  0
EMV_DATA                         String                  2
EMV_ONLINE_APPROVE               int                     1
EMV_ONLINE_DENIAL                int                     3
EMV_ONLINE_FAIL                  int                     "encryptData"
EMV_ONLINE_REFER_TO_CARD_ISSUER  int                     "encryptResult"
ENCRYPT_DATA                     String                  "outAuthCode"
ENCRYPT_RESULT                   String                  "outAuthData"
OUT_AUTH_CODE                    String                  "outAuthRespCode"
OUT_AUTH_DATA                    String                  "outIssuerScript"
OUT_AUTH_RESP_CODE               String                  "outSpecialAuthRespCode"
OUT_ISSUER_SCRIPT                String
OUT_SPECIAL_AUTH_RESP_CODE       String                  Value
                                                         "outPinBlock"
5.12 ConstantEmv.POIEmvCoreManager.EmvPinConstraints     "outPinTryCounter"
                                                         "outPinVerifyResult"
Constant Name                    Type                    "pinBlockFormat"
OUT_PIN_BLOCK                    String                  "pinBypass"
OUT_PIN_TRY_COUNTER              String                  "pinCard"
OUT_PIN_VERIFY_RESULT            String                  "pinCardRandom"
PIN_BLOCK_FORMAT                 String
PIN_BYPASS                       String
PIN_CARD                         String
PIN_CARD_RANDOM                  String

                                   102
PIN_DUKPT_KEY_LENGTH            String                   "pinDukptKeyLength"
PIN_ENCRYPT                     String                   "pinEncrypt"
PIN_EXPONENT                    String                   "pinExponent"
PIN_IS_ORDER                    String                   "isOrder "
PIN_ISO_FMT0                    int                      0
PIN_ISO_FMT1                    int                      1
PIN_ISO_FMT1_SM4                int                      5
PIN_ISO_FMT2                    int                      2
PIN_ISO_FMT2_SM4                int                      6
PIN_ISO_FMT3                    int                      3
PIN_ISO_FMT3_SM4                int                      7
PIN_ISO_FMT4                    int                      4
PIN_KEY_INDEX                   String                   "pinKeyId"
PIN_KEY_MODE                    String                   "pinKeyMode"
PIN_KEY_MODE_DUKPT              int                      3
PIN_KEY_MODE_TPK                int                      1
PIN_LENGTH_LIMIT                String                   "lengthLimit"
PIN_MODULE                      String                   "pinModule"
PIN_TIMEOUT                     String                   "pinTimeout"
PIN_TYPE                        String                   "pinType"
VERIFY_CANCELED                 int                      4
VERIFY_ERROR                    int                      3
VERIFY_NO_PASSWORD              int                      1
VERIFY_PIN_BLOCK                int                      2
VERIFY_SUCCESS                  int                      0
VERIFY_TIMEOUT                  int                      5

5.13 ConstantEmv.POIEmvCoreManager.EmvResultConstraints  Value
                                                         "appleData"
Constant Name                   Type                     "appleMerchant"
APPLE_DATA                      String                   "appleResult"
APPLE_MERCHANT                  String                   "cvm"
APPLE_RESULT                    String                   2
CVM                             String                   0
CVM_CONFIRMATION_CODE_VERIFIED  int                      1
CVM_NO_CVM                      int                      "emvData"
CVM_SIGNATURE                   int                      "encryptData"
EMV_DATA                        String                   "encryptResult"
ENCRYPT_DATA                    String                   "scriptResult"
ENCRYPT_RESULT                  String                   3
SCRIPT_RESULT                   String                   1
SECOND_TAP_CANCEL               int
SECOND_TAP_FAIL                 int

                                  103
SECOND_TAP_SUCCESS            int                          0
SECOND_TAP_TIMEOUT            int                          2

5.14 ConstantEmv.POIEmvCoreManager.EmvServiceConstraints   Value
                                                           "Config"
Constant Name                 Type                         "DF02"
CONFIG                        String                       "DF30"
TAG_PRMACQ_SET_DELIMITER      String                       "DF32"
TAG_PRMACQ_SET_INDEX          String                       "DF31"
TAG_PRMACQ_SET_KCV            String                       "DF19"
TAG_PRMACQ_SET_KEY            String                       "DF01"
TAG_SERVICE_SET_DATA          String                       "DF16"
TAG_SERVICE_SET_DELIMITER     String                       "DF18"
TAG_SERVICE_SET_ID            String                       "DF17"
TAG_SERVICE_SET_MANAGEMENT    String                       "DF21"
TAG_SERVICE_SET_PRIORITY      String                       "DF20"
TAG_SERVICE_SET_PRMACQ        String
TAG_SERVICE_SET_PRMISS        String                       Value
                                                           "BypassPINEntry"
5.15 ConstantEmv.POIEmvCoreManager.EmvTerminalConstraints  "CardHolderConfirm"
                                                           "Config"
Constant Name                 Type                         "DefaultDDOL"
BYPASS_PIN_ENTRY              String                       "DefaultTDOL"
CARD_HOLDER_CONFIRM           String                       "ExceptionFile"
CONFIG                        String                       "FloorLimitChecking"
DEFAULT_DDOL                  String                       "ForcedAccept"
DEFAULT_TDOL                  String                       "ForcedOnline"
EXCEPTION_FILE                String                       "GetDataForPINCounter"
FLOOR_LIMIT_CHECKING          String                       "IfdSerialNumber"
FORCED_ACCEPT                 String                       "IssuerReferral"
FORCED_ONLINE                 String                       "LanguageSelect"
GET_DATA_FOR_PIN_COUNTER      String                       "MerchantCategoryCode"
IFD_SERIAL_NUMBER             String                       "MerchantId"
ISSUER_REFERRAL               String                       "MerchantName"
LANGUAGE_SELECT               String                       "Pse"
MERCHANT_CATEGORY_CODE        String                       "RandomTransactionSelection"
MERCHANT_ID                   String                       "RevocationIssuerPublicKey"
MERCHANT_NAME                 String                       24
PSE                           String                       23
RANDOM_TRANSACTION_SELECTION  String
REVOCATION_ISSUER_PUBLIC_KEY  String
SETTINGS_AMEX                 int
SETTINGS_DISCOVER             int

                                104
SETTINGS_INTERAC                     int     29
SETTINGS_JCB                         int     25
SETTINGS_MASTERCARD                  int     22
SETTINGS_MIR                         int     26
SETTINGS_PURE                        int     28
SETTINGS_RUPAY                       int     27
SETTINGS_UNIONPAY                    int     21
SETTINGS_VISA                        int     20
SUBSEQUENT_BYPASS_PIN_ENTRY          String  "SubsequentBypassPINEntry"
TAG_AMEX_SET_ENTRY_POINT             String  "DF30"
TAG_AMEX_SET_KERNEL_CONFIG           String  "DF1B"
TAG_AMEX_SET_QUALIFIERS              String  "9F6E"
TAG_AMEX_SET_STATUS_ZERO_AMOUNT      String  "DF32"
TAG_CARD_DATA_INPUT_CAPABILITY       String  "DF8117"
TAG_DISCOVER_SET_ENTRY_POINT         String  "DF30"
TAG_DISCOVER_SET_QUALIFIERS          String  "9F66"
TAG_DISCOVER_SET_STATUS_ZERO_AMOUNT  String  "DF32"
TAG_EFTPOS_SET_ENTRY_POINT           String  "DF30"
TAG_EFTPOS_SET_KERNEL_CONFIG         String  "DF1B"
TAG_EFTPOS_SET_QUALIFIERS            String  "9F66"
TAG_EFTPOS_SET_STATUS                String  "DF31"
TAG_EFTPOS_SET_ZERO_AMOUNT           String  "DF32"
TAG_JCB_SET_ENTRY_POINT              String  "DF30"
TAG_JCB_SET_KERNEL_CONFIG            String  "DF1B"
TAG_JCB_SET_QUALIFIERS               String  "9F53"
TAG_JCB_SET_STATUS                   String  "DF31"
TAG_JCB_SET_ZERO_AMOUNT              String  "DF32"
TAG_MASTERCARD_SET_CVM_CAPABILITIES  String  "DF8118"
TAG_MASTERCARD_SET_DEFAULT_UDOL      String  "DF811A"
TAG_MASTERCARD_SET_KERNEL_CONFIG     String  "DF811B"
TAG_MASTERCARD_SET_KERNEL_ID         String  "DF810C"
TAG_MASTERCARD_SET_MAGSTRIPE_APP_VE
RSION                                String  "9F6D"
TAG_MASTERCARD_SET_MAGSTRIPE_CVM_C
APABILITIES                          String  "DF811E"
TAG_MASTERCARD_SET_MAGSTRIPE_NO_CV
M_CAPABILITIES                       String  "DF812C"
TAG_MASTERCARD_SET_MOBILE_SUPPORT_I
NDICATOR                             String  "9F7E"
TAG_MASTERCARD_SET_NO_CVM_CAPABILIT
IES                                  String  "DF8119"
TAG_MASTERCARD_SET_RRP_ACCURACY_TH
RESHOLD                              String  "DF8136"

                                     105
TED
TAG_MASTERCARD_SET_RRP_MAX_GRACE     String  "DF8133"
TAG_MASTERCARD_SET_RRP_MIN_GRACE     String  "DF8132"
TAG_MASTERCARD_SET_RRP_MISMATCH_TH
RESHOLD                              String  "DF8137"
TAG_MASTERCARD_SET_RRP_RAPDU_EXPEC
TED                                  String  "DF8135"
TAG_MIR_SET_ENTRY_POINT
TAG_MIR_SET_QUALIFIERS               String  "DF30"
TAG_MIR_SET_STATUS_ZERO_AMOUNT       String  "9F66"
TAG_PURE_SET_ENTRY_POINT             String  "DF32"
TAG_PURE_SET_KERNEL_CONFIG           String  "DF30"
TAG_PURE_SET_QUALIFIERS              String  "DF1B"
TAG_PURE_SET_STATUS                  String  "C7"
TAG_PURE_SET_ZERO_AMOUNT             String  "DF31"
TAG_SECURITY_CAPABILITY              String  "DF32"
TAG_UNIONPAY_SET_ENTRY_POINT         String  "DF811F"
TAG_UNIONPAY_SET_QUALIFIERS          String  "DF30"
TAG_UNIONPAY_SET_STATUS_ZERO_AMOUNT  String  "9F66"
TAG_VISA_SET_ENTRY_POINT             String  "DF32"
TAG_VISA_SET_KERNEL_CONFIG           String  "DF30"
TAG_VISA_SET_QUALIFIERS              String  "DF1B"
TAG_VISA_SET_STATUS_ZERO_AMOUNT      String  "9F66"
TERMINAL_CAPABILITY                  String  "DF32"
TERMINAL_COUNTRY_CODE                String  "TerminalCapability"
TERMINAL_ENTRY_MODE                  String  "TerminalCountryCode"
TERMINAL_EX_CAPABILITY               String  "TerminalEntryMode"
TERMINAL_ID                          String  "TerminalExCapability"
TERMINAL_TYPE                        String  "TerminalId"
TRANS_CURRENCY_CODE                  String  "TerminalType"
TRANS_CURRENCY_EXP                   String  "TransCurrencyCode"
TRANS_REFER_CURRENCY_CODE            String  "TransCurrencyExp"
TRANS_REFER_CURRENCY_EXP             String  "TransReferCurrencyCode"
TYPE_AMEX                            String  "TransReferCurrencyExp"
TYPE_CONFIG                          int     7
TYPE_DISCOVER                        int     2
TYPE_INTERAC                         int     6
TYPE_MASTERCARD                      int     10
TYPE_MIR                             int     5
TYPE_RUPAY                           int     8
TYPE_TERMINAL                        int     9
TYPE_UNIONPAY                        int     1
TYPE_VISA                            int     4
                                     int     3

                                     106
VELOCITY_CHECKING                 String                    "VelocityChecking"

5.16 ConstantEmv.POIEmvCoreManager.EmvTransDataConstraints  Value
                                                            "accountMaskHead"
Constant Name                     Type                      "accountMaskTail"
ACCOUNT_MASK_HEAD                 String                    "accountType"
ACCOUNT_MASK_TAIL                 String                    "amountConfig"
ACCOUNT_TYPE                      String                    "appleVas"
AMOUNT_CONFIG                     String                    "clSpecialType"
APPLE_VAS                         String                    "ctSpecialType"
CL_SPECIAL_TYPE                   String                    "encryptBase64"
CT_SPECIAL_TYPE                   String                    "encryptContact"
ENCRYPT_BASE64                    String                    "encryptContactless"
ENCRYPT_CONTACT                   String                    "encryptEmvData"
ENCRYPT_CONTACTLESS               String                    "encryptKeyIndex"
ENCRYPT_EMV_DATA                  String                    "encryptKeyMode"
ENCRYPT_KEY_INDEX                 String                    1
ENCRYPT_KEY_MODE                  String                    "encryptMagstripe"
ENCRYPT_KEY_MODE_TRANS_ARMOR      int                       "encryptMode"
ENCRYPT_MAGSTRIPE                 String                    2
ENCRYPT_MODE                      String                    1
ENCRYPT_MODE_CBC                  int                       1
ENCRYPT_MODE_ECB                  int                       2
ENCRYPT_OPEN_CONTACT              int                       4
ENCRYPT_OPEN_CONTACTLESS          int                       "encryptPadding"
ENCRYPT_OPEN_MAGSTRIPE            int                       "encryptSHA1"
ENCRYPT_PADDING                   String                    "encryptType"
ENCRYPT_SHA1                      String                    3
ENCRYPT_TYPE                      String                    4
ENCRYPT_TYPE_DUKPT_DATA_REQUEST   int                       2
ENCRYPT_TYPE_DUKPT_DATA_RESPONSE  int                       5
ENCRYPT_TYPE_DUKPT_MAC            int                       6
ENCRYPT_TYPE_DUKPT_PIN            int                       1
ENCRYPT_TYPE_RSA                  int                       7
ENCRYPT_TYPE_TDK                  int                       "encryptVector"
ENCRYPT_TYPE_TTK                  int                       "googleSmartTap"
ENCRYPT_VECTOR                    String                    "openEncrypt"
GOOGLE_SMART_TAP                  String                    "rsaTransArmorKeyId"
OPEN_ENCRYPT                      String                    "rsaTransArmorPosId"
RSA_TRANS_ARMOR_KEY_ID            String                    "specialContact"
RSA_TRANS_ARMOR_POS_ID            String                    "specialContactTime"
SPECIAL_CONTACT                   String
SPECIAL_CONTACT_TIME              String

                                    107
SPECIAL_MAGSTRIPE_TIME          String  "specialMagstripeTime"
SPECIAL_START_MODE              String  "specialStartMode"
SPECIAL_TYPE                    String  "specialType"
START_A                         int     0
START_B                         int     1
START_C                         int     2
START_D                         int     3
TARNS_COUNTER                   String  "tarnsCounter"
TRANS_AMOUNT                    String  "transAmount"
TRANS_AMOUNT_OTHER              String  "transAmountOther"
TRANS_DATE                      String  "transDate"
TRANS_FALLBACK                  String  "transFallback"
TRANS_MODE                      String  "transMode"
TRANS_TIME                      String  "transTime"
TRANS_TIMEOUT                   String  "transTimeout"
TRANS_TYPE                      String  "transType"
USE_ABECS                       String  "useABECS"
USE_CARD_READ_SUCCESS           String  "useCardReadSuccess"
USE_CT_RUPAY                    String  "useCTRupay"
USE_DELAY_PIN                   String  "useDelayPIN"
USE_ENCRYPT_AMEX_TRACK          String  "useEncryptAmexTrack"
USE_FILTER                      String  "useFilter"
USE_FORCED_AID_SELECTION        String  "useForcedAIDSelection"
USE_FORCED_ICC_AID_SELECTION    String  "useForcedIccAIDSelection"
USE_FORCED_RETURN_OF_CARD       String  "useForcedReturnOfCard"
USE_GAC1_FILTER                 String  "useGac1Filter"
USE_GAC2_FILTER                 String  "useGac2Filter"
USE_GPO_BEFORE_FILTER           String  "useGpoBeforeFilter"
USE_LOG                         String  "log"
USE_MAGSTRIPE_FILTER            String  "useMagstripeFilter"
USE_PPSE_FAIL_SEND_AIDS_OPTION  String  "usePPSEFailSendAidsOption"
USE_SELECT_AFTER_FILTER         String  "useSelectAfterFilter"
USE_SELECT_KERNEL               String  "useSelectKernel"
USE_SPECIAL_AID_SELECTION       String  "useSpecialAIDSelection"
USE_USA_VISA                    String  "useUSAVisa"
ENCRYPT_TRACK_USE_BCD           String  "encryptTrackUseBCD"
DOUBLE_BCD                      String  "doubleBCD"
ENCRYPT_TRACK2_EXPIRATION_DATE  String  "encryptTrack2ExpirationData"

5.17 ConstantPrinter            Type    Value
                                int     0
Constant Name
STATUS_IDLE                       108
STATUS_OVERHEAT                          int    2
STATUS_PRINTING                          int    1

5.18 ConstantPrinter.Align               Type   Description
                                         ENUM   Center alignment
Enum Constant                            ENUM   Left alignment
CENTER                                   ENUM   Right alignment
LEFT
RIGHT                                    TYPE   Description
                                         ENUM   CODABAR 1D format.
5.19 ConstantPrinter.BarcodeFormat       ENUM   Code 128 1D format.
                                         ENUM   Code 39 1D format.
Enum Constant                            ENUM   Code 93 1D format.
CODABAR                                  ENUM   Data Matrix 2D barcode format.
CODE_128                                 ENUM   EAN-8 1D format.
CODE_39                                  ENUM   QR Code 2D barcode format.
CODE_93                                  ENUM   UPC-E 1D format.
DATA_MATRIX
EAN_8                                    TYPE   Description
QR_CODE                                  ENUM   Aborts all pending print jobs in the
UPC_E                                    ENUM   queue
                                                Ignores current error and continues
5.20 ConstantPrinter.PrintFailurePolicy  Type   next print
                                         float
Enum Constant                            float  Value
ABORT_ALL                                float  36.0f
                                                24.0f
IGNORE_AND_CONTINUE                        109  16.0f

5.21 ConstantPrinter.FontSize                      Type  Value

Constant Name                                      int   2
LARGE
NORMAL                                             int   0
SMALL
                                                   int   1
5.22 ConstantSecurity
                                                   int   1
Constant Name
AUTHENTICATION_BOTH                                int   2
AUTHENTICATION_GENERATION
AUTHENTICATION_VERIFICATION
DUKPT_KEY_SELECT_DATA_REQUEST
DUKPT_KEY_SELECT_DATA_RESPONSE

DUKPT_KEY_SELECT_PIN_ENCRYPTION                    int  3

DUKPT_MAC_MODE_CBC                                 int  2

DUKPT_MAC_MODE_ECB                                 int  0

DUKPT_MODE_AES_MODE                                int  128

ENCRYPTION_ALGORITHM_AES                           int  16

ENCRYPTION_ALGORITHM_SM4                           int  32

ENCRYPTION_ALGORITHM_TDES                          int  0

ENCRYPTION_MECHANISM_DUKPT                         int  2

ENCRYPTION_MECHANISM_MK_SK                         int  1

KCV_MODE_CHK_0                                     int  1

KCV_MODE_CHK_EVEN                                  int  3

KCV_MODE_CHK_ODD                                   int  2

KCV_MODE_NO_VERIFY                                 int  0

KEY_ALG_TYPE_2TDEA                                 int  0

KEY_ALG_TYPE_3TDEA                                 int  16

KEY_ALG_TYPE_AES_128                               int  32

KEY_ALG_TYPE_AES_192                               int  48

KEY_ALG_TYPE_AES_256                               int  64

KSN_AUTO_INCREASING_BY_DUKPT_TDES_MAC_BOTH_KEY     int  0

KSN_NOT_AUTO_INCREASING_BY_DUKPT_TDES_MAC_BOTH_KEY int  20

KSN_NOT_AUTO_INCREASING_BY_DUKPT_TDES_MAC_RSP_KEY  int  40

MAC_ALGORITHM_ANSI_X9_19                           int  2

MAC_ALGORITHM_ANSI_X9_9                            int  3

MAC_ALGORITHM_CBC                                  int  0

MAC_ALGORITHM_XOR_ECB_MAC                          int  1

MAC_MODE_ANSI_X9_19                                int  2

MAC_MODE_ANSI_X9_9                                 int  3

MAC_MODE_CBC                                       int  0

MAC_MODE_XOR_ECB_MAC                               int  1

NOT_SELF_INCREASING                                int  0

OPERATION_DIRECTION_DECRYPT                        int  0

OPERATION_DIRECTION_ENCRYPT                        int  1

OPERATION_MODE_CBC                                 int  2

OPERATION_MODE_ECB                                 int  0

PED_CALC_DES_MODE_CBC_DEC                          int  2

PED_CALC_DES_MODE_CBC_ENC                          int  3

PED_CALC_DES_MODE_ECB_DEC                          int  0

PED_CALC_DES_MODE_ECB_ENC                          int  1

PED_CALC_DUKPT_MODE_DEC                            int  0

PED_CALC_DUKPT_MODE_ENC                            int  1

PED_CALC_RSA_MODE_NO_PADDING                       int  0

PED_CALC_RSA_MODE_OAEP_PADDING                     int  2

PED_CALC_RSA_MODE_PKCS1_PADDING                    int  1

                                 110
PED_PROTECT_KEY_TYPE_MKSK
PED_PROTECT_KEY_TYPE_RSA                     int  0
PED_PROTECT_TYPE_DEC
PED_PROTECT_TYPE_TR31                        int  2
PED_PROTECT_WRITE_TYPE_DUKPT
PED_PROTECT_WRITE_TYPE_TLK                   int  1
PED_PROTECT_WRITE_TYPE_TMK
PED_TAK                                      int  0
PED_TDK
PED_TEK                                      int  2
PED_TIK
PED_TLK                                      int  0
PED_TMK
PED_TPK                                      int  1
PED_TTK
PINBLOCK_DUKPT_FMT_ISO9564_0                 int  4
PINBLOCK_DUKPT_FMT_ISO9564_0_KSN_INC
PINBLOCK_DUKPT_FMT_ISO9564_1                 int  5
PINBLOCK_DUKPT_FMT_ISO9564_1_KSN_INC
PINBLOCK_DUKPT_FMT_ISO9564_2                 int  6
PINBLOCK_DUKPT_FMT_ISO9564_2_KSN_INC
PINBLOCK_DUKPT_FMT_ISO9564_4                 int  7
PINBLOCK_DUKPT_FMT_ISO9564_4_KSN_INC
PINBLOCK_TPK_FMT_ISO9564_0                   int  1
PINBLOCK_TPK_FMT_ISO9564_1
PINBLOCK_TPK_FMT_ISO9564_3                   int  2
PINBLOCK_TPK_FMT_ISO9564_4
SELF_INCREASING                              int  3
USE_BOTH_WAYS_KEY
USE_DATA_DECRYPT_KEY                         int  9
USE_DATA_ENCRYPT_KEY
WRITE_DUKPT_WITH_TMK_ALG_TYPE_AES            int  32
WRITE_DUKPT_WITH_TMK_ALG_TYPE_TDES
                                             int  0

                                             int  33

                                             int  1

                                             int  34

                                             int  2

                                             int  36

                                             int  4

                                             int  0

                                             int  1

                                             int  2

                                             int  4

                                             int  64

                                             int  2

                                             int  1

                                             int  0

                                             int  17

                                             int  16

5.23 ConstantScanner

Constant Name                                Type
ALL_BARCODES                                 ConstantScanner.BarcodeFormat[]
ONE_DIMENSIONAL_BARCODES                     ConstantScanner.BarcodeFormat[]
TWO_DIMENSIONAL_BARCODES                     ConstantScanner.BarcodeFormat[]

5.24 ConstantScanner.BarcodeFormat

Enum Constant         Type Description

                                        111
                     Stacked barcode format used in logistics and industrial applications
CODABLOCKF       1D  Primarily for telecom equipment, supports digits and hyphens
                     High-density linear barcode supporting ASCII, widely used in logistics and retail
CODE11           1D  General-purpose alphanumeric barcode for industrial applications
                     Improved version of Code 39 with higher density character support
CODE128          1D  International standard retail barcode (13-digit)
                     Compact version of EAN-13 for small products (8-digit)
CODE39           1D  Supply chain barcode based on Code 128 standard
                     Compact barcode for small retail items like produce
CODE93           1D  Hong Kong variant of Interleaved 2 of 5 barcode
                     Air cargo specific barcode format
EAN13            1D  Industrial variant of 25 barcodes
                     High-density numeric barcode for carton labeling
EAN8             1D  Variant of 25 barcode format
                     Inventory management barcode (digits only)
GS1_128          1D  UK barcode standard supporting full ASCII
                     North American retail product barcode (12-digit)
GS1_DATABAR      1D  Compressed version of UPC-A for small packages
                     US Postal Service tracking barcode
HK25             1D  Compact matrix barcode suitable for small spaces
                     2D barcode for product identification and marking
IATA25           1D  Dot-based barcode for high-speed industrial printing
                     Chinese-developed 2D barcode for Chinese characters
INDUSTRIAL25     1D  GS1-compliant version of Data Matrix
                     Chinese national standard 2D barcode
ITF25            1D  Fixed-size matrix barcode used in logistics
                     Compact PDF417 variant for ID documents
MATRIX25         1D  Stacked 2D barcode for transportation and ID cards
                     Popular matrix barcode for general-purpose use
MSI              1D

TELEPEN          1D

UPCA             1D

UPCE             1D

USPS4ST          1D

AZTEC            2D

DATAMATRIX       2D

DOTCODE          2D

GRIDMATRIX       2D

GS1_DATAMATRIX 2D

HANXIN           2D

MAXICODE         2D

MICROPDF         2D

PDF417           2D

QRCODE           2D

5.25 ConstantScanner.ScannerCameraType

Enum Constant        TYPE               Description
CAMERA_FRONT         ENUM               Front Camera
CAMERA_REAR          ENUM               Rear Camera
SCANNER              ENUM               E-Series Scanner

5.26 ConstantScanner.BarcodeSupport

Enum Constant        TYPE               Description
ALL_SUPPORT          ENUM               This barcode type is supported by both cameras and scanner
CAMERA_SUPPORT       ENUM               This barcode type is only supported by front/rear cameras
SCANNER_SUPPORT      ENUM               This barcode type is only supported by scanner

                                        112

Enum Constant                 TYPE           Description
BUTTON_BACKSPACE              ENUM           Backspace key
BUTTON_ENTER                  ENUM           Enter key
BUTTON_ESC                    ENUM           Escape key
BUTTON0                       ENUM           Number key 0
BUTTON1                       ENUM           Number key 1
BUTTON2                       ENUM           Number key 2
BUTTON3                       ENUM           Number key 3
BUTTON4                       ENUM           Number key 4
BUTTON5                       ENUM           Number key 5
BUTTON6                       ENUM           Number key 6
BUTTON7                       ENUM           Number key 7
BUTTON8                       ENUM           Number key 8
BUTTON9                       ENUM           Number key 9

5.28 ConstantPrinter.GrayPercent

Enum Constant                                TYPE           Description
GRAY_100                                     ENUM           100% gray level (fully opaque gray).
GRAY_70                                      ENUM           70% gray level.
GRAY_80                                      ENUM           80% gray level.
GRAY_90                                      ENUM           90% gray level

5.29 ConstantPrinter.GlobalFontSize                         Description
                                                            Large size.
Enum Constant                                TYPE           Normal size.
LARGE                                        ENUM           Small size.
NORMAL                                       ENUM
SMALL                                        ENUM           Description
                                                            Multiplier value of 0.5.
5.30 ConstantPrinter.LineSpaceMultiplier                    Multiplier value of 1.0.
                                                            Multiplier value of 1.5.
Enum Constant                                TYPE           Multiplier value of 2.0.
MULTIPLIER_05                                ENUM
MULTIPLIER_10                                ENUM           Description
MULTIPLIER_15                                ENUM           bluetooth
MULTIPLIER_20                                ENUM           localhost

5.31 ConstantEcr.ConnectType

Enum Constant                                TYPE
BT                                           ENUM
HOST                                         ENUM

                                             113
                                        ENUM               Connection timed out.
Enum Constant                           ENUM               Connected.
CONNECT_TIMEOUT                         ENUM               Connection error occurred.
CONNECTED                               ENUM               Disconnected.
CONNECTION_ERROR                        ENUM               Initial state.
DISCONNECTED                            ENUM               Read error occurred.
IDLE                                    ENUM               Server creation error occurred.
READ_ERROR                              ENUM               Server is listening.
SERVER_CREATE_ERROR                     ENUM               Write error occurred.
SERVER_LISTENING
WRTE_ERROR                              TYPE               Description
                                        int                Capacitive pinpad
5.33 ConstantGeneral.IndicatorType      int                Physical pinpad

Enum Constant
PINPAD_CAPACITIVE
PINPAD_PHYSICAL

