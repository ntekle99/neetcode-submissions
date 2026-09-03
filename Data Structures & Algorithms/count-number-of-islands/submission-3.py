class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        c = len(grid)
        r = len(grid[0])
        total_islands = 0
        def dfs(i,j,st):

            if  i+1 < c and grid[i+1][j] == "1" and (i+1,j) not in st:
                st.add((i+1,j))
                dfs(i+1,j,st)

            if i-1 > -1 and grid[i-1][j] == "1" and (i-1,j) not in st:
                st.add((i-1,j))
                dfs(i-1,j,st)

            if j+1 < r and grid[i][j+1] == "1"  and (i,j+1) not in st:
                st.add((i,j+1))
                dfs(i,j+1,st)

            if j-1 > -1 and grid[i][j-1] == "1" and (i,j-1) not in st:
                st.add((i,j-1))
                dfs(i,j-1,st)
    
        st = set()
        for i in range(c):
            for j in range(r):
                if grid[i][j] == "1" and (i,j) not in st:
                    st.add((i,j))
                    dfs(i,j,st)
                    total_islands+=1
        return total_islands

        