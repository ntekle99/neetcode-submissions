class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1,1

        for n in nums:
            temp = currMax
            currMax = max(n*currMax,n*currMin,n)
            currMin = min(n*temp,n*currMin,n)
            res = max(res,currMax,currMin)
            
        return res
        
