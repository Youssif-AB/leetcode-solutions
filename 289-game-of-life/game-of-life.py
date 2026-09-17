class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbor_board = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                neighbors = []
                
                for q in [1, 0, -1]:
                    for z in [1, 0, -1]:
                        if q == 0 and z == 0:
                            continue
                        if 0 <= i + q <= len(board) - 1 and 0 <= j + z <= len(board[i]) - 1:
                            neighbors.append(board[i + q][j + z])
                neighbor_board.append(neighbors)
        
        counter = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    if neighbor_board[counter].count(1) < 2:
                        board[i][j] = 0
                    elif neighbor_board[counter].count(1) > 3:
                        board[i][j] = 0
                else:
                    if neighbor_board[counter].count(1) == 3:
                        board[i][j] = 1
                counter += 1