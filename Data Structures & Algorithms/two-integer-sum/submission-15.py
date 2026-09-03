from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = defaultdict(int)
        #(4,0),(3,1) (2,2) (1,3)
        for i in range(len(nums)):
            dct[target-nums[i]] = i
        
        # dct[3], dct[4], dct[5], dct[6]
        for i in range(len(nums)):
            if dct[nums[i]] and i!=dct[nums[i]]:
                return [min(i,dct[nums[i]]), max(i,dct[nums[i]])]


        