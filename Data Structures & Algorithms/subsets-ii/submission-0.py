class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
# F T F
# 2  
        def dfs(nums,lst):
            if len(nums) == 0:
                self.res.append(lst.copy())
                return

            lst.append(nums[0])
            dfs(nums[1:],lst)

            lst.pop()
            i = 0
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(nums[i+1:],lst)
            return

        dfs(nums,[])
        return self.res