 5. Entity Class Definition ............................................................................................................33
  5.1 com.kozen.terminalmanager.Const .............................................................................................33
  5.2 com.kozen.terminalmanager.location.constant.LocationConstant .................................................... 34
  5.3 LocationConstant.GeoLanguage ................................................................................................ 34
  5.4 LocationConstant.LocationMode ................................................................................................34

                                                                                             4
  5.6 ApnConfiguration ....................................................................................................................35
  5.7 com.kozen.terminalmanager.device.constant.WakeUpType ........................................................... 35
 5. Entity Class Definition

5.1 com.kozen.terminalmanager.Const  Type    Value
                                     int     -1
Constant Name                        int     0
FUN_ERROR                            String  "android.intent.action.XC_TERMINAL_MANAGE
FUN_SUCC                                     R_SERVICE"
TERMINAL_MANAGER_SERVICE_ACTION      String  "com.kozen.terminalmanager.service.TerminalMana
                                             gerService"
TERMINAL_MANAGER_SERVICE_CLASS       String  "com.kozen.terminalmanager.service"

TERMINAL_MANAGER_SERVICE_PACKAGE

                                     33

Constant Name                      Type                            Value
GEO_BUNDLE_KEY_CUSTOMID            String                          "customId"
GEO_BUNDLE_KEY_FENCESTATUS         String                          "event"
GEO_BUNDLE_KEY_LOCERRORCODE        String                          "location_errorcode"
GEO_STATUS_IN                      int                             1
GEO_STATUS_LOCFAIL                 int                             4
GEO_STATUS_OUT                     int                             2
GPS_ACCURACY_BAD                   int                             0
GPS_ACCURACY_GOOD                  int                             1
GPS_ACCURACY_UNKNOWN               int                             -1
GPS_STATUS_MODE_SAVING             int                             3
GPS_STATUS_NOGPSPERMISSION         int                             4
GPS_STATUS_NOGPSPROVIDER           int                             1
GPS_STATUS_OFF                     int                             2
GPS_STATUS_OK                      int                             0
LOCATION_PROVIDER_GPS              String                          "gps"
LOCATION_PROVIDER_LBS              String                          "lbs"
LOCATION_TYPE_CELL                 int                             6
LOCATION_TYPE_COARSE_LOCATION      int                             11
LOCATION_TYPE_FIX_CACHE            int                             4
LOCATION_TYPE_GPS                  int                             1
LOCATION_TYPE_LAST_LOCATION_CACHE  int                             9
LOCATION_TYPE_OFFLINE              int                             8
LOCATION_TYPE_SAME_REQ             int                             2
LOCATION_TYPE_WIFI                 int                             5
TRUSTED_LEVEL_BAD                  int                             4
TRUSTED_LEVEL_HIGH                 int                             1
TRUSTED_LEVEL_LOW                  int                             3
TRUSTED_LEVEL_NORMAL               int                             2

5.3 LocationConstant.GeoLanguage

Enum Constant   TYPE               Description
DEFAULT         ENUM               Returns reverse geocoding info in local language
EN              ENUM               Always returns reverse geocoding info in English
ZH              ENUM               Always returns reverse geocoding info in Chinese

5.4 LocationConstant.LocationMode

Enum Constant   TYPE               Description
Battery_Saving  ENUM               Low-power positioning mode
Device_Sensors  ENUM               Device-only positioning mode
Hight_Accuracy  ENUM               High-accuracy positioning mode

                                                 34

Enum Constant                    TYPE     Description
BEIDOU_FIRST                     ENUM     In high-accuracy positioning mode, performs a single location
                                          operation and prioritizes returning BeiDou satellite positioning
DEFAULT                          ENUM     information.
                                          In high-accuracy positioning mode, performs a single location
GPS_FIRST                        ENUM     operation, and the system returns the first available positioning
                                          result.
                                          In high-accuracy positioning mode, performs a single location
                                          operation and prioritizes returning GPS satellite positioning
                                          information

5.6 ApnConfiguration

Constant Name                    TYPE     Description
apn                              String   APN name.
authType                         int      Authentication type.
current                          boolean  Enable current APN.
mcc                              String   Mobile Country Code (MCC).
mmsc                             String   MMSC URL.
mmsPort                          String   MMS proxy port.
mmsProxy                         String   MMS proxy address.
mnc                              String   MNC Mobile Network Code (MNC).
name                             String   Entry name.
numeric                          String   Operator Network Identification.
password                         String   APN password.
port                             String   Proxy port.
protocol                         String   The protocol to use to connect to this APN.
proxy                            String   Proxy address.
roaming_protocol                 String   The protocol to use to connect to this APN when roaming.
server                           String   Server address.
type                             String   Comma-delimited list of APN types.
user                             String   APN username.

5.7 com.kozen.terminalmanager.device.constant.WakeUpType

Enum Constant                    TYPE     Description
TAP_OR_INSERT_CARD               ENUM     Wake up by IC card insertion or NFC card tapping
SCREEN_DOUBLE_TAP                ENUM     Wake up by screen double tap
LIFT_TO_WAKE                     ENUM     Lift to wake screen

