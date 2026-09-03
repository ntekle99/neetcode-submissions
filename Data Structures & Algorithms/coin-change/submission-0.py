class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0

        memo = {}
        def dfs(curr):
            if curr in memo:
                return memo[curr]
            if curr == amount:
                return 0
            if curr > amount:
                return float('inf')

            min_val = float('inf')
            for coin in coins:
                res = dfs(curr+coin)
                if res !=float('inf'):
                    min_val = min(min_val,res+1)
            
            memo[curr] = min_val
            return memo[curr]

        res = (dfs(0))
        if res == float('inf'):
            return -1
        return res