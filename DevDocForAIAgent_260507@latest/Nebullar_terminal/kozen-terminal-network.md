---
title: "kozen-terminal-network"
source: "KOZEN Terminal manager SDK Development Documentation_260422.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - network
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines Kozen Terminal Manager Network module APIs for APN configuration management including adding and enabling/disabling APN configurations via INetworkManager."
---

## Overview

Network module providing APN configuration management functionality via INetworkManager obtained via TerminalManager.INSTANCE.getNetworkManager() or TerminalManager.networkManager().

## Function List

| Function Name | Description |
|---|---|
| int addApn(ApnConfiguration config) | Add an APN |
| int enableApn(String name) | Enable an APN |

## Details

### addApn

| Prototype    | Prototype int addApn(ApnConfiguration config) |
| ------------ | --- |
| Function     | Function Adds an APN configuration. |
| Parameters   | Parameters config - The APN configuration to add. |
| Return Value | Return value Return:  0: Success Others: Failure (refer to NetworkError). |
| Notes        | Notes  |

### enableApn

| Prototype    | Prototype int enableApn(String name) |
| ------------ | --- |
| Function     | Function Enables an APN configuration. |
| Parameters   | Parameters name - The name of the APN. Pass null to disable the currently used APN. |
| Return Value | Return value Return:  0: Success Others: Failure (refer to NetworkError). |
| Notes        | Notes  |


### Notes

- See [[kozen-terminal-entities]] for ApnConfiguration entity class definition.

## Notes

No additional notes.

## Related Links

- [[kozen-terminal-overview]]
- [[kozen-terminal-entities]]
- [[kozen-terminal-device]]
