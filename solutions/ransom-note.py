# https://leetcode.com/problems/ransom-note

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for i in magazine:
            if i in ransomNote:
                ransomNote = ransomNote.replace(i, "", 1)
            if ransomNote == "":
                return True
        return False
        