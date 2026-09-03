from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct=defaultdict(int)
        for i in range(len(nums)):
            dct[nums[i]] = i
        if target % 2 == 0 and target / 2 in dct:
            temp=[]
            index=[]
            for i in range(len(nums)):
                if target / 2 == nums[i]:
                    temp.append(nums[i])
                    index.append(i)
                if len(temp) > 1:
                    return [index[0],index[1]]

        lst=[]
        print(dct)
        for i in range(len(nums)):
            if target-nums[i] in dct and target-nums[i] != target /2:
                lst.append(dct[nums[i]])
                lst.append(dct[target-nums[i]])
                return lst