import keyboard
from threading import Thread
from utils import getAnswer, getScrText
from tkinter import *


def createWindow(root):     
    # Get answer
    answer = getAnswer(getScrText())

    # Window width x height + right + down
    root.geometry("300x80+300+1050")

    # This line modify opacity of the window
    root.attributes('-alpha', 1)

    # Window title
    root.title(answer)   

    # Content
    lbl=Label(root, text=answer)
    lbl.place(x=5, y=5)

    # Status of the window: set to icon, it is minimized
    root.state(newstate='iconic')

    # Invisible icon, check 
    try:
        root.iconbitmap('./icon.ico')
    except:
        pass
    
    # Start window loop
    root.mainloop()

def closeWindow():
    while True:
        if keyboard.read_key() == 'x':            
            print("Pressed X")       
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
            print("Pressed Z")

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
