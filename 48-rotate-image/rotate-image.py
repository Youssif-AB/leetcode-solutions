class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        ##new rows = old column
        ##new columns = len(matrix) - 1 - old row

        reference = []

        nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                nums.append(matrix[i][j])
            reference.append(nums)
            nums = []
        
        for i in range(len(reference)):
            for j in range(len(reference[i])):
                matrix[j][len(matrix) - 1 - i] = reference[i][j]
        
        



        