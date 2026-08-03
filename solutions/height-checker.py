# https://leetcode.com/problems/height-checker

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        k = 0
        for i in range(len(heights)):
            if heights[i] != sorted(heights)[i]:
                k = k + 1

        return k
        