import time
import cv2
import mss
import numpy
import pytesseract
import keyboard
import webbrowser
import os
import subprocess


def giveAnswer(text):


    if "What is the prefix length notation for the subnet mask 255.255.255.224?" in text:
        f = open("text.txt", "a+") # Create txt file
        f.write("/27") # Answer
        f.close()
        webbrowser.open("text.txt") # Open Notepad Window
        time.sleep(1)
        os.remove("text.txt") # Remove file

    elif "How many valid host addresses are available on an IPv4 subnet that is" in text:
        f = open("text.txt", "a+")
        f.write("62")
        f.close()
        webbrowser.open("text.txt")
        time.sleep(1)
        os.remove("text.txt")

    else:
        print("No answer or question found.")


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

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

