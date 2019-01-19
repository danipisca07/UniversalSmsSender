from tkinter import *
import time
import subprocess
import os


def sendMessages():
    message = text.get("1.0", END)
    os.system(f"pipenv run python bulkSend.py \"{message}\"")


root = Tk()  # basic window

topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# topFrame content
label = Label(topFrame, text='Message: ')
text = Text(topFrame, width=150, height=15)
label.pack(side=LEFT)
text.pack(side=RIGHT)

# bottomFrame content
button = Button(bottomFrame, text="Send Messages", command=sendMessages)
button.pack()

root.mainloop()  # keep the window open even once it's rendered (it keeps in loop)
