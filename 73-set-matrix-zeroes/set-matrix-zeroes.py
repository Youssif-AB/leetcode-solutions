class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows_to_rem = []
        cols_to_rem = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows_to_rem.append(i)
                    cols_to_rem.append(j)


        for i in range(len(matrix)):
            if i in rows_to_rem:
                matrix[i] = [x * 0 for x in matrix[i]]
            for j in range(len(matrix[i])):
                if j in cols_to_rem:
                    matrix[i][j] = 0
        
        