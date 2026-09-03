class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        final_max = 0
        l_change = False
        if len(prices) <= 1:
            return 0

        while l < len(prices):
            print(r)
            print(l)
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                final_max = max(profit,final_max)
            else:
                l +=1
                l_change = True
            if r!=len(prices)-1:
                r+=1
            else:
                if l_change == True:
                    l_change = False
                else:
                    l+=1
        return final_max