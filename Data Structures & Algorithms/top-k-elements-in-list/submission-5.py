from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = defaultdict(int)
        for i in range(len(nums)):
            dct[nums[i]]+=1
        lst = [[] for _ in range(len(nums) + 1)]
        for num in dct:
            lst[dct[num]].append(num)
        res = []
        for i in range(len(nums),-1,-1):
            if lst[i] == [float('inf')]:
                continue
            if len(res) == k:
                return res
            for num in lst[i]:
                res.append(num)
        return res