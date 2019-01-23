from tkinter import Tk, Frame, Label, Text, Button, END, TOP, BOTTOM, LEFT, RIGHT
import os


def sendMessages():
    message = text.get("1.0", END)
    os.system(f"pipenv run python bulkSend.py \"{message}\"")


def extractNumbers():
    xlsxFile = filePath.get("1.0", END).strip()
    os.system(f"pipenv run python xlsxToNumPy.py \"{xlsxFile}\" 39")


root = Tk()  # basic window

topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# topFrame content
label1 = Label(topFrame, text='XLSX file path: ', width=16)
filePath = Text(topFrame, width=120, height=1)
filePath.insert(END, "numbers.xlsx")
label1.pack(side=LEFT)
button1 = Button(topFrame, text="Extract numbers", command=extractNumbers)
button1.pack(side=RIGHT)
filePath.pack(side=RIGHT)

# bottomFrame content
label2 = Label(bottomFrame, text='Message: ', width=16)
text = Text(bottomFrame, width=120, height=15)
label2.pack(side=LEFT)
button2 = Button(bottomFrame, text="Send Messages", command=sendMessages)
button2.pack(side=RIGHT)
text.pack(side=RIGHT)


root.mainloop()  # keep the window open even once it's rendered (it keeps in loop)
