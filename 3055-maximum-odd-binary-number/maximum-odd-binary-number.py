class Solution(object):
    def maximumOddBinaryNumber(self, s):
        onec = 0
        finals = ''
        for i in s:
            if i == "1":
                onec += 1
     
        for i in range(len(s)):
            if onec > 1 or i == len(s) - 1:
                finals += "1"
                onec -= 1
            else:
                finals += "0"
        
        return finals
        
        