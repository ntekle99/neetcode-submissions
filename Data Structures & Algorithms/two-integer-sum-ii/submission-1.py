from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow_pointer = 0
        size = len(numbers)-1 
        fast_pointer = size    
        # 1,5,6,10,11 goal = 15

        while True:
            if numbers[slow_pointer] + numbers[fast_pointer] > target:
                fast_pointer -=1
            if numbers[slow_pointer] + numbers[fast_pointer] < target:
                slow_pointer+=1
            if numbers[slow_pointer] + numbers[fast_pointer] == target:
                return [slow_pointer+1,fast_pointer+1]


    


            

