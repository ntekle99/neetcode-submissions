class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array=[0]*len(nums)
        right_array=[0]*len(nums)
        size = len(nums)
        for i in range(size):
            #left_array = [1,2,8,48]
            #right_array = [48 48, 24,6]
            rev_index = size-1-i
            if i == 0:
                left_array[i] = nums[i]
                right_array[rev_index] = nums[rev_index]
            else:
                left_array[i] = nums[i] * left_array[i-1]
                right_array[rev_index] = nums[rev_index] * right_array[rev_index+1]
        final_lst =[0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                final_lst[i] = right_array[i+1]
            elif i == size-1:
                final_lst[i] = left_array[i-1]
            else:
                final_lst[i] = left_array[i-1] * right_array[i+1]
        return final_lst


        