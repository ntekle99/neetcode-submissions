class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dct_1 = {}
        dct_2 = {}
        for i in range(len(s)):
            if s[i] in dct_1:
                dct_1[s[i]]+=1
            else:
                dct_1[s[i]] = 1
            if t[i] in dct_2:
                dct_2[t[i]]+=1
            else:
                dct_2[t[i]] = 1

        if dct_2 == dct_1:
            return True
        return False
        