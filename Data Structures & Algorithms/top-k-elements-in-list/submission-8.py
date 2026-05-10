class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)


        freq = [[] for i in range(len(nums)+1)]
        for n,c in hashmap.items():
            freq[c].append(n)

        res = []
        for i in range(len(nums), 0, -1):
            for w in freq[i]:
                res.append(w)
                if len(res) == k:
                    return res
