class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num]+=1
        lst = []
        for num in dct:
            lst.append([dct[num],num])
        lst.sort(reverse=True)
        final_lst = []

        for i in range(k):
            final_lst.append(lst[i][1])
        return final_lst
        

        