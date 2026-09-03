class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i,holding):
            if i >= len(prices):
                return 0
            elif (i,holding) in memo:
                return memo[(i,holding)]

            nothing = dfs(i+1,holding)

            if holding:
                res = prices[i]+ dfs(i+2,False)
            else:
                res = dfs(i+1,True) - prices[i]

            memo[(i,holding)] = max(res,nothing)
            return memo[(i,holding)]


        return dfs(0,False)
