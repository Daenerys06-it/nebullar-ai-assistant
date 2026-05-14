---
title: "kozen-terminal-permission"
source: "KOZEN Terminal manager SDK Development Documentation_260422.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - permission
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines required Android system permissions for the Kozen Terminal Manager SDK across all modules: DeviceManager, ResourceManager, LocationManager, DeviceInfoManager, and CertificationManager."
---

## Overview

Required Android system Super Permissions for the Kozen Terminal Manager SDK. These permissions must be granted at runtime or via device admin controls.

## Permission List

| Permission Name | Related Module | Tooltips |
| --- | --- | --- |
| android.permission.SUPER_PERMISSIONS_DEVICE | DeviceManager | Read and modify system time, timezone, and other system settings |
| android.permission.SUPER_PERMISSIONS_RESOURCE | ResourceManager | Install or update resource packages (e.g., fonts, images, applications) |
| android.permission.SUPER_PERMISSIONS_LOCATION | LocationManager | Get device location (GPS / Cell tower) |
| android.permission.SUPER_PERMISSIONS_DEVICE_INFO | DeviceInfoManager | Collect device info (SN, IMEI, hardware) |
| android.permission.SUPER_PERMISSIONS_NETWORK | NetworkManager | Manage network access and firewall rules |

## Related Links

- [[kozen-terminal-overview]]
- [[kozen-terminal-certification]]
