import time
import cv2
import mss
import numpy
import pytesseract
import keyboard
import webbrowser
import os
import webview


question_list = [
    "pisciati",
    "Which action is performed by a client when establishing communication with a server via the use of UDP at the transport layer",
    ]

def getQuestion(index):
    return question_list[index].lower().replace(" ", "")

def destroy(window):
    time.sleep(5)
    try:
        window.destroy()
    except:
        print("Window already closed")

def createWindow(answer):
    f = open("text.txt", "a+")
    f.write(answer)
    f.close()
    window = webview.create_window(answer, 'text.txt', width=100, height=50, y=1080)
    webview.start(destroy, window)
    time.sleep(0.3)
    os.remove("text.txt")

# +----------------------------------------------------------------+
# +---------------------- Yanderedev momentum ---------------------+
# +----------------------------------------------------------------+

def giveAnswer(text):
    if getQuestion(1) in text:
        createWindow("The client randomly selects a source port number.")

    else:
        createWindow("No answer or question found")