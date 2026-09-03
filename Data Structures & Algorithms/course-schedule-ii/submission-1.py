class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dct = {}
        for crs,preq in prerequisites:
            if crs not in dct:
                dct[crs] = []
            dct[crs].append(preq)

        print(dct)

        visit = set()   
        cycle = set()    
        lst = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            if crs not in dct:
                visit.add(crs)
                lst.append(crs)
                return True

            cycle.add(crs)
            for pre in dct[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)

            visit.add(crs)
            lst.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return lst



                