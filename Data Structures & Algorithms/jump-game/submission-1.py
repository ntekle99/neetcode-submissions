class Solution:
    def canJump(self, nums: List[int]) -> bool:
        arr_2 = [None]*len(nums)
        arr_2[0] = True
        for i in range(len(nums)):
            jump_length = nums[i]
            if arr_2[i] == True:
                if i+jump_length >= len(nums):
                    return True
                for j in range(jump_length+1):
                    arr_2[i+j] = True
        if arr_2[-1] == None:
            return False
        return arr_2[-1]