---
title: "kozen-terminal-certification"
source: "KOZEN Terminal manager SDK Development Documentation_260422.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - certification
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines Kozen Terminal Manager Certification module APIs for managing application signature certificates, including update, delete, and query operations via ICertificationManager."
---

## Overview

Certification management API providing certificate update, deletion, and query functionality via ICertificationManager obtained via TerminalManager.INSTANCE.getCertificationManager() (Java) or TerminalManager.certificationManager() (Kotlin).

## Function List

| Function Name | Description |
|---------------|-------------|
| List<String> getAppSignatureInfo() | Get the app signature certificate information |
| int updateAppSignature(String certData) | Update the app signature certificate |

## Details

### updateAppSignature

| Prototype    | Prototype int updateAppSignature(String certData) |
| ------------ | --- |
| Function     | Function Updates the application's signature certificate. |
| Parameters   | Parameters Parameters: certData- Certificate Data |
| Return Value | Return value Return: - 0: Success - Others: Failure (specific error codes refer to CertificationError). |
| Notes        | Notes For failure cases, refer to CertificationError for detailed error codes. |

### deleteAppSignature

| Prototype    | Prototype int deleteAppSignature(String certData) |
| ------------ | --- |
| Function     | Function Deletes the application's signature certificate. |
| Parameters   | Parameters Parameters: certData- Certificate Data to Be Deleted |
| Return Value | Return value Return: - 0: Success - Others: Failure (specific error codes refer to CertificationError). |
| Notes        | Notes For failure cases, refer to CertificationError for detailed error codes. |

### getAppSignatureInfo

| Prototype    | Prototype List<String> getAppSignatureInfo() |
| ------------ | --- |
| Function     | Function Get the application's signature certificate information. |
| Parameters   | Parameters  |
| Return Value | Return value Return: Certificate Details List |
| Notes        | Notes  |


## Notes

- All failure return codes refer to CertificationError for detailed error codes.

## Related Links

- [[kozen-terminal-overview]]
- [[kozen-terminal-errors]]
