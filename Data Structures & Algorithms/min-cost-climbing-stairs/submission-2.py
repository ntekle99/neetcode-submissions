class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        cost.append(0)

        def dfs(i):
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i-1),dfs(i-2))
            return memo[i]
        
        return dfs(len(cost)-1)

        
            
        