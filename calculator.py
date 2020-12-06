#pyhton GUI Project 1
#making a simple calculator
#2nd Dec 2020, 11:16 (Start)
#edned on 15:00
# def f(a):
#     return ((eval(compile(str(a),"<string>", 'eval'))))
from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Calculator by iashyam")
root.iconbitmap('D:\Tkinter_gui\calculator.ico')
e = Entry(root, width = 50,  borderwidth = 4)
e.grid(row=0, column=0, columnspan =4)

def number(num):
    temp = e.get()
    e.delete(0, END)
    e.insert(0,  str(temp) + str(num))

def equal():
    try:
        b = str(e.get())
        e.delete(0, END)
        e.insert(0, (eval(compile(b,"<string>", 'eval'))))
    except Exception as w:
        messagebox.showerror(title='Error', message=w)




def clear():
    e.delete(0,END)


button_0 = Button(root, padx=40,pady=20, text = '0', command= lambda: number('0'))
button_1 = Button(root, padx=40,pady=20, text = '1', command= lambda: number('1'))
button_2 = Button(root, padx=40,pady=20, text = '2', command= lambda: number('2'))
button_3 = Button(root, padx=40,pady=20, text = '3', command= lambda: number('3'))
button_4 = Button(root, padx=40,pady=20, text = '4', command= lambda: number('4'))
button_5 = Button(root, padx=40,pady=20, text = '5', command= lambda: number('5'))
button_6 = Button(root, padx=40,pady=20, text = '6', command= lambda: number('6'))
button_7 = Button(root, padx=40,pady=20, text = '7', command= lambda: number('7'))
button_8 = Button(root, padx=40,pady=20, text = '8', command= lambda: number('8'))
button_9 = Button(root, padx=40,pady=20, text = '9', command= lambda: number('9'))
button_plus = Button(root, padx=40,pady=20, text = '+', command= lambda: number("+"))
button_minus = Button(root, padx=40,pady=20, text = '-', command= lambda: number('-'))
button_x = Button(root, padx=40,pady=20, text = 'x', command= lambda: number('*'))
button_devide = Button(root, padx=40,pady=20, text = '/', command= lambda: number("/"))
button_equal = Button(root, padx=39,pady=20, text = '=', command= equal)
button_clear = Button(root, padx=40,pady=20, text = 'c', command= clear)
button_exit = Button(root, padx=85,pady=20, text = 'Exit', command= root.quit)


button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_0.grid(row=4,column=1)
button_plus.grid(row=1,column=3)
button_minus.grid(row=2,column=3)
button_x.grid(row=3,column=3)

button_devide.grid(row=4,column=3)
button_clear.grid(row=4,column=0)
button_equal.grid(row=4,column=2)
button_exit.grid(row=6,column=1, columnspan = 2)


root.mainloop()