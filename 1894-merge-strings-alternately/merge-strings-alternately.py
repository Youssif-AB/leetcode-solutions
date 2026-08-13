class Solution(object):
    def mergeAlternately(self, word1, word2):
        wordn = ""
        length = min(len(word1), len(word2))
        for i in range(length):
            wordn += word1[i]
            wordn += word2[i]
        
        if len(word1) > len(word2):
            for i in range(length,len(word1)):
                wordn += word1[i]
        elif len(word2) > len(word1):
            for i in range(length, len(word2)):
                wordn += word2[i]

        return wordn


        