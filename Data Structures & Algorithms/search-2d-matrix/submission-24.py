class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        small_flag = False
        big_left = 0
        big_right = len(matrix)-1
        while big_left <= big_right:
            big_mid = (big_left + big_right) // 2
            # print("big_left " + str(big_left),"big right " + str(big_right), "big mid " + str(big_mid))
            # print(len(matrix))
            
            if matrix[big_mid][0] <= target <= matrix[big_mid][-1]:
                break
            elif matrix[big_mid][0] > target:
                big_right = big_mid - 1
            elif matrix[big_mid][0] < target:
                big_left = big_mid + 1
            else:
                return False

        small_left = 0
        small_right = len(matrix[big_mid])-1    
        while small_left <= small_right:
            small_mid = (small_left + small_right) // 2
            print(small_right,small_left,small_mid)
            if matrix[big_mid][small_mid] == target:
                return True
            if matrix[big_mid][small_mid] > target:
                small_right = small_mid -1
            if matrix[big_mid][small_mid] < target:
                small_left = small_mid + 1

        return False

