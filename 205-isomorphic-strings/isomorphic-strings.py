from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sdict = {}

        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]] = t[i]
            else:
                if t[i] != sdict[s[i]]:
                    return False
        
        if len(sdict) != len(set(sdict.values())):
            return False

        return True
