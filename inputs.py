#Python GUI Lecture 3
#taking inputs from user
#2nd Dec 2020, 9:54

from tkinter import *

root = Tk()
#taking the entry from user
label = Label(root, text = "Enter Your Name: ", pady = 10)
name = Entry(root)
name.insert(0, "Name")
space = Label(root, text = "          ")
label.pack()
name.pack()
space.pack()

#definign a button
def greet():
    hello = "Hello  "
    label = Label(root, text = hello + name.get())
    label.pack()

button = Button(root, text = "Submit", command = greet)
button.pack()
root.mainloop()