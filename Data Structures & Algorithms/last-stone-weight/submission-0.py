class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        for i in range(len(stones)):
            heapq.heappush(arr,-stones[i])
        while len(arr) > 1:
            x = heapq.heappop(arr)
            y = heapq.heappop(arr)
            if x == y:
                pass
            else:
                diff = abs((-x) - (-y))
                heapq.heappush(arr,-diff)
        if len(arr) == 0:
            return 0
        return -arr[0]
