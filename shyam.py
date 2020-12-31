from tkinter import *
from PIL import Image, ImageTk

class scroller:
    def __init__(self):
        window = Tk()
        window.title("Scroller")
        window.geometry('500x300')
        scroler = Scrollbar(window, bg='green')
        scroler.pack(side=LEFT, fill=Y)

        self.canvas = Canvas(window, width = 400, height=300, bg='blue',yscrollcommand=scroler.set)
        self.canvas.pack()

        self.img = ImageTk.PhotoImage(Image.open('image.jpg'))


        self.canvas.create_oval(20,20, 480,480, fill = 'red', tags='oval')
        scroler.config(command=self.canvas.yview)

        window,mainloop()

if __name__ == '__main__':
    scroller()