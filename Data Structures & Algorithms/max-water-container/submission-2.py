class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1

        maxSize= 0

        while l < r:
            size = (r-l) * min(heights[l], heights[r])
            maxSize = max(maxSize, size)

            if heights[l] <= heights[r]:
                l +=1
            else:
                r-=1
        
        return maxSize
