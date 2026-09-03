class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        curr_row = set()
        curr_col = set()
        curr_box = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] in curr_row:
                    print(curr_row,i,j)
                    print("gg")
                    return False
                elif board[i][j] !='.':
                    curr_row.add(board[i][j])
                if board[j][i] in curr_col:
                    print("lol")
                    return False
                elif board[j][i] !='.':
                    curr_col.add(board[j][i])

                box_row = (j%3) + (i%3)*3 
                box_col = int(int(j)/3) + int(int(i)/3)*3
                if board[box_row][box_col] in curr_box:
                    print("hi")
                    return False
                elif board[box_row][box_col]!='.':
                    curr_box.add(board[box_row][box_col])
            curr_row.clear()
            curr_col.clear()
            curr_box.clear()
        return True