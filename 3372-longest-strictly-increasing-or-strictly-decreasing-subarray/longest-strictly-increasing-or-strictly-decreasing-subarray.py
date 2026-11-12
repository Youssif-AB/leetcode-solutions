class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        strictly_increasing = [nums[0]]
        strictly_decreasing = [nums[0]]

        strictly_increasing_sum = []
        strictly_decreasing_sum = []

        for i in range(1, len(nums)):
            
            print(strictly_increasing)
            if nums[i] > nums[i - 1]:
                strictly_increasing.append(nums[i])
            else:
                strictly_increasing_sum.append(strictly_increasing)
                strictly_increasing = []
                strictly_increasing.append(nums[i])
            
            if nums[i] < nums[i - 1]:
                strictly_decreasing.append(nums[i])
            else:
                strictly_decreasing_sum.append(strictly_decreasing)
                strictly_decreasing = []
                strictly_decreasing.append(nums[i])
            
        if strictly_increasing:
            strictly_increasing_sum.append(strictly_increasing)
        
        if strictly_decreasing:
            strictly_decreasing_sum.append(strictly_decreasing)
            
        lengths = 0
        for i in strictly_increasing_sum:
            if len(i) > lengths:
                lengths = len(i)
        for i in strictly_decreasing_sum:
            if len(i) > lengths:
                lengths = len(i)
        return lengths

        