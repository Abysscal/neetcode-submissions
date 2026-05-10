class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for i in range(len(nums)+1)]

        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            if len(freq[i]) != 0:
                for c in freq[i]:
                    res.append(c)
                    if len(res) == k:
                        return res
