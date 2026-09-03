class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # pointer_1 = 0
        # pointer_2 = 1
        cost.append(0)

        # for i in range(2,len(cost)):
        #     cost[i] = min(cost[pointer_1]+cost[i],cost[pointer_2]+cost[i])
        #     print(cost)
        #     pointer_1+=1
        #     pointer_2+=1
        # return cost[-1]
        def dfs(i,memo={}):
            if i >= len(cost)-2:
                return 0     
            if i in memo:
                return memo[i]
            memo[i] = min(dfs(i+1) + cost[i+1],dfs(i+2) + cost[i+2])
            return memo[i]
        return min(dfs(0)+cost[0],dfs(1)+cost[1])

        # [1,2,3]
        # i = 0
        # if i == 2
        # dfs(0) = (dfs(1)-> 0 + 2 + 0 + 0) + 1 + 0 + 2

# 1,2,1,2,1,1,1

# p = 0,1
# 1,2,2,4,3,4,4