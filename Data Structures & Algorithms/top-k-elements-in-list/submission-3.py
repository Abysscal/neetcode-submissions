class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)

        freq = [[] for i in range(len(nums)+1)]
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for pos in range(len(freq)-1,-1,-1):
            if len(freq[pos]) != 0:
                for n in freq[pos]:
                    res.append(n)
                    if len(res) == k:
                        return res 