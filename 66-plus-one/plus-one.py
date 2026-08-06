class Solution(object):
    def plusOne(self, digits):
        num = ''
        finallist = []
        for i in digits:
            num += str(i)

        for i in str(int(num) + 1):
            finallist.append(int(i))
        
        return finallist