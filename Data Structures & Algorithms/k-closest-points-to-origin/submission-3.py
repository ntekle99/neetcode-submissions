import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ordering_arr = []
        x1 = 0
        y1 = 0
        org_vals = []
        for x2,y2 in points:
            distance = (((x1-x2)**2) + ((y1-y2)**2))
            ordering_arr.append((distance,x2,y2))
            heapq.heappush(org_vals,(distance,x2,y2))
        final_lst = []
        while k!=0:
            x = heapq.heappop(org_vals)
            final_lst.append([x[1],x[2]])
            k-=1
        return final_lst
