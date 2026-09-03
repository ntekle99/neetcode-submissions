from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dq.append((i,j))
        
        total_min = -1
        while dq:
            size = len(dq)
            for _ in range(size):
                i,j = dq.popleft()
                for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if -1<ni<len(grid) and -1<nj<len(grid[0]) and grid[ni][nj] ==1:
                        grid[ni][nj] = 2
                        dq.append((ni,nj))
            total_min+=1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                    
        if total_min == -1:
            return 0
        return total_min
        
