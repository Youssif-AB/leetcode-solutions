# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        val = arr[len(arr) - 1]
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > val:
                temp = arr[i]
                arr[i] = val
                val = temp
            else:
                arr[i] = val


        arr[len(arr) - 1] = -1
        return arr
