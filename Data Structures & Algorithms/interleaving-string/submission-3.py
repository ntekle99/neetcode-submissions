class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        if len(s3) != (len(s1) + len(s2)):
            return False

        self.res = False
        self.size = len(s3) 

        def dfs(i,j,fake_s3):
            if (i,j) in memo:
                return memo[(i,j)]
            if len(fake_s3) == 0:
                self.res = True
                return
            if i+j == self.size:
                return

            if i < len(s1) and j < len(s2) and s1[i] == s3[i+j] and s2[j] == s3[i+j]:
                fake_s3 = fake_s3[1:]
                dfs(i+1,j,fake_s3)
                if self.res is False:
                    dfs(i,j+1,fake_s3)
            elif i < len(s1) and s1[i] == s3[i+j]:
                fake_s3 = fake_s3[1:]
                dfs(i+1,j,fake_s3)
            elif j < len(s2) and s2[j] == s3[i+j]:
                fake_s3 = fake_s3[1:]
                dfs(i,j+1,fake_s3)
            else:
                dfs(i+1,j,fake_s3)
                if self.res is False:
                    dfs(i,j+1,fake_s3)

            memo[(i,j)] = self.res
            return

        dfs(0,0,s3)
        return self.res
            

            