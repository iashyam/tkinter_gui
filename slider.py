from tkinter import *

class window:
    def __init__(self):
        window = Tk()
        window.title('Slider')
        window.geometry('400x400')

        self.slider = Scale(window,from_=0, to=200)
        self.slider.pack()
        self.slider.bind('<Button-1>',tick)
        
        window.mainloop()

def tick(self, event , *args):
    label = Label(window,text=f"Slider value = ")
    label.pack()
    label.config(text=str(self.slider.get()))
    print(event.x)
    label.after(100)
    label.update()
window()