class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [0]*len(nums)
        right_arr = [0]*len(nums)
        final_arr= [0]*len(nums)

        left_arr[0] = nums[0]
        for i in range(1,len(nums)):
            left_arr[i]=nums[i]*left_arr[i-1]

        right_arr[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            right_arr[i] = nums[i]*right_arr[i+1]
            
        final_arr[0] = right_arr[1]

        for i in range(1,len(nums)-1):
            final_arr[i] = left_arr[i-1]*right_arr[i+1]
        final_arr[-1]=left_arr[-2]

        return final_arr