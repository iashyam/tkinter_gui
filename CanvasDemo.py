from tkinter import *
class CanvasDemo:
    def __init__(self):
        window = Tk()
        window.title("Canvas Demo")
        window.iconbitmap("iiii.ico")

        self.canvas = Canvas(window, width=350, height=350, bg='white')
        self.canvas.pack()

        frame= LabelFrame(window)
        frame.pack()

        btrac = Button(frame, text="Ractangle",command=self.displayRac)
        btoval = Button(frame, text="Oval",command=self.displayOval)
        Arc = Button(frame, text="Arc",command=self.Arc)
        Polygon = Button(frame, text="Polygon",command=self.Polygon)
        Line = Button(frame, text="Line",command=self.Line)
        String = Button(frame, text="String",command=self.String)
        Clear = Button(frame, text="Clear", command=self.clear)
        exit = Button(frame,text="Exit",command=window.quit)

        btrac.grid(row=0,column=0)
        btoval.grid(row=0,column=1)
        Arc.grid(row=0,column=2)
        Polygon.grid(row=0,column=3)
        Line.grid(row=0,column=4)
        String.grid(row=0,column=5)
        Clear.grid(row=0,column=6)
        exit.grid(row=0,column=7)

        window.mainloop()

    def displayRac(self):
        self.canvas.delete("rac",'oval','arc','polygon','lines','string')
        self.canvas.create_rectangle(20, 20 , 90, 100,fill='red', tags='rac')

    def displayOval(self):
        self.canvas.delete("rac",'oval','arc','polygon','lines','string')
        self.canvas.create_oval(20,20,90,100, fill="blue", tags='oval')

    def Arc(self):
        self.canvas.delete("rac",'oval','arc','polygon','lines','string')
        self.canvas.create_arc(20,20,90,100,start=0, extent=90, width=5,fill='yellow', tags='arc')

    def Polygon(self):
        self.canvas.delete("rac",'oval','arc','polygon','lines','string')
        self.canvas.create_polygon(20,25,10,10,15,30,140,10,110,100, fill='green', tags='polygon')

    def Line(self):
        self.canvas.delete("rac",'oval','arc','polygon','lines','string')
        self.canvas.create_line(50,50,300,300,width=6,tags='lines', arrow='first')

    def String(self):
        self.canvas.delete("rac",'oval','arc','polygon','lines','string')
        self.canvas.create_text(150,150,text = "My Name is Shyam",font="Times 20 bold",tags="string")

    def clear(self):
        self.canvas.delete("rac",'oval','arc','polygon','lines','string')
        self.canvas.delete("rac",'oval','arc','polygon','lines','string')



CanvasDemo()