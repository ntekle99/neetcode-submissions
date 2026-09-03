class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r=0
        mx_length = 0
        st = set()

        while r < len(s):
            if s[r] in st:
                st.remove(s[l])
                l+=1
            else:
                st.add(s[r])
                r+=1
                mx_length = max(mx_length,len(st))
        return mx_length

            
            
