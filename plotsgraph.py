from tkinter import *
from math import sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class graphs:
    def __init__(self):
        self.root = Tk()
        self.root.title("Displayig graphs")



        btn = Button(self.root, text="Graph", command=self.graph)
        btn.pack()


        self.root.mainloop()

    def graph(self):
        self.new = Toplevel()

        figure = Figure(figsize=(2,2), dpi=200)

        x =   [-1*i for i in range(100, 0 , -1)] + [i for i in range(100)]
        y = [sin(pi*i/40)**2 for i in x]

        plot1 = figure.add_subplot(111)
        plot1.plot(x,y)
        plot1.set_yticklabels([])
        plot1.set_xticklabels([])

        canvs = FigureCanvasTkAgg(figure, master=self.new)
        canvs.draw()
        canvs.get_tk_widget().pack(fill=BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvs,self.new)
        toolbar.update()
        canvs.get_tk_widget().pack(fill=BOTH, expand=True)





if __name__ == '__main__':
    graphs()