class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_st = set()
        col_st = set()
        diag_st = set()
        cnt=0
        for i in range(9):
            for section in range(9):
                
                diag_row = int((section%3) + ((i)%3)*3)
                diag_col = int((int(section/3)) + (((int(i/3))*3)))
                print("Group " + str(cnt))
                if board[section][i] not in row_st:
                    row_st.add(board[section][i])
                elif board[section][i]!='.':
                    print("hi")
                    return False

                if board[i][section] not in col_st:
                    col_st.add(board[i][section])
                elif board[i][section]!='.':
                    print("bye")
                    return False
                cnt+=1
                

                if board[diag_row][diag_col] not in diag_st:
                    diag_st.add(board[diag_row][diag_col])
                elif board[diag_row][diag_col]!= '.':
                    print("lol")
                    return False
            row_st.clear()
            col_st.clear()
            diag_st.clear()

        return True