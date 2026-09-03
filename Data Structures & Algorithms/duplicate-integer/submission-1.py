class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_set = set()
        for i in range(len(nums)):
            dup_set.add(nums[i])
        print(dup_set)
        return len(dup_set) != len(nums)
        