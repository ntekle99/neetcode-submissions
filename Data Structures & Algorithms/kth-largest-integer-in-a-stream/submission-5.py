import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        for i in range(len(nums)):
            nums[i] = (nums[i])
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.arr = nums
        self.perma_k = k
        

    def add(self, val: int) -> int:
        if len(self.arr) < self.perma_k:
            heapq.heappush(self.arr,val)
        elif val > self.arr[0]:
            heapq.heappop(self.arr)
            heapq.heappush(self.arr,val)
        return self.arr[0]

        


