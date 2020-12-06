from tkinter import *

smith = Tk()
def slide():
	my_label = Label(smith, text=horizontal.get()).pack()
	smith.geometry(str(horizontal.get()) + "x" + str(400))

horizontal = Scale(smith, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

btn = Button(smith, text="set", command=slide).pack()

smith.mainloop()
