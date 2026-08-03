# https://leetcode.com/problems/remove-element

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == val:
                    for z in range(j + 1, len(nums)):
                        temp = nums[z-1]
                        nums[z - 1] = nums[z]
                        nums[z] = temp
                   
                    
                    
        for q in nums:
            if q == val:
                k = k + 1

        print(nums)
        print(k)
        print(len(nums) - k)
        return len(nums) - k