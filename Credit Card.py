from Craditcard import Card
from tkinter import *
from tkinter import messagebox

class validator:
    def __init__(self):p
        self.window = Tk()
        self.window.title("Credit Card Validator")
        self.window.geometry('180x100')

        self.window.resizable(width=NO, height=NO)
        self.card_num = StringVar()
        self.lbl = Label(self.window, text = "Enter Credit Card Number: ")
        self.lbl.pack(anchor=W, padx=20)

        self.entry = Entry(self.window, textvariable=self.card_num, bg= 'gray', width=25)
        self.entry.pack(anchor=W, padx=20)

        self.result = Label(self.window, text = '')
        self.result.pack()

        self.result_button = Button(self.window, text= "Check", command = self.check,bg='blue')
        self.result_button.pack()

        self.window.mainloop()

    def check(self):
        try:
            object = Card(self.card_num.get())
            if self.card_num.get() == '':
                self.result.config(text="Please Enter Card Number.", fg='red')
            else:
                if object.Isvalid():
                    self.result.config(text= "Card is Valid!")
                else:
                    self.result.config(text="Card is not Valid!")

        except :
            messagebox.showerror(title='Error', message='Please Enter An Integer!')

if __name__ == '__main__':
    validator()