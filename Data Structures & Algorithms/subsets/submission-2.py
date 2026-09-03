class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(temp,lst):
            if len(temp) == 0:
                self.res.append(lst.copy())
                return
            lst.append(temp[0])
            dfs(temp[1:],lst)

            lst.pop()
            dfs(temp[1:],lst)
            return 
        dfs(nums,[])
        return self.res