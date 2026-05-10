class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)

        count = [[] for i in range(len(nums)+1)]

        for n,c in hashMap.items():
            count[c].append(n)

        res = []
        for i in range(len(count)-1, 0, -1):
            if len(count[i]) != 0:
                for val in count[i]:
                    res.append(val)
                    if len(res) == k:
                        return res


