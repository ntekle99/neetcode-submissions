class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def dfs(val):  
            if val in memo:
                return memo[val]
            if val == n:
                return 1
            elif val > n:
                return 0
            memo[val] = dfs(val+1) + dfs(val+2)
            return memo[val]
            
        return dfs(0)