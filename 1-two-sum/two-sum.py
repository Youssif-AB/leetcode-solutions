class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        maps = {}

        for i in range(len(nums)):
            maps[nums[i]] = target - nums[i]
        

        for i in range(len(nums)):
            if maps[nums[i]] in nums and nums.index(maps[nums[i]]) != i:
                return[i, nums.index(maps[nums[i]])]