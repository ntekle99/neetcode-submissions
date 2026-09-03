class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(amount,j):
            if (amount,j) in memo:
                return memo[(amount,j)]
            if amount == 0:
                return 1
            if amount < 0:
                return 0

            total_cnt = 0
            for i in range(j,len(coins)):
                total_cnt += dfs(amount-coins[i],i)
            memo[(amount,j)] = total_cnt
            return total_cnt
        
        return dfs(amount,0)