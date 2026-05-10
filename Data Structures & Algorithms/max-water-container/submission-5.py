class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1

        biggest = 0

        while l<r:
            container = (r-l) * min(heights[l], heights[r])
            biggest = max(container, biggest)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return biggest