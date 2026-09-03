class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        mx_len = 1
        mx_str = s[0]
        
        l,r = 0,0
        for i in range(len(s)):
                l,r = i-1,i+1
                temp_str = s[i]
                temp_len = 1

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    temp_len +=2
                    temp_str = s[l] + temp_str + s[r] 
                    
                    if temp_len > mx_len:
                        mx_len = temp_len
                        mx_str = temp_str
                    l-=1
                    r+=1

        for i in range(1,len(s)):
            l,r = i-1,i

            if l >= 0 and r < len(s) and s[l] == s[r]:
                temp_str = s[l] + s[r]
                temp_len = 2
                if temp_len > mx_len:
                        mx_len = temp_len
                        mx_str = temp_str
                l-=1
                r+=1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    temp_len +=2
                    temp_str = s[l] + temp_str + s[r] 
                    if temp_len > mx_len:
                        mx_len = temp_len
                        mx_str = temp_str
                    l-=1
                    r+=1

        return mx_str
             
                

            