class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}

        for i in nums:
            numsMap[i] = numsMap.get(i,0) + 1

        freqMap = [[] for i in range(len(nums)+1)]

        for key,v in numsMap.items():
            freqMap[v].append(key)

        res = []
        for i in range(len(nums),0,-1):
            for val in freqMap[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
        return res


