import time
import cv2
import mss
import numpy
import pytesseract
import keyboard

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

mon = {'top': 10, 'left': 0, 'width': 1700, 'height': 500}

with mss.mss() as sct:
    while True:
        if keyboard.read_key() == 'ì':

            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

            text = pytesseract.image_to_string(im)
            print(text)

            # cv2.imshow('Image', im)

            # Press "0" to quit
            if cv2.waitKey(25) & 0xFF == ord('0'):
                cv2.destroyAllWindows()
                break
