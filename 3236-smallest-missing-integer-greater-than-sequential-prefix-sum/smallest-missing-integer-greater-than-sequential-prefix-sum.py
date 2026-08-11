class Solution(object):
    def missingInteger(self, nums):
        
        counter = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                counter += nums[i]
            else:
                break
        
        x = counter
        while x in nums:
            x +=1
        return x
            

        