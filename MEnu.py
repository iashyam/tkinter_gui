from tkinter import *

root = Tk()
root.title("Menu")
menubar = Menu(root)
root.config(menu=menubar)

def this():
    pass

file = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=file)
file.add_command(label='New', command=this)
file.add_command(label='New Window', command=this)
file.add_command(label='Open...', command=this)
file.add_command(label='Save', command=this)
file.add_command(label='Save AS...', command=this)
file.add_separator()
file.add_command(label='Page Setup', command=this)
file.add_command(label='Print', command=this)
file.add_separator()
file.add_command(label='Exit', command=root.quit)

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label='Undo', command=this)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', command=this)
edit_menu.add_command(label='Copy', command=this)
edit_menu.add_command(label='Paste', command=this)
edit_menu.add_separator()
edit_menu.add_command(label='Find', command=this)
edit_menu.add_command(label='Find and Replace', command=this)
edit_menu.add_command(label='Delete', command=this)


text = Text()
text.config(font='Times 16 bold')
text.pack()
root.mainloop()