#Python GUI Lecture No 6u
#Diffrent types of message boxes
#04-12-2020 08:23

from tkinter import *
from tkinter import messagebox

root = Tk()

def info():
    messagebox.showinfo(title="info", message="this is an info")
def error():
    messagebox.showerror(title="Error",message="You are chutiya!")
def que():
    messagebox.askquestion(title="Question", message="Are you a chutiya?")
def warn():
    messagebox.showwarning(title='Warning',message="Chutiyas can't see this!")

Button(root, text='info', command= info).pack()
Button(root, text='error', command= error).pack()
Button(root, text='que', command= que).pack()
Button(root, text='warn', command= warn).pack()


root.mainloop()