class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []


# 2,2,2,2
        def dfs(nums,target,lst):
            if target == 0:
                self.res.append(lst.copy())
                return
            if target < 0:
                return
            if len(nums) == 0:
                return
            
            lst.append(nums[0])
            dfs(nums,target-nums[0],lst)

            lst.pop()
            dfs(nums[1:],target,lst)
            return
        dfs(nums,target,[])
        return self.res