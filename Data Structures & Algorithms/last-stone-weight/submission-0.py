class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while stones and len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x-y == 0:
                continue
            else:
                newValue = abs(x-y)
                heapq.heappush(stones,-newValue)
        
        if stones:
            return -stones[-1]
        else:
            return 0