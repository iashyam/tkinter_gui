from math import pi, sin, cos,tan, atan
import time

from tkinter import *

class event:
    def __init__(self):
        window = Tk()

        

        self.canas = Canvas(window, width=400, height=400,bg='white')
        self.canas.pack()

        self.canas.create_oval(20,20,380,380,width=2,tags="circle")
        self.canas.create_line(200,30,200,200,arrow=FIRST,width=4, tags ='line')

        while True:

            self.radius = 170
            self.x = 200
            self.y = 30

            if (self.y-30) == 0:
                self.theta = 0
            else:
                self.theta = atan((self.x - 200)/(self.y-30))

            self.d_thetha = pi/60
            dx = self.radius*cos(self.theta+self.d_thetha)
            dy = self.radius*sin(self.theta+self.d_thetha)

            # self.canas.delete("line")
            # time.sleep(100)
            self.canas.create_line(self.x,self.y,200,200,arrow=FIRST,width=4, tags ='line')
            
            self.x += dx
            self.y += dy

        window.mainloop()

if __name__ == "__main__":
    event()