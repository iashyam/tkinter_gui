class valid:
    def __init__(self, board, entry, position):
        self.board = board
        self.entry = entry
        self.i = position[0]
        self.j = position[1]

    def isValid(self):
        return self.checkRow() and self.checkCol() and self.checkBox()

    def checkRow(self):
        for row in range(9):
            if row != self.i and self.entry != self.board[row][self.j]:
                return True
        return False

    def checkCol(self):
        for col in range(9):
            if col != self.j and self.entry != self.board[self.i][col]:
                return True
        return False

    def checkBox(self):
        for row in range(3*(self.i//3) + 3*(self.i//3)+3):
            for col in range(3*(self.j//3), 3*(self.j//3)+3):
                if self.i != row and self.j != col and self.entry != self.board[row][col]:
                    return True
        return False


