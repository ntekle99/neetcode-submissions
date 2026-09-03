class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        mx = 0
        distance = r-l
        while l < r:
            print(mx,l,r)
            mx = max(mx,min(heights[l],heights[r])*distance)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            distance-=1
        return mx
