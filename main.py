import time
import cv2
import mss
import numpy
import pytesseract
import keyboard
import webbrowser
import os
import subprocess
import webview


def createWindow(answer):
    f = open("text.txt", "a+")
    f.write(answer)
    f.close()
    window = webview.create_window(answer, 'text.txt', width=100, height=50, )
    webview.start()
    time.sleep(1)
    os.remove("text.txt")

# Yanderedev momentum
def giveAnswer(text):
    if "What is the prefix length notation for the subnet mask 255.255.255.224?" in text:
        createWindow("/27") # Answer

    elif "How many valid host addresses are available on an IPv4 subnet that is" in text:
        createWindow("62")

    elif "Which subnet mask would be used if 5 host bits are available?" in text:
        createWindow("255.255.255.224")

    elif "A network administrator subnets the 192.168.10.0/24 network into subnets with /26" in text:
        createWindow("4")

    else:
        createWindow("No answer or question found")

# Importazione Pytesseract esterno; da sistemare
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Dimensione della cattura
mon = {'top': 10, 'left': 0, 'width': 1920, 'height': 600}

with mss.mss() as sct:
    while True:
        if keyboard.read_key() == 'ì':

            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

            text = pytesseract.image_to_string(im)
            # cv2.imshow('Image', im)

            giveAnswer(text)

            # Press "0" to quit
            if cv2.waitKey(25) & 0xFF == ord('0'):
                cv2.destroyAllWindows()
                break
