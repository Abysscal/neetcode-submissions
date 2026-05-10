class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxArea = 0
        while l<r:
            lowestH = min(heights[l], heights[r])
            sum = lowestH * (r-l)

            maxArea = max(maxArea,sum)

            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1

        return maxArea