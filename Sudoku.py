#<----importing libraries--->
from  tkinter import *
from tkinter import messagebox
import time
import random
from random import randint, shuffle

#<---Making  a simple GUI For calculator--->

smith = Tk()
smith.title("Sudoku")
#smith.iconbitmap('game.ico')
smith.geometry('260x350')
smith.minsize(260,350)
smith.maxsize(260,350)
smith.resizable(height=NO,width=NO)


#Creating  a labl frame to make it look better
root = LabelFrame(smith, padx=15, pady=15, bg="#99b3ff")
root.pack()


# <----Creating the boxes---->

frame1 = LabelFrame(root, padx=2, pady=2)
frame2 = LabelFrame(root, padx=2, pady=2)
frame3 = LabelFrame(root, padx=2, pady=2)
frame4 = LabelFrame(root, padx=2, pady=2)
frame5 = LabelFrame(root, padx=2, pady=2)
frame6 = LabelFrame(root, padx=2, pady=2)
frame7 = LabelFrame(root, padx=2, pady=2)
frame8 = LabelFrame(root, padx=2, pady=2)
frame9 = LabelFrame(root, padx=2, pady=2)

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=0, column=2)
frame4.grid(row=1, column=0)
frame5.grid(row=1, column=1)
frame6.grid(row=1, column=2)
frame7.grid(row=2, column=0)
frame8.grid(row=2, column=1)
frame9.grid(row=2, column=2)

# <-----x--boxes creted------>

#<----creting entires------->

a00  = Entry(frame1, width=3)
a01  = Entry(frame1, width=3)
a02  = Entry(frame1, width=3)
a10  = Entry(frame1, width=3)
a11  = Entry(frame1, width=3)
a12  = Entry(frame1, width=3)
a20  = Entry(frame1, width=3)
a21  = Entry(frame1, width=3)
a22  = Entry(frame1, width=3)

a03  = Entry(frame2, width=3)
a04  = Entry(frame2, width=3)
a05  = Entry(frame2, width=3)
a13  = Entry(frame2, width=3)
a14  = Entry(frame2, width=3)
a15  = Entry(frame2, width=3)
a23  = Entry(frame2, width=3)
a24  = Entry(frame2, width=3)
a25  = Entry(frame2, width=3)

a06  = Entry(frame3, width=3)
a07  = Entry(frame3, width=3)
a08  = Entry(frame3, width=3)
a16  = Entry(frame3, width=3)
a17  = Entry(frame3, width=3)
a18  = Entry(frame3, width=3)
a26  = Entry(frame3, width=3)
a27  = Entry(frame3, width=3)
a28  = Entry(frame3, width=3)

a30  = Entry(frame4, width=3)
a31  = Entry(frame4, width=3)
a32  = Entry(frame4, width=3)
a40  = Entry(frame4, width=3)
a41  = Entry(frame4, width=3)
a42  = Entry(frame4, width=3)
a50  = Entry(frame4, width=3)
a51  = Entry(frame4, width=3)
a52  = Entry(frame4, width=3)


a33  = Entry(frame5, width=3)
a34  = Entry(frame5, width=3)
a35  = Entry(frame5, width=3)
a43  = Entry(frame5, width=3)
a44  = Entry(frame5, width=3)
a45  = Entry(frame5, width=3)
a53  = Entry(frame5, width=3)
a54  = Entry(frame5, width=3)
a55  = Entry(frame5, width=3)


a36  = Entry(frame6, width=3)
a37  = Entry(frame6, width=3)
a38  = Entry(frame6, width=3)
a46  = Entry(frame6, width=3)
a47  = Entry(frame6, width=3)
a48  = Entry(frame6, width=3)
a56  = Entry(frame6, width=3)
a57  = Entry(frame6, width=3)
a58  = Entry(frame6, width=3)

a60  = Entry(frame7, width=3)
a61  = Entry(frame7, width=3)
a62  = Entry(frame7, width=3)
a70  = Entry(frame7, width=3)
a71  = Entry(frame7, width=3)
a72  = Entry(frame7, width=3)
a80  = Entry(frame7, width=3)
a81  = Entry(frame7, width=3)
a82  = Entry(frame7, width=3)


a63  = Entry(frame8, width=3)
a64  = Entry(frame8, width=3)
a65 = Entry(frame8, width=3)
a73  = Entry(frame8, width=3)
a74  = Entry(frame8, width=3)
a75  = Entry(frame8, width=3)
a83  = Entry(frame8, width=3)
a84  = Entry(frame8, width=3)
a85  = Entry(frame8, width=3)


a66  = Entry(frame9, width=3)
a67  = Entry(frame9, width=3)
a68  = Entry(frame9, width=3)
a76  = Entry(frame9, width=3)
a77  = Entry(frame9, width=3)
a78  = Entry(frame9, width=3)
a86  = Entry(frame9, width=3)
a87  = Entry(frame9, width=3)
a88  = Entry(frame9, width=3)



a00.grid(row=0, column=0)
a01.grid(row=0, column=1)
a02.grid(row=0, column=2)
a10.grid(row=1, column=0)
a11.grid(row=1, column=1)
a12.grid(row=1, column=2)
a20.grid(row=2, column=0)
a21.grid(row=2, column=1)
a22.grid(row=2, column=2)

a30.grid(row=0, column=0)
a31.grid(row=0, column=1)
a32.grid(row=0, column=2)
a40.grid(row=1, column=0)
a41.grid(row=1, column=1)
a42.grid(row=1, column=2)
a50.grid(row=2, column=0)
a51.grid(row=2, column=1)
a52.grid(row=2, column=2)

a60.grid(row=0, column=0)
a61.grid(row=0, column=1)
a62.grid(row=0, column=2)
a70.grid(row=1, column=0)
a71.grid(row=1, column=1)
a72.grid(row=1, column=2)
a80.grid(row=2, column=0)
a81.grid(row=2, column=1)
a82.grid(row=2, column=2)

a03.grid(row=0, column=0)
a04.grid(row=0, column=1)
a05.grid(row=0, column=2)
a13.grid(row=1, column=0)
a14.grid(row=1, column=1)
a15.grid(row=1, column=2)
a23.grid(row=2, column=0)
a24.grid(row=2, column=1)
a25.grid(row=2, column=2)

a33.grid(row=0, column=0)
a34.grid(row=0, column=1)
a35.grid(row=0, column=2)
a43.grid(row=1, column=0)
a44.grid(row=1, column=1)
a45.grid(row=1, column=2)
a53.grid(row=2, column=0)
a54.grid(row=2, column=1)
a55.grid(row=2, column=2)

a63.grid(row=0, column=0)
a64.grid(row=0, column=1)
a65.grid(row=0, column=2)
a73.grid(row=1, column=0)
a74.grid(row=1, column=1)
a75.grid(row=1, column=2)
a83.grid(row=2, column=0)
a84.grid(row=2, column=1)
a85.grid(row=2, column=2)

a06.grid(row=0, column=0)
a07.grid(row=0, column=1)
a08.grid(row=0, column=2)
a16.grid(row=1, column=0)
a17.grid(row=1, column=1)
a18.grid(row=1, column=2)
a26.grid(row=2, column=0)
a27.grid(row=2, column=1)
a28.grid(row=2, column=2)

a36.grid(row=0, column=0)
a37.grid(row=0, column=1)
a38.grid(row=0, column=2)
a46.grid(row=1, column=0)
a47.grid(row=1, column=1)
a48.grid(row=1, column=2)
a56.grid(row=2, column=0)
a57.grid(row=2, column=1)
a58.grid(row=2, column=2)

a66.grid(row=0, column=0)
a67.grid(row=0, column=1)
a68.grid(row=0, column=2)
a76.grid(row=1, column=0)
a77.grid(row=1, column=1)
a78.grid(row=1, column=2)
a86.grid(row=2, column=0)
a87.grid(row=2, column=1)
a88.grid(row=2, column=2)



# <-----Listing Entries into a list----->

entries = ([[a00, a01, a02, a03, a04, a05, a06, a07, a08],
          [a10, a11, a12, a13, a14, a15, a16, a17, a18],
          [a20, a21, a22, a23, a24, a25, a26, a27, a28],
          [a30, a31, a32, a33, a34, a35, a36, a37, a38],
          [a40, a41, a42, a43, a44, a45, a46, a47, a48],
          [a50, a51, a52, a53, a54, a55, a56, a57, a58],
          [a60, a61, a62, a63, a64, a65, a66, a67, a68],
          [a70, a71, a72, a73, a74, a75, a76, a77, a78],
          [a80, a81, a82, a83, a84, a85, a86, a87, a88]])

k = time.time()

# <---------Showing time and Score------>

def tick():
    begin = time.time() - k
    seconds = (int(begin))
    min = seconds//60
    sec = seconds%60
    if sec <10:
        global time_string
        time_string =  str(min) + ':' + '0' + str(sec)
    else:
        time_string = str(min) + ':' + str(sec)
    time_label.config(text=time_string)
    time_label.after(1000,tick)

global time_label
time_label = Label(smith, relief=SUNKEN)
tick()
time_label.pack(ipadx=113)

# <-----Defining a function to check if the sudoku is right----->

def check():
    global valid
    valid = False
    A00 = a00.get()
    A01 = a01.get()
    A02 = a02.get()
    A03 = a03.get()
    A04 = a04.get()
    A05 = a05.get()
    A06 = a06.get()
    A07 = a07.get()
    A08 = a08.get()

    A10 = a10.get()
    A11 = a11.get()
    A12 = a12.get()
    A13 = a13.get()
    A14 = a14.get()
    A15 = a15.get()
    A16 = a16.get()
    A17 = a17.get()
    A18 = a18.get()

    A20 = a20.get()
    A21 = a21.get()
    A22 = a22.get()
    A23 = a23.get()
    A24 = a24.get()
    A25 = a25.get()
    A26 = a26.get()
    A27 = a27.get()
    A28 = a28.get()

    A30 = a30.get()
    A31 = a31.get()
    A32 = a32.get()
    A33 = a33.get()
    A34 = a34.get()
    A35 = a35.get()
    A36 = a36.get()
    A37 = a37.get()
    A38 = a38.get()

    A40 = a40.get()
    A41 = a41.get()
    A42 = a42.get()
    A43 = a43.get()
    A44 = a44.get()
    A45 = a45.get()
    A46 = a46.get()
    A47 = a47.get()
    A48 = a48.get()

    A50 = a50.get()
    A51 = a51.get()
    A52 = a52.get()
    A53 = a53.get()
    A54 = a54.get()
    A55 = a55.get()
    A56 = a56.get()
    A57 = a57.get()
    A58 = a58.get()

    A60 = a60.get()
    A61 = a61.get()
    A62 = a62.get()
    A63 = a63.get()
    A64 = a64.get()
    A65 = a65.get()
    A66 = a66.get()
    A67 = a67.get()
    A68 = a68.get()

    A70 = a70.get()
    A71 = a71.get()
    A72 = a72.get()
    A73 = a73.get()
    A74 = a74.get()
    A75 = a75.get()
    A76 = a76.get()
    A77 = a77.get()
    A78 = a78.get()

    A80 = a80.get()
    A81 = a81.get()
    A82 = a82.get()
    A83 = a83.get()
    A84 = a84.get()
    A85 = a85.get()
    A86 = a86.get()
    A87 = a87.get()
    A88 = a88.get()

    a = ([[A00, A01, A02, A03, A04, A05, A06, A07, A08],
          [A10, A11, A12, A13, A14, A15, A16, A17, A18],
          [A20, A21, A22, A23, A24, A25, A26, A27, A28],
          [A30, A31, A32, A33, A34, A35, A36, A37, A38],
          [A40, A41, A42, A43, A44, A45, A46, A47, A48],
          [A50, A51, A52, A53, A54, A55, A56, A57, A58],
          [A60, A61, A62, A63, A64, A65, A66, A67, A68],
          [A70, A71, A72, A73, A74, A75, A76, A77, A78],
          [A80, A81, A82, A83, A84, A85, A86, A87, A88]])

    for i in range(9):
        for j in range(9):
            a[i][j] = str(a[i][j])

    #Showing the results in a message box
    if ValidRow(a) and ValidRow(a) and ValidBox(a):
        messagebox.showinfo(title = 'Result', message="Shyam Says- \nCongratulations! \nYou got it right.\nDone in time " + time_string + ' Sec.')
    else:
        messagebox.showerror(title= 'Result', message="Shyam says- \nSudoku is not right! \nDone in time " + time_string + ' Sec.')




#check Button
Check = Button(root, text="Check", command=check)
Check.grid(row=3, column=0, columnspan=3, pady=(20,5))



# <-----Basic GUI Completed------>

# <-----Giving the GUI intial conditions----->

#making a complete sudoku as source of initial conditions!

def compare(list):
    standrad = ['1','2','3','4','5','6','7','8','9']
    return sorted(list) == standrad

def ValidRow(a):
    for i in a:
        if not compare(i):
            return False
    return True

def ValidColumn(a):
    for i in range(9):
        col = []
        for j in range(9):
            col.append(a[j][i])
        if not compare(col):
            return False
    return True

def ValidBox(a):
    for i in range(0,9,3):
        for j in range(0,9,3):
            nums = a[i][j:j+3] + a[i+1][j:j+3] + a[i+2][j:j+3]
            if not compare(nums):
                return False
        return True

#definig a function to give some hints to solve!
def hints():

    grid = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

    numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # A function to check if the grid is full
    def checkGrid(grid):
        for row in range(0, 9):
            for col in range(0, 9):
                if grid[row][col] == 0:
                    return False

        # We have a complete grid!
        return True


    # A backtracking/recursive function to check all possible combinations of numbers until a solution is found
    def solveGrid(grid):
        global counter
        # Find next empty cell
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                for value in range(1, 10):
                    # Check that this value has not already be used on this row
                    if not (value in grid[row]):
                        # Check that this value has not already be used on this column
                        if not value in (
                        grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col],
                        grid[7][col], grid[8][col]):
                            # Identify which of the 9 squares we are working on
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(0, 3)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(0, 3)]
                                else:
                                    square = [grid[i][6:9] for i in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(3, 6)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(3, 6)]
                                else:
                                    square = [grid[i][6:9] for i in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(6, 9)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(6, 9)]
                                else:
                                    square = [grid[i][6:9] for i in range(6, 9)]
                            # Check that this value has not already be used on this 3x3 square
                            if not value in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                if checkGrid(grid):
                                    counter += 1
                                    break
                                else:
                                    if solveGrid(grid):
                                        return True
                break
        grid[row][col] = 0


    numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    # A backtracking/recursive function to check all possible combinations of numbers until a solution is found
    def fillGrid(grid):
        global counter
        # Find next empty cell
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                shuffle(numberList)
                for value in numberList:
                    # Check that this value has not already be used on this row
                    if not (value in grid[row]):
                        # Check that this value has not already be used on this column
                        if not value in (
                        grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col],
                        grid[7][col], grid[8][col]):
                            # Identify which of the 9 squares we are working on
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(0, 3)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(0, 3)]
                                else:
                                    square = [grid[i][6:9] for i in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(3, 6)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(3, 6)]
                                else:
                                    square = [grid[i][6:9] for i in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(6, 9)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(6, 9)]
                                else:
                                    square = [grid[i][6:9] for i in range(6, 9)]
                            # Check that this value has not already be used on this 3x3 square
                            if not value in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                if checkGrid(grid):
                                    return True
                                else:
                                    if fillGrid(grid):
                                        return True
                break
        grid[row][col] = 0


    # Generate a Fully Solved Grid
    fillGrid(grid)

    count = 0

    hints = random.randint(30,60)

    while count<hints:
        row = random.randrange(0,9)
        column= random.randrange(0,9)
        entries[row][column].delete(0,END)
        entries[row][column].insert(0, str(grid[row][column]))
        count += 1

hints()




#function to create a new game
def newgame():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, END)
    hints()

    # <---------Showing time and Score------>

    k = time.time()

    def tick():
        begin = time.time() - k
        seconds = (int(begin))
        min = seconds // 60
        sec = seconds % 60
        if sec < 10:
            global time_string
            time_string = str(min) + ':' + '0' + str(sec)
        else:
            time_string = str(min) + ':' + str(sec)
        time_label.config(text=time_string)
        time_label.after(1000, tick)

    global time_label
    time_label.destroy()

    time_label = Label(smith, relief=SUNKEN)
    tick()

    time_label.pack(ipadx=113)

#New game Button
New = Button(root, text="New Game", command= newgame)
New.grid(row=4, column=0, columnspan=3, pady=(5,17))

# <----Initial Conditions Given----->

smith.mainloop()
