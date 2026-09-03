class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        def dfs(candidates,target,lst):
            if target == 0:
                self.res.append(lst.copy())
                return
            if target < 0 or len(candidates) == 0:
                return

            lst.append(candidates[0])
            dfs(candidates[1:],target-candidates[0],lst)
            lst.pop()
            i = 0
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i += 1
            
            dfs(candidates[i+1:],target,lst)
            return
        dfs(candidates,target,[])
        return self.res