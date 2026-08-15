class Solution(object):
    def reverseWords(self, s):
        construction = ""
        word = ""

        for i in s:
            if i == " ":
                if word == "":
                    continue
                else:
                    construction += word
                    construction += i
                    word = ""
            else:
                word += i
            
        construction += word
        lcons = construction.split(" ")
        lcons.reverse()
        
        construction = ""
        for i in lcons:
            construction += i
            construction += " "
    
        return construction.rstrip().lstrip()
                
        