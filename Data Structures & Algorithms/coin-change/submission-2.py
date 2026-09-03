class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')

            min_res = float('inf')
            for c in coins:
                min_res = min(min_res,1+dfs(amount-c))

            memo[amount] = min_res
            return min_res
        
        res = dfs(amount)
        if res == float('inf'):
            return -1
        return res