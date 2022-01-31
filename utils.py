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
    "What is the prefix length notation for the subnet mask 255.255.255.224",
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

# Yanderedev momentum
def giveAnswer(text):
    if getQuestion(1) in text:
        createWindow("/27")

    else:
        createWindow("No answer or question found")