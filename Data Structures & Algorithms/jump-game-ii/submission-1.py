class Solution:
    def jump(self, nums: List[int]) -> int:
        arr_2 = [0]*(len(nums))
        for i in range(len(nums)):
            jump_length = nums[i]
            if (jump_length + i) > len(nums)-1:
                jump_length = len(nums)-1-i
            curr_val = arr_2[i]
            if jump_length == 0:
                continue
            for j in range(jump_length+1):
                if arr_2[i+j] == 0:
                    arr_2[i+j]=1+curr_val
                else:
                    arr_2[i+j]=min(arr_2[i+j],1+curr_val)
        return arr_2[-1]