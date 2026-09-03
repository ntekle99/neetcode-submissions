class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def dfs(stk,op,cl):
            if len(stk) == n*2:
                self.res.append(''.join(stk))
                return

            print(op,stk)
            if op < n:
                stk.append("(")
                dfs(stk,op+1,cl)
                stk.pop()
            
            if cl < op:
                stk.append(")")
                dfs(stk,op,cl+1)
                stk.pop()
        dfs([],0,0)
        return self.res

                 