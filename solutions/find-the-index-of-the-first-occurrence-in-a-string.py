# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                print(haystack[i])
                print(needle[0])
                follows = True
                for z in range(1, len(needle)):
                    if (i + z) > len(haystack) - 1 or haystack[i + z] != needle[z]:
                        follows = False
                if follows == True:
                    return i
        
        return -1

        


        