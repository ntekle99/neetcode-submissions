class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        self.Atlantic = False
        self.Pacific = False
        r = len(heights)
        c = len(heights[0])
# 5 5
        def dfs(i,j):
            if i == r-1 or j == c-1:
                self.Atlantic = True
            if i == 0 or j == 0:
                self.Pacific = True
            if self.Atlantic and self.Pacific:
                return
            
            st.add((i,j))
            
            if ((-1 < i < r-1) and heights[i][j] >= heights[i+1][j]) and (i+1,j) not in st:
                dfs(i+1,j)
            if ((0 < i < r) and heights[i][j] >= heights[i-1][j]) and (i-1,j) not in st:
                dfs(i-1,j)
            if ((-1 < j < c-1) and heights[i][j] >= heights[i][j+1]) and (i,j+1) not in st:
                dfs(i,j+1)
            if ((0 < j < c) and heights[i][j] >= heights[i][j-1])  and (i,j-1) not in st:
                dfs(i,j-1)

            st.remove((i,j))
            return 



        final_lst = []
        st = set()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                dfs(i,j)
                if self.Atlantic and self.Pacific:
                    final_lst.append([i,j])
                self.Atlantic = False
                self.Pacific = False
        return final_lst

