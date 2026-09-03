class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        size = len(nums)-2
        def dfs(curr,nums):
            if curr in memo:
                return memo[curr]
            if curr == 0:
                return nums[curr]
            elif curr < 0:
                return 0
            
            memo[curr] = max(dfs(curr-2,nums),dfs(curr-3,nums)) + nums[curr]
            print(memo)
            return memo[curr]

        output_1 = dfs(size,nums[1:])
        memo.clear()
        output_2 = dfs(size-1,nums[1:])
        memo.clear()
        output_3 = dfs(size,nums[:-1])
        memo.clear()
        output_4 = dfs(size-1,nums[:-1])
        print(output_1,output_2,output_3,output_4)
        return max(output_1,output_2,output_3,output_4)

        
        