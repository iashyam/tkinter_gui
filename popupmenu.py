from tkinter import *

class Popupmenu:
    def __init__(self):
        window = Tk()
        window.title("PopUp Menu")
        self.main_menu = Menu(window, tearoff = 0)

        self.main_menu.add_command(label='Oval',command=self.draw_oval)
        self.main_menu.add_command(label='Ractangle', command=self.draw_rec)
        self.main_menu.add_command(label='line', command=self.draw_line)
        self.main_menu.add_command(label='Clear', command=self.clear)

        self.canvas = Canvas(window, height=400,width=400,bg='white')
        self.canvas.pack()
        self.canvas.bind('<Button-3>', self.popup)

        window.mainloop()

    def draw_oval(self):
        self.canvas.create_oval(20,20, 380,380, tags='oval')

    def draw_rec(self):
        self.canvas.create_rectangle(20, 20, 380, 380, tags = 'rec')

    def draw_line(self):
        self.canvas.create_line(30, 200, 200, 200, tags = 'line')

    def clear(self):
        self.canvas.delete('oval','rec','line')

    def popup(self,event):
        self.main_menu.post(event.x_root, event.y_root)


if __name__ == '__main__':
    Popupmenu()