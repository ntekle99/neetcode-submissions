from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in dct:
                return [dct[nums[i]],i] 
            dct[target-nums[i]] = i
            

        