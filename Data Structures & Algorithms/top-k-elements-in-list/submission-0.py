class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        maxVal = max(counter, key= counter.get)
        res = []
        for i in range(k):
            res.append(maxVal)
            counter[maxVal] = -1
            maxVal = max(counter, key= counter.get)
        
        return res