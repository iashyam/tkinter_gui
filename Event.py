from tkinter import *

class Event:
    def __init__(self):

        self.color = 'yellow'

        window = Tk()
        window.title("Event Demo")
        window.iconbitmap('iiii.ico')

        self.canvas = Canvas(window, width=400, height=400)
        self.canvas.pack(fill = BOTH, expand=1)

        menu = Menu(window)
        window.config(menu=menu)
        menu.add_command(label='Red', command=self.redCircle)
        menu.add_command(label='Blue', command=self.blueCircle)
        menu.add_command(label='Green', command=self.greenCircle)
        menu.add_command(label='Clear', command=self.clear)

        self.canvas.bind('<Button-1>', self.drawcircle)

        window.mainloop()


    def redCircle(self):
        self.color = 'Red'

    def blueCircle(self):
        self.color = 'Blue'
    def greenCircle(self):
        self.color = 'green'


    def drawcircle(self,event):
        self.canvas.create_rectangle(event.x,event.y, event.x_root+20, event.y_root+20, fill=self.color, tags='one')

    def clear(self):
        self.canvas.delete('one')

if __name__ == '__main__':
    Event()