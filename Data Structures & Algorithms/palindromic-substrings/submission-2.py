class Solution:
    def countSubstrings(self, s: str) -> int:

        def palin(l,r,res):
            for i in range(len(s)):
                if r < len(s) and s[l] == s[r]:
                    print([l],[r])
                    res+=1
                    if l > 0 and r < len(s)-1:
                        temp_l=l-1
                        temp_r=r+1
                        while s[temp_l] == s[temp_r]:
                            print([temp_l],[temp_r])
                            res+=1
                            if temp_l > 0 and temp_r < len(s)-1:
                                temp_l-=1
                                temp_r+=1
                            else:
                                break
                l+=1
                r+=1
            return res

        return palin(0,0,0) + palin(0,1,0)       

        