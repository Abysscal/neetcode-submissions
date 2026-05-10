class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = count.get(i,0) + 1

        freq = [[] for i in range(len(nums)+1)]

        for index,(key,value) in enumerate(count.items()):
            freq[value].append(key)
        
        res = []
        for i in range(len(freq)-1, -1,-1):
            while freq[i] and k != 0:
                res.append(freq[i][-1])
                freq[i].pop()
                k-=1
        return res