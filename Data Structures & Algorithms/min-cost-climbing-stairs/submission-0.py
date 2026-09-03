class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pointer_1 = 0
        pointer_2 = 1
        cost.append(0)

        for i in range(2,len(cost)):
            cost[i] = min(cost[pointer_1]+cost[i],cost[pointer_2]+cost[i])
            print(cost)
            pointer_1+=1
            pointer_2+=1
        return cost[-1]


# 1,2,1,2,1,1,1

# p = 0,1
# 1,2,2,4,3,4,4