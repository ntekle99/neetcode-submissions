from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = defaultdict(int)
        lst = [0] * (len(nums)+1)
        for i in range(len(nums)):
            dct[nums[i]]+=1

        #7:2
        
        for key in dct:
            if lst[dct[key]] == 0:
                lst[dct[key]] = [key]
            else:
                lst[dct[key]].append(key)

        final_lst=[]
        for i in range(len(lst)):
            if type(lst[len(lst)-i-1]) == list:
                for j in range(len(lst[len(lst)-i-1])):
                    final_lst.append(lst[len(lst)-i-1][j])
                    k-=1
                    if k == 0:
                        return final_lst
            else:
                if lst[len(lst)-i-1] != 0:
                    final_lst.append(lst[len(lst)-i-1])
                    k-=1
                    if k ==0:
                        return final_lst

            



        
        