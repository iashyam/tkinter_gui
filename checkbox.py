from tkinter import *
root = Tk()

var = StringVar()

c = Checkbutton(root, text = "This is a checkbox", variable= var,onvalue='checked', offvalue='unchecked').pack()
def button():
    label = Label(root, text = var.get()).pack()
button = Button(root, text="See the result", command=button).pack()

root.mainloop()