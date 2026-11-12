class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        strictly_increasing = [nums[0]]
        strictly_decreasing = [nums[0]]

        strictly = []
        strictly = []

        for i in range(1, len(nums)):
            
            if nums[i] > nums[i - 1]:
                strictly_increasing.append(nums[i])
            else:
                strictly.append(strictly_increasing)
                strictly_increasing = []
                strictly_increasing.append(nums[i])
            
            if nums[i] < nums[i - 1]:
                strictly_decreasing.append(nums[i])
            else:
                strictly.append(strictly_decreasing)
                strictly_decreasing = []
                strictly_decreasing.append(nums[i])
            
        if strictly_increasing:
            strictly.append(strictly_increasing)
        
        if strictly_decreasing:
            strictly.append(strictly_decreasing)

        lengths = 0
        for i in strictly:
            if len(i) > lengths:
                lengths = len(i)
                
        return lengths

        