class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        def dfs(i,j):
            if (i < 0 or i >= rows) or (j < 0 or j >= cols) or (grid[i][j]=='0') or ((i,j) in visited):
                return
            visited.add((i,j))
            directions =[[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in directions:
                dfs(i+dr,j+dc)

        islands = 0
        for i in (range(rows)):
            for j in (range(cols)):
                if (i,j) not in visited and grid[i][j] == '1':
                    dfs(i,j)
                    islands +=1
        return islands