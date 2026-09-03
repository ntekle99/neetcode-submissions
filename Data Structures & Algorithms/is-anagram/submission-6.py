class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_1 = {}
        dct_2 = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in dct_1:
                dct_1[s[i]]+=1
            else:
                dct_1[s[i]] = 1
            if t[i] in dct_2:
                dct_2[t[i]]+=1
            else:
                dct_2[t[i]]=1
        
        print(dct_1,dct_2)
        for key in dct_1:
            if key not in dct_2:
                return False
            if dct_1[key] != dct_2[key]:
                return False
        return True
