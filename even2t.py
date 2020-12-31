from tkinter import *

class event:
    def __init__(self):
        window = Tk()
        window.geometry('400x200')

        self.canvas = Canvas(window, height=200, width=400)
        self.canvas.pack(fill=BOTH, expand=1)

        self.canvas.bind("<Button-1>", self.event1)

        window.mainloop()
    
    def event1(self, event):
        
        dx = 3
        dy = 3
        x = event.x
        y = event.y
        self.canvas.create_text(x,y, text='Happy New Year',font='Times 26', tags='text')
        while True:
            self.canvas.move('text', dx, dy)
            self.canvas.after(100)
            self.canvas.update()
            

if __name__ == "__main__":
    event()