class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i,state):
            print(memo)
            if i == len(prices):
                return 0
            if (i,state) in memo:
                return memo[(i,state)]

            if state == "cooldown":
                #-1 means on cooldown
                res = dfs(i+1,"can_buy")

            elif state == "can_buy":  
                # can buy can skip
                res = max(dfs(i+1,"can_sell")-prices[i],dfs(i+1,state))
                
            else: 
                # can sell or skip
                res = max(dfs(i+1,"cooldown")+prices[i],dfs(i+1,state))
            
            memo[(i,state)] = res
            return res
            

        return dfs(0,"can_buy")


        
            