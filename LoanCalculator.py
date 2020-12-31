from tkinter import *

class windo:
    def __init__(self):
        root = Tk()

        window = LabelFrame(root, padx=20, pady=20)
        window.pack()

        self.annual = StringVar()
        self.years = StringVar()
        self.amount = StringVar()

        self.monthly_text = '1000'
        self.total_text = '100000'

        Label(window, text="annual interest rate".title()).grid(row=0, column=0, sticky=W)
        Label(window, text="Number of Years").grid(row=1, column=0, sticky=W)
        Label(window, text="Loan Amount").grid(row=2, column=0, sticky=W)
        Label(window, text="Monthly Payment").grid(row=3, column=0, sticky=W)
        Label(window, text='Total Payment').grid(row=4, column=0, sticky=W)
        self.monthly = Label(window, text="")
        self.monthly.grid(row=3, column=1)
        self.total = Label(window, text="")
        self.total.grid(row=4, column=1)
        self.annual_entry = Entry(window, textvariable=self.annual, justify=RIGHT).grid(row=0, column=1)
        self.years_entry = Entry(window, textvariable=self.years, justify=RIGHT).grid(row=1, column=1)
        self.amount_entry = Entry(window, textvariable=self.amount, justify=RIGHT).grid(row=2, column=1)
        self.compute = Button(window, text = "Compute Payment", command = self.command).grid(row=5, column=1, sticky=E)

        root.mainloop()

    def command(self):
        self.total_text = str((float(self.annual.get())*float(self.years.get())*float(self.amount.get()))/100)
        self.monthly_text = str(int(float(self.total_text)/12))
        self.monthly.config(text = self.monthly_text)
        self.total.config(text =self.total_text)

windo()