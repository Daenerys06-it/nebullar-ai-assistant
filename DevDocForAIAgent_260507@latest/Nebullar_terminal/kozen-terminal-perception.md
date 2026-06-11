---
title: "kozen-terminal-perception"
source: "KOZEN Terminal manager SDK Development Documentation_260422.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - perception
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines Kozen Terminal Manager Perception info module APIs for retrieving device sensor data including battery cycle count, design capacity, current max capacity, health percentage, health status, small battery voltage, and print distance history via IPerceptionInfoManager."
---

## Overview

Perception info module providing device health and sensor data retrieval including battery analytics and printer tracking via IPerceptionInfoManager obtained via TerminalManager.INSTANCE.getPerceptionInfoManager().

## Function List

| Function Name | Description |
|---------------|-------------|
| ArrayList<String> getBatteryCurrentMaxCapacity() | Get the current max capacity list of the main battery |
| ArrayList<String> getBatteryCycleCount() | Get the cycle count list of the main battery |
| ArrayList<String> getBatteryDesignCapacity() | Get the factory design capacity list of the main battery |
| ArrayList<String> getBatteryHealthPercent() | Get the battery health percentage list |
| ArrayList<String> getBatteryHealthStatus() | Get the battery health status list |
| ArrayList<String> getPrintDistance() | Get the print distance list |
| ArrayList<String> getSmallBatteryVoltage() | Get the small battery voltage list |

## Details

### collectPerceptionData

| Prototype    | Prototype android.os.ParcelFileDescriptor collectPerceptionData() |
| ------------ | --- |
| Function     | Function Get perception data as a file stream |
| Parameters   | Parameters  |
| Return Value | Return Value Return: File descriptor for perception data;  null if no data (file size < 2MB or not found) |
| Notes        | Notes Returns a file descriptor containing buried point (analytics) data. |

### getBatteryCycleCount

| Prototype    | Prototype ArrayList<String> getBatteryCycleCount() |
| ------------ | --- |
| Function     | Function Get large battery cycle count list |
| Parameters   | Parameters  |
| Return Value | Return Value Return: List of cycle counts in the format: "yyyyMMdd,count" (e.g., "20250630,100") |
| Notes        | Notes Each item represents the total charge cycle count on a specific date. |

### getBatteryDesignCapacity

| Prototype    | Prototype ArrayList<String> getBatteryDesignCapacity() |
| ------------ | --- |
| Function     | Function Get large battery design capacity list |
| Parameters   | Parameters  |
| Return Value | Return Value Return: List in the format: "yyyyMMdd,capacity" (e.g., "20250630,2800") |
| Notes        | Notes Represents the designed capacity of the battery on a given date. |

### getBatteryCurrentMaxCapacity

| Prototype    | Prototype ArrayList<String> getBatteryCurrentMaxCapacity() |
| ------------ | --- |
| Function     | Function Get current max capacity of large battery |
| Parameters   | Parameters  |
| Return Value | Return Value Return: List in the format: "yyyyMMdd,capacity" (e.g., "20250630,2750") |
| Notes        | Notes Indicates the actual current maximum charge capacity over time. |

### getBatteryHealthPercent

| Prototype    | Prototype ArrayList<String> getBatteryHealthPercent() |
| ------------ | --- |
| Function     | Function Get battery health percentage list |
| Parameters   | Parameters  |
| Return Value | Return Value Return: List in the format: "yyyyMMdd,healthPercent" (e.g., "20250630,100") |
| Notes        | Notes Battery health percentage over time. |

### getBatteryHealthStatus

| Prototype    | Prototype ArrayList<String> getBatteryHealthStatus() |
| ------------ | --- |
| Function     | Function Get battery health status list |
| Parameters   | Parameters  |
| Return Value | Return Value Return: List in the format: "yyyyMMdd,status" (e.g., "20250630,0") |
| Notes        | Notes Health status values may refer to different health categories |

### getSmallBatteryVoltage

| Prototype    | Prototype ArrayList<String> getSmallBatteryVoltage() |
| ------------ | --- |
| Function     | Function Get small battery voltage list |
| Parameters   | Parameters  |
| Return Value | Return Value Return: List in the format: "yyyyMMdd,voltage" (e.g., "20250630,24") |
| Notes        | Notes Voltage data for the small/internal battery. |

### getPrintDistance

| Prototype    | Prototype ArrayList<String> getPrintDistance() |
| ------------ | --- |
| Function     | Function Get print distance history list |
| Parameters   | Parameters  |
| Return Value | Return Value Return:List in the format: "yyyyMMdd,distance" (e.g., "20250630,45000") |
| Notes        | Notes Represents cumulative printing distance (in meters) by date. |


## Notes

- All list-type APIs return data in `yyyyMMdd,value` format (e.g., `20250630,100`).
- collectPerceptionData returns a ParcelFileDescriptor for buried point (analytics) data; returns null if file size < 2MB or file not found.

## Related Links

- [[kozen-terminal-overview]]
- [[kozen-terminal-device]]
