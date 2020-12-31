from tkinter import  *

class scrol:
    def __init__(self):
        window = Tk()
        window.geometry('180x60')

        scroller = Scrollbar(window)
        scroller.pack(side=RIGHT,fill=Y)

        text = Text(window, width=40, height=5, wrap=WORD, yscrollcommand=scroller.set)
        text.pack(fill=Y,expand=1)

        scroller.config(command=text.yview)

        window.mainloop()

if __name__ == '__main__':
    scrol()