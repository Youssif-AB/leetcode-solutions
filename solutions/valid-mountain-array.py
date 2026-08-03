# https://leetcode.com/problems/valid-mountain-array

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        val = 0
        index = 0
        if len(arr) < 3:
            return False
        else:
            for i in range(len(arr)):
                if arr[i] > val:
                    val = arr[i]
                    index = i
            
            if index == 0 or index == len(arr) - 1:
                return False
            
            for j in range(1, index):
                if arr[j] <= arr[j - 1]:
                    return False
            
            for j in range(index + 1, len(arr)):
                if arr[j] >= arr[j - 1]:
                    return False
            
            return True

            

            
        