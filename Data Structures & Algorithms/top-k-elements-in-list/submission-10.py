class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = dict()
        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        freqList = [ [] for i in range(len(nums)+1)]

        for key,value in numCount.items():
            freqList[value].append(key)

        topk = []

        for i in range(len(freqList)-1, 0, -1):
            while freqList[i]:
                topk.append(freqList[i].pop())
                k-=1
                if k == 0:
                    return topk