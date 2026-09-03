class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        width = len(text1)
        height = len(text2)
        mat = []
        for i in range(height+1):
            row = [0] * (width+1)
            mat.append(row)
        for i in range(height,0,-1):
            for j in range(width,0,-1):
                if text1[j-1] == text2[i-1]:
                    mat[i-1][j-1] = 1 + mat[i][j]  
                else:
                    mat[i-1][j-1] = max(mat[i][j-1], mat[i-1][j])
        return mat[0][0]



            
                    

        
           

        
        