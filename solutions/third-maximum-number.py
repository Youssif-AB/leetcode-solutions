# https://leetcode.com/problems/third-maximum-number

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        final = sorted(set(nums))
        print(final)
        if len(final) >= 3:
            return final[len(final) - 3]
        else:
            return max(final)
        