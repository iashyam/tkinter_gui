from random import random, randint
import numpy as np
import isvalid
#making a grid with 0
class sudoku():
    def __init__(self):
        self.board = np.zeros([9,9])
        self.full = False
        for i in range(5):
            for j in range(5):
                self.board[randint(0,8)][randint(0,8)] = randint(1,9)

    def solve(self):
        find = self.posEmpty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if isvalid.valid(self.board, i, (row, col)).isValid():
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False


    def isEmpty(self, pos):
        if self.board[pos[0]][pos[1]] == 0:
            return True
        else:
            return False

    def posEmpty(self):
        for i in range(9):
            for j in range(9):
                if self.isEmpty((i,j)):
                    return i , j
        return  None


    def SolValid(self):
        for i in range(9):
            for j in range(9):
                if not isvalid.valid(self.board, self.board[i][j], (i,j)).isValid():
                    return False
        return True

    def print(self):
        print(self.board)

if __name__ == '__main__':
    a  = sudoku()
    a.print()









