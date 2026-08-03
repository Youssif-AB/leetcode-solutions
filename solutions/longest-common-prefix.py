# https://leetcode.com/problems/longest-common-prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        final = ""

        for i, letter in enumerate(strs[0]):
            level = True
            for word in strs[1:]:
                if i >= len(word):
                    level = False
                for j, letter2 in enumerate(word): 
                    if letter != letter2 and j == i:
                        level = False
                        break
            
            if level:
                final += letter
            else:
                break

        return final
        