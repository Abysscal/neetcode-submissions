class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countdict = {}

        for i in nums:
            countdict[i] = countdict.get(i, 0) + 1

        freqlist = [[] for a in range(len(nums)+1)]
        for num,freq in countdict.items():
            freqlist[freq].append(num)

        res = []
        for freq in range(len(freqlist)-1, 0, -1):
            for value in freqlist[freq]:
                if k == 0:
                    break
                res.append(value)
                k-=1

        return res