class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]*len(nums)
        right_prod = [1]*len(nums)
        res=[]
        for i in range(1,len(nums)):
            left_prod[i] = left_prod[i-1]*nums[i-1]
            right_prod[len(nums)-1-i] = right_prod[len(nums)-i]*nums[len(nums)-i]
        for i in range(len(nums)):
            res.append(left_prod[i]*right_prod[i])
        return res