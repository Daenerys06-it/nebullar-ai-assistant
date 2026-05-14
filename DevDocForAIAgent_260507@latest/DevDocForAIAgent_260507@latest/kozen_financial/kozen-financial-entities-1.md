---
title: "kozen-financial-entities-1"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - entity_classes
created: "2026-04-30"
updated: "2026-04-30"
summary: "Defines EMV entity classes used by Kozen Financial SDK EMV APIs, including CAPK, AID, exception file, and revocation IPK data models for POS engineers."
related:
  - "kozen-financial-emv-1"
  - "kozen-financial-emv-2"
  - "kozen-financial-entities-2"
  - "kozen-financial-entities-3"
---

## Overview

Defines EMV entity classes used by Kozen Financial SDK EMV APIs, including CAPK, AID, exception file, and revocation IPK data models for POS engineers.

## Entity Class Definition

### EmvCapk

| Constant Name | Type | Value | Description |
| --- | --- | --- | --- |
| ALGO_IND_RSA | int | 1 | – |
| ALGO_IND_SM | int | 4 | – |
| AlgorithmInd | byte | – | Algorithm Flag. |
| CapkIndex | byte | – | Capk Index. |
| Checksum | byte[] | – | Checksum. |
| CREATOR | android.os.Parcelable.Creator<EmvCapk> | – | – |
| Exponent | byte[] | – | Exponent. |
| HASH_IND_NOT | int | 0 | – |
| HASH_IND_SHA1 | int | 1 | – |
| HashInd | byte | – | HASH Algorithm Flag. |
| Module | byte[] | – | Module. |
| RID | byte[] | – | Application Registration Service Provider ID. |

### EmvAid

| Constant Name | Type | Description |
| --- | --- | --- |
| AcquirerIdentifier | byte[] | Acquirer Identifier. Tag: 9F01.Value Type : byte[]. Required Field. |
| AdditionalTerminalCapabilities | byte[] | Additional Terminal Capabilities. Tag: 9F40.Value Type : byte[].Required Field. |
| AID | byte[] | Application Id.  Tag: 9F06. Value Type: byte[]. Required Field. |
| CombinationData | byte[] | Combination Data. public byte[] CombinationData Combination Data. Set Parameters for AID Will Overwrite the Default Parameters. Not Related to CombinationType. eg. aid.CombinationData = getKernel(getLimit(999999999999L,  999999999999L,  999999999999L,  999999999999L),  HexUtil.parseHex("9F660436004000"), null, null, null, null); The getKernel Function is Defined to Set Parameters for Different Card Organizations Can Set EMV Standard Tag. "DF10", "DF11", "DF12", "DF13", "DF14", "DF17" in this Function are Custom Tags. Just Pass in the Tag and Value that Need to be Set as Parameters.  eg. 9F660436004000. private static byte[] getKernel(byte[] kernel, byte[] visa, byte[] unionpay, byte[] mastercard, byte[] discover, byte[] mir) {     BerTlvBuilder tlvBuilder = new BerTlvBuilder();     if (kernel != null) {         tlvBuilder.addBytes(new BerTag("DF10"), kernel);     }     if (visa != null) {         tlvBuilder.addBytes(new BerTag("DF11"), visa);     }     if (unionpay != null) {         tlvBuilder.addBytes(new BerTag("DF12"), unionpay);     }     if (mastercard != null) {         tlvBuilder.addBytes(new BerTag("DF13"), mastercard);     }     if (discover != null) {         tlvBuilder.addBytes(new BerTag("DF14"), discover);     }     if (mir != null) {         tlvBuilder.addBytes(new BerTag("DF17"), mir);     }     return tlvBuilder.buildArray(); } Set CVM Parameters. "DF01", "DF02", "DF03", "DF04" in this Function are Custom Tags. Just Pass in the Tag and Value that Need to be Set as Parameters. eg. 999999999999L,  999999999999L,  999999999999L,  999999999999L. private static byte[] getLimit(long contactlessLimit, long contactlessCVMLimit, long contactlessFloorLimit, long contactlessDynamicLimit) {     BerTlvBuilder tlvBuilder = new BerTlvBuilder(); tlvBuilder.addBytes(new BerTag("DF01"),  getAmount(contactlessLimit)); tlvBuilder.addBytes(new BerTag("DF02"),  getAmount(contactlessCVMLimit)); tlvBuilder.addBytes(new BerTag("DF03"),  getAmount(contactlessFloorLimit)); tlvBuilder.addBytes(new BerTag("DF04"),  getAmount(contactlessDynamicLimit));     return tlvBuilder.buildArray(); } private static byte[] getAmount(long value) {     StringBuilder builder = new StringBuilder(12);     builder.append(value);     while (builder.length() < 12) {         builder.insert(0, '0');     }     return HexUtil.parseHex(builder.toString()); } |
| CombinationType | int | Combination Type. Not Usage. Value Type : int. |
| ContactlessCVMLimit | int | Contactless CVM Required Limit. Value Type : int. Optional Field. |
| ContactlessCVMLimitL | long | Contactless CVM Required Limit. Value Type : long. Optional Field. |
| ContactlessFloorLimit | int | Contactless Floor Limit. Value Type : int. Optional Field. |
| ContactlessFloorLimitL | long | Contactless Floor Limit. Value Type : long. Optional Field. |
| ContactlessTransLimit | int | Contactless Transaction Limit. Value Type : int. Optional Field. |
| ContactlessTransLimitL | long | Contactless Transaction Limit. Value Type : long. Optional Field. |
| CREATOR | static final  android.os.Parcelable.Creator | – |
| dDOL | byte[] | Default dDOL. Tag: 97. Value Type : byte[]. Required Field. |
| DynamicTransLimit | int | Dynamic Trans Limit. Value Type : int. Optional Field. |
| DynamicTransLimitL | long | Dynamic Trans Limit. Value Type : long. Optional Field. |
| FloorLimit | int | Floor Limit. Value Type : int. Optional Field. |
| MaxTargetPercentage | int | The Maximum Target Percentage of Offset Random Selection. Value Type : int. Optional Field. |
| MerchantCategoryCode | byte[] | Merchant Category Code. Tag: 9F15. Value Type : byte[].Required Field. |
| SelectIndicator | boolean | Application Select Indicator:  True: FULL_MATCH, False: PART_MATCH. Value Type : boolean. Optional Field. |
| TACDefault | byte[] | TAC-Default. Tag: DF8120.Value Type: byte[].Required Field. |
| TACDenial | byte[] | TAC-Denial. Tag : DF8121.Value Type : byte[].Required Field. |
| TACOnline | byte[] | TAC-Online. Tag : DF8122.Value Type : byte[].Required Field. |
| TargetPercentage | int | Target Percentage of Random Selection. Value Type : int. Optional Field. |
| tDOL | byte[] | Default tDOL. Tag : 9F49.Value Type : byte[].Required Field. |
| TerminalCapabilities | byte[] | Terminal Capability. Value Type : byte[]. Required Field. |
| TerminalCountryCode | byte[] | Terminal Country Code. Tag : 9F1A.Value Type : byte[].Required Field. |
| TerminalRiskManagementData | byte[] | Terminal Risk Management Data. Tag : 9F1D.Value Type : byte[].Required Field. |
| TerminalType | byte[] | Terminal Type. Value Type : byte[]. Required Field. |
| Threshold | int | Threshold of Bias Random Selection. Value Type : int. Optional Field. |
| TransCurrencyCode | byte[] | Trans Currency Code. Tag : 5F2A.Value Type : byte[]. Required Field. |
| TransCurrencyExp | byte[] | Trans Currency Exp. Tag : 5F36.Value Type : byte[]. Required Field. |
| TypeIndicator | boolean | Application Type Indicator:  True: Contactless, False: Both for Contact and Contactless. Value Type : boolean. Optional Field. |
| Version | byte[] | Application Version. Tag : 9F09.Value Type : byte[]. Required Field. |

### EmvExceptionFile

| Constant Name | Type | Description |
| --- | --- | --- |
| CapkIndex | byte | Capk Index Value Type : byte[]. Required Field. |
| CREATOR | static final android.os.Parcelable.Creator<EmvRevocationIPK> | – |
| RID | byte[] | RID Tag : 9F06.Value Type : byte[]. Required Field. |
| SerialNo | byte[] | SerialNumber Value Type : byte[]. Required Field. |

### EmvRevocationIPK

| Constant Name | Type | Description |
| --- | --- | --- |
| CREATOR | static final android.os.Parcelable.Creator<EmvExceptionFile> | – |
| PAN | byte[] | Primary Account Number. (PAN). Value Type : byte[]. Required Field. |
| SerialNo | byte[] | Serial Number. Value Type : byte[]. Required Field. |

## Related Links

- [[kozen-financial-emv-1]]
- [[kozen-financial-emv-2]]
- [[kozen-financial-entities-2]]
- [[kozen-financial-entities-3]]
