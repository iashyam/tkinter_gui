from tkinter import *
class chessBoard:
    def __init__(self):
        self.window = Tk()
        self.window.title('ChessBoard')
        self.color = 'white'
        self.window.resizable(width=NO, height=NO)


        for i in range(8):
            for j in range(8):
                if ((i+1)%2 == 0 and (j+1)%2 == 1) \
                        or((i+1)%2==1 and (j+1)%2==0) :
                    self.color = 'black'
                else:
                    self.color = 'white'
                self.canvas().grid(row=i, column=j)

        self.window.mainloop()

    def canvas(self):
        return Canvas(self.window, width=40, height=40, bg=self.color)
chessBoard()