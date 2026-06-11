---
title: "kozen-component-secondary-screen"
source: "KOZEN Component SDK Development Documentation _260129.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - secondary_screen
summary: "Defines Kozen Component SDK SecondaryScreen module APIs for secondary display control including image display, video playback, screen power/brightness control, boot logo, resolution, custom view, wallpaper, and IResultCallback notifications."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-component-overview"
  - "kozen-component-errors"
  - "kozen-component-entities"
---

## Overview

Secondary screen operation module providing display control functionality via ISecondaryScreen obtained via ComponentEngine.INSTANCE.getSecondaryScreenManager() or ComponentEngine.secondaryScreenManager.

### Secondary Display Interface Declaration

The secondary display is designed solely for the presentation and interaction of content. To ensure user data security and comply with information security standards and regulatory requirements, it is strictly prohibited to use this module for sensitive data display.

## Function List

| Function Name | Description |
|----|----|
| int showPic(String picPath) | Display a single image |
| int showPic(ArrayList\<String\> picPathList, int intervalSeconds) | Image slideshow |
| int showVideo(String videoPath) | Display a video |
| int power(boolean on) | Power on/off the screen |
| int setBrightness(int value) | Set the screen brightness |
| int setBootLogo(String filePath) | Set the boot logo image |
| int[] getScreenResolution() | Get the screen resolution |
| void show(View view, IResultCallback callback) | Display a custom view |
| void show(View view, ArrayList\<PicData\> picDataList, IResultCallback callback) | Display custom view with slideshow |
| int showWallpaper() | Display the default wallpaper |
| int getPowerOnStatus() | Get power-on status |
| int getBrightness() | Get current brightness |

## Details

### showPic (single)

| Prototype    | int showPic(String picPath) |
| ------------ | --- |
| Function     | Display a single image |
| Parameters   | picPath - path to the image file |
| Return Value | int result code |
| Notes        | — |

### showPic (slideshow)

| Prototype    | int showPic(ArrayList\<String\> picPathList, int intervalSeconds) |
| ------------ | --- |
| Function     | Image slideshow |
| Parameters   | picPathList - list of image paths; intervalSeconds - display interval |
| Return Value | int result code |
| Notes        | — |

### showVideo

| Prototype    | int showVideo(String videoPath) |
| ------------ | --- |
| Function     | Display a video |
| Parameters   | videoPath - path to the video file |
| Return Value | int result code |
| Notes        | — |

### power

| Prototype    | int power(boolean on) |
| ------------ | --- |
| Function     | Power on/off the screen |
| Parameters   | on - true to turn on, false to turn off |
| Return Value | int result code |
| Notes        | — |

### setBrightness

| Prototype    | int setBrightness(int value) |
| ------------ | --- |
| Function     | Set the screen brightness |
| Parameters   | value - brightness level |
| Return Value | int result code |
| Notes        | — |

### setBootLogo

| Prototype    | int setBootLogo(String filePath) |
| ------------ | --- |
| Function     | Set the boot logo image |
| Parameters   | filePath - path to the logo image |
| Return Value | int result code |
| Notes        | — |

### getScreenResolution

| Prototype    | int[] getScreenResolution() |
| ------------ | --- |
| Function     | Get the resolution of the secondary screen |
| Parameters   | — |
| Return Value | int array [width, height] |
| Notes        | — |

### show (custom view)

| Prototype    | void show(android.view.View view, IResultCallback resultCallback) |
| ------------ | --- |
| Function     | Display a custom view |
| Parameters   | view - android View to display; resultCallback - callback for result |
| Return Value | — |
| Notes        | — |

### show (custom view with slideshow)

| Prototype    | void show(android.view.View view, ArrayList\<PicData\> picDataList, IResultCallback resultCallback) |
| ------------ | --- |
| Function     | Display a custom view with optional image slideshow |
| Parameters   | view - android View; picDataList - list of PicData objects; resultCallback - callback for result |
| Return Value | — |
| Notes        | — |

### showWallpaper

| Prototype    | int showWallpaper() |
| ------------ | --- |
| Function     | Display the default wallpaper |
| Parameters   | — |
| Return Value | int result code |
| Notes        | — |

### getPowerOnStatus

| Prototype    | int getPowerOnStatus() |
| ------------ | --- |
| Function     | Get power-on status of the secondary screen |
| Parameters   | — |
| Return Value | int result code |
| Notes        | — |

### getBrightness

| Prototype    | int getBrightness() |
| ------------ | --- |
| Function     | Get current screen brightness |
| Parameters   | — |
| Return Value | int result code |
| Notes        | — |

### IResultCallback

| Prototype    | void onSuccess() |
| ------------ | --- |
| Function     | View display success |
| Parameters   | — |
| Return Value | — |
| Notes        | — |

| Prototype    | void onFailure(int errorCode, String msg) |
| ------------ | --- |
| Function     | View display failure |
| Parameters   | errorCode - error code; msg - error message |
| Return Value | — |
| Notes        | — |

## Notes

No additional notes.

## Related Links

- [[kozen-component-overview]]
- [[kozen-component-errors]]
- [[kozen-component-entities]]
