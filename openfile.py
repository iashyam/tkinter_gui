#python GUI lecture 8
#creating Open file dialouge box
#04-12-2020 12:43

from tkinter import *
from tkinter import filedialog

root = Tk()

def upload():
    global file
    root.file = filedialog.askopenfilename(initialdir="D:\Tkinter_gui")
    file = root.file

def open():
    f = open(file, 'r')

button = Button(root, text="Upload File", command=upload).pack()
button = Button(root, text = "Open File", command = open).pack()

root.mainloop()