class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthofls = 0
        string = []
        counter = 0
        for i in range(len(s)):
            if s[i] not in string:
                string.append(s[i])
                counter += 1
            else:
                if counter > lengthofls:
                    lengthofls = counter
                
                j = 0
                while j < len(string):
                    if string[j] == s[i]:
                        string.pop(j)
                        counter -= 1
                        break
                    else:
                        string.pop(j)
                        j -= 1
                        counter -= 1
                    j += 1
                string.append(s[i])
                counter += 1
        if counter > lengthofls:
            lengthofls = counter
        
        return lengthofls

        