class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        c = len(grid)
        r = len(grid[0])
        x = [0]
        final_total = 0

        def dfs(i,j,x):
            if (i < 0 or i >= c or j < 0 or j >=r or grid[i][j]==0):
                return
            grid[i][j] = 0
            x[0]+=1

            dfs(i-1,j,x)
            dfs(i+1,j,x)
            dfs(i,j+1,x)
            dfs(i,j-1,x)


        for i in range(c):
            for j in range(r):
                if grid[i][j] == 1:
                    dfs(i,j,x)
                    final_total = max(final_total,x[0])
                    x[0] = 0
        return final_total