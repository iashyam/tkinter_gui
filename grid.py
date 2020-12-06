#Python GUI lecture 2
#Positioning with grid

from tkinter import *
root = Tk()
myLabel = Label(root, text = "Welcome to tkinter")
myName = Label(root, text = "My Name is Shyam!")
myCollege = Label(root, text = "St. Stephen's College")
myLabel2 = Label(root, text= "You are  a programmer!")
myLabel.grid(row = 0, column = 0)
myName.grid(row = 0, column = 1)
myCollege.grid(row=1, column= 2)
myLabel2.grid(row=1, column = 1)
root.mainloop()
