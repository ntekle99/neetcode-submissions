from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dq = deque()
        atl_st = set()
        pac_st = set()

        rows, cols = len(heights), len(heights[0])

        for j in range(cols):
            pac_st.add((0, j))
            dq.append((0, j))
            atl_st.add((rows-1, j))
            dq.append((rows-1, j))

        for i in range(rows):
            pac_st.add((i, 0))
            dq.append((i, 0))
            atl_st.add((i, cols-1))
            dq.append((i, cols-1))

        

        while dq:
            i,j = dq.popleft()
            for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if -1<ni<len(heights) and -1<nj<len(heights[0]) and heights[ni][nj] >= heights[i][j]:

                    if (i,j) in atl_st and (i,j) in pac_st and (ni,nj) not in pac_st and (ni,nj) not in atl_st:
                       atl_st.add((ni,nj))
                       pac_st.add((ni,nj))
                       dq.append((ni,nj))
                    if (i,j) in pac_st and (ni,nj) not in pac_st:
                        pac_st.add((ni,nj))
                        dq.append((ni,nj))

                    if (i,j) in atl_st and (ni,nj) not in atl_st:
                        atl_st.add((ni,nj))
                        dq.append((ni,nj))
        
        final_lst = []
        for i,j in atl_st:
            if (i,j) in pac_st:
                final_lst.append([i,j])

        return final_lst


