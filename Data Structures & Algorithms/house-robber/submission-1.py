class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        

        def dfs(i, memo = {}):
            if i >= len(nums)-3:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(dfs(i+2)+nums[i+2], dfs(i+3)+nums[i+3])
            return memo[i]


        return max(dfs(0)+nums[0], dfs(1)+nums[1])


# [2,9,8,3,6]
# i = 2
# cap = 3