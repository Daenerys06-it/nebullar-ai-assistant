---
title: "kozen-terminal-location"
source: "KOZEN Terminal manager SDK Development Documentation_260422.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - location
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines Kozen Terminal Manager Location module APIs for GPS/cell tower positioning, geofencing, APK blocklist management, and location listener callbacks via ILocationManager."
---

## Overview

Location module providing GPS and cell tower positioning with geofencing support, APK blocklist management, and location change callbacks via ILocationManager obtained via TerminalManager.INSTANCE.getLocationManager() or TerminalManager.locationManager().

### Privacy Statement

Our location interface is designed solely to provide location-related services to applications.

- It does not actively collect device information such as SN, IMEI, or hardware identifiers.
- It does not transmit any device information or location data to external servers without explicit application request and authorization.
- All data access is limited to the scope necessary for location service functionality.
- This ensures that the interface complies with user privacy protection and security requirements.

## Function List

| Function Name | Description |
|---------------|-------------|
| List<String> getBlockOpenAppList() | Get the list of blocked APKs |
| boolean isInBlockOpenAppList(String pkgName) | Check if an APK is in block |
| void onDestroy() | Destroy location and geofencing resources |
| int open() | Start the location module and initialize related resources. |
| int open(String key) | Start the location module and initialize related resources by key. |
| int open(LocationConstant.LocationType locationType) | Enable the positioning module, specify the positioning method, and initialize the related resources. |
| int open(String key,  LocationConstant.LocationType locationType) | Enable the positioning module, specify the positioning key and method, and initialize the related resources. |
| int registerGeoFenceCreateListener(IGeoFenceCreateListener  listener) | Register a listener for geofence creation results |
| int registerLocationListener(ILocationChangedListener listener) | Register a location callback listener |
| int removeAllGeoFence() | Remove all geofences |
| int removeFromBlockOpenAppList(String pkgName) | Remove an APK from the blocked list |
| int setGeoFenceResultAction(String action,  String pkgName) | Set the action to receive geofence status broadcasts. |
| int setLocationOption(LocationClientOption locationClientOption) | Set location parameters |
| int startOnceLocation() | Start a single location request |
| int stopLocation() | Stop location services |
| int unRegisterLocationListener() | Remove the location listener |
| int addGeoFence(double longitude,  double latitude,  float radius,  String customId) | Create a circular geofence |

## Details

### open

| Prototype    | Prototype int open() |
| ------------ | --- |
| Function     | Function Enables the location module and initializes related resources. |
| Parameters   | Parameters  |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes  |

### open (with key)

| Prototype    | Prototype int open(String key) |
| ------------ | --- |
| Function     | Function Enables the location module and initializes related resources. |
| Parameters   | Parameters key - The API key for location.  By default, the system-signed key is used.  |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes If the system-signed key fails (location fails with error code ERROR_CODE_FAILURE_AUTH), Please contact Kozen FAE to generate a special API key. Then call onDestroy first, and use this API to reinitialize the location module by passing the API key. |

### setLocationOption

| Prototype    | Prototype int setLocationOption(LocationClientOption locationClientOption) |
| ------------ | --- |
| Function     | Function Set location parameters. Must be used after open is successful. |
| Parameters   | Parameters locationClientOption - Location parameters. |
| Return Value | Return value 0: Operation successful; Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes Default configuration parameters:  1. High-accuracy mode;  2. Location request interval is 2000ms;  3. Network location timeout is 30s;  4. No reverse geocoding address information;  5. Reverse geocoding language is selected based on the region;  6. Signal selection is network plus GPS |

### startOnceLocation

| Prototype    | Prototype int startOnceLocation() |
| ------------ | --- |
| Function     | Function Start a single location request. Must be used after open is successful. |
| Parameters   | Parameters  |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes The location request will automatically stop after completion. You can also call stopLocation to terminate the location request during the process |

### registerLocationListener

| Prototype    | Prototype int registerLocationListener(ILocationChangedListener listener) |
| ------------ | --- |
| Function     | Function Registers a location callback listener |
| Parameters   | Parameters listener - Callback interface for location updates. |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes Must be used after open is successful. Only one listener can be registered globally; new registrations will overwrite previous ones. Call unRegisterLocationListener to remove the listener when it is no longer needed |

### unRegisterLocationListener

| Prototype    | Prototype int unRegisterLocationListener() |
| ------------ | --- |
| Function     | Function Removes the location listener.  |
| Parameters   | Parameters  |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes Must be used after open is successful. |

### stopLocation

| Prototype    | Prototype int stopLocation() |
| ------------ | --- |
| Function     | Function Stop the location service.  |
| Parameters   | Parameters  |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes Must be used after open is successful. |

### addGeoFence

| Prototype    | Prototype int addGeoFence(double longitude,  double latitude,  float radius,  String customId) |
| ------------ | --- |
| Function     | Function Creates a circular geofence.  |
| Parameters   | Parameters longitude - Longitude of the geofence center;  latitude - Latitude of the geofence center;  radius - Radius of the geofence (minimum 100 meters);  customId - Custom geofence ID, must be unique. |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes Must be used after open is successful. |

### registerGeoFenceCreateListener

| Prototype    | Prototype int registerGeoFenceCreateListener(IGeoFenceCreateListener listener) |
| ------------ | --- |
| Function     | Function Registers a listener for geofence creation results.  |
| Parameters   | Parameters listener - Callback interface for geofence creation. |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes Must be used after open is successful. |

### setGeoFenceResultAction

| Prototype    | Prototype int setGeoFenceResultAction(String action, String pkgName) |
| ------------ | --- |
| Function     | Function Set the action for receiving geofence status broadcasts.  |
| Parameters   | Parameters action - Broadcast action;  pkgName - Package name for receiving the broadcast. |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes Multiple settings will use the last one. Must be used after open is successful. |

### removeAllGeoFence

| Prototype    | Prototype int removeAllGeoFence() |
| ------------ | --- |
| Function     | Function Removes all geofences.  |
| Parameters   | Parameters  |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes Must be used after open is successful. |

### addToBlockOpenAppList

| Prototype    | Prototype int addToBlockOpenAppList(String pkgName) |
| ------------ | --- |
| Function     | Function Add an APK to a block list |
| Parameters   | Parameters pkgName - Package name of the APK. |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes  |

### removeFromBlockOpenAppList

| Prototype    | Prototype int removeFromBlockOpenAppList(String pkgName) |
| ------------ | --- |
| Function     | Function Remove an APK from the blocked list |
| Parameters   | Parameters pkgName - Package name of the APK. |
| Return Value | Return value 0: Operation successful;  Others: Operation failed. Refer to LocationError for specific error codes. |
| Notes        | Notes  |

### isInBlockOpenAppList

| Prototype    | Prototype boolean isInBlockOpenAppList(String pkgName) |
| ------------ | --- |
| Function     | Function Check if an APK is in block |
| Parameters   | Parameters pkgName - Package name of the APK. |
| Return Value | Return value true: APK is disabled;  false: APK is not disabled. |
| Notes        | Notes  |

### getBlockOpenAppList

| Prototype    | Prototype List<String> getBlockOpenAppList() |
| ------------ | --- |
| Function     | Function Retrieves the list of blocked APKs. |
| Parameters   | Parameters  |
| Return Value | Return value Returns the list of disabled APK package names. |
| Notes        | Notes  |

### onDestroy

| Prototype    | Prototype void onDestroy() |
| ------------ | --- |
| Function     | Function Destroys the location and geofence resources.  |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes Call this method when the location module is no longer needed. |

### open (with LocationType)

| Prototype    | Prototype int open(LocationConstant.LocationType locationType) |
| ------------ | --- |
| Function     | Function Enable the location module and initialize with the specified method |
| Parameters   | Parameters Parameters: locationType - The desired location method (from LocationConstant.LocationType) |
| Return Value | Return Value Return: 0 - Operation succeeded Others - Operation failed (see LocationError for detailed error codes) |
| Notes        | Notes Initializes the location module and allocates necessary resources according to the specified method. |

### open (with key and LocationType)

| Prototype    | Prototype int open(String key,  LocationConstant.LocationType locationType) |
| ------------ | --- |
| Function     | Function Enable the location module and initialize with the specified key and method |
| Parameters   | Parameters Parameters: key - API key for location services.  By default, the system-signed key is used.  If the system key fails (error code ERROR_CODE_FAILURE_AUTH), contact support for a special API key.  After obtaining the key, call onDestroy() first, then re-initialize using this API with the new key. locationType - The desired location method (from LocationConstant.LocationType) |
| Return Value | Return Value Return: 0 - Operation succeeded Others - Operation failed (see LocationError for detailed error codes) |
| Notes        | Notes This method starts the location module and allocates necessary resources for the specified location method. |

### Location Changed Callback

`void onLocationChanged(MapLocation mapLocation,  int errorCode,  String errorDetail)` — Location changed callback

| Prototype    | Prototype void onLocationChanged(MapLocation mapLocation,  int errorCode,  String errorDetail) |
| ------------ | --- |
| Function     | Function Location changed callback  |
| Parameters   | Parameters mapLocation - Location result information;  errorCode - Error code;  errorDetail - Detailed error information. |
| Return Value | Return value  |
| Notes        | Notes This method is called when the location is completed. |


### GeoFence Create Callback

`void onGeoFenceCreateFinished(List<GeoFence> geoFenceList,  int errorCode,  String customId)` — Callback for geofence creation completion

| Prototype    | Prototype void onGeoFenceCreateFinished(List<GeoFence> geoFenceList,  int errorCode,  String customId) |
| ------------ | --- |
| Function     | Function Callback for geofence creation completion. |
| Parameters   | Parameters geoFenceList - List of created geofences (only available if creation is successful, otherwise empty);  errorCode - Error code;  customId - Custom business ID associated with this operation. |
| Return Value | Return value  |
| Notes        | Notes  |


## Notes

- Location parameters must be set via setLocationOption before calling startOnceLocation.
- Geofence radius must be at least 100 meters.
- Geofence customId must be unique.

## Related Links

- [[kozen-terminal-overview]]
- [[kozen-terminal-entities]]
- [[kozen-terminal-errors]]
