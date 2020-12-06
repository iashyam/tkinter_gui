#pyhton GUI project 2
#Image Viewer using Python
#03-12-2020 07:07

from tkinter import *
root = Tk()
root.title("Image Viwer")
root.iconbitmap('icon.ico')

label1 = Label(root, text= "1", padx=100, pady=100, bg= 'indigo')
label2 = Label(root, text= "2", padx=100, pady=100, bg='blue')
label3 = Label(root, text= "3", padx=100, pady=100,bg='green')
label4 = Label(root, text= "4", padx=100, pady=100,bg='yellow')
label5 = Label(root, text= "5", padx=100, pady=100,bg='red')
label = label1
labels = [label1,label2,label3,label4,label5]
label.grid(row=0,column=0,columnspan=3)

def back(number):
    if number == 0:
       back_button = Button(root, text="<<", state=DISABLED)
    else:
        global label
        global fore_button
        label.grid_forget()
        label = labels[number - 1]
        label.grid(row=0, column=0, columnspan=3)
        back_button = Button(root, text="<<", command=lambda: back(number - 1))
        fore_button = Button(root, text=">>", command=lambda: fore(number - 1))
        back_button.grid(row=1, column=0)
        fore_button.grid(row=1, column=2)
        status = Label(root, text=f"Image {labels.index(label)+1} of {len(labels)}", bd=1, relief=SUNKEN)
        status.grid(row=2, column=0, columnspan=1, sticky=W + E)


def fore(number):
    if number ==4:
        fore_button = Button(root, text=">>", command=lambda: fore(number), state=DISABLED)
        fore_button.grid(row=1, column=2)
    else:
        global label
        global back_button
        #global fore_button
        label.grid_forget()
        label = labels[number + 1]
        label.grid(row=0, column=0, columnspan=3)
        back_button = Button(root, text="<<", command=lambda: back(number + 1))
        fore_button = Button(root, text=">>", command=lambda: fore(number + 1))
        back_button.grid(row=1, column=0)
        fore_button.grid(row=1, column=2)
        status = Label(root, text=f"Image {labels.index(label)+1} of {len(labels)}", bd=1, relief=SUNKEN)
        status.grid(row=2, column=0, columnspan=1, sticky=W + E)



back_button  = Button(root, text="<<", command=lambda:back(len(labels)), state=DISABLED)
exit_button  = Button(root, text="Exit", command=root.quit)
fore_button  = Button(root, text=">>", command=lambda:fore(0))
status = Label(root, text = f"Image {1} of {len(labels)}", bd=1, relief = SUNKEN)

back_button.grid(row=1,column=0)
fore_button.grid(row=1,column=2)
exit_button.grid(row=1,column=1)
status.grid(row=2,column=0,columnspan=1, pady=10,sticky=W+E)


root.mainloop()