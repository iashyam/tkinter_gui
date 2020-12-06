import numpy as np
import math
import matplotlib.pyplot as plt
from tkinter import *
root = Tk()
root.title("Matlpotlib Charts")

def graph():
    a = [i/10 for i in range(1,100)]
    b = [math.sin(math.pi/i) for i in a]
    plt.plot(a, b)
    plt.show()

btn = Button(root, text="Graph it!", command=graph).pack()



root.mainloop()