#Python project 3
# Quiz app
# 04-12-2020 10:00

from tkinter import *
from tkinter import messagebox

root = Tk()

def question(text,options,correct):
    team = StringVar()
    q = Label(root, text=text)
    q.pack(anchor=W)
    for name, nation in options:
        Radiobutton(root, text=name, variable=team, value=nation, tristatevalue="x").pack(anchor=W)

a = [('India', 'India'),('Australia','Australia'),('Pakistan','Pakistan'),('England','Engalnd')]
q1 = 'Who won the world cuo 2019?'
b = [(1,1),(2,2),(4,4),(5,5)]

question(q1, a, 'India')



root.mainloop()