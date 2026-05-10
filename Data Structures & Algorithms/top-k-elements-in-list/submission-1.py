class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topKhash = defaultdict(list)
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for value, c in count.items():
            topKhash[c].append(value)

        result = []
        for i in range(len(nums), 0, -1):
            if i in topKhash:
                result += topKhash[i]

        return result[:k]

