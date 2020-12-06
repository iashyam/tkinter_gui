from tkinter import *
root = Tk()

var = StringVar()
a = ['Kohli', 'Smith', 'Root', 'Kane']
menu = OptionMenu(root, var, *a)
var.set(a[0])
menu.pack()
root.mainloop()