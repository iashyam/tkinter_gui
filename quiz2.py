from tkinter import *

root = Tk()
root.title("Quiz by Shyam")

frame = LabelFrame(root, padx=15, pady=15)
frame.pack()

top = Toplevel()

def opt(option):
    j = []
    for i in option:
        j.append((str(i), str(i)))
    return j
def question(que, option, correct):
    label = Label(frame, text = que)
    label.pack(anchor=W)
    r = StringVar()
    for a,b in opt(option):
        Radiobutton(frame, text=a, variable=r, value=b,tristatevalue='x').pack(anchor=W)
    def check():

        if r.get() == str(correct):
            text = f"Correct\n {correct} is the correct answer."
        else:
            text = f"Wrong \n {correct} is the correct answer."
        label = Label(top, text=text).pack(anchor=W)
    btn = Button(frame, text="Check", command=check).pack()

question('Who is Indian captain?',["Rohit Sharma", 'Virat Kohli','MS Dhoni','KL Rahul'], 'Virat Kohli')
question('How many times have India won the worldcup?',[1,2,3,4],2)
question('How many wickets have Jems Anderson taken?',[800,500,647,600],600)

root.mainloop()