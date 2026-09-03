class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        if m == 1 and n == 1:
            return 1
        

        def dfs(i,l):
            if (i,l) in memo:
                return memo[(i,l)]
            if i == m-1 and l == n-1:
                return 0
            elif i == m-1 or l == n-1:
                return 1
            
            memo[(i,l)] = dfs(i+1,l) + dfs(i,l+1)
            return memo[(i,l)]
        
        return dfs(0,0)