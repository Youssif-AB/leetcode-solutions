class Solution(object):
    def gcdOfStrings(self, str1, str2):
        minword = ""
        maxword = ""
        if len(str1) >= len(str2):
            minword = str2
            maxword = str1
        else:
            minword = str1
            maxword = str2

        construction = ""
        smallestprefix = ""
        for i in minword:
            construction += i
       
            if maxword.replace(construction, "") == "" and minword.replace(construction, "") == "":
                smallestprefix = construction
            print(smallestprefix)
            
        return smallestprefix
            

