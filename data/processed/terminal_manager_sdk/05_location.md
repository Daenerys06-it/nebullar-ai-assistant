 3.5 Location module ...............................................................................................................18
Declaration on Location Interface ................................................................................................... 18
Our location interface is designed solely to provide location-related services to applications. ..................18
 It does not actively collect device information such as SN, IMEI, or hardware identifiers. ................. 18
 It does not transmit any device information or location data to external servers without explicit

application request and authorization. ............................................................................................. 18
 All data access is limited to the scope necessary for location service functionality. .......................... 18
This ensures that the interface complies with user privacy protection and security requirements. ............. 18
-- Get Location module - getLocationManager-- ............................................................................ 18
3.5.1 Enables the location module and initializes related resources ..................................................... 19
3.5.2 Enables the location module and initializes related resources by key ........................................... 19
3.5.3 Set location parameters ......................................................................................................... 19
3.5.4 Start a single location request .................................................................................................19
3.5.5 Registers a location callback listener ...................................................................................... 20
3.5.6 Removes the location listener .................................................................................................20
3.5.7 Stop the location service ........................................................................................................20
3.5.8 Creates a circular geofence .................................................................................................... 20
3.5.9 Registers a listener for geofence creation results ....................................................................... 21
3.5.10 Set the action for receiving geofence status broadcasts ............................................................. 21
3.5.11 Removes all geofences .........................................................................................................21
3.5.12 Add an APK to a block list ...................................................................................................21
3.5.13 Remove an APK from the blocked list ................................................................................... 21
3.5.14 Check if an APK is in block ................................................................................................. 22
3.5.15 Retrieves the list of blocked APKs ........................................................................................ 22
3.5.16 Disables the geofence feature ............................................................................................... 22
3.5.17 Enable the location module and initialize with the specified method .......................................... 22
3.5.18 Enable the location module and initialize with the specified key and method ...............................22
-- Location changed listener - ILocationChangedListener-- ............................................................. 23
3.5.19 Location changed callback ...................................................................................................23
-- GeoFence create listener - GeoFenceCreateListener -- ................................................................23
3.5.20 Callback for geofence creation completion ..............................................................................23
 3.5 Location module

Declaration on Location Interface
Our location interface is designed solely to provide location-related services to applications.
 It does not actively collect device information such as SN, IMEI, or hardware identifiers.
 It does not transmit any device information or location data to external servers without explicit application request

      and authorization.
 All data access is limited to the scope necessary for location service functionality.
This ensures that the interface complies with user privacy protection and security requirements.

-- Get Location module - getLocationManager--

int addToBlockOpenAppList(String pkgName)                                                            Add an APK to a block list
List<String> getBlockOpenAppList()
boolean isInBlockOpenAppList(String pkgName)                                                         Get the list of blocked APKs
void onDestroy()                                                                                     Check if an APK is in block
int open()                                                                                           Destroy location and geofencing resources
                                                                                                     Start the location module and initialize
int open(String key)                                                                                 related resources.
                                                                                                     Start the location module and initialize
int open(LocationConstant.LocationType locationType)                                                 related resources by key.
                                                                                                     Enable the positioning module, specify the
int open(String key,                                                                                 positioning method, and initialize the related
LocationConstant.LocationType locationType)                                                          resources.
                                                                                                     Enable the positioning module, specify the
int registerGeoFenceCreateListener(IGeoFenceCreateListener                                           positioning key and method, and initialize the
listener)                                                                                            related resources.
int registerLocationListener(ILocationChangedListener listener)                                      Register a listener for geofence creation
int removeAllGeoFence()                                                                              results
int removeFromBlockOpenAppList(String pkgName)                                                       Register a location callback listener
int setGeoFenceResultAction(String action,                                                           Remove all geofences
String pkgName)                                                                                      Remove an APK from the blocked list
int setLocationOption(LocationClientOption locationClientOption)                                     Set the action to receive geofence status
int startOnceLocation()                                                                              broadcasts.
int stopLocation()                                                                                   Set location parameters
                                                                                                     Start a single location request
                                                                                                 18  Stop location services
int addGeoFence(double longitude,                                    Create a circular geofence
double latitude,
float radius,
String customId)

3.5.1 Enables the location module and initializes related resources

Prototype     int open()
Function      Enables the location module and initializes related resources.
Parameters
              0: Operation successful;
Return value  Others: Operation failed. Refer to LocationError for specific error codes.

Notes

3.5.2 Enables the location module and initializes related resources by key

Prototype     int open(String key)
Function      Enables the location module and initializes related resources.
Parameters    key - The API key for location.
Return value  By default, the system-signed key is used.
              0: Operation successful;
Notes         Others: Operation failed. Refer to LocationError for specific error codes.
              If the system-signed key fails (location fails with error code ERROR_CODE_FAILURE_AUTH),
              Please contact Kozen FAE to generate a special API key. Then call onDestroy first, and use this
              API to reinitialize the location module by passing the API key.

3.5.3 Set location parameters

Prototype     int setLocationOption(LocationClientOption locationClientOption)
Function      Set location parameters. Must be used after open is successful.
Parameters    locationClientOption - Location parameters.
Return value  0: Operation successful; Others: Operation failed. Refer to LocationError for specific error codes.
              Default configuration parameters:
Notes         1. High-accuracy mode;
              2. Location request interval is 2000ms;
              3. Network location timeout is 30s;
              4. No reverse geocoding address information;
              5. Reverse geocoding language is selected based on the region;
              6. Signal selection is network plus GPS

3.5.4 Start a single location request

Prototype     int startOnceLocation()
Function      Start a single location request. Must be used after open is successful.
Parameters
                                                                             19
Notes         Others: Operation failed. Refer to LocationError for specific error codes.
              The location request will automatically stop after completion. You can also call stopLocation to
              terminate the location request during the process

3.5.5 Registers a location callback listener

Prototype     int registerLocationListener(ILocationChangedListener listener)
Function      Registers a location callback listener
Parameters    listener - Callback interface for location updates.
Return value  0: Operation successful;
              Others: Operation failed. Refer to LocationError for specific error codes.
Notes         Must be used after open is successful. Only one listener can be registered globally; new
              registrations will overwrite previous ones.
              Call unRegisterLocationListener to remove the listener when it is no longer needed

3.5.6 Removes the location listener

Prototype     int unRegisterLocationListener()
Function      Removes the location listener.
Parameters
              0: Operation successful;
Return value  Others: Operation failed. Refer to LocationError for specific error codes.
              Must be used after open is successful.
Notes

3.5.7 Stop the location service

Prototype     int stopLocation()
Function      Stop the location service.
Parameters
              0: Operation successful;
Return value  Others: Operation failed. Refer to LocationError for specific error codes.
              Must be used after open is successful.
Notes

3.5.8 Creates a circular geofence

Prototype     int addGeoFence(double longitude,
Function      double latitude,
Parameters    float radius,
Return value  String customId)
              Creates a circular geofence.
              longitude - Longitude of the geofence center;
              latitude - Latitude of the geofence center;
              radius - Radius of the geofence (minimum 100 meters);
              customId - Custom geofence ID, must be unique.
              0: Operation successful;

                                                                             20
              Must be used after open is successful.

3.5.9 Registers a listener for geofence creation results

Prototype     int registerGeoFenceCreateListener(IGeoFenceCreateListener listener)
Function      Registers a listener for geofence creation results.
Parameters    listener - Callback interface for geofence creation.
              0: Operation successful;
Return value  Others: Operation failed. Refer to LocationError for specific error codes.
              Must be used after open is successful.
Notes

3.5.10 Set the action for receiving geofence status broadcasts

Prototype     int setGeoFenceResultAction(String action, String pkgName)
Function      Set the action for receiving geofence status broadcasts.
Parameters    action - Broadcast action;
              pkgName - Package name for receiving the broadcast.
Return value  0: Operation successful;
Notes         Others: Operation failed. Refer to LocationError for specific error codes.
              Multiple settings will use the last one. Must be used after open is successful.

3.5.11 Removes all geofences

Prototype     int removeAllGeoFence()
Function      Removes all geofences.
Parameters
              0: Operation successful;
Return value  Others: Operation failed. Refer to LocationError for specific error codes.
              Must be used after open is successful.
Notes

3.5.12 Add an APK to a block list

Prototype     int addToBlockOpenAppList(String pkgName)
Function      Add an APK to a block list
Parameters    pkgName - Package name of the APK.
              0: Operation successful;
Return value  Others: Operation failed. Refer to LocationError for specific error codes.

Notes

3.5.13 Remove an APK from the blocked list

Prototype     int removeFromBlockOpenAppList(String pkgName)
Function      Remove an APK from the blocked list
Parameters    pkgName - Package name of the APK.
Return value  0: Operation successful;

                                                                             21

Notes

3.5.14 Check if an APK is in block

Prototype     boolean isInBlockOpenAppList(String pkgName)
Function      Check if an APK is in block
Parameters    pkgName - Package name of the APK.
              true: APK is disabled;
Return value  false: APK is not disabled.

Notes

3.5.15 Retrieves the list of blocked APKs

Prototype     List<String> getBlockOpenAppList()
Function      Retrieves the list of blocked APKs.
Parameters
Return value  Returns the list of disabled APK package names.
Notes

3.5.16 Disables the geofence feature

Prototype     void onDestroy()
Function      Destroys the location and geofence resources.
Parameters
Return value  Call this method when the location module is no longer needed.
Notes

3.5.17 Enable the location module and initialize with the specified method

Prototype     int open(LocationConstant.LocationType locationType)
Function      Enable the location module and initialize with the specified method
Parameters    Parameters:
Return Value  locationType - The desired location method (from LocationConstant.LocationType)
              Return:
Notes         0 - Operation succeeded
              Others - Operation failed (see LocationError for detailed error codes)
              Initializes the location module and allocates necessary resources according to the specified
              method.

3.5.18 Enable the location module and initialize with the specified key and method

Prototype     int open(String key,
              LocationConstant.LocationType locationType)
Function      Enable the location module and initialize with the specified key and method
Parameters    Parameters:

                                                                             22
Notes         By default, the system-signed key is used.
              If the system key fails (error code ERROR_CODE_FAILURE_AUTH), contact support for a
              special API key.
              After obtaining the key, call onDestroy() first, then re-initialize using this API with the new key.
              locationType - The desired location method (from LocationConstant.LocationType)
              Return:
              0 - Operation succeeded
              Others - Operation failed (see LocationError for detailed error codes)
              This method starts the location module and allocates necessary resources for the specified location
              method.

-- Location changed listener - ILocationChangedListener--

void onLocationChanged(MapLocation mapLocation,             Location changed callback
int errorCode,
String errorDetail)

3.5.19 Location changed callback

Prototype     void onLocationChanged(MapLocation mapLocation,
Function      int errorCode,
Parameters    String errorDetail)
Return value  Location changed callback
Notes         mapLocation - Location result information;
              errorCode - Error code;
              errorDetail - Detailed error information.

              This method is called when the location is completed.

-- GeoFence create listener - GeoFenceCreateListener --

void onGeoFenceCreateFinished(List<GeoFence> geoFenceList,  Callback for geofence creation completion
int errorCode,
String customId)

3.5.20 Callback for geofence creation completion

Prototype     void onGeoFenceCreateFinished(List<GeoFence> geoFenceList,
Function      int errorCode,
Parameters    String customId)
              Callback for geofence creation completion.
              geoFenceList - List of created geofences (only available if creation is successful, otherwise
              empty);

                                                                             23
              customId - Custom business ID associated with this operation.

Return value
Notes

