 3.2 Certification module

-- Get Certification module - getCertificationManager--

int deleteAppSignature(String certData)                                          Delete the app signature certificate
List<String> getAppSignatureInfo()                                               Get the app signature certificate information
int updateAppSignature(String certData)                                          Update the app signature certificate

3.2.1 Updates the application's signature certificate

Prototype     int updateAppSignature(String certData)
Function      Updates the application's signature certificate.

                                                                             10
Return value  certData- Certificate Data
Notes         Return:
              - 0: Success
              - Others: Failure (specific error codes refer to CertificationError).
              For failure cases, refer to CertificationError for detailed error codes.

3.2.2 Deletes the application's signature certificate

Prototype     int deleteAppSignature(String certData)
Function      Deletes the application's signature certificate.
Parameters    Parameters:
              certData- Certificate Data to Be Deleted
Return value  Return:
Notes         - 0: Success
              - Others: Failure (specific error codes refer to CertificationError).
              For failure cases, refer to CertificationError for detailed error codes.

3.2.3 Get the application's signature certificate information

Prototype     List<String> getAppSignatureInfo()
Function      Get the application's signature certificate information.
Parameters
              Return:
Return value  Certificate Details List

Notes

