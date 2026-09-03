from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = defaultdict(int)
        for num in nums:
            dct[num]+=1
        lst = [[] for _ in range(len(nums) + 1)]
        for num in dct:
            lst[dct[num]].append(num)
        res = []
        for i in range(len(nums),-1,-1):
            for num in lst[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res