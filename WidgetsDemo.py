#28-12-2020
from tkinter import *

class widgetsDemo:
    def __init__(self):
        window = Tk()
        window.title("Widgets Demo!!")

        #add a check Button, and radio button
        frame1 = LabelFrame(window, padx=10,pady=10)
        frame1.pack()

        #adding a check box
        self.var1 = IntVar()
        self.var2 = IntVar()
        check = Checkbutton(frame1,text = "Bold",command = self.checkbutton_event, variable=self.var1)
        #@Creating Two RadioButtons
        radio_red = Radiobutton(frame1, text= "Red",bg = "red",variable = self.var2, value=0, command = self.radio_event)
        radio_blue = Radiobutton(frame1, bg = "Blue", text= "Blue",variable = self.var2, value=1, command = self.radio_event)
        check.grid(row=0, column=0)
        radio_red.grid(row=0, column=1)
        radio_blue.grid(row=0, column=2)

        #Create a frame for Entry, button and meaage
        frame2 = LabelFrame(window, padx=10, pady=10)
        frame2.pack()
        self.name = StringVar()
        name_label = Label(frame2, text= "Enter Your Name  ")
        name_entry = Entry(frame2, textvariable = self.name)
        name_button = Button(frame2, text = "Get Name", bg='Blue', fg='White', command=self.buttonEvent)
        name_message = Message(frame2, text= "We are getting your name!")
        name_label.grid(row=0,column=0)
        name_entry.grid(row=1, column=0)
        name_button.grid(row=2, column=0)
        name_message.grid(row=3, column=0)

        text = Text()
        text.pack()
        text.insert(END, 'This is a text')

        window.mainloop()

    def checkbutton_event(self):
        print("Blod")

    def radio_event(self):
        if self.var2.get() == 0:
            print("Red")
        else:
            print("Blue")

    def buttonEvent(self):
        print(self.name.get())

widgetsDemo()