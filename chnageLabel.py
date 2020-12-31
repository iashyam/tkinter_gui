#28-12-2030
from tkinter import *

class changelabel:
    def __init__(self):
        window = Tk()
        window.title("Change Label")
        window.iconbitmap("iiii.ico")

        frame1 = LabelFrame(window)
        frame1.pack()

        self.lbl = Label(frame1, text="Welcome to Python!", font="98")
        self.lbl.pack()

        frame2 = LabelFrame(window)
        frame2.pack()
        self.text = StringVar()
        text_entry = Entry(frame2, textvariable= self.text)
        text_entry.config(bg='red',fg='white')
        btn  = Button(frame2, text = "Change", command = self.change)
        self.color = IntVar()
        blue  = Radiobutton(frame2, text="Blue",variable=self.color,value=1,command=self.changeColour)
        red  = Radiobutton(frame2, text="Red",variable=self.color,value=2,command=self.changeColour)
        text_entry.pack()
        btn.pack()
        blue.pack()
        red.pack()

        self.hi = Text()
        self.hi.pack()

        self.hi.insert(END, "Programming is fun!")
        self.hi["bg"] = 'blue'
        self.hi["fg"] = "white"

        window.mainloop()

    def change(self):
        self.lbl["text"] = self.text.get()

    def changeColour(self):
        if self.color.get() == 1:
            self.lbl['fg'] = 'blue'
            self.hi['bg'] = 'blue'
        elif self.color.get() == 2:
            self.lbl['fg'] = 'red'
            self.hi['bg'] = 'red'

changelabel()