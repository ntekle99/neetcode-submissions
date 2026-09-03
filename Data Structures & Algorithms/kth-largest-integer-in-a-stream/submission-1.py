import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        self.arr = nums
        self.perma_k = k  

    def add(self, val: int) -> int:
        heapq.heappush(self.arr,-val)
        print(self.arr)
        nums  = [0]*(self.perma_k)
        for i in range(self.perma_k):
            nums[i] = (heapq.heappop(self.arr))
        returned_num = nums[-1]

        for i in range(self.perma_k):
            heapq.heappush(self.arr,nums[self.perma_k-i-1])

        print(self.arr)
        return -returned_num

