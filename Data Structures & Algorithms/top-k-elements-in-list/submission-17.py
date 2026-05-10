class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countdict = {}
        res = []

        for i in nums:
            countdict[i] = countdict.get(i,0) + 1

        freqtable = [[] for _ in range(0,len(nums)+1)]

        for val,count in countdict.items():
            freqtable[count].append(val)

        for i in range(len(freqtable)-1, 0, -1):
            for j in range(len(freqtable[i])):
                res.append(freqtable[i].pop())
                k -= 1
                if k == 0:
                    return res