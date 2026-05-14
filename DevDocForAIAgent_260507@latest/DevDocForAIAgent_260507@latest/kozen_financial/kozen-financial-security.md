---
title: "kozen-financial-security"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - security
summary: "Defines Kozen Financial SDK Security module APIs for key management and cryptographic operations including write/read/generate RSA keys, DUKPT key management, 3DES/RSA/SM4 encryption/decryption, MAC calculation (standard, DUKPT, DUKPT_AES, DUKPT_TDES), KSN operations, random numbers, and key erasure."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-financial-overview"
  - "kozen-financial-init"
---

## Overview

Security module providing cryptographic and key management via ISecurityManager from FinancialEngine.INSTANCE.getSecurityManager() or FinancialEngine.securityManager().

## Function List

| Function Name | Description |
|--            |-----------|
| int writeKey(int srcKeyType, int srcKeyIndex, int keyType, int index,  byte[] keyIn,  byte[] kcv) | Write keys |
| int writeKeyDukpt(int index,  byte[] keyIn,  byte[] ksnIn,  byte[] kcv) | Write DUKPT keys |
| int generateRsaKey(int pubKeyIndex,  int priKeyIndex,  int size) | Generate RSA keys |
| int writeRsaKey(int keyIndex,  byte[] modulus,  byte[] exponent) | Write RSA keys |
| int readRsaKey(int keyIndex,  byte[] keyOut,  byte[] modulusOut,  byte[] exponentOut) | Read RSA keys |
| int getRandom(int length,  byte[] keyOut) | Get random numbers compliant with NIST SP800-90A |
| int getKCV(int keyIndex,  int keyType,  byte[] kcvOut) | Get KCV for the corresponding key type |
| int calcDukpt(int index,  int keyMode,  int algType,  int mode,  byte[] dataIn,  byte[] aesIv,   byte[] dataOut) | Encrypt or decrypt data by DUKPT |
| int calcRsa(int keyIndex, int mode, byte[] dataIn, byte[] dataOut) | RSA encryption or decryption |
| int calcDes(int keyIndex,  int mode,  byte[] dataIn,  byte[] dataOut) | 3DES data encryption and decryption |
| int calcMac(int index,  int keyType,  byte[] iv,  byte[] dataIn,  byte[] dataOut) | Calculate MAC |
| int calcMacDukpt(int index,  int keyType,  int mode,  byte[] dataIn,  byte[] dataOut) | Calculate MAC by DUKPT |
| int getKsnDukpt(int index,  byte[] ksnOut) | Get the KSN for the key at the specified index |
| int increaseKsnDukpt(int index) | Increase KSN |
| int calcMacDukptDes(int tikIndex,  int operationMode,  int ksnMode,  int macAlgorithm,  byte[] dataIn,  byte[] initVector,  byte[] dataOut,  byte[] usedKsn) | Calculate MAC using the DUKPT_TDES algorithm |
| int eraseAllKey() | Erase all keys |
| int writeKeyDukptDes(int tikIndex,  int tlkIndex,  byte[] keyIn,  byte[] ksnIn,  byte[] kcv) | Write DUKPT_DES key |
| int writeKeyMKSK(int srcKeyType,  int srcKeyIndex,  int keyType,  int encryptionAlgorithm,  int index,  byte[] keyIn,  byte[] kcv) | Write MK/SK key |
| int calcRsaDecrypt(int keyIndex,  int mode,  byte[] dataIn,  byte[] dataOut) | Perform RSA encryption or decryption (supports both public/private key decryption) |
| int calcRsaEncrypt(int keyIndex,  int mode,  byte[] dataIn,  byte[] dataOut) | Perform RSA encryption (supports public/private key encryption) |
| int writeKeyTR31(String tr31KeyBlock,  int srcKeyType,  int srcKeyIndex, int writeKeyType,  int writeKeyIndex,  int writeKeyAlgorithm) | Write TR31 key using extension method |
| int writeKeyMKSK(int srcKeyType,  int srcKeyIndex,  int keyType,  int encryptionAlgorithm,  int index,  byte[] keyIn,  int kcvMode,  byte[] kcv) | Write MK/SK key with support for encryption algorithm and KCV mode |
| int writeKeyDukptAes(int tikIndex,  int tlkIndex,  byte[] keyIn,  byte[] ksnIn,  int kcvMode,  byte[] kcv) | Write DUKPT_AES key (supports TLK and KCV mode) |
| int writeKeyDukptDes(int tikIndex,  int tlkIndex,  byte[] keyIn,  byte[] ksnIn,  int kcvMode,  byte[] kcv) | Write DUKPT_DES key (supports KCV mode) |
| int readRsaKey(int keyIndex,  android.os.Bundle bundle) | Read RSA key information |
| int calcDukptAes(int tikIndex,  int keyUsage,  int algType,  byte[] initVector,  int operationDirection,  int operationMode,  int ksnMode,  byte[] dataIn,  byte[] aesIv,  byte[] dataOut,  byte[] usedKsn) | Encrypt or decrypt data using DUKPT_AES (supports ksnMode and usedKsn) |
| int calcMacDukptAes(int tikIndex,  int keyUsage,  int algType,  int macAlgorithm,  int ksnMode,  byte[] dataIn,  byte[] dataOut,  byte[] usedKsn) | Compute MAC using DUKPT_AES key |
| int calcSM4(int keyIndex,  int mode,  byte[] dataIn,  byte[] dataOut) | Encrypt or decrypt data using SM4 algorithm |

## Details

### writeKey

| Prototype    | Prototype int writeKey(int srcKeyType, int srcKeyIndex, int keyType, int index,  byte[] keyIn,  byte[] kcv) |
| ------------ | --- |
| Function     | Function Write keys |
| Parameters   | Parameters Parameters: srcKeyType - Source key type Such as ConstantSecurity.PED_TLK, ConstantSecurity.PED_TMK srcKeyIndex - Source key index the key index used to decrypt the target key. TLK: Only 1 group is supported, and the index range is [1,1]. TMK: Supports 64 groups, the index range is [1, 64]. TPK: Supports 64 groups, the index range is [1, 64]. TAK: Supports 64 groups, the index range is [1, 64]. TDK: Supports 64 groups, the index range is [1, 64]. TEK: Supports 64 groups, the index range is [1, 64]. TTK: Supports 64 groups, the index range is [1, 64]. Note: TPK, TAK, TDK, TEK, TTK share the index space. Key indexes can not be duplicated. If duplication occurs, the later written key will overwrite the previously injected key. keyType - Key type, as follows: ConstantSecurity.PED_TLK ConstantSecurity.PED_TMK ConstantSecurity.PED_TPK ConstantSecurity.PED_TAK ConstantSecurity.PED_TDK ConstantSecurity.PED_TEK ConstantSecurity.PED_TTK index - Key index, as follows: TLK: Only 1 group is supported, and the index range is [1,1]. TMK: Supports 64 groups, the index range is [1, 64]. TPK: Supports 64 groups, the index range is [1, 64]. TAK: Supports 64 groups, the index range is [1, 64]. TDK: Supports 64 groups, the index range is [1, 64]. TEK: Supports 64 groups, the index range is [1, 64]. TTK: Supports 64 groups, the index range is [1, 64]. Note: TPK, TAK, TDK, TEK, TTK share the index space. Key indexes should not be duplicated. If duplication occurs, the later written key will overwrite the previously injected key. keyIn - Key information, supported key lengths: [8, 16, 24, 32] kcv - KCV value  |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### writeKeyDukpt

| Prototype    | Prototype int writeKeyDukpt(int index,  byte[] keyIn,  byte[] ksnIn,  byte[] kcv) |
| ------------ | --- |
| Function     | Function Write DUKPT keys |
| Parameters   | Parameters Parameters: index - Key index (supported range 1～10) keyIn - Key data ksnIn - Initialization KSN kcv - KCV value |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### generateRsaKey

| Prototype    | Prototype int generateRsaKey(int pubKeyIndex,  int priKeyIndex,  int size) |
| ------------ | --- |
| Function     | Function Generate RSA keys |
| Parameters   | Parameters Parameters: pubKeyIndex - Public key index priKeyIndex - Private key index size - Key size |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes Note: The key index range is 1～4, only support two sets of public and private keys. |

### writeRsaKey

| Prototype    | Prototype int writeRsaKey(int keyIndex,  byte[] modulus,  byte[] exponent) |
| ------------ | --- |
| Function     | Function Write RSA keys |
| Parameters   | Parameters Parameters: keyIndex - Key index modulus - Modulus exponent - Exponent |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes Note: If the length of the exponent is less than the length of the modulus, the key type written is a public key. If the length of the exponent is equal to the length of the modulus, the key type written is private key. |

### readRsaKey

| Prototype    | Prototype int readRsaKey(int keyIndex,  byte[] keyOut,  byte[] modulusOut,  byte[] exponentOut) |
| ------------ | --- |
| Function     | Function Read RSA keys |
| Parameters   | Parameters Parameters: keyIndex - Key index keyOut - Key information modulusOut - Key modulus exponentOut - Key exponent |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### getRandom

| Prototype    | Prototype int getRandom(int length,  byte[] keyOut) |
| ------------ | --- |
| Function     | Function Get random numbers compliant with NIST SP800-90A |
| Parameters   | Parameters Parameters: length - Length of the random number keyOut - Random number |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### getKCV

| Prototype    | Prototype int getKCV(int keyIndex,  int keyType,  byte[] kcvOut) |
| ------------ | --- |
| Function     | Function Get KCV for the corresponding key type |
| Parameters   | Parameters Parameters: keyIndex - Key index keyType - Key type, as follows: ConstantSecurity.PED_TLK ConstantSecurity.PED_TMK ConstantSecurity.PED_TPK ConstantSecurity.PED_TAK ConstantSecurity.PED_TDK ConstantSecurity.PED_TEK ConstantSecurity.PED_TIK ConstantSecurity.PED_TTK kcvOut - KCV value |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### calcDukpt

| Prototype    | Prototype int calcDukpt(int index,  int keyMode,  int algType,  int mode,  byte[] dataIn,  byte[] aesIv,   byte[] dataOut) |
| ------------ | --- |
| Function     | Function Encrypt or decrypt data by DUKPT |
| Parameters   | Parameters Parameters: index - Key index keyMode - Dukpt mode, can be as follows ConstantSecurity.PED_CALC_DUKPT_MODE_DEC: 0x01 ConstantSecurity.PED_CALC_DUKPT_MODE_ENC: 0x02 algType - Algorithm type, can be as follows ConstantSecurity.KEY_ALG_TYPE_2TDEA ConstantSecurity.KEY_ALG_TYPE_3TDEA ConstantSecurity.KEY_ALG_TYPE_AES_128 ConstantSecurity.KEY_ALG_TYPE_AES_192 ConstantSecurity.KEY_ALG_TYPE_AES_256 mode - Operation Mode, can be as follows ConstantSecurity.DUKPT_MAC_MODE_ECB: ECB Mode. ConstantSecurity.DUKPT_MAC_MODE_CBC: CBC Mode. dataIn - Input data aesIv - Initialization vector, pass null for ECB mode, or pass an 8-byte vector for other encryption modes dataOut - Encrypted data |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### calcRsa

| Prototype    | Prototype int calcRsa(int keyIndex, int mode, byte[] dataIn, byte[] dataOut) |
| ------------ | --- |
| Function     | Function RSA encryption or decryption |
| Parameters   | Parameters Parameters: keyIndex - Key index mode - RSA padding Mode, can be as follows ConstantSecurity.PED_CALC_RSA_MODE_NO_PADDING ConstantSecurity.PED_CALC_RSA_MODE_PKCS1_PADDING ConstantSecurity.PED_CALC_RSA_MODE_OAEP_PADDING dataIn - Input data dataOut - Encrypted or decrypted data |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### calcDes

| Prototype    | Prototype int calcDes(int keyIndex,  int mode,  byte[] dataIn,  byte[] dataOut) |
| ------------ | --- |
| Function     | Function 3DES data encryption and decryption |
| Parameters   | Parameters Parameters: keyIndex - Index of TDK. mode - Encryption and Decryption Mode, can be as follows ConstantSecurity.PED_CALC_DES_MODE_ECB_DEC ConstantSecurity.PED_CALC_DES_MODE_ECB_ENC ConstantSecurity.PED_CALC_DES_MODE_CBC_DEC ConstantSecurity.PED_CALC_DES_MODE_CBC_ENC dataIn - Input data dataOut - Encrypted or decrypted data |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### calcMac

| Prototype    | Prototype int calcMac(int index,  int keyType,  byte[] iv,  byte[] dataIn,  byte[] dataOut) |
| ------------ | --- |
| Function     | Function Calculate MAC |
| Parameters   | Parameters Parameters: index - TAK key index keyType - MAC algorithm type, can be as follows ConstantSecurity.MAC_MODE_CBC: CBC-MAC. ConstantSecurity.MAC_MODE_XOR_ECB_MAC: XOR-ECB-MAC. ConstantSecurity.MAC_MODE_ANSI_X9_19: ANSI-X9.19 MAC. ConstantSecurity.MAC_MODE_ANSI_X9_9: ANSI-X9.9 MAC. iv - Initialization vector dataIn - input data dataOut - Calculated data |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### calcMacDukpt

| Prototype    | Prototype int calcMacDukpt(int index,  int keyType,  int mode,  byte[] dataIn,  byte[] dataOut) |
| ------------ | --- |
| Function     | Function Calculate MAC by DUKPT |
| Parameters   | Parameters index - dukpt key index keyType - Key Type : This Code is Coded by Two Part: X | Y E.g 0x00 | 0x40. X (Key Usage) can be as follows 0x00 : ConstantSecurity.AUTHENTICATION_GENERATION. 0x01 : ConstantSecurity.AUTHENTICATION_VERIFICATION. 0x02 : ConstantSecurity.AUTHENTICATION_BOTH. Y (Derive Key Algorithm Type)  can be as follows 0x00 : ConstantSecurity.KEY_ALG_TYPE_2TDEA. 0x10: ConstantSecurity.KEY_ALG_TYPE_3TDEA. 0x20: ConstantSecurity.KEY_ALG_TYPE_AES_128. 0x30: ConstantSecurity.KEY_ALG_TYPE_AES_192. 0x40: ConstantSecurity.KEY_ALG_TYPE_AES_256. mode - MAC Operation Control Code. This Code is Coded by Three Part: X | Y | Z. E.g 0x00 | 0x04 | 0x80. X (Algorithm Type) can be as follows 0x00 : ConstantSecurity.MAC_MODE_CBC. 0x01 : ConstantSecurity.MAC_MODE_XOR_ECB_MAC. 0x02 : ConstantSecurity.MAC_MODE_ANSI_X9_19. Y (KSN Self Increasing Mode) can be as follows 0x00 : ConstantSecurity.NOT_SELF_INCREASING. 0x40: ConstantSecurity.SELF_INCREASING. Z (Dukpt Mode,default is 0x80) can be as follows 0x80 : ConstantSecurity.DUKPT_MODE_AES_MODE. dataIn - data involved in the calculation dataOut - data after calculation |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### getKsnDukpt

| Prototype    | Prototype int getKsnDukpt(int index,  byte[] ksnOut) |
| ------------ | --- |
| Function     | Function Get the KSN for the key at the specified index |
| Parameters   | Parameters Parameters: index - Key index ksnOut - KSN value |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### increaseKsnDukpt

| Prototype    | Prototype int increaseKsnDukpt(int index) |
| ------------ | --- |
| Function     | Function Increase KSN |
| Parameters   | Parameters Parameters: index - Key index |
| Return Value | Return value Returns: 0: The operation is successfully executed;  Others: The operation fails. Please refer to SecurityError for more information |
| Notes        | Notes  |

### calcMacDukptDes

| Prototype    | Prototype int calcMacDukptDes(int tikIndex,  int operationMode,  int ksnMode,  int macAlgorithm,  byte[] dataIn,  byte[] initVector,  byte[] dataOut,  byte[] usedKsn) |
| ------------ | --- |
| Function     | Function Calculate MAC using the DUKPT_TDES algorithm |
| Parameters   | Parameters Parameters: tikIndex - DUKPT key index operationMode - Encryption mode:     • ConstantSecurity.OPERATION_MODE_ECB     • ConstantSecurity.OPERATION_MODE_CBC ksnMode - KSN mode:     • ConstantSecurity.KSN_AUTO_INCREASING_BY_DUKPT_TDES_MAC_BOTH_KEY     • ConstantSecurity.KSN_NOT_AUTO_INCREASING_BY_DUKPT_TDES_MAC_BOTH_KEY     • ConstantSecurity.KSN_NOT_AUTO_INCREASING_BY_DUKPT_TDES_MAC_RSP_KEY macAlgorithm - MAC algorithm:     • ConstantSecurity.MAC_ALGORITHM_CBC     • ConstantSecurity.MAC_ALGORITHM_XOR_ECB_MAC     • ConstantSecurity.MAC_ALGORITHM_ANSI_X9_19 (TDES only)     • ConstantSecurity.MAC_ALGORITHM_ANSI_X9_9 (TDES only) dataIn - Input data to be used in MAC calculation initVector - Initialization vector (8 bytes for CBC; null for ECB) dataOut - Output MAC result (8 bytes) usedKsn - KSN used in calculation |
| Return Value | Return Value Return: 0 - Success;  Others - Failure. See SecurityError for details |
| Notes        | Notes This method calculates a MAC value using the DUKPT TDES algorithm with the provided input, mode, and algorithm settings. |

### eraseAllKey

| Prototype    | Prototype int eraseAllKey() |
| ------------ | --- |
| Function     | Function Erase all keys |
| Parameters   | Parameters  |
| Return Value | Return Value Return: 0 - Success;  Others - Failure. See SecurityError for details |
| Notes        | Notes This method deletes all stored cryptographic keys. |

### writeKeyDukptDes

| Prototype    | Prototype int writeKeyDukptDes(int tikIndex,  int tlkIndex,  byte[] keyIn,  byte[] ksnIn,  byte[] kcv) |
| ------------ | --- |
| Function     | Function Write DUKPT_DES key |
| Parameters   | Parameters Parameters: tikIndex - TIK key index (valid range: 1–10) tlkIndex - TLK key index (set to 0 if TLK is not used) keyIn - Key data ksnIn - Initial KSN kcv - Key Check Value |
| Return Value | Return Value Return: 0 - Success;  Others - Failure. See SecurityError for details |
| Notes        | Notes This method writes a DUKPT DES key along with its initial KSN and KCV to the specified index. |

### writeKeyMKSK

| Prototype    | Prototype  int writeKeyMKSK(int srcKeyType,  int srcKeyIndex,  int keyType,  int encryptionAlgorithm,  int index,  byte[] keyIn,  byte[] kcv) |
| ------------ | --- |
| Function     | Function Write MK/SK key |
| Parameters   | Parameters Parameters: srcKeyType - Source key type:     • ConstantSecurity.PED_TLK     • ConstantSecurity.PED_TMK srcKeyIndex - Source key index:     • ConstantSecurity.TLK: only index 1 is supported     • ConstantSecurity.TMK: index range [1, 64] keyType - Target key type:     • ConstantSecurity.PED_TLK • ConstantSecurity.PED_TMK • ConstantSecurity.PED_TPK • ConstantSecurity.PED_TAK • ConstantSecurity.PED_TDK • ConstantSecurity.PED_TEK • ConstantSecurity.PED_TTK encryptionAlgorithm - Encryption algorithm:     • ConstantSecurity.ENCRYPTION_ALGORITHM_TDES • ConstantSecurity.ENCRYPTION_ALGORITHM_AES • ConstantSecurity.ENCRYPTION_ALGORITHM_SM4 index - Key index:     • TLK: [1,1]; others (TMK, TPK, etc.): [1,64] Note: TPK, TAK, TDK, TEK, TTK share the same index space;  avoid duplication to prevent overwriting. keyIn - Key data (supported lengths: 8, 16, 24, 32 bytes) kcv - Key check value |
| Return Value | Return Value Return: 0 - Success;  Others - Failure. See SecurityError for details |
| Notes        | Notes This method writes Master or Session keys (MK/SK). Not applicable for DUKPT key injection. |

### calcRsaDecrypt

| Prototype    | Prototype int calcRsaDecrypt(int keyIndex,  int mode,  byte[] dataIn,  byte[] dataOut) |
| ------------ | --- |
| Function     | Function Perform RSA encryption or decryption (supports both public/private key decryption) |
| Parameters   | Parameters Parameters: keyIndex - Key index used for encryption/decryption mode - Padding mode:     • ConstantSecurity.PED_CALC_RSA_MODE_NO_PADDING     • ConstantSecurity.PED_CALC_RSA_MODE_PKCS1_PADDING     • ConstantSecurity.PED_CALC_RSA_MODE_OAEP_PADDING dataIn - Input data dataOut - Output data after encryption/decryption |
| Return Value | Return Value Return: >= 0 - Length of valid data in data Out< 0 - Failure. See error code definition |
| Notes        | Notes This method performs RSA operations using the specified key and padding mode.  Decryption with both public and private keys is supported. |

### calcRsaEncrypt

| Prototype    | Prototype int calcRsaEncrypt(int keyIndex,  int mode,  byte[] dataIn,  byte[] dataOut) |
| ------------ | --- |
| Function     | Function Perform RSA encryption (supports public/private key encryption) |
| Parameters   | Parameters Parameters: keyIndex - Key index used for encryption mode - Padding mode:     • ConstantSecurity.PED_CALC_RSA_MODE_NO_PADDING     • ConstantSecurity.PED_CALC_RSA_MODE_PKCS1_PADDING     • ConstantSecurity.PED_CALC_RSA_MODE_OAEP_PADDING dataIn - Original input data dataOut - Encrypted output data |
| Return Value | Return Value Return: >= 0 - Length of valid data in data Out< 0 - Error code (operation failed) |
| Notes        | Notes This method performs RSA encryption using the specified key and padding mode.  Both public and private key encryption are supported. |

### writeKeyTR31

| Prototype    | Prototype int writeKeyTR31(String tr31KeyBlock,  int srcKeyType,  int srcKeyIndex, int writeKeyType,  int writeKeyIndex,  int writeKeyAlgorithm) |
| ------------ | --- |
| Function     | Function Write TR31 key using extension method |
| Parameters   | Parameters Parameters: tr31KeyBlock - TR31 format key data   srcKeyType - Source key type: • ConstantSecurity.PED_TLK  • ConstantSecurity.PED_TMK srcKeyIndex - Source key index   writeKeyType - Target key type:  • ConstantSecurity.PED_TMK  • ConstantSecurity.PED_TPK  • ConstantSecurity.PED_TAK  • ConstantSecurity.PED_TDK  • ConstantSecurity.PED_TEK  • ConstantSecurity.PED_TTK   writeKeyIndex - Target key index   writeKeyAlgorithm - Target key algorithm: • ConstantSecurity.ENCRYPTION_ALGORITHM_TDES  • ConstantSecurity.ENCRYPTION_ALGORITHM_AES |
| Return Value | Return Value Return:   0 - Success   Others - Failure (see SecurityError) |
| Notes        | Notes  |

### writeKeyMKSK (KCV mode)

| Prototype    | Prototype int writeKeyMKSK(int srcKeyType,  int srcKeyIndex,  int keyType,  int encryptionAlgorithm,  int index,  byte[] keyIn,  int kcvMode,  byte[] kcv) |
| ------------ | --- |
| Function     | Function Write MK/SK key with support for encryption algorithm and KCV mode |
| Parameters   | Parameters Parameters: srcKeyType - Source key type: • ConstantSecurity.PED_TLK  • ConstantSecurity.PED_TMK   srcKeyIndex - Index of the source key used to encrypt the target key  • TLK: Index range [1,1]  • TMK: Index range [1,64]  keyType - Target key type:   • ConstantSecurity.PED_TLK,  • ConstantSecurity.PED_TMK,  • ConstantSecurity.PED_TPK,  • ConstantSecurity.PED_TAK,  • ConstantSecurity.PED_TDK,  • ConstantSecurity.PED_TEK,  • ConstantSecurity.PED_TTK   encryptionAlgorithm - Algorithm type:  • ConstantSecurity.ENCRYPTION_ALGORITHM_TDES  • ConstantSecurity.ENCRYPTION_ALGORITHM_AES  • ConstantSecurity.ENCRYPTION_ALGORITHM_SM4   index - Key index:  • TLK: [1,1]  • Others (TMK, TPK, TAK, TDK, TEK, TTK): [1,64]   Note: TPK, TAK, TDK, TEK, TTK share index space; newer entries overwrite previous ones at the same index.   keyIn - Key value (length: 8, 16, 24, or 32 bytes)   kcvMode - KCV validation mode:  • ConstantSecurity.KCV_MODE_NO_VERIFY  • ConstantSecurity.KCV_MODE_CHK_0  • ConstantSecurity.KCV_MODE_CHK_ODD  • ConstantSecurity.KCV_MODE_CHK_EVEN   kcv - KCV value (required if kcvMode != 0, length: 8 bytes) |
| Return Value | Return Value Return:   0 - Success   Others - Failure (see SecurityError) |
| Notes        | Notes Extended version of MK/SK key injection with encryption algorithm and KCV verification support |

### writeKeyDukptAes

| Prototype    | Prototype int writeKeyDukptAes(int tikIndex,  int tlkIndex,  byte[] keyIn,  byte[] ksnIn,  int kcvMode,  byte[] kcv) |
| ------------ | --- |
| Function     | Function Write DUKPT_AES key (supports TLK and KCV mode) |
| Parameters   | Parameters Parameters: tikIndex - TIK key index (range: 1–10) tlkIndex - TLK key index (set to 0 if TLK not used)  keyIn - Key value (supported lengths: 16 / 24 / 32 bytes)  ksnIn - Initial KSN (12 bytes)  kcvMode - KCV validation mode:  • ConstantSecurity.KCV_MODE_NO_VERIFY  • ConstantSecurity.KCV_MODE_CHK_0  • ConstantSecurity.KCV_MODE_CHK_ODD  • ConstantSecurity.KCV_MODE_CHK_EVEN  kcv - KCV value (required if kcvMode != 0, length: 8 bytes) |
| Return Value | Return Value Return:   0 - Success   Others - Failure (see SecurityError) |
| Notes        | Notes Used to inject AES-based DUKPT keys with optional TLK and KCV validation support |

### writeKeyDukptDes (KCV mode)

| Prototype    | Prototype int writeKeyDukptDes(int tikIndex,  int tlkIndex,  byte[] keyIn,  byte[] ksnIn,  int kcvMode,  byte[] kcv) |
| ------------ | --- |
| Function     | Function Write DUKPT_DES key (supports KCV mode) |
| Parameters   | Parameters Parameters: tikIndex - TIK key index (range: 1–10)  tlkIndex - TLK key index (set to 0 if TLK not used) keyIn - Key value  ksnIn - Initial KSN (10 bytes)  kcvMode - KCV validation mode:  • ConstantSecurity.KCV_MODE_NO_VERIFY  • ConstantSecurity.KCV_MODE_CHK_0  • ConstantSecurity.KCV_MODE_CHK_ODD  • ConstantSecurity.KCV_MODE_CHK_EVEN  kcv - KCV value (required if kcvMode != 0, length: 8 bytes) |
| Return Value | Return Value Return:   0 - Success   Others - Failure (see SecurityError) |
| Notes        | Notes Used for injecting DUKPT DES keys with optional TLK and KCV validation support. |

### readRsaKey (Bundle)

| Prototype    | Prototype int readRsaKey(int keyIndex,  android.os.Bundle bundle) |
| ------------ | --- |
| Function     | Function Read RSA key information |
| Parameters   | Parameters Parameters: keyIndex – RSA key index  bundle – Output container for key data.  Keys are defined in ConstantSecurity.RSA_BUNDLE_KEY |
| Return Value | Return Value Return:  0 – Success  Others – Failure (see SecurityError) |
| Notes        | Notes Used to retrieve RSA key data from a specific key index. |

### calcDukptAes

| Prototype    | Prototype int calcDukptAes(int tikIndex,  int keyUsage,  int algType,  byte[] initVector,  int operationDirection,  int operationMode,  int ksnMode,  byte[] dataIn,  byte[] aesIv,  byte[] dataOut,  byte[] usedKsn) |
| ------------ | --- |
| Function     | Function Encrypt or decrypt data using DUKPT_AES (supports ksnMode and usedKsn) |
| Parameters   | Parameters Parameters: tikIndex – Key index   keyUsage – Key usage mode      • ConstantSecurity.USE_DATA_ENCRYPT_KEY      • ConstantSecurity.USE_DATA_DECRYPT_KEY      • ConstantSecurity.USE_BOTH_WAYS_KEY   algType – AES algorithm type      • ConstantSecurity.KEY_ALG_TYPE_AES_128 • ConstantSecurity.KEY_ALG_TYPE_AES_192  • ConstantSecurity.KEY_ALG_TYPE_AES_256   initVector – Initial vector (8 bytes; pass empty if ECB mode)   operationDirection – Direction of operation: encrypt or decrypt      • ConstantSecurity.OPERATION_DIRECTION_ENCRYPT      • ConstantSecurity.OPERATION_DIRECTION_DECRYPT   operationMode – Operation mode      • ConstantSecurity.OPERATION_MODE_ECB      • ConstantSecurity.OPERATION_MODE_CBC   ksnMode – KSN handling mode      • ConstantSecurity.SELF_INCREASING      • ConstantSecurity.NOT_SELF_INCREASING   dataIn – Data to encrypt/decrypt   aesIv – 16-byte AES IV   dataOut – Output buffer for result   usedKsn – Output: used KSN (12 bytes) |
| Return Value | Return Value Return: 0 – Success Others – Failure (see SecurityError) |
| Notes        | Notes Performs AES encryption or decryption using a DUKPT key and configurable modes |

### calcMacDukptAes

| Prototype    | Prototype int calcMacDukptAes(int tikIndex,  int keyUsage,  int algType,  int macAlgorithm,  int ksnMode,  byte[] dataIn,  byte[] dataOut,  byte[] usedKsn) |
| ------------ | --- |
| Function     | Function Compute MAC using DUKPT_AES key |
| Parameters   | Parameters Parameters: tikIndex – DUKPT key index   keyUsage – Key usage mode      • ConstantSecurity.AUTHENTICATION_GENERATION      • ConstantSecurity.AUTHENTICATION_VERIFICATION      • ConstantSecurity.AUTHENTICATION_BOTH   algType – AES algorithm type      • ConstantSecurity.KEY_ALG_TYPE_AES_128  • ConstantSecurity.KEY_ALG_TYPE_AES_192  • ConstantSecurity.KEY_ALG_TYPE_AES_256   macAlgorithm – MAC algorithm      • ConstantSecurity.MAC_ALGORITHM_CBC      • ConstantSecurity.MAC_ALGORITHM_XOR_ECB_MAC      • ConstantSecurity.MAC_ALGORITHM_ANSI_X9_19   ksnMode – KSN handling mode      • ConstantSecurity.SELF_INCREASING      • ConstantSecurity.NOT_SELF_INCREASING   dataIn – Data to compute MAC from   dataOut – Output MAC data (16 bytes)   usedKsn – Output: used KSN (12 bytes) |
| Return Value | Return Value Return: 0 – Success Others – Failure (see SecurityError) |
| Notes        | Notes Computes MAC using the specified AES DUKPT key, algorithm, and mode. |

### calcSM4

| Prototype    | Prototype int calcSM4(int keyIndex,  int mode,  byte[] dataIn,  byte[] dataOut) |
| ------------ | --- |
| Function     | Function Encrypt or decrypt data using SM4 algorithm |
| Parameters   | Parameters Parameters: keyIndex – Index of the key used for encryption/decryption   mode – Operation mode and direction:     • ConstantSecurity.PED_CALC_DES_MODE_ECB_DEC     • ConstantSecurity.PED_CALC_DES_MODE_ECB_ENC     • ConstantSecurity.PED_CALC_DES_MODE_CBC_DEC     • ConstantSecurity.PED_CALC_DES_MODE_CBC_ENC  dataIn – Input data   dataOut – Output data (same length as input) |
| Return Value | Return Value Return: 0 – Success Others – Failure (see SecurityError) |
| Notes        | Notes Supports ECB and CBC modes for encryption and decryption with SM4 |

## Notes

No additional notes.

## Related Links

- [[kozen-financial-overview]]
- [[kozen-financial-init]]
