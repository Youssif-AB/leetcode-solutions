class Solution(object):
    def increasingTriplet(self, nums):
        small = nums[0]
        medium = max(nums)

        for i in range(len(nums)):
            if nums[i] < small:
                small = nums[i]

            if nums[i] > small and nums[i] < medium:
                medium = nums[i]
            
            if nums[i] > medium:
                return True

        return False