class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True
        if len(edges) == 1:
            if edges[0][0] == edges[0][1]:
                return False
            return True
        
        dct = {}
        unique_nums = set()
        for a,b in edges:
            if a not in dct:
                dct[a] = []
            if b not in dct:
                dct[b] = []
            dct[a].append(b)
            dct[b].append(a)

            if a not in unique_nums:
                unique_nums.add(a)
            if b not in unique_nums:
                unique_nums.add(b)
        
        print(dct)
        visit = set()   
        cycle = set()
        def dfs(node):
            if node in cycle:
                return True
            if node in visit:
                return False
            
            visit.add(node)
            cycle.add(node)
            for child in dct[node]:
                if not dfs(child):
                    return False
            cycle.remove(node)

            return True
    
        res = dfs(edges[0][0])
        if res == True and len(visit) == len(unique_nums):
            return True
        return False

        # Rule 1 one tree cant be pointed too by multiple trees
        # 0->1
        # 1->0
        # 1->2

        # 1->3 
        # 1->4
        