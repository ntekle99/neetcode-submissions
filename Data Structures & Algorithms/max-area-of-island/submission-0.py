class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total = self.explore(grid, i, j, visited)
                if total > max_area:
                    max_area = total
        return max_area
            

    def explore(self,graph,r,c,visited):
        pos = (r,c)
        rowinBounds = (0 <= r < len(graph))
        colInBounds = (0 <= c < len(graph[0]))
        if pos in visited:
            return 0
        if not rowinBounds or not colInBounds:
            return 0
        if graph[r][c] == 0:
            return 0
        visited.add(pos)
        size = 1 
        size+=self.explore(graph,r+1,c,visited)
        size+=self.explore(graph,r-1,c,visited)
        size+=self.explore(graph,r,c+1,visited)
        size+=self.explore(graph,r,c-1,visited)

        return size