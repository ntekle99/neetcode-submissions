class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset=[]
        def dfs(i,total):
            if target == total:
                res.append(subset.copy())
                return
            elif total > target or i >= len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1,total+candidates[i])

            subset.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,total)
        dfs(0,0)
        return res