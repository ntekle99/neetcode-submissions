class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        final_max = 0
        l_change = False
        if len(prices) <= 1:
            return 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                final_max = max(profit,final_max)
            else:
                l = r
            r+=1
        return final_max