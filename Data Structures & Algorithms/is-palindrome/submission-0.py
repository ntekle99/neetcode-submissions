class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        rev_lst=[]
        lst = []
        for i in range(len(s)):
            if s[i].isalnum():
                lst.append(s[i])
        for i in range(len(s)):
            rev_i = len(s)-1-i
            if s[rev_i].isalnum():
                rev_lst.append(s[rev_i])
        return lst == rev_lst
            
        