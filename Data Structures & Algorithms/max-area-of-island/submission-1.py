class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i,j) in visited or grid[i][j] == 0:
                return 0 
            visited.add((i,j)) 
            count = 1 
            print(counter)        
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in directions:
                count += dfs(i + dr,j + dc)
            return count

        max_num = 0
        counter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    counter = dfs(i,j)
                    if counter > max_num:
                        max_num = counter
                    counter = 0
        return max_num

        