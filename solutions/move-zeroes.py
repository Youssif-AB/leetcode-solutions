# https://leetcode.com/problems/move-zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == 0:
                for z in range(j + 1, len(nums)):
                    temp = nums[z-1]
                    nums[z - 1] = nums[z]
                    nums[z] = temp