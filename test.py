#Python GUI Lecture no. 4
#inserting icon and images
#02-12-2020 15:21

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Shyam's Window")
root.iconbitmap('D:\Tkinter_gui\icon.ico')
root.geometry("40x40")

simi = ImageTk.PhotoImage(Image.open('simi_chahal.jpg'))
label = Label(image = simi)
label.grid(row=0,column=0,columnspan=3)
back_button = Button(root, text = '>>')
fore_button = Button(root, text = '<<')
exit = Button(root, text='Exit', command=root.quit())
back_button.grid(row=1,column=0)
fore_button.grid(row=1,column=3)
exit.grid(row=1,column=2)


root.mainloop()
