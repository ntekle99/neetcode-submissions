class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(total,i):
            if i==len(nums) and total == target:
                print("hi")
                return 1
            elif i==len(nums) and total!=target:
                return 0
            if (total,i) in memo:
                return memo[(total,i)]

            
            memo[(total,i)] = dfs(total+nums[i],i+1) + dfs(total-nums[i],i+1)
            return memo[(total,i)]

        return dfs(0,0)
        
        