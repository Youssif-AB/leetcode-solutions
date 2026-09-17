class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # rows
        valid = True
        for i in range(len(board)):
            if len(set(board[i])) != (len(board[i]) - (board[i].count(".") - 1)):
                valid = False

        #cols
        for j in range(len(board[0])):
            col = []
            for i in range(len(board)):
                col.append(board[i][j])
            if len(set(col)) != (len(col) - (col.count(".") - 1)):
                valid = False

        #3's
        threes = []
        three = []
        nums = [(0,2),(2,5),(5,8)]

        ##row 0,2 col 0,2
        #row 2,5 col 0,2
        #row 5,8 col 0,2

        for i in range(3):
            for j in range(3):
                three.append(board[i][j])

        threes.append(three)
        three = []

        for i in range(3):
            for j in range(3, 6):
                three.append(board[i][j])

        threes.append(three)
        three = []

        for i in range(3):
            for j in range(6, 9):
                three.append(board[i][j])

        threes.append(three)
        three = []


        for i in range(3, 6):
            for j in range(3):
                three.append(board[i][j])

        threes.append(three)
        three = []

        for i in range(3, 6):
            for j in range(3, 6):
                three.append(board[i][j])

        threes.append(three)
        three = []

        for i in range(3, 6):
            for j in range(6, 9):
                three.append(board[i][j])
        threes.append(three)
        three = []

        for i in range(6, 9):
            for j in range(3):
                three.append(board[i][j])

        threes.append(three)
        three = []

        for i in range(6, 9):
            for j in range(3, 6):
                three.append(board[i][j])

        threes.append(three)
        three = []

        for i in range(6, 9):
            for j in range(6, 9):
                three.append(board[i][j])

        threes.append(three)
        three = []
        
        for i in threes:
            if len(set(i)) != (len(i) - (i.count(".") - 1)):
                valid = False

        

        return(valid)
        