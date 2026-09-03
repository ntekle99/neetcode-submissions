class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s)-1
        while l < r:
            print(l,r)
            print(s[l],s[r])
            if s[l].isalnum() is False:
                l+=1
            elif s[r].isalnum() is False: 
                r-=1
            else:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False
        return True