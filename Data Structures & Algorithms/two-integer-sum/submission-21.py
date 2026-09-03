class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            dct[target-nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in dct and i!= dct[nums[i]]:
                min_val = min(i,dct[nums[i]])
                max_val = max(i,dct[nums[i]])
                return [min_val,max_val]