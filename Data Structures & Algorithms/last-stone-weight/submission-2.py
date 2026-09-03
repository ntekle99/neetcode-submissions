import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            greatest = -heapq.heappop(stones)
            second_greatest = -heapq.heappop(stones)
            if greatest != second_greatest:
                heapq.heappush(stones,-(greatest-second_greatest))
        if len(stones) == 0:
            return 0
        return -stones[0]