from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = defaultdict(int)
        for i in range(len(nums)):
            dct[nums[i]]+=1
        lst = [[float('inf')]]*(len(nums)+1)
        for num in dct:
            print(dct[num])
            if lst[dct[num]] == [float('inf')]:
                lst[dct[num]] = [num]
            else:
                lst[dct[num]].append(num)
        print(lst)
        res = []
        for i in range(len(nums),-1,-1):
            if lst[i] == [float('inf')]:
                continue
            if len(res) == k:
                return res
            for num in lst[i]:
                res.append(num)
        return res