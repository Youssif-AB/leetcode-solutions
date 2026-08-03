# https://leetcode.com/problems/running-sum-of-1d-array

class Solution(object):
    def runningSum(self, nums):
        final = []

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
                
        
        return nums