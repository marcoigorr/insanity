# Insanity
Program that reads text from screen and gives answer based on 75 if else :)

Check **Realeases** to install Insanity -> [**Here**](https://github.com/marcoigorr/insanity/releases)

If you know you know
## Usage
    
- press **'z'** to get the answer window when you have on screen the question.

- press **'x'** to close dialogue.

## Requirements for working on source code

To make sure that the script works correctly, you must dowload Tesseract-OCT binary and move it in the directory with main.pyw
 
- GitHub Page: https://github.com/tesseract-ocr/tesseract
  
- Download here: https://github.com/UB-Mannheim/tesseract/wiki

Then add this line of code:

    pytesseract.pytesseract.tesseract_cmd = '.\\Tesseract-OCR\\tesseract.exe'
  
