class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1

        freqMap = defaultdict(list)

        for val, freq in hashmap.items():
            freqMap[freq].append(val)

        res = []
        for i in range(len(nums),0,-1):
            if freqMap[i]:
                while freqMap[i]:
                    res.append(freqMap[i].pop())
                    k -= 1
                    if k == 0:
                        return res

        return res