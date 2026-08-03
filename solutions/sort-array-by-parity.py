# https://leetcode.com/problems/sort-array-by-parity

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 != 0:
                for j in range(i + 1, len(nums)):
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]

        return nums
        