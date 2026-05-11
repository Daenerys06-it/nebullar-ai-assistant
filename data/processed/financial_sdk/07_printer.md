 3.7 Printing Operation module ................................................................................................. 49
-- Get printing operation module - getPrinterManager -- ................................................................. 49
3.7.1 Open the printer module ........................................................................................................50
3.7.2 Get the current status of the printer .........................................................................................50
3.7.3 Feed paper before starting printing ......................................................................................... 51
3.7.4 Set print grayscale ................................................................................................................ 51
3.7.5 Set print font ........................................................................................................................51
3.7.6 Set print line space ...............................................................................................................52
3.7.7 Add the text to the print cache ............................................................................................... 52
3.7.8 Add a line of text with different styles to the print cache ............................................................ 52
3.7.9 Add a blank line to the print cache ......................................................................................... 52
3.7.10 Add the barcode to the print cache ........................................................................................53
3.7.11 Add the bitmap to the print cache ......................................................................................... 53
3.7.12 Trigger the printing operation to print out the content in the print cache ..................................... 53
3.7.13 Trigger the printing operation to print out the content in the print cache ..................................... 54
3.7.14 Turn off the printer ............................................................................................................. 54
3.7.15 Configure whether to clear print cache after paper-out warning .................................................54
3.7.16 Set printer gray level by percentage .......................................................................................54
3.7.17 Get current printer gray level percentage ............................................................................... 55
3.7.18 Set global font size for printing ............................................................................................. 55
3.7.19 Get current global font size .................................................................................................. 55
3.7.20 Set line spacing multiplier for printing ...................................................................................55
3.7.21 Get current line spacing multiplier ........................................................................................56
-- Print result callback - IPrintResultCallback -- ...........................................................................56
3.7.22 Callback when the printing finishes successfully .....................................................................56
3.7.23 Callback when an error occurs during the printing process ....................................................... 56
 3.7 Printing Operation module                                                                       Add the barcode to the print cache.
-- Get printing operation module - getPrinterManager --                                              Add the bitmap to the print cache.
int addBarcode(BarcodePrintLine barcodeLine)                                                         Add the text to the print cache.
int addBitmap(BitmapPrintLine bitmapLine)                                                            Add a line of text with different styles to the
int addText(TextPrintLine textLine)                                                                  print cache.
int addText(List<TextPrintLine> textLines)                                                           Turn off the printer.
void close()                                                                                         Perform the paper feeding action before
int feedPaper(int lines)                                                                             starting printing. The main purpose is to
                                                                                                     adjust the paper position of the printer to
                                                                                                 49  ensure that the printed content can be output
                                                                                                     accurately.
int open()                                                        Turn on the printer.
int setFont(String path)                                          Set print font.
int setGray(int gray)                                             Set print grayscale.
int setLineSpace(int line)                                        Set print line space.
int startPrint(ConstantPrinter.PrintFailurePolicy failurePolicy,  Execute print job to print the buffered content
IPrintResultCallback callback)
int startPrint(IPrintResultCallback callback)                     Trigger the printing operation to print out the
                                                                  content in the print cache.
int wrapLine(int lines)                                           Add a blank line to the print cache, which
                                                                  serves the function of line breaking.
int setClearPrintCacheOnPaperOut(boolean isClear)                 Set whether to clear the print cache after
                                                                  a paper-out warning
int setGrayByPercent(ConstantPrinter.GrayPercent percent)         Set print density
ConstantPrinter.GlobalFontSize getGlobalFontSize()                Get the global font size
ConstantPrinter.GrayPercent getGrayByPercent()                    Get the current print density percentage
ConstantPrinter.LineSpaceMultiplier getLineSpaceByMultiplier()    Get line spacing information
int setGlobalFontSize(ConstantPrinter.GlobalFontSize size)        Set the global font size
int setLineSpaceByMultiplier(ConstantPrinter.LineSpaceMultiplier  Set the line spacing
lineSpaceMultiplier)

3.7.1 Open the printer module

Prototype     int open()
Function      Open the printer module
Parameters
Return value  Return:
              0: The operation is successfully executed;
Notes         Others: The operation fails.
              For the specific meaning of the error code, please refer to the definitions in PrinterError and
              CommonError

3.7.2 Get the current status of the printer

Prototype     int getPrinterStatus()
Function      Get the current status of the printer.
Parameters
Return value  Return:
              A negative return value: The operation fails;
Notes         For the specific meaning of the error code, please refer to the definitions in the PrinterError and
              CommonError.
              A positive return value: The operation is successfully executed;
              For the specific meaning of the status code, please refer to the definitions in the ConstantPrint.

                                                                             50

Prototype             int feedPaper(int lines)
Function              It is used to feed paper before starting the printing process.
Parameters            Parameters:
Return value          lines - The number of lines to feed (must be an integer greater than 0).
                      Return:
Notes                 0: The operation is successfully executed;
                      Others: The operation fails.
                      For the specific meaning of the error code, please refer to the definitions in PrinterError and
                      CommonError
                      The main purpose is to adjust the printer's paper position, ensuring accurate print output.
                      Must be used after the printer has been opened.

3.7.4 Set print grayscale

Prototype             int setGray(int gray)
Function              Set print grayscale
Parameters            Parameters:
                      gray - Default: 1200.
Return value          Smaller values make prints lighter; larger values make prints darker. Adjust in steps of 200 for
                      consistent results.
Notes                 Return:
                      0: The operation is successfully executed;
                      Others: The operation fails.
                      For the specific meaning of the error code, please refer to the definitions in PrinterError and
                      CommonError
                      Must be used after the printer has been opened

3.7.5 Set print font

Prototype             int setFont(String path)
Function              Set print font
Parameters            Parameters:
Return value          path - The path to the font resource package.
                      Return:
Notes                 0: The operation is successfully executed;
                      Others: The operation fails.
                      For the specific meaning of the error code, please refer to the definitions in PrinterError and
                      CommonError
                      Must be used after the printer has been opened.

                                           51

Prototype     int setLineSpace(int line)
Function      Set print line space
Parameters    Parameters:
Return value  line - An integer greater than 0.
              Return:
Notes         0: The operation is successfully executed;
              Others: The operation fails.
              For the specific meaning of the error code, please refer to the definitions in PrinterError and
              CommonError
              Must be used after the printer has been opened.

3.7.7 Add the text to the print cache

Prototype     int addText(TextPrintLine textLine)
Function      Add the text to the print cache
Parameters    Parameters:
Return value  textLine - TextPrintLine type(used to define the text content and style for printing).
              Return:
Notes         0: The operation is successfully executed;
              Others: The operation fails.
              For the specific meaning of the error code, please refer to the definitions in PrinterError and
              CommonError
              Must be used after the printer has been opened.

3.7.8 Add a line of text with different styles to the print cache

Prototype     int addText(List<TextPrintLine> textLines)
Function      Add a line of text with different styles to the print cache
Parameters    Parameters:
              textLines - An array of the TextPrintLine type. Recommend to use the TextPrintLineHelper utility
Return value  class to construct the TextPrintLine array. This can simplify the development process and make
              the calls clearer and more straightforward.
Notes         Return:
              0: The operation is successfully executed;
              Others: The operation fails.
              For the specific meaning of the error code, please refer to the definitions in PrinterError and
              CommonError
              Must be used after the printer has been opened.

3.7.9 Add a blank line to the print cache

Prototype     int wrapLine(int lines)
Function      Add a blank line to the print cache, which serves the function of line breaking

                                                                             52
Return value  lines - Number of lines, an integer greater than 0.
              Return:
Notes         0: The operation is successfully executed;
              Others: The operation fails.
              For the specific meaning of the error code, please refer to the definitions in PrinterError and
              CommonError
              Must be used after the printer has been opened.

3.7.10 Add the barcode to the print cache

Prototype     int addBarcode(BarcodePrintLine barcodeLine)
Function      Add the barcode to the print cache
Parameters    Parameters:
              barcodeLine - BarcodePrintLine Type. Used to define the print content, type, size, and style of the
Return value  barcode.
              Return:
Notes         0: The operation is successfully executed;
              Others: The operation fails.
              For the specific meaning of the error code, please refer to the definitions in PrinterError and
              CommonError
              Must be used after the printer has been opened.

3.7.11 Add the bitmap to the print cache

Prototype     int addBitmap(BitmapPrintLine bitmapLine)
Function      Add the bitmap to the print cache
Parameters    Parameters:
Return value  bitmapLine - BitmapPrintLine Type. Used to define the picture to be printed and its style.
              Return:
Notes         0: The operation is successfully executed;
              Others: The operation fails.
              For the specific meaning of the error code, please refer to the definitions in PrinterError and
              CommonError
              Must be used after the printer has been opened.

3.7.12 Trigger the printing operation to print out the content in the print cache

Prototype     int startPrint(ConstantPrinter.PrintFailurePolicy failurePolicy,
Function      IPrintResultCallback callback)
Parameters    Execute print job to print the buffered content
Return value  Parameters:
              failurePolicy - Policy for handling failed prints (how to process remaining tasks after a single print
              failure);
              callback - Callback for monitoring print status.
              Return:

                                                                             53
              Others: The operation fails.
              For the specific meaning of the error code, please refer to the definitions in PrinterError and
              CommonError
              Must be used after the printer has been opened

3.7.13 Trigger the printing operation to print out the content in the print cache

Prototype     int startPrint(IPrintResultCallback callback)
Function      Trigger the printing operation to print out the content in the print cache
Parameters    Parameters:
Return value  callback - Monitor the status callbacks of the printing process.
              Return:
Notes         0: The operation is successfully executed;
              Others: The operation fails.
              For the specific meaning of the error code, please refer to the definitions in PrinterError and
              CommonError
              Must be used after the printer has been opened.

3.7.14 Turn off the printer

Prototype     void close()
Function      Turn off the printer
Parameters
Return value  Turn off the printer and release related resources after the printing operation is completed.
Notes

3.7.15 Configure whether to clear print cache after paper-out warning

Prototype     int setClearPrintCacheOnPaperOut(boolean isClear)
Function      Configure whether to clear print cache after paper-out warning
Parameters    Parameters:
              isClear -
Return Value  · true: Warning pops up only once. After clicking confirm, it will not show again. Print cache is
Notes         cleared. (Default behavior, persists after reboot)
              · false: Warning persists until the paper-out condition is resolved. After the warning closes,
              printing resumes without clearing the cached data.
              Return:
              0 - Operation succeeded
              Others - Operation failed. Refer to PrinterError and CommonError for error details
              Only applies to paper-out warnings; does not affect high/low temperature alerts.

3.7.16 Set printer gray level by percentage

Prototype     int setGrayByPercent(ConstantPrinter.GrayPercent percent)
Function      Set printer gray level by percentage

                                                                             54
Return Value  percent - Gray level percentage (see ConstantPrinter.GrayPercent)
              Return:
Notes         0 - Success
              Others - Failure (see PrinterError / CommonError)
              Adjusts the print density using predefined percentage levels

3.7.17 Get current printer gray level percentage

Prototype     ConstantPrinter.GrayPercent getGrayByPercent()
Function      Get current printer gray level percentage
Parameters
Return Value  Return:
              Gray level percentage (GrayPercent enum)
Notes         Retrieves the current print density setting

3.7.18 Set global font size for printing

Prototype     int setGlobalFontSize(ConstantPrinter.GlobalFontSize size)
Function      Set global font size for printing
Parameters    Parameters:
Return Value  size - Font size (see ConstantPrinter.GlobalFontSize)
              Return:
Notes         0 - Success
              Others - Failure (see PrinterError / CommonError)
              Sets the default font size used in all printing operations

3.7.19 Get current global font size

Prototype     ConstantPrinter.GlobalFontSize getGlobalFontSize()
Function      Get current global font size
Parameters
Return Value  Return:Font size (GlobalFontSize enum)
Notes         Returns the currently applied global font size

3.7.20 Set line spacing multiplier for printing

Prototype     int setLineSpaceByMultiplier(ConstantPrinter.LineSpaceMultiplier lineSpaceMultiplier)
Function      Set line spacing multiplier for printing
Parameters    Parameters:
Return Value  lineSpaceMultiplier - Line spacing setting (see LineSpaceMultiplier enum)
              Return:
Notes         0 - Success
              Others - Failure (see PrinterError / CommonError)
              Adjusts the vertical spacing between printed lines

                                                  55

Prototype     ConstantPrinter.LineSpaceMultiplier getLineSpaceByMultiplier()
Function      Get current line spacing multiplier
Parameters
Return Value  Return:
              Line spacing multiplier (LineSpaceMultiplier enum)
Notes         Retrieves the current line spacing configuration

-- Print result callback - IPrintResultCallback --

void onFinish()                                 Callback when the printing finishes successfully.
void onError(int error, String msg)             Callback when an error occurs during the printing process.

3.7.22 Callback when the printing finishes successfully

Prototype     void onFinish()
Function      Callback when the printing finishes successfully
Parameters
Return value  Developers can handle the post - printing - success logic in this method, such as releasing
Notes         resources, updating the interface status, and closing the printer using the close method.

3.7.23 Callback when an error occurs during the printing process

Prototype     void onError(int error,String msg)
Function      Callback when an error occurs during the printing process
Parameters    Parameters:
              error - Error code. Refer to PrinterError.
Return value  msg - Error message.
Notes
              When receiving the PRINTER_ERROR_PRINT error type, you can try closing the printer first,
              then reopening it and retrying.

