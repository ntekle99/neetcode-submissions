class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm %2 == 1:
            return False
        
        memo = {}
        def dfs(i,target):
            if (i,target) in memo:
                return memo[(i,target)]
            if target == 0:
                return True
            if target < 0 or i == len(nums):
                return False


            res = dfs(i+1,target-nums[i])
            if res is False:
                res = dfs(i+1,target)
            
            memo[(i,target-nums[i])] = res
            return res

        return dfs(0,sm/2)
