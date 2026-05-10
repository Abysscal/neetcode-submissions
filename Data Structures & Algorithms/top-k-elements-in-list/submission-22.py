class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return []
        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1

        freqMap = [[] for i in range(len(nums)+1)]

        for val, freq in hashmap.items():
            freqMap[freq].append(val)

        res = []
        for freq in range(len(nums),0,-1):
            for val in freqMap[freq]:
                res.append(val)
                if len(res) == k:
                    return res

