class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        sorted_arr = []

        for i in range(len(mat) + len(mat[0]) - 1):
            sorted_arr.append([])
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                sorted_arr[i + j].append(mat[i][j])
        
        for z in range(len(sorted_arr)):
            if (z + 1) % 2 != 0:
                sorted_arr[z] = sorted_arr[z][::-1]
        
        ans = []

        for i in range(len(sorted_arr)):
            for j in range(len(sorted_arr[i])):
                ans.append(sorted_arr[i][j])
        
        return ans
        