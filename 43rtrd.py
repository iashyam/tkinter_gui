from tkinter import *
from PIL import Image, ImageTk
class images:
    def __init__(self):
        window = Tk()

        self.img  = ImageTk.PhotoImage(Image.open('pexels-luis-gomes-546819.jpg'))
        canvas = Canvas(window,width=500, height=500)
        canvas.pack()

        canvas.create_image(250,250,image = self.img)

        window.mainloop()
images()