class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dct = {}
        for a, b in prerequisites:
            if a not in dct:
                dct[a] = []
            dct[a].append(b)

        visit = set()

        def dfs(key):
            if key in visit:
                return False
            if key not in dct:
                return True
            if len(dct[key]) == 0:
                return True
            
            visit.add(key)
            
            for pre in dct[key]:
                if not dfs(pre):
                    return False
            visit.remove(key)
            dct[key] = []
            return True

        total_cnt = 0
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
