 4. Error Code Definition ............................................................................................................. 86
  4.1 CardReaderError .................................................................................................................... 86
  4.2 CommonError ......................................................................................................................... 88
  4.3 GeneralError .......................................................................................................................... 88
  4.4 PinpadError ........................................................................................................................... 88
  4.5 PrinterError ........................................................................................................................... 89
  4.6 ScannerError ..........................................................................................................................89
  4.7 SecurityError ..........................................................................................................................90
  4.8 EmvError ...............................................................................................................................91
  4.9 PosEmvErrorCode ...................................................................................................................93
  4.10 EcrError .............................................................................................................................. 94
 4. Error Code Definition                         Error Description                       Error Value
                                                  APDU Error                                   -70004
4.1 CardReaderError                               Card Check Other Error                       -70003
                                                  Contact Card ATR Data Error                  -72001
Error Code                                        IC Card Not Supported                        -72000
CARD_APDU_OTHER_ERROR                             Contact Card Insertion Failed                -72002
CARD_CHECK_OTHER_ERROR
CARD_CONTACT_ATR_ERROR                         86
CARD_CONTACT_NO_SUPPORT
CARD_CONTACT_OTHERS_ERROR
CARD_CONTACTLESS_NO_SUPPORT              IC Card Not Supported                     -73000
CARD_CONTACTLESS_OTHERS_ERROR            Contactless Card Other Error              -73002
CARD_EXIST_STATUS_OTHER_ERROR            Card Present Status Other Error           -70005
CARD_FELICA_ATS_ERROR                    Contactless Card ATS Data Error           -74001
CARD_FELICA_NO_SUPPORT                   IC Card Not Supported                     -74000
CARD_FELICA_OTHERS_ERROR                 Contactless Card Other Error              -74002
                                         Magnetic Track or Data Verification
CARD_MAG_INVALID_ERROR                   Failed                                    -71003
                                         Magnetic Card Swipe Failed, Please Retry
CARD_MAG_NEED_RETRY_ERROR                No Data in Magnetic Track                 -71002
CARD_MAG_NO_DATA_ERROR                   Magnetic Card Not Supported               -71001
CARD_MAG_NO_SUPPORT                      Magnetic Card Swipe Failed                -71000
CARD_MAG_OTHERS_ERROR                    IC Card Already Powered Off               -71004
CARD_READER_CONTACT_ALREADY_CLOSE        Contact Card Check Failed                 -72006
CARD_READER_CONTACT_CHECK_ERROR          Contact Card Power-Off Failed             -72004
CARD_READER_CONTACT_OFF_ERROR            Magnetic Card Check Open Failed           -72005
CARD_READER_CONTACT_OPEN_ERROR           Contactless Card Already Powered Off      -72003
CARD_READER_CONTACTLESS_ALREADY_CLOSE    Contactless Card Check Failed             -73006
CARD_READER_CONTACTLESS_CHECK_ERROR      Multiple Contactless Cards Detected       -73004
CARD_READER_CONTACTLESS_MULTI_CARD       Contactless Card Power-Off Failed         -73007
CARD_READER_CONTACTLESS_OFF_ERROR        Magnetic Card Check Open Failed           -73005
CARD_READER_CONTACTLESS_OPEN_ERROR       Contactless Card Already Powered Off      -73003
CARD_READER_FELICA_ALREADY_CLOSE         Contactless Card Check Failed             -74006
CARD_READER_FELICA_CHECK_ERROR           Contactless Card Power-Off Failed         -74004
CARD_READER_FELICA_OFF_ERROR             Magnetic Card Check Open Failed           -74005
CARD_READER_FELICA_OPEN_ERROR            Magnetic Card Check Failed                -74003
CARD_READER_MAG_CHECK_ERROR              Magnetic Card Power-Off Failed            -71006
CARD_READER_MAG_OFF_ERROR                Magnetic Card Check Open Failed           -71007
CARD_READER_MAG_OPEN_ERROR               Card Power-Off Other Error                -71005
CARD_READER_OFF_OTHER_ERROR              Card Type Error                           -70002
CARD_TYPE_ERROR                          NFC TAG already closed                    -70001
NFC_TAG_ALREADY_CLOSE                    NFC TAG data error                        -75006
NFC_TAG_NDEF_MESSAGE_ERROR               NDEFMessage data length exceeds limit     -75004
                                         (max: 255 bytes)
NFC_TAG_NDEF_MESSAGE_LENGTH_ERROR        NFC TAG not supported                     -75005
                                         NFC TAG close failed
NFC_TAG_NO_SUPPORT                       NFC TAG open failed                       -75000
NFC_TAG_OFF_ERROR                        Other NFC TAG error                       -75002
NFC_TAG_OPEN_ERROR                       NFC TAG write failed                      -75001
NFC_TAG_OTHERS_ERROR                     Simultaneous contactless and Felica card  -75007
NFC_TAG_WRITE_MESSAGE_ERROR              check not supported                       -75003
NOT_SUPPORT_CHECK_CONTACTLESS_AND_FELIC  Simultaneous contactless and Felica card
A_SIMULTANEOUS                           power-on not supported                    -73008
NOT_SUPPORT_OPEN_CONTACTLESS_AND_FELICA
_SIMULTANEOUS                                                                      -73009

87
                                           Illegal parameters                    -10002
Error Code
FINANCIAL_PARAMETERS_INVALID

FINANCIAL_SERVICE_DISCONNECT               Financial services are not connected, -10001
                                           please initialize financial services

FINANCIAL_VERSION_NOT_MATCH                Financial Services SDK  version -10000
                                           mismatch
FEATURE_NOPERMISSION                       Permission not granted             -10010
FEATURE_UNSUPPORTED                        Feature unsupported                -10011

4.3 GeneralError

Error Code                                 Error Description                     Error Value
GENERAL_ERROR_INIT                         General module initialization error   -20000
GENERAL_OTHER_ERROR                        Other general error                   -20001
GENERAL_PARAMETERS_INVALID                 Invalid parameters                    -20002
GENERAL_NAVIGATION_BUTTON_TYPE_INVALID     Invalid navigation button type        -20003
GENERAL_SCREEN_ROTATION_ERROR              Screen rotation error                 -20004
GENERAL_SET_BEEP_ERROR                     Failed to set beep                    -20005
GENERAL_INDICATOR_TYPE_ERROR               Indicator type error                  -20100
GENERAL_INDICATOR_TYPE_PINPAD_CAPACITIVE   Capacitive PINPAD indicator type
_ERROR                                     error                                 -20101

4.4 PinpadError

Error Code                                 Error Description                     Error Value
PINPAD_OTHER_ERROR                         Other PINPAD error                    -60000
PINPAD_START_ERROR                         Failed to start PINPAD                -60001
PINPAD_CANCEL_ERROR                        PINPAD operation canceled             -60002
                                           Screen orientation changed during     -60003
PINPAD_SCREEN_ORIENTATION_CHANGED          PINPAD operation                      -60004
                                           PIN key coordinate calculation error  -60005
PIN_KEY_COORDINATE_CALCULATION_ERROR       Failed to switch to blind PIN mode    -60006
PIN_SWITCH_BLIND_MODE_ERROR                Failed to calculate physical PINPAD
SP_ERROR_PHYSICAL_PINPAD_CALCULATE_KEY_P   key position                          -60007
OSITION_ERROR                              Current service provider does not
CURRENT_SP_NOT_SUPPORT_GET_PINPAD_TYPE_E   support getting PINPAD type           -60008
RROR                                       Current service provider does not
CURRENT_SP_NOT_SUPPORT_PHYSICAL_PINPAD_E   support physical PINPAD               -60009
RROR                                       Physical PINPAD does not support key  -60010
PHYSICAL_PINPAD_NOT_SUPPORT_KEY_POSITION_  position parameters
PARAM_ERROR                                Invalid key view position parameters
PINPAD_KEY_VIEW_POSITION_PARAM_ERROR

                              88
CUSTOM_PINPAD_START_ERROR           Failed to start custom PINPAD              -60012
BLIND_PINPAD_START_ERROR            Failed to start blind PINPAD               -60013

4.5 PrinterError                    Error Description                          Error Value
                                    Printer not initialized or initialization  -50000
Error Code                          failed
PRINTER_ERROR_INIT                  No printer device                          -50001
                                    Printer not opened                         -50002
PRINTER_ERROR_NO_PRINTER            Print failed                               -50003
PRINTER_ERROR_NOT_OPENED            Printer overheating                        -50004
PRINTER_ERROR_PRINT                 Printer out of paper                       -50005
PRINTER_ERROR_OVERHEAT              Printing is not possible when the          -50006
PRINTER_ERROR_NO_PAPER              battery level is low
PRINTER_ERROR_LOW_POWER             No content to print                        -50007
                                    Other unknown error                        -50008
PRINTER_ERROR_NO_CONTENT            Print queue overflow                       -50009
PRINTER_ERROR_OTHER                 Screen off, unable to print                -50010
PRINTER_ERROR_QUEUE_OVER_FLOW       Feature or parameter not supported         -50011
PRINTER_ERROR_SCREEN_OFF            Configuration not allowed during           -50012
PRINTER_ERROR_NOT_SUPPORT           printing
PRINTER_ERROR_PRINTING
                                    Error Description                          Error Value
4.6 ScannerError                    Scanner service not found                  -30000
                                    Scanner service unavailable                -30001
Error Code                          Failed to connect to scanner service       -30002
SCANNER_SERVICE_NOT_FIND            Scanner service not connected, please      -30003
SCANNER_SERVICE_UNAVAILABLE         call open to initialize
SCANNER_SERVICE_CONNECT_FAILED      Other unknown error                        -30004
SCANNER_SERVICE_DISCONNECT          Camera is occupied, please call close to   -30005
                                    release resources first
SCANNER_OTHER_ERROR                 Current device does not support this       -30006
CAMERA_OCCUPIED                     camera type
                                    Failed to get camera information,          -30007
CAMERA_UNKNOWN                      please rebind Financial SDK
                                    Camera initialization failed, try close    -30008
GET_CAMERA_INFO_ERROR               then open again
                                    Camera does not support light control      -30009
INIT_CAMERA_ERROR                   Failed to turn on fill light, must be      -30010
                                    called after scan UI is started
NOT_SUPPORT_LIGHT_CONTROL           No decode type set, please set scan        -30011
OPEN_LIGHT_FAILED

NO_SCAN_TYPE_SET

                                89
                                          Failed to enable or disable decode type,
PARAMETER_EXCEPTION                       please check parameters                   -30013
NOT_SUPPORTED_FEATURE                     Parameter exception                       -30014
                                          Current camera type does not support
PREVIEW_MODE_EXCEPTION                    this feature                              -30015
CAMERA_SESSION_ERROR                      Preview mode exception                    -30016
CAMERA_CLOSED_ERROR                       Camera session error                      -30017
                                          Camera was unexpectedly closed

4.7 SecurityError

Error Code                                Error Description                         Error Value
SECURITY_ERROR_INIT                                                                 -40000
SECURITY_OTHER_ERROR                      Security module not initialized           -40001

SECURITY_PARAMETERS_INVALID               Other error (e.g. system                  -40002

SECURITY_KEY_TYPE_OUT_OF_RANGE            interface call exception)                 -40003
SECURITY_KEY_INDEX_OUT_OF_RANGE                                                     -40004
SECURITY_DATA_INDEX_OUT_OF_RANGE          Invalid parameters (null or               -40005
SECURITY_TLK_INDEX_OUT_OF_RANGE                                                     -40006
SECURITY_KEY_IN_EMPTY_ERROR               illegal format)                           -40007
SECURITY_DATA_IN_EMPTY_ERROR                                                        -40008
SECURITY_DATA_OUT_NULL_ERROR              Key type out of range                     -40009
SECURITY_DATA_OUT_LENGTH_ERROR                                                      -40010
                                          Key index out of range
SECURITY_KCV_MODE_ERROR                                                             -40011
SECURITY_KCV_ERROR                        Data index out of range                   -40012
SECURITY_RANDOM_KEY_OUT_OF_RANGE                                                    -40013
                                          TLK index out of range
SECURITY_KCV_VALUE_OUT_OF_RANGE                                                     -40014
SECURITY_MKSK_KEY_TYPE_ERROR              Key input data is empty                   -40100
SECURITY_MKSK_SRC_KEY_TYPE_ERROR                                                    -40101
SECURITY_MKSK_KEY_INDEX_ERROR             Input data is empty                       -40102
SECURITY_MKSK_SRC_KEY_INDEX_ERROR                                                   -40103
SECURITY_MKSK_KEY_LENGTH_ERROR            Output data is null                       -40104
SECURITY_MKSK_ENCRYPTION_ALGORITHM_ERROR                                            -40105
                                          Output        buffer       length
SECURITY_MKSK_CALC_MODE_ERROR                                                       -40106
SECURITY_MKSK_MAC_MODE_ERROR              insufficient                              -40107
SECURITY_MKSK_MAC_OUT_OF_RANGE                                                      -40108
                                          KCV mode error
SECURITY_MKSK_CALC_OUT_OF_RANGE                                                     -40109
                                          KCV parameter error

                                          Random key output length out

                                          of range

                                          KCV output value out of range

                                          MK/SK key type out of range

                                          MK/SK source key type error

                                          MK/SK key index error

                                          MK/SK source key index error

                                          MK/SK key length error

                                          MK/SK encryption algorithm

                                          error

                                          MK/SK calculation mode error

                                          MK/SK MAC mode error

                                          MK/SK MAC output length out

                                          of range

                                          MK/SK calculation output

                        90
SECURITY_SM4_CALC_OUT_OF_RANGE             SM4 calculation mode error     -40111
                                           SM4 calculation output length
SECURITY_DUKPT_TIK_INDEX_ERROR             out of range                   -40200
SECURITY_DUKPT_SRC_KEY_INDEX_ERROR         DUKPT TIK key index error      -40201
SECURITY_DUKPT_KEY_USAGE_ERROR             DUKPT source key index error   -40202
                                           DUKPT key usage parameter
SECURITY_DUKPT_KEY_ALG_TYPE_ERROR          error                          -40203
                                           DUKPT key algorithm type
SECURITY_DUKPT_MAC_ALG_TYPE_ERROR          error                          -40204
                                           DUKPT MAC algorithm type
SECURITY_DUKPT_INIT_VECTOR_ERROR           error                          -40205
                                           DUKPT init vector parameter
SECURITY_DUKPT_AES_VECTOR_ERROR            error                          -40206
                                           DUKPT AES init vector
SECURITY_DUKPT_KEY_TYPE_ERROR              parameter error                -40207
                                           DUKPT key type parameter
SECURITY_DUKPT_OPERATION_MODE_ERROR        error                          -40208
SECURITY_DUKPT_OPERATION_DIRECTION_ERROR   DUKPT operation mode error     -40209
                                           DUKPT operation direction
SECURITY_DUKPT_KSN_MODE_ERROR              error                          -40210
SECURITY_DUKPT_KEY_LENGTH_ERROR            DUKPT KSN mode error           -40211
SECURITY_DUKPT_CALC_OUT_OF_RANGE           DUKPT key length error         -40212
                                           DUKPT calculation output
SECURITY_DUKPT_MAC_OUT_OF_RANGE            length out of range            -40213
                                           DUKPT MAC output length out
SECURITY_DUKPT_KSN_OUT_OF_RANGE            of range                       -40214
                                           DUKPT KSN output length out
SECURITY_RSA_KEY_INDEX_OUT_OF_RANGE        of range                       -40300
SECURITY_RSA_PADDING_MODE_ERROR            RSA key index out of range     -40301
SECURITY_RSA_RESPONSE_DATA_EMPTY           RSA padding mode error         -40302
SECURITY_RSA_OUT_DATA_LENGTH_OUT_OF_RANGE  RSA response data is empty     -40303
                                           RSA output data length out of
SECURITY_TR31_SRC_KEY_TYPE_ERROR           range                          -40401
SECURITY_TR31_SRC_KEY_INDEX_ERROR          TR31 source key type error     -40402
SECURITY_TR31_KEY_TYPE_ERROR               TR31 source key index error    -40403
SECURITY_TR31_KEY_INDEX_ERROR              TR31 key type error            -40404
SECURITY_TR31_KEY_BLOCK_EMPTY_ERROR        TR31 key index error           -40405
SECURITY_TR31_KEY_ALGORITHM_ERROR          TR31 key block is empty        -40406
                                           TR31 key algorithm type error

4.8 EmvError

Error Code                Error Description                               Error Value
EMV_AID_OTHER_ERROR       Other AID parameter error                       -80100

                     91
                                           error
EMV_CAPK_OTHER_ERROR                       Other CAPK error                      -80200
EMV_DELETE_AID_ERROR                       Error deleting AID parameter          -80109
EMV_DELETE_APPLE_MERCHANT_ERROR            Error deleting Apple Merchant         -80405
EMV_DELETE_APPLE_TERMINAL_ERROR            Error deleting Apple Terminal         -80402
EMV_DELETE_CAPK_ERROR                      Error deleting CAPK                   -80209
EMV_DELETE_DRL_ERROR                       Error deleting DRL configuration      -80310
EMV_DELETE_EXCEPTION_FILE_ERROR            Error deleting ExceptionFile          -80305
EMV_DELETE_REVOCATION_IPK_ERROR            Error deleting RevocationIPK          -80308
EMV_DELETE_SERVICE_ERROR                   Error deleting RuPay Service          -80314
EMV_DRL_OTHER_ERROR                        Other DRL configuration error         -80309
EMV_GET_APPLE_MERCHANT_ERROR               Error retrieving Apple Merchant       -80404
EMV_GET_DRL_ERROR                          Error retrieving DRL configuration    -80311
EMV_GET_KERNEL_VERSION_ERROR               Error retrieving Kernel version       -80316
EMV_GET_SERVICE_ERROR                      Error retrieving RuPay Service        -80315
EMV_GET_TERMINAL_ERROR                     Error retrieving terminal parameters  -80302
EMV_OTHER_ERROR                            Other EMV error                       -80001
EMV_SERVICE_OTHER_ERROR                    Other RuPay Service error             -80312
EMV_SET_AID_ERROR                          Error setting AID parameter           -80108
EMV_SET_AID_ERROR_AID_NULL                 Error loading AID parameter, AID is   -80101
                                           null
EMV_SET_AID_ERROR_DDOL_NULL                Error loading AID parameter, DDOL is  -80103
                                           null
EMV_SET_AID_ERROR_TACDEFAULT_NULL          Error loading AID parameter,          -80107
                                           TACDefault is null
EMV_SET_AID_ERROR_TACDENIAL_NULL           Error loading AID parameter,          -80105
                                           TACDenial is null
EMV_SET_AID_ERROR_TACONLINE_NULL           Error loading AID parameter,          -80106
                                           TACOnline is null
EMV_SET_AID_ERROR_TDOL_NULL                Error loading AID parameter, TDOL is  -80104
                                           null
EMV_SET_AID_ERROR_VERSION_NULL             Error loading AID parameter, Version  -80102
                                           is null
EMV_SET_APPLE_MERCHANT_ERROR               Error setting Apple Merchant          -80403
EMV_SET_APPLE_TERMINAL_ERROR               Error setting Apple Terminal          -80401
EMV_SET_CAPK_ERROR                         Error setting CAPK                    -80208
EMV_SET_CAPK_ERROR_ALGORITHM_IND_NULL      Error loading CAPK parameter,         -80206
                                           AlgorithmInd is null
EMV_SET_CAPK_ERROR_CAPK_INDEX_NULL         Error loading CAPK parameter,         -80202
                                           CapkIndex is null
EMV_SET_CAPK_ERROR_CHECK_SUM_NULL          Error loading CAPK parameter,         -80205
                                           Checksum is null
EMV_SET_CAPK_ERROR_Exponent_NULL           Error loading CAPK parameter,         -80204

                                       92
                                         Error loading CAPK parameter,
EMV_SET_CAPK_ERROR_MODULE_NULL           HashInd is null                         -80203
                                         Error loading CAPK parameter,
EMV_SET_CAPK_ERROR_RID_NULL              Module is null                          -80201
                                         Error loading CAPK parameter, RID is
EMV_SET_CARD_INFO_RESPONSE_ERROR         null                                    -81004
EMV_SET_DRL_ERROR                        Error setting card confirmation result  -80309
EMV_SET_EXCEPTION_FILE_ERROR             Error setting DRL configuration         -80304
EMV_SET_KERNEL_ERROR                     Error setting ExceptionFile             -80317
EMV_SET_ONLINE_RESPONSE_ERROR            Error setting KernelTag                 -81006
EMV_SET_PIN_RESPONSE_ERROR               Error setting online result             -81005
EMV_SET_REVOCATION_IPK_ERROR             Error setting PIN result                -80307
EMV_SET_SELECT_RESPONSE_ERROR            Error setting RevocationIPK             -81003
                                         Error setting multi-application
EMV_SET_SELECT_RESPONSE_POSITION_ERROR   selection result                        -81007
                                         Error confirming position in
EMV_SET_SERVICE_ERROR                    multi-application selection result      -80313
EMV_SET_TERMINAL_ERROR                   Error setting RuPay Service             -80301
EMV_START_TRANSACTION_ERROR              Error loading terminal parameters       -81001
EMV_STOP_TRANSACTION_ERROR               Error starting transaction              -81002
EMV_SUCCESS                              Error stopping transaction              0
EMV_TERMINAL_EXCEPTION_FILE_OTHER_ERROR  Success                                 -80303
EMV_TERMINAL_OTHER_ERROR                 Other ExceptionFile error               -80300
EMV_TERMINAL_REVOCATION_IPK_OTHER_ERROR  Other terminal parameter error          -80306
                                         Other RevocationIPK error

4.9 PosEmvErrorCode

Error Code                               Error Description                       Error Value
APPLE_VAS_APPROVED                       Apple Vas Approved.                     6
APPLE_VAS_FAILED                         Apple Vas Failed.                       -41
APPLE_VAS_UNTREATED                      Apple Vas Untreated.                    -40
APPLE_VAS_WAITING_ACTIVATION             Apple Vas Waiting Activation.           -43
APPLE_VAS_WAITING_INTERVENTION           Apple Vas Waiting Intervention.         -42
EMV_APP_BLOCKED                          Application Blocked.                    -7
EMV_APP_EMPTY                            No Application.                         -9
EMV_APPROVED                             Transaction Approved.                   1
EMV_APPROVED_ONLINE                      Transaction Online Approved.            2
EMV_CANCEL                               Trans Cancel.                           -1
EMV_CARD_BLOCKED                         Card Locked.                            -8
EMV_CARD_ERROR                           Abecs Fallback.                         -40
EMV_COMMAND_FAIL                         Read the Card Fail.                     -3
EMV_DATA_ERROR                           Card Data Error.                        -81

                                93
EMV_DELAYED_APPROVED                          Transaction Delayed Approved.          5
EMV_ENCRYPT_ERROR                             Trade Encrypt Error.                   -30
EMV_FALLBACK                                  Fallback.                              -4
EMV_FORCE_APPROVED                            Transaction Force Approved.            4
EMV_GPO_6985                                  Command GPO 6985.                      -50
EMV_MULTI_CONTACTLESS                         Read Multi Contactless.                -5
EMV_NOT_ACCEPTED                              Not Accepted.                          -11
EMV_NOT_ALLOWED                               Not Allowed.                           -10
EMV_OK                                        Handle OK.                             0
EMV_OTHER_ERROR                               Other Error Exceptions.                -999
EMV_OTHER_ICC_INTERFACE                       Not Pure Magnetic Strip.               -6
EMV_OTHER_INTERFACE                           Try Another Interface.                 -14
EMV_READ_RECORD_ERROR                         Command Read Record Error.             -80
EMV_SEE_PHONE                                 See Phone.                             -13
EMV_TERMINATED                                Terminated.                            -12
EMV_TERMINATED_ON_MCCS                        Terminated On MCCS.                    -44
EMV_TIMEOUT                                   Trans Timeout.                         -2
EMV_UNENCRYPTED                               Trade Unencrypted.                     -31
EXCEPTION_ERROR                               Exception Error.                       255
PARAMETER_ERROR                               Parameter Error.                       254

4.10 EcrError                                 Error Description                      Error Value
                                              Failed to close connection                    -90006
Error Code                                    Connection failed                             -90003
ECR_CONNECT_CLOSE_FAILED                      Connection parameter info is empty            -90001
ECR_CONNECT_FAILED                            Connection parameter format exception         -90002
ECR_CONNECT_INFO_EMPTY                        ECR module not initialized                    -90000
ECR_CONNECT_INFO_FORMAT_EXCEPTION             File handle is null                           -90004
ECR_ERROR_INIT                                File handle format exception                  -90005
ECR_FD_EMPTY                                  Write data is empty                           -90007
ECR_FD_FORMAT_EXCEPTION                       Write data exception                          -90008
ECR_WRITE_DATA_EMPTY
ECR_WRITE_DATA_FAILED

