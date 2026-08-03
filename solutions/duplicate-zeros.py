# https://leetcode.com/problems/duplicate-zeros

class Solution(object):
    def duplicateZeros(self, arr):
        
        def notoddcheck(array, end):
            count = 0
            for i in range(0, end):
                if array[i] == 0:
                    count +=1
                else:
                    count == 0
            return count % 2 == 0
        
        if arr[0] == 0:
            temp = arr[1]
            arr[1] = 0
            for z in range(2, len(arr)):
                arr[z], temp = temp, arr[z]
                
            for i in range(2, len(arr)):
                if arr[i] == 0 and notoddcheck(arr, i) and i != len(arr) - 1:
                    temp = arr[i + 1]
                    arr[i + 1] = 0
                    for z in range(i + 2, len(arr)):
                        arr[z], temp = temp, arr[z]
        else:       
            for i in range(0, len(arr)):
                if arr[i] == 0 and notoddcheck(arr, i) and i != len(arr) - 1:
                    temp = arr[i + 1]
                    arr[i + 1] = 0
                    for z in range(i + 2, len(arr)):
                        arr[z], temp = temp, arr[z]
        
        return arr
                    
                    