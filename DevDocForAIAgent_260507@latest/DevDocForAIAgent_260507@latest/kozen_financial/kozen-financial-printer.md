---
title: "kozen-financial-printer"
source: "KOZEN Financial SDK Development Documentation _260428.docx"
type: "api_doc"
company: "kozen"
status: "stable"
confidence: "high"
tags:
  - api_doc
  - printer
summary: "Defines Kozen Financial SDK Printer module APIs for print operations including open/close, feed, font/line-space/brightness settings, text/barcode/bitmap cache, start print with failure policy, and IPrintResultCallback (onFinish, onError)."
created: "2026-04-30"
updated: "2026-04-30"
related:
  - "kozen-financial-overview"
  - "kozen-financial-init"
---

## Overview

Printer operation module providing thermal printing via IPrinterManager from FinancialEngine.INSTANCE.getPrinterManager() or FinancialEngine.printerManager().

## Function List

| Function Name | Description |
|--            |-----------|
| int open() | Open the printer module |
| int getPrinterStatus() | Get the current status of the printer. |
| int feedPaper(int lines) | It is used to feed paper before starting the printing process. |
| int setGray(int gray) | Set print grayscale |
| int setFont(String path) | Set print font |
| int setLineSpace(int line) | Set print line space |
| int addText(TextPrintLine textLine) | Add the text to the print cache |
| int addText(List<TextPrintLine> textLines) | Add a line of text with different styles to the print cache |
| int wrapLine(int lines) | Add a blank line to the print cache, which serves the function of line breaking |
| int addBarcode(BarcodePrintLine barcodeLine) | Add the barcode to the print cache |
| int addBitmap(BitmapPrintLine bitmapLine) | Add the bitmap to the print cache |
| int startPrint(ConstantPrinter.PrintFailurePolicy failurePolicy,  IPrintResultCallback callback) | Execute print job to print the buffered content |
| int startPrint(IPrintResultCallback callback) | Trigger the printing operation to print out the content in the print cache |
| void close() | Turn off the printer |
| int setClearPrintCacheOnPaperOut(boolean isClear) | Configure whether to clear print cache after paper-out warning |
| int setGrayByPercent(ConstantPrinter.GrayPercent percent) | Set printer gray level by percentage |
| ConstantPrinter.GrayPercent getGrayByPercent() | Get current printer gray level percentage |
| int setGlobalFontSize(ConstantPrinter.GlobalFontSize size) | Set global font size for printing |
| ConstantPrinter.GlobalFontSize getGlobalFontSize() | Get current global font size |
| int setLineSpaceByMultiplier(ConstantPrinter.LineSpaceMultiplier lineSpaceMultiplier) | Set line spacing multiplier for printing |
| ConstantPrinter.LineSpaceMultiplier getLineSpaceByMultiplier() | Get current line spacing multiplier |
| IPrintResultCallback | IPrintResultCallback |
| void onFinish() | Callback when the printing finishes successfully |
| void onError(int error,String msg) | Callback when an error occurs during the printing process |

## Details

### open

| Prototype    | Prototype int open() |
| ------------ | --- |
| Function     | Function Open the printer module |
| Parameters   | Parameters  |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes  |

### getPrinterStatus

| Prototype    | Prototype int getPrinterStatus() |
| ------------ | --- |
| Function     | Function Get the current status of the printer. |
| Parameters   | Parameters  |
| Return Value | Return value Return: A negative return value: The operation fails; For the specific meaning of the error code, please refer to the definitions in the PrinterError and CommonError. A positive return value: The operation is successfully executed; For the specific meaning of the status code, please refer to the definitions in the ConstantPrint. |
| Notes        | Notes  |

### feedPaper

| Prototype    | Prototype int feedPaper(int lines) |
| ------------ | --- |
| Function     | Function It is used to feed paper before starting the printing process. |
| Parameters   | Parameters Parameters: lines - The number of lines to feed (must be an integer greater than 0). |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes The main purpose is to adjust the printer's paper position, ensuring accurate print output.  Must be used after the printer has been opened. |

### setGray

| Prototype    | Prototype int setGray(int gray) |
| ------------ | --- |
| Function     | Function Set print grayscale |
| Parameters   | Parameters Parameters: gray - Default: 1200.  Smaller values make prints lighter; larger values make prints darker. Adjust in steps of 200 for consistent results. |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes Must be used after the printer has been opened |

### setFont

| Prototype    | Prototype int setFont(String path) |
| ------------ | --- |
| Function     | Function Set print font |
| Parameters   | Parameters Parameters: path - The path to the font resource package. |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes Must be used after the printer has been opened. |

### setLineSpace

| Prototype    | Prototype int setLineSpace(int line) |
| ------------ | --- |
| Function     | Function Set print line space |
| Parameters   | Parameters Parameters: line - An integer greater than 0. |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes Must be used after the printer has been opened. |

### addText

| Prototype    | Prototype int addText(TextPrintLine textLine) |
| ------------ | --- |
| Function     | Function Add the text to the print cache |
| Parameters   | Parameters Parameters: textLine - TextPrintLine type(used to define the text content and style for printing). |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes Must be used after the printer has been opened. |

### addText (list)

| Prototype    | Prototype int addText(List<TextPrintLine> textLines) |
| ------------ | --- |
| Function     | Function Add a line of text with different styles to the print cache |
| Parameters   | Parameters Parameters: textLines - An array of the TextPrintLine type. Recommend to use the TextPrintLineHelper utility class to construct the TextPrintLine array. This can simplify the development process and make the calls clearer and more straightforward. |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes Must be used after the printer has been opened. |

### wrapLine

| Prototype    | Prototype int wrapLine(int lines) |
| ------------ | --- |
| Function     | Function Add a blank line to the print cache, which serves the function of line breaking |
| Parameters   | Parameters Parameters: lines - Number of lines, an integer greater than 0. |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes Must be used after the printer has been opened. |

### addBarcode

| Prototype    | Prototype int addBarcode(BarcodePrintLine barcodeLine) |
| ------------ | --- |
| Function     | Function Add the barcode to the print cache |
| Parameters   | Parameters Parameters: barcodeLine - BarcodePrintLine Type. Used to define the print content, type, size, and style of the barcode. |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes Must be used after the printer has been opened. |

### addBitmap

| Prototype    | Prototype int addBitmap(BitmapPrintLine bitmapLine) |
| ------------ | --- |
| Function     | Function Add the bitmap to the print cache |
| Parameters   | Parameters Parameters: bitmapLine - BitmapPrintLine Type. Used to define the picture to be printed and its style. |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes Must be used after the printer has been opened. |

### startPrint (with policy)

| Prototype    | Prototype int startPrint(ConstantPrinter.PrintFailurePolicy failurePolicy,  IPrintResultCallback callback) |
| ------------ | --- |
| Function     | Function Execute print job to print the buffered content |
| Parameters   | Parameters Parameters: failurePolicy - Policy for handling failed prints (how to process remaining tasks after a single print failure); callback - Callback for monitoring print status. |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes Must be used after the printer has been opened |

### startPrint (plain)

| Prototype    | Prototype int startPrint(IPrintResultCallback callback) |
| ------------ | --- |
| Function     | Function Trigger the printing operation to print out the content in the print cache |
| Parameters   | Parameters Parameters: callback - Monitor the status callbacks of the printing process. |
| Return Value | Return value Return: 0: The operation is successfully executed;  Others: The operation fails.  For the specific meaning of the error code, please refer to the definitions in PrinterError and CommonError |
| Notes        | Notes Must be used after the printer has been opened. |

### close

| Prototype    | Prototype void close() |
| ------------ | --- |
| Function     | Function Turn off the printer |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes Turn off the printer and release related resources after the printing operation is completed. |

### setClearPrintCacheOnPaperOut

| Prototype    | Prototype int setClearPrintCacheOnPaperOut(boolean isClear) |
| ------------ | --- |
| Function     | Function Configure whether to clear print cache after paper-out warning |
| Parameters   | Parameters Parameters: isClear -  • true: Warning pops up only once. After clicking confirm, it will not show again. Print cache is cleared. (Default behavior, persists after reboot) • false: Warning persists until the paper-out condition is resolved. After the warning closes, printing resumes without clearing the cached data. |
| Return Value | Return Value Return: 0 - Operation succeeded Others - Operation failed. Refer to PrinterError and CommonError for error details |
| Notes        | Notes Only applies to paper-out warnings; does not affect high/low temperature alerts. |

### setGrayByPercent

| Prototype    | Prototype int setGrayByPercent(ConstantPrinter.GrayPercent percent) |
| ------------ | --- |
| Function     | Function Set printer gray level by percentage |
| Parameters   | Parameters Parameters: percent - Gray level percentage (see ConstantPrinter.GrayPercent) |
| Return Value | Return Value Return: 0 - Success Others - Failure (see PrinterError / CommonError) |
| Notes        | Notes Adjusts the print density using predefined percentage levels |

### getGrayByPercent

| Prototype    | Prototype ConstantPrinter.GrayPercent getGrayByPercent() |
| ------------ | --- |
| Function     | Function Get current printer gray level percentage |
| Parameters   | Parameters  |
| Return Value | Return Value Return: Gray level percentage (GrayPercent enum) |
| Notes        | Notes Retrieves the current print density setting |

### setGlobalFontSize

| Prototype    | Prototype int setGlobalFontSize(ConstantPrinter.GlobalFontSize size) |
| ------------ | --- |
| Function     | Function Set global font size for printing |
| Parameters   | Parameters Parameters: size - Font size (see ConstantPrinter.GlobalFontSize) |
| Return Value | Return Value Return: 0 - Success Others - Failure (see PrinterError / CommonError) |
| Notes        | Notes Sets the default font size used in all printing operations |

### getGlobalFontSize

| Prototype    | Prototype ConstantPrinter.GlobalFontSize getGlobalFontSize() |
| ------------ | --- |
| Function     | Function Get current global font size |
| Parameters   | Parameters  |
| Return Value | Return Value Return:Font size (GlobalFontSize enum) |
| Notes        | Notes Returns the currently applied global font size |

### setLineSpaceByMultiplier

| Prototype    | Prototype int setLineSpaceByMultiplier(ConstantPrinter.LineSpaceMultiplier lineSpaceMultiplier) |
| ------------ | --- |
| Function     | Function Set line spacing multiplier for printing |
| Parameters   | Parameters Parameters: lineSpaceMultiplier - Line spacing setting (see LineSpaceMultiplier enum) |
| Return Value | Return Value Return: 0 - Success Others - Failure (see PrinterError / CommonError) |
| Notes        | Notes Adjusts the vertical spacing between printed lines |

### getLineSpaceByMultiplier

| Prototype    | Prototype ConstantPrinter.LineSpaceMultiplier getLineSpaceByMultiplier() |
| ------------ | --- |
| Function     | Function Get current line spacing multiplier |
| Parameters   | Parameters  |
| Return Value | Return Value Return: Line spacing multiplier (LineSpaceMultiplier enum) |
| Notes        | Notes Retrieves the current line spacing configuration |

### IPrintResultCallback

### onFinish

| Prototype    | Prototype void onFinish() |
| ------------ | --- |
| Function     | Function Callback when the printing finishes successfully |
| Parameters   | Parameters  |
| Return Value | Return value  |
| Notes        | Notes Developers can handle the post - printing - success logic in this method, such as releasing resources, updating the interface status, and closing the printer using the close method. |

### onError

| Prototype    | Prototype void onError(int error,String msg) |
| ------------ | --- |
| Function     | Function Callback when an error occurs during the printing process |
| Parameters   | Parameters Parameters: error - Error code. Refer to PrinterError. msg - Error message. |
| Return Value | Return value  |
| Notes        | Notes When receiving the PRINTER_ERROR_PRINT error type, you can try closing the printer first, then reopening it and retrying. |

## Notes

No additional notes.

## Related Links

- [[kozen-financial-overview]]
- [[kozen-financial-init]]
