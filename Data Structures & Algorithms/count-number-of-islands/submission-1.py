class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        r = len(grid)
        c = len(grid[0])

        visited = set()

        def bfs(i,j):
            for dr,dl in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = i + dr, j + dl
                if 0 <= nr < r and 0 <= nc < c:
                        if grid[i+dr][j+dl] == '1' and (nr, nc) not in visited:
                            visited.add((i+dr,j+dl))
                            bfs(dr+i,dl+j)

        cnt = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and (i,j) not in visited:
                    visited.add((i,j))
                    cnt+=1
                    bfs(i,j)

        return cnt
