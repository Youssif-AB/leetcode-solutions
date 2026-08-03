# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

class Solution(object):
    def numberOfSteps(self, num):
        count = 0
        while (num != 0):
            if num % 2 == 0:
                num = num/2
                count += 1
            else:
                num = num - 1
                count += 1
        
        return count
        