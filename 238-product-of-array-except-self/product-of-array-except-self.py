class Solution(object):
    def productExceptSelf(self, nums):
        prefy = []
        prexy = []
        ans = []
        lproduct = 1
        rproduct = 1

        for i in range(len(nums)):
            if i == 0:
                prefy.append(1)
                continue
            lproduct *= nums[i - 1]
            prefy.append(lproduct)
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                prexy.append(1)
                continue
            rproduct *= nums[i + 1]
            prexy.append(rproduct)
            
        prexy.reverse()
        
        for i in range(len(nums)):
            ans.append(prefy[i] * prexy[i])
        
        return ans

        