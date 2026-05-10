class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        highest = 0
        while l <r:
            vol = (r-l) * min(heights[l], heights[r])
            highest = max(vol, highest)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1

        return highest
