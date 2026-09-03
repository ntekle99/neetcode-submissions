from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct = defaultdict(int)
        dct_2 = defaultdict(int)
        if len(t) != len(s):
            return False
        for i in range(len(s)):
            dct[s[i]] +=1
            dct_2[t[i]] +=1
        return dct == dct_2