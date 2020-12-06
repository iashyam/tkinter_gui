#Python GUI lecture 3
#Creating Buttons
#2nd Dec 2020

from tkinter import *
root = Tk()

#giving action to button
def click():
    result = Label(root, text = "Good Morning, Shyam!")
    result.pack()

#creating a button
label = Label(root, text = "Is your name Shyam?")
click = Button(root, text="Yes", command= click, bg = "blue", fg = '#ffffff', padx =5)

label.pack()
click.pack()

root.mainloop()