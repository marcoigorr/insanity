
import mss
import numpy
import pytesseract
import keyboard
from utils import giveAnswer

def main():
    
    with mss.mss() as sct:
        while True:
            if keyboard.read_key() == 'z':

                im = numpy.asarray(sct.grab(mon))
                # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

                text = pytesseract.image_to_string(im)
                # cv2.imshow('Image', im)

                text = text.replace("\n", " ")
                text = text.replace(" ", "")
                text = text.lower()            

                giveAnswer(text)
            else:
                pass

if __name__ == "__main__":

    pytesseract.pytesseract.tesseract_cmd = '.\\Tesseract-OCR\\tesseract.exe'

    # Screen capture settings
    mon = {'top': 100, 'left': 0, 'width': 1920, 'height': 600}

    # Answer file creation
    open('text.txt', 'w')

    main()
