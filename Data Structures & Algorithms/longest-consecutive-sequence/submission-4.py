class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        temp_iterator = 0
        mx_len = 0
        for i in range(len(nums)):
            if nums[i]-1 not in st:
                while nums[i]+1+temp_iterator in st:
                    temp_iterator+=1
                    print(nums[i]+1+temp_iterator)
                mx_len = max(mx_len,1+temp_iterator)
                temp_iterator = 0
        return mx_len