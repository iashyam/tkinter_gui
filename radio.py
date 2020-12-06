#Pyhton GUI Lecture 5
#Creating Radio Boxp

from tkinter import *
root = Tk()
root.title("Predict")
team = StringVar()
options = [('Australia','Australia'),('India', 'India'),('England','England'),('Oman','Oman')]


def check():
    if team.get() == 'England':
        text = "Correct\n England Won worldcup 2019."
    else:
        text = "Wrong \n England Won worldcup 2019."
    label = Label(frame, text = text).pack(anchor= E)


frame = LabelFrame(root, padx=10,pady=10)
frame.pack()
q = Label(frame,text="Who won world cup 2019?")
q.pack(anchor= E)
for name, nation in options:
    Radiobutton(frame, text=name, variable=team, value=nation,tristatevalue="x").pack(anchor=W)

button = Button(frame,text= "Check",command= check).pack()

root.mainloop()