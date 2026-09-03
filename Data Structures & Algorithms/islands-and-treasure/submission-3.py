from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        dq = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dq.append((i,j))
        
        while dq:
            i,j=dq.popleft()
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:                
                ni, nj = i + di, j + dj                
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj]== 2**31 - 1:
                    grid[ni][nj] = grid[i][j] + 1
                    dq.append((ni, nj))
