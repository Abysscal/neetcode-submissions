class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}

        for i in nums:
            countmap[i] = countmap.get(i,0) + 1

        freqmap = [[] for i in range(len(nums)+1)]

        for val, freq in countmap.items():
            freqmap[freq].append(val)
        
        res = []
        for i in range(len(nums), 0, -1):
            for c in freqmap[i]:
                res.append(c)
                k -= 1
                if k == 0:
                    return res
        
        return res 