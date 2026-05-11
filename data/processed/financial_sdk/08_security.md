 3.8 Security module ............................................................................................................... 56
-- Get security module - getSecurityManager -- ............................................................................. 56
3.8.1 Write keys ...........................................................................................................................59
3.8.2 Write DUKPT keys ...............................................................................................................60
3.8.3 Generate RSA keys ...............................................................................................................61
3.8.4 Write RSA keys ................................................................................................................... 61
3.8.5 Read RSA keys ....................................................................................................................62
3.8.6 Get random numbers .............................................................................................................62
3.8.7 Get KCV for the corresponding key type .................................................................................. 62
3.8.8 Encrypt or decrypt data by DUKPT .........................................................................................63
3.8.9 RSA encryption or decryption ................................................................................................ 63
3.8.10 3DES data encryption and decryption ....................................................................................64
3.8.11 Calculate MAC ...................................................................................................................64
3.8.12 Calculate MAC by DUKPT .................................................................................................. 65
3.8.13 Get the KSN for the key at the specified index ........................................................................ 66

                                                                                         5
3.8.15 Calculate MAC using the DUKPT_TDES algorithm ................................................................. 66
3.8.16 Erase all keys .................................................................................................................... 67
3.8.17 Write DUKPT_DES key ...................................................................................................... 67
3.8.18 Write MK/SK key ............................................................................................................... 68
3.8.19 Perform RSA encryption or decryption ...................................................................................69
3.8.20 Perform RSA encryption ...................................................................................................... 69
3.8.21 Write TR31 key using extension method ................................................................................ 69
3.8.22 Write MK/SK key with support for encryption algorithm and KCV mode .....................................70
3.8.23 Write DUKPT_AES key (supports TLK and KCV mode) .......................................................... 71
3.8.24 Write DUKPT_DES key (supports KCV mode) ........................................................................72
3.8.25 Read RSA key information ...................................................................................................72
3.8.26 Encrypt or decrypt data using DUKPT_AES (supports ksnMode and usedKsn) ............................ 73
3.8.27 Compute MAC using DUKPT_AES key ................................................................................. 74
3.8.28 Encrypt or decrypt data using SM4 algorithm ..........................................................................74
 3.8 Security module                                              3DES data encryption and decryption

-- Get security module - getSecurityManager --

int calcDes(int keyIndex,
int mode,
byte[] dataIn,
byte[] dataOut)

                                                         56
int keyMode,
int algType,                                          Calculate MAC
int mode,
byte[] dataIn,                                        Calculate MAC using DUKPT
byte[] aesIv,
byte[] dataOut)                                       RSA encryption or decryption
int calcMac(int index,
int keyType,                                          Generate RSA keys
byte[] iv,                                            Get the KCV for the corresponding key type
byte[] dataIn,                                        Get the KSN value by specified index
byte[] dataOut)                                       Get random numbers compliant with NIST
int calcMacDukpt(int index,                           SP800-90A
int keyType,                                          Increase KSN
int mode,                                             Read RSA keys
byte[] dataIn,
byte[] dataOut)                                       Write keys
int calcRsa(int keyIndex,
int mode,                                             Write DUKPT keys
byte[] dataIn,
byte[] dataOut)                                       Write RSA keys
int generateRsaKey(int pubKeyIndex,
int priKeyIndex, int size)           57
int getKCV(int keyIndex,
int keyType,
byte[] kcvOut)
int getKsnDukpt(int index,
byte[] ksnOut)
int getRandom(int length,
byte[] keyOut)
int increaseKsnDukpt(int index)
int readRsaKey(int keyIndex,
byte[] keyOut,
byte[] modulusOut,
byte[] exponentOut)
int writeKey(int srcKeyType,
int srcKeyIndex,
int keyType,
int index,
byte[] keyIn, byte[] kcv)
int writeKeyDukpt(int index,
byte[] keyIn,
byte[] ksnIn,
byte[] kcv)
int writeRsaKey(int keyIndex,
byte[] exponent)                                        algorithm
int calcMacDukptDes(int tikIndex,
int operationMode,                                      Erase all keys
int ksnMode,                                            Write DUKPT_DES keys
int macAlgorithm,
byte[] dataIn,                                          Inject MK/SK keys
byte[] aesIv,
byte[] dataOut,                                         Perform RSA decryption
byte[] usedKsn)                                         (supports public/private key decryption)
int eraseAllKey()                                       Perform RSA encryption
int writeKeyDukptDes(int tikIndex,                      (supports public/private key encryption)
int tlkIndex,                                           Write TR31 key using the extended method
byte[] keyIn,
byte[] ksnIn,                                           Write MK/SK key (supports encryption
byte[] kcv)                                             algorithm type and KCV mode)
int writeKeyMKSK(int srcKeyType,
int srcKeyIndex,                       58
int keyType,
int encryptionAlgorithm,
int index,
byte[] keyIn,
byte[] kcv)
int calcRsaDecrypt(int keyIndex,
int mode,
byte[] dataIn,
byte[] dataOut)
int calcRsaEncrypt(int keyIndex,
int mode,
byte[] dataIn,
byte[] dataOut)
int writeKeyTR31(String tr31KeyBlock,
int srcKeyType,
int srcKeyIndex,
int writeKeyType,
int writeKeyIndex,
int writeKeyAlgorithm)
int writeKeyMKSK(int srcKeyType,
int srcKeyIndex,
int keyType,
int encryptionAlgorithm,
int index,
byte[] keyIn,
int kcvMode,
byte[] kcv)
int tlkIndex,                                                                        KCV mode)
byte[] keyIn,
byte[] ksnIn,                                                                        Write DUKPT_DES key (supports KCV
int kcvMode,                                                                         mode)
byte[] kcv)
int writeKeyDukptDes(int tikIndex,                                                   Read RSA key
int tlkIndex,                                                                        Encrypt or decrypt data using DUKPT_AES
byte[] keyIn,                                                                        (supports ksnMode and usedKsn)
byte[] ksnIn,
int kcvMode,                                                                         Calculate MAC using DUKPT_AES
byte[] kcv)
int readRsaKey(int keyIndex,                                                         Encrypt or decrypt data using SM4
android.os.Bundle bundle)
int calcDukptAes(int tikIndex,
int keyUsage,
int algType,
byte[] initVector,
int operationDirection,
int operationMode,
int ksnMode,
byte[] dataIn,
byte[] aesIv,
byte[] dataOut,
byte[] usedKsn)
int calcMacDukptAes(int tikIndex,
int keyUsage,
int algType,
int macAlgorithm,
int ksnMode,
byte[] dataIn,
byte[] dataOut,
byte[] usedKsn)
int calcSM4(int keyIndex,
int mode,
byte[] dataIn,
byte[] dataOut)

3.8.1 Write keys

Prototype         int writeKey(int srcKeyType,
                  int srcKeyIndex,
                  int keyType,
                  int index,
                  byte[] keyIn,

                                                                                 59
Parameters    Write keys
              Parameters:
              srcKeyType - Source key type
              Such as ConstantSecurity.PED_TLK, ConstantSecurity.PED_TMK
              srcKeyIndex - Source key index
              the key index used to decrypt the target key.
              TLK: Only 1 group is supported, and the index range is [1,1].
              TMK: Supports 64 groups, the index range is [1, 64].
              TPK: Supports 64 groups, the index range is [1, 64].
              TAK: Supports 64 groups, the index range is [1, 64].
              TDK: Supports 64 groups, the index range is [1, 64].
              TEK: Supports 64 groups, the index range is [1, 64].
              TTK: Supports 64 groups, the index range is [1, 64].
              Note: TPK, TAK, TDK, TEK, TTK share the index space. Key indexes can not be duplicated. If
              duplication occurs, the later written key will overwrite the previously injected key.
              keyType - Key type, as follows:
              ConstantSecurity.PED_TLK
              ConstantSecurity.PED_TMK
              ConstantSecurity.PED_TPK
              ConstantSecurity.PED_TAK
              ConstantSecurity.PED_TDK
              ConstantSecurity.PED_TEK
              ConstantSecurity.PED_TTK
              index - Key index, as follows:
              TLK: Only 1 group is supported, and the index range is [1,1].
              TMK: Supports 64 groups, the index range is [1, 64].
              TPK: Supports 64 groups, the index range is [1, 64].
              TAK: Supports 64 groups, the index range is [1, 64].
              TDK: Supports 64 groups, the index range is [1, 64].
              TEK: Supports 64 groups, the index range is [1, 64].
              TTK: Supports 64 groups, the index range is [1, 64].
              Note: TPK, TAK, TDK, TEK, TTK share the index space. Key indexes should not be duplicated. If
              duplication occurs, the later written key will overwrite the previously injected key.
              keyIn - Key information, supported key lengths: [8, 16, 24, 32]
              kcv - KCV value

Return value  Returns:
Notes         0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.2 Write DUKPT keys

Prototype     int writeKeyDukpt(int index,

                                                                             60
Parameters    byte[] ksnIn,
              byte[] kcv)
Return value  Write DUKPT keys
Notes         Parameters:
              index - Key index (supported range 110)
              keyIn - Key data
              ksnIn - Initialization KSN
              kcv - KCV value
              Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.3 Generate RSA keys

Prototype     int generateRsaKey(int pubKeyIndex,
Function      int priKeyIndex,
Parameters
               int size)
Return value  Generate RSA keys
Notes         Parameters:
              pubKeyIndex - Public key index
              priKeyIndex - Private key index
              size - Key size
              Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information
              Note: The key index range is 14, only support two sets of public and private keys.

3.8.4 Write RSA keys

Prototype     int writeRsaKey(int keyIndex,
Function      byte[] modulus,
Parameters    byte[] exponent)
              Write RSA keys
Return value  Parameters:
Notes         keyIndex - Key index
              modulus - Modulus
              exponent - Exponent
              Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information
              Note: If the length of the exponent is less than the length of the modulus, the key type written is a
              public key. If the length of the exponent is equal to the length of the modulus, the key type written
              is private key.

                                                                             61

Prototype     int readRsaKey(int keyIndex,
              byte[] keyOut,
Function      byte[] modulusOut,
Parameters    byte[] exponentOut)
              Read RSA keys
Return value  Parameters:
Notes         keyIndex - Key index
              keyOut - Key information
              modulusOut - Key modulus
              exponentOut - Key exponent
              Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.6 Get random numbers

Prototype     int getRandom(int length,
Function      byte[] keyOut)
Parameters    Get random numbers compliant with NIST SP800-90A
              Parameters:
Return value  length - Length of the random number
              keyOut - Random number
Notes         Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.7 Get KCV for the corresponding key type

Prototype     int getKCV(int keyIndex,
              int keyType,
Function      byte[] kcvOut)
Parameters    Get KCV for the corresponding key type
              Parameters:
              keyIndex - Key index
              keyType - Key type, as follows:
              ConstantSecurity.PED_TLK
              ConstantSecurity.PED_TMK
              ConstantSecurity.PED_TPK
              ConstantSecurity.PED_TAK
              ConstantSecurity.PED_TDK
              ConstantSecurity.PED_TEK
              ConstantSecurity.PED_TIK

                                                                             62
Notes         kcvOut - KCV value
              Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.8 Encrypt or decrypt data by DUKPT

Prototype     int calcDukpt(int index,
Function      int keyMode,
Parameters    int algType,
              int mode,
Return value  byte[] dataIn,
Notes         byte[] aesIv,
              byte[] dataOut)
              Encrypt or decrypt data by DUKPT
              Parameters:
              index - Key index
              keyMode - Dukpt mode, can be as follows
              ConstantSecurity.PED_CALC_DUKPT_MODE_DEC: 0x01
              ConstantSecurity.PED_CALC_DUKPT_MODE_ENC: 0x02
              algType - Algorithm type, can be as follows
              ConstantSecurity.KEY_ALG_TYPE_2TDEA
              ConstantSecurity.KEY_ALG_TYPE_3TDEA
              ConstantSecurity.KEY_ALG_TYPE_AES_128
              ConstantSecurity.KEY_ALG_TYPE_AES_192
              ConstantSecurity.KEY_ALG_TYPE_AES_256
              mode - Operation Mode, can be as follows
              ConstantSecurity.DUKPT_MAC_MODE_ECB: ECB Mode.
              ConstantSecurity.DUKPT_MAC_MODE_CBC: CBC Mode.
              dataIn - Input data
              aesIv - Initialization vector, pass null for ECB mode, or pass an 8-byte vector for other encryption
              modes
              dataOut - Encrypted data
              Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.9 RSA encryption or decryption

Prototype     int calcRsa(int keyIndex, int mode, byte[] dataIn, byte[] dataOut)
Function      RSA encryption or decryption
Parameters    Parameters:

                                        63
Notes         mode - RSA padding Mode, can be as follows
              ConstantSecurity.PED_CALC_RSA_MODE_NO_PADDING
              ConstantSecurity.PED_CALC_RSA_MODE_PKCS1_PADDING
              ConstantSecurity.PED_CALC_RSA_MODE_OAEP_PADDING
              dataIn - Input data
              dataOut - Encrypted or decrypted data
              Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.10 3DES data encryption and decryption

Prototype     int calcDes(int keyIndex,
Function      int mode,
Parameters    byte[] dataIn,
              byte[] dataOut)
Return value  3DES data encryption and decryption
Notes         Parameters:
              keyIndex - Index of TDK.
              mode - Encryption and Decryption Mode, can be as follows
              ConstantSecurity.PED_CALC_DES_MODE_ECB_DEC
              ConstantSecurity.PED_CALC_DES_MODE_ECB_ENC
              ConstantSecurity.PED_CALC_DES_MODE_CBC_DEC
              ConstantSecurity.PED_CALC_DES_MODE_CBC_ENC
              dataIn - Input data
              dataOut - Encrypted or decrypted data
              Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.11 Calculate MAC

Prototype     int calcMac(int index,
              int keyType,
Function      byte[] iv,
Parameters    byte[] dataIn,
              byte[] dataOut)
              Calculate MAC
              Parameters:
              index - TAK key index
              keyType - MAC algorithm type, can be as follows
              ConstantSecurity.MAC_MODE_CBC: CBC-MAC.

                                            64
Notes         ConstantSecurity.MAC_MODE_ANSI_X9_19: ANSI-X9.19 MAC.
              ConstantSecurity.MAC_MODE_ANSI_X9_9: ANSI-X9.9 MAC.
              iv - Initialization vector
              dataIn - input data
              dataOut - Calculated data
              Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.12 Calculate MAC by DUKPT

Prototype     int calcMacDukpt(int index,
              int keyType,
Function      int mode,
Parameters    byte[] dataIn,
              byte[] dataOut)
              Calculate MAC by DUKPT
              index - dukpt key index
              keyType - Key Type :
              This Code is Coded by Two Part: X | Y
              E.g 0x00 | 0x40.
              X (Key Usage) can be as follows
              0x00 : ConstantSecurity.AUTHENTICATION_GENERATION.
              0x01 : ConstantSecurity.AUTHENTICATION_VERIFICATION.
              0x02 : ConstantSecurity.AUTHENTICATION_BOTH.
              Y (Derive Key Algorithm Type) can be as follows
              0x00 : ConstantSecurity.KEY_ALG_TYPE_2TDEA.
              0x10: ConstantSecurity.KEY_ALG_TYPE_3TDEA.
              0x20: ConstantSecurity.KEY_ALG_TYPE_AES_128.
              0x30: ConstantSecurity.KEY_ALG_TYPE_AES_192.
              0x40: ConstantSecurity.KEY_ALG_TYPE_AES_256.
              mode - MAC Operation Control Code.
              This Code is Coded by Three Part: X | Y | Z.
              E.g 0x00 | 0x04 | 0x80.
              X (Algorithm Type) can be as follows
              0x00 : ConstantSecurity.MAC_MODE_CBC.
              0x01 : ConstantSecurity.MAC_MODE_XOR_ECB_MAC.
              0x02 : ConstantSecurity.MAC_MODE_ANSI_X9_19.
              Y (KSN Self Increasing Mode) can be as follows
              0x00 : ConstantSecurity.NOT_SELF_INCREASING.
              0x40: ConstantSecurity.SELF_INCREASING.
              Z (Dukpt Mode,default is 0x80) can be as follows
              0x80 : ConstantSecurity.DUKPT_MODE_AES_MODE.

                                                                             65
Notes         dataOut - data after calculation
              Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.13 Get the KSN for the key at the specified index

Prototype     int getKsnDukpt(int index,
Function      byte[] ksnOut)
Parameters    Get the KSN for the key at the specified index
              Parameters:
Return value  index - Key index
              ksnOut - KSN value
Notes         Returns:
              0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.14 Increase KSN

Prototype     int increaseKsnDukpt(int index)
Function      Increase KSN
Parameters    Parameters:
Return value  index - Key index
              Returns:
Notes         0: The operation is successfully executed;
              Others: The operation fails. Please refer to SecurityError for more information

3.8.15 Calculate MAC using the DUKPT_TDES algorithm

Prototype     int calcMacDukptDes(int tikIndex,
              int operationMode,
Function      int ksnMode,
Parameters    int macAlgorithm,
              byte[] dataIn,
              byte[] initVector,
              byte[] dataOut,
              byte[] usedKsn)
              Calculate MAC using the DUKPT_TDES algorithm
              Parameters:
              tikIndex - DUKPT key index
              operationMode - Encryption mode:
              · ConstantSecurity.OPERATION_MODE_ECB

                                                                             66
Notes         ksnMode - KSN mode:
              · ConstantSecurity.KSN_AUTO_INCREASING_BY_DUKPT_TDES_MAC_BOTH_KEY
              · ConstantSecurity.KSN_NOT_AUTO_INCREASING_BY_DUKPT_TDES_MAC_BOTH_KEY
              · ConstantSecurity.KSN_NOT_AUTO_INCREASING_BY_DUKPT_TDES_MAC_RSP_KEY
              macAlgorithm - MAC algorithm:
              · ConstantSecurity.MAC_ALGORITHM_CBC
              · ConstantSecurity.MAC_ALGORITHM_XOR_ECB_MAC
              · ConstantSecurity.MAC_ALGORITHM_ANSI_X9_19 (TDES only)
              · ConstantSecurity.MAC_ALGORITHM_ANSI_X9_9 (TDES only)
              dataIn - Input data to be used in MAC calculation
              initVector - Initialization vector (8 bytes for CBC; null for ECB)
              dataOut - Output MAC result (8 bytes)
              usedKsn - KSN used in calculation
              Return:
              0 - Success;
              Others - Failure. See SecurityError for details
              This method calculates a MAC value using the DUKPT TDES algorithm with the provided input,
              mode, and algorithm settings.

3.8.16 Erase all keys

Prototype     int eraseAllKey()
Function      Erase all keys
Parameters
Return Value  Return:
              0 - Success;
Notes         Others - Failure. See SecurityError for details
              This method deletes all stored cryptographic keys.

3.8.17 Write DUKPT_DES key

Prototype     int writeKeyDukptDes(int tikIndex,
              int tlkIndex,
Function      byte[] keyIn,
Parameters    byte[] ksnIn,
              byte[] kcv)
Return Value  Write DUKPT_DES key
              Parameters:
              tikIndex - TIK key index (valid range: 1­10)
              tlkIndex - TLK key index (set to 0 if TLK is not used)
              keyIn - Key data
              ksnIn - Initial KSN
              kcv - Key Check Value
              Return:

                            67
              Others - Failure. See SecurityError for details
              This method writes a DUKPT DES key along with its initial KSN and KCV to the specified index.

3.8.18 Write MK/SK key

Prototype     int writeKeyMKSK(int srcKeyType,
Function      int srcKeyIndex,
Parameters    int keyType,
              int encryptionAlgorithm,
Return Value  int index,
Notes         byte[] keyIn,
              byte[] kcv)
              Write MK/SK key
              Parameters:
              srcKeyType - Source key type:
              · ConstantSecurity.PED_TLK
              · ConstantSecurity.PED_TMK
              srcKeyIndex - Source key index:
              · ConstantSecurity.TLK: only index 1 is supported
              · ConstantSecurity.TMK: index range [1, 64]
              keyType - Target key type:
              · ConstantSecurity.PED_TLK
              · ConstantSecurity.PED_TMK
              · ConstantSecurity.PED_TPK
              · ConstantSecurity.PED_TAK
              · ConstantSecurity.PED_TDK
              · ConstantSecurity.PED_TEK
              · ConstantSecurity.PED_TTK
              encryptionAlgorithm - Encryption algorithm:
              · ConstantSecurity.ENCRYPTION_ALGORITHM_TDES
              · ConstantSecurity.ENCRYPTION_ALGORITHM_AES
              · ConstantSecurity.ENCRYPTION_ALGORITHM_SM4
              index - Key index:
              · TLK: [1,1]; others (TMK, TPK, etc.): [1,64]
              Note: TPK, TAK, TDK, TEK, TTK share the same index space;
              avoid duplication to prevent overwriting.
              keyIn - Key data (supported lengths: 8, 16, 24, 32 bytes)
              kcv - Key check value
              Return:
              0 - Success;
              Others - Failure. See SecurityError for details
              This method writes Master or Session keys (MK/SK). Not applicable for DUKPT key injection.

                        68

Prototype     int calcRsaDecrypt(int keyIndex,
Function      int mode,
Parameters    byte[] dataIn,
              byte[] dataOut)
Return Value  Perform RSA encryption or decryption (supports both public/private key decryption)
Notes         Parameters:
              keyIndex - Key index used for encryption/decryption
              mode - Padding mode:
              · ConstantSecurity.PED_CALC_RSA_MODE_NO_PADDING
              · ConstantSecurity.PED_CALC_RSA_MODE_PKCS1_PADDING
              · ConstantSecurity.PED_CALC_RSA_MODE_OAEP_PADDING
              dataIn - Input data
              dataOut - Output data after encryption/decryption
              Return:
              >= 0 - Length of valid data in data
              Out< 0 - Failure. See error code definition
              This method performs RSA operations using the specified key and padding mode.
              Decryption with both public and private keys is supported.

3.8.20 Perform RSA encryption

Prototype     int calcRsaEncrypt(int keyIndex,
Function      int mode,
Parameters    byte[] dataIn,
              byte[] dataOut)
Return Value  Perform RSA encryption (supports public/private key encryption)
Notes         Parameters:
              keyIndex - Key index used for encryption
              mode - Padding mode:
              · ConstantSecurity.PED_CALC_RSA_MODE_NO_PADDING
              · ConstantSecurity.PED_CALC_RSA_MODE_PKCS1_PADDING
              · ConstantSecurity.PED_CALC_RSA_MODE_OAEP_PADDING
              dataIn - Original input data
              dataOut - Encrypted output data
              Return:
              >= 0 - Length of valid data in data
              Out< 0 - Error code (operation failed)
              This method performs RSA encryption using the specified key and padding mode.
              Both public and private key encryption are supported.

3.8.21 Write TR31 key using extension method

Prototype     int writeKeyTR31(String tr31KeyBlock,
              int srcKeyType,

                                                                             69
Parameters    int writeKeyType,
              int writeKeyIndex,
Return Value  int writeKeyAlgorithm)
Notes         Write TR31 key using extension method
              Parameters:
              tr31KeyBlock - TR31 format key data
              srcKeyType - Source key type:
              · ConstantSecurity.PED_TLK
              · ConstantSecurity.PED_TMK
              srcKeyIndex - Source key index
              writeKeyType - Target key type:
              · ConstantSecurity.PED_TMK
              · ConstantSecurity.PED_TPK
              · ConstantSecurity.PED_TAK
              · ConstantSecurity.PED_TDK
              · ConstantSecurity.PED_TEK
              · ConstantSecurity.PED_TTK
              writeKeyIndex - Target key index
              writeKeyAlgorithm - Target key algorithm:
              · ConstantSecurity.ENCRYPTION_ALGORITHM_TDES
              · ConstantSecurity.ENCRYPTION_ALGORITHM_AES
              Return:
              0 - Success
              Others - Failure (see SecurityError)

3.8.22 Write MK/SK key with support for encryption algorithm and KCV mode

Prototype     int writeKeyMKSK(int srcKeyType,
              int srcKeyIndex,
Function      int keyType,
Parameters    int encryptionAlgorithm,
              int index,
              byte[] keyIn,
              int kcvMode,
              byte[] kcv)
              Write MK/SK key with support for encryption algorithm and KCV mode
              Parameters:
              srcKeyType - Source key type:
              · ConstantSecurity.PED_TLK
              · ConstantSecurity.PED_TMK
              srcKeyIndex - Index of the source key used to encrypt the target key
              · TLK: Index range [1,1]
              · TMK: Index range [1,64]

                                                                             70
Notes         · ConstantSecurity.PED_TLK,
              · ConstantSecurity.PED_TMK,
              · ConstantSecurity.PED_TPK,
              · ConstantSecurity.PED_TAK,
              · ConstantSecurity.PED_TDK,
              · ConstantSecurity.PED_TEK,
              · ConstantSecurity.PED_TTK
              encryptionAlgorithm - Algorithm type:
              · ConstantSecurity.ENCRYPTION_ALGORITHM_TDES
              · ConstantSecurity.ENCRYPTION_ALGORITHM_AES
              · ConstantSecurity.ENCRYPTION_ALGORITHM_SM4
              index - Key index:
              · TLK: [1,1]
              · Others (TMK, TPK, TAK, TDK, TEK, TTK): [1,64]
              Note: TPK, TAK, TDK, TEK, TTK share index space; newer entries overwrite previous ones at the
              same index.
              keyIn - Key value (length: 8, 16, 24, or 32 bytes)
              kcvMode - KCV validation mode:
              · ConstantSecurity.KCV_MODE_NO_VERIFY
              · ConstantSecurity.KCV_MODE_CHK_0
              · ConstantSecurity.KCV_MODE_CHK_ODD
              · ConstantSecurity.KCV_MODE_CHK_EVEN
              kcv - KCV value (required if kcvMode != 0, length: 8 bytes)
              Return:
              0 - Success
              Others - Failure (see SecurityError)
              Extended version of MK/SK key injection with encryption algorithm and KCV verification support

3.8.23 Write DUKPT_AES key (supports TLK and KCV mode)

Prototype     int writeKeyDukptAes(int tikIndex,
              int tlkIndex,
Function      byte[] keyIn,
Parameters    byte[] ksnIn,
              int kcvMode,
              byte[] kcv)
              Write DUKPT_AES key (supports TLK and KCV mode)
              Parameters:
              tikIndex - TIK key index (range: 1­10)
              tlkIndex - TLK key index (set to 0 if TLK not used)
              keyIn - Key value (supported lengths: 16 / 24 / 32 bytes)
              ksnIn - Initial KSN (12 bytes)
              kcvMode - KCV validation mode:
              · ConstantSecurity.KCV_MODE_NO_VERIFY

                                                                             71
Notes         · ConstantSecurity.KCV_MODE_CHK_ODD
              · ConstantSecurity.KCV_MODE_CHK_EVEN
              kcv - KCV value (required if kcvMode != 0, length: 8 bytes)
              Return:
              0 - Success
              Others - Failure (see SecurityError)
              Used to inject AES-based DUKPT keys with optional TLK and KCV validation support

3.8.24 Write DUKPT_DES key (supports KCV mode)

Prototype     int writeKeyDukptDes(int tikIndex,
Function      int tlkIndex,
Parameters    byte[] keyIn,
              byte[] ksnIn,
Return Value  int kcvMode,
Notes         byte[] kcv)
              Write DUKPT_DES key (supports KCV mode)
              Parameters:
              tikIndex - TIK key index (range: 1­10)
              tlkIndex - TLK key index (set to 0 if TLK not used)
              keyIn - Key value
              ksnIn - Initial KSN (10 bytes)
              kcvMode - KCV validation mode:
              · ConstantSecurity.KCV_MODE_NO_VERIFY
              · ConstantSecurity.KCV_MODE_CHK_0
              · ConstantSecurity.KCV_MODE_CHK_ODD
              · ConstantSecurity.KCV_MODE_CHK_EVEN
              kcv - KCV value (required if kcvMode != 0, length: 8 bytes)
              Return:
              0 - Success
              Others - Failure (see SecurityError)
              Used for injecting DUKPT DES keys with optional TLK and KCV validation support.

3.8.25 Read RSA key information

Prototype     int readRsaKey(int keyIndex,
Function      android.os.Bundle bundle)
Parameters    Read RSA key information
              Parameters:
Return Value  keyIndex ­ RSA key index
              bundle ­ Output container for key data.
              Keys are defined in ConstantSecurity.RSA_BUNDLE_KEY
              Return:
              0 ­ Success

                                                72
              Used to retrieve RSA key data from a specific key index.

3.8.26 Encrypt or decrypt data using DUKPT_AES (supports ksnMode and usedKsn)

Prototype     int calcDukptAes(int tikIndex,
Function      int keyUsage,
Parameters    int algType,
              byte[] initVector,
Return Value  int operationDirection,
Notes         int operationMode,
              int ksnMode,
              byte[] dataIn,
              byte[] aesIv,
              byte[] dataOut,
              byte[] usedKsn)
              Encrypt or decrypt data using DUKPT_AES (supports ksnMode and usedKsn)
              Parameters:
              tikIndex ­ Key index
              keyUsage ­ Key usage mode
              · ConstantSecurity.USE_DATA_ENCRYPT_KEY
              · ConstantSecurity.USE_DATA_DECRYPT_KEY
              · ConstantSecurity.USE_BOTH_WAYS_KEY
              algType ­ AES algorithm type
              · ConstantSecurity.KEY_ALG_TYPE_AES_128
              · ConstantSecurity.KEY_ALG_TYPE_AES_192
              · ConstantSecurity.KEY_ALG_TYPE_AES_256
              initVector ­ Initial vector (8 bytes; pass empty if ECB mode)
              operationDirection ­ Direction of operation: encrypt or decrypt
              · ConstantSecurity.OPERATION_DIRECTION_ENCRYPT
              · ConstantSecurity.OPERATION_DIRECTION_DECRYPT
              operationMode ­ Operation mode
              · ConstantSecurity.OPERATION_MODE_ECB
              · ConstantSecurity.OPERATION_MODE_CBC
              ksnMode ­ KSN handling mode
              · ConstantSecurity.SELF_INCREASING
              · ConstantSecurity.NOT_SELF_INCREASING
              dataIn ­ Data to encrypt/decrypt
              aesIv ­ 16-byte AES IV
              dataOut ­ Output buffer for result
              usedKsn ­ Output: used KSN (12 bytes)
              Return:
              0 ­ Success
              Others ­ Failure (see SecurityError)
              Performs AES encryption or decryption using a DUKPT key and configurable modes

                                                                             73

Prototype     int calcMacDukptAes(int tikIndex,
Function      int keyUsage,
Parameters    int algType,
              int macAlgorithm,
Return Value  int ksnMode,
Notes         byte[] dataIn,
              byte[] dataOut,
              byte[] usedKsn)
              Compute MAC using DUKPT_AES key
              Parameters:
              tikIndex ­ DUKPT key index
              keyUsage ­ Key usage mode
              · ConstantSecurity.AUTHENTICATION_GENERATION
              · ConstantSecurity.AUTHENTICATION_VERIFICATION
              · ConstantSecurity.AUTHENTICATION_BOTH
              algType ­ AES algorithm type
              · ConstantSecurity.KEY_ALG_TYPE_AES_128
              · ConstantSecurity.KEY_ALG_TYPE_AES_192
              · ConstantSecurity.KEY_ALG_TYPE_AES_256
              macAlgorithm ­ MAC algorithm
              · ConstantSecurity.MAC_ALGORITHM_CBC
              · ConstantSecurity.MAC_ALGORITHM_XOR_ECB_MAC
              · ConstantSecurity.MAC_ALGORITHM_ANSI_X9_19
              ksnMode ­ KSN handling mode
              · ConstantSecurity.SELF_INCREASING
              · ConstantSecurity.NOT_SELF_INCREASING
              dataIn ­ Data to compute MAC from
              dataOut ­ Output MAC data (16 bytes)
              usedKsn ­ Output: used KSN (12 bytes)
              Return:
              0 ­ Success
              Others ­ Failure (see SecurityError)
              Computes MAC using the specified AES DUKPT key, algorithm, and mode.

3.8.28 Encrypt or decrypt data using SM4 algorithm

Prototype     int calcSM4(int keyIndex,
              int mode,
Function      byte[] dataIn,
Parameters    byte[] dataOut)
              Encrypt or decrypt data using SM4 algorithm
              Parameters:
              keyIndex ­ Index of the key used for encryption/decryption

                                                    74
Notes         · ConstantSecurity.PED_CALC_DES_MODE_ECB_DEC
              · ConstantSecurity.PED_CALC_DES_MODE_ECB_ENC
              · ConstantSecurity.PED_CALC_DES_MODE_CBC_DEC
              · ConstantSecurity.PED_CALC_DES_MODE_CBC_ENC
              dataIn ­ Input data
              dataOut ­ Output data (same length as input)
              Return:
              0 ­ Success
              Others ­ Failure (see SecurityError)
              Supports ECB and CBC modes for encryption and decryption with SM4

