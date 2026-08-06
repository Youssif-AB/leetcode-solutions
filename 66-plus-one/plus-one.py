class Solution(object):
    def plusOne(self, digits):
        num = ''
        finallist = []
        for i in digits:
            num += str(i)
        
        num = str(int(num) + 1)

        for i in str(num):
            finallist.append(int(i))
        
        return finallist