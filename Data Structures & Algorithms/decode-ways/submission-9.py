class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        if s == "" or s[0] == "0":
            return 0

        def dfs(s,i):
            if len(s) == 0:
                return 1
            if s[0] == "0":
                return 0
            if len(s) == 1:
                return 1
            if i in memo:
                return memo[i]

            if (s[0] == "1" and s[1]!="0") or (s[0] == "2" and (s[1]!= "0" and s[1]!= "7" and s[1]!= "8" and s[1]!= "9")): 
                memo[i] = dfs(s[1:],i+1) + dfs(s[2:],i+2)
            elif (s[0] == "1" and s[1]=="0") or (s[0]=="2" and s[1]=="0"):
                memo[i] = dfs(s[2:],i+2)
            else:
                memo[i] = dfs(s[1:],i+1)

            return memo[i]
        return dfs(s,0)

            
