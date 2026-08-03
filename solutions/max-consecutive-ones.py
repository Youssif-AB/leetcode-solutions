# https://leetcode.com/problems/max-consecutive-ones

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        counts = []
        count = 0
        for i in nums:
            print(i)
            if i == 1:
                count +=1
            else:
                counts.append(count)
                count = 0
        if count != 0:
            counts.append(count)
                
        return max(counts)
        