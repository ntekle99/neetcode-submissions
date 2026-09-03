# a b c e
# s f e s
# a d e e


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board[0])
        c = len(board)
        self.res = False

        def dfs(i,j,k):
            print(i,j,k)
            if k == len(word):
                self.res = True
                return
            if (i > -1 and i < c and j > -1 and j < r and board[i][j] == word[k] and (i,j) not in st) is False:
                return
            else:
                st.add((i,j))
                dfs(i+1,j,k+1)
                dfs(i-1,j,k+1)
                dfs(i,j+1,k+1)
                dfs(i,j-1,k+1)
                st.remove((i,j))
                return


        st = set()
        for i in range(c):
            for j in range(r):
                if board[i][j] == word[0]:
                    res = dfs(i,j,0)
                    if self.res:
                        return True
        return False
