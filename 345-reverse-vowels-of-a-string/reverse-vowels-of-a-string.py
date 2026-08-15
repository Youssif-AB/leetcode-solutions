class Solution(object):
    def reverseVowels(self, s):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        svowels = []
        for i in s:
            if i in vowels:
                print(i)
                svowels.append(i)
        print(svowels)
        svowels.reverse()
        print(svowels)
        counter = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s = s[:i] + svowels[counter] + s[i + 1:]
                counter += 1
        
        return s



        """
        :type s: str
        :rtype: str
        """
        