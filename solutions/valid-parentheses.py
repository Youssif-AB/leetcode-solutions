# https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        answers = {')':'(', '}':'{', ']':'['}

        brackets = []
        for bracket in s:
            if bracket in ['(', '{', '[']:
                brackets.append(bracket)
            elif bracket in [')', '}', ']']:
                if not brackets or brackets.pop() != answers[bracket]:
                    return False
        return not brackets

            


        
        