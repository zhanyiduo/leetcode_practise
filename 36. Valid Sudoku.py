'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row base rule
        for idx, row in enumerate(board):
            if not self.checkvalid(row):
                return False
        # col base rule
        for i in range(9):
            col = [board[j][i] for j in range(9)]
            if not self.checkvalid(col):
                return False
        # block base rule validation
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = [board[i + x][j + y] for x in range(3) for y in range(3)]
                if not self.checkvalid(block):
                    return False
        return True

    def checkvalid(self, comb):
        combint = []
        for i in comb:
            if i == ".":
                continue
            else:
                ele = int(i)
                if ele in combint:
                    return False
                else:
                    combint.append(ele)
        return True
