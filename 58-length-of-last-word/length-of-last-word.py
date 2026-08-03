class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for i in range(len(s) - 1, -1, -1):
            print(s[i])
            if s[i] != " ":
                print("yes")
                count += 1
            
            if i != 0 and s[i - 1] == " " and s[i] != " ":
                break
        return count
