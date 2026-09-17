class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        reference = []

        nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                nums.append(matrix[i][j])
            reference.append(nums)
            nums = []

        print(reference)
        for i in range(len(reference)):
            for j in range(len(reference[i])):
                if reference[i][j] == 0:
                    print(reference[i][j])
                    for q in range(0, len(reference[i])):
                        matrix[i][q] = 0
                    for z in range(0, len(reference)):
                        matrix[z][j] = 0
        
        