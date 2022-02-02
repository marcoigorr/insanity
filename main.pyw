import keyboard, time, os, sys
from threading import Thread
from utils import getAnswer, getScrText
from tkinter import *
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt



def createWindow(root):     

    root.geometry("250x50")

    root.title("TkWindow")
           
    answer = getAnswer(getScrText())

    lbl=Label(root, text=answer)
    lbl.place(x=5, y=5)

    root.mainloop()

def closeWindow():
    while True:
        if keyboard.read_key() == 'x':            
            # print("Pressed X")       
            try:                             
                root.quit()
                root.withdraw()
            except:
                pass
        else:
            pass

def main():
    while True:
        if keyboard.read_key() == 'z':
            # print("Pressed Z")

            global root
            root = Tk()
            createWindow(root)
        else:
            pass

# -------------------- main --------------------
if __name__ == "__main__":
       
    # Defining 2 threads to run symultaneousley, the window and the colse window function
    t1 = Thread(target = main)
    t2 = Thread(target = closeWindow)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()

    t1.join()
    t2.join()
