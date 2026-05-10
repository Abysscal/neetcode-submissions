class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        res = 0

        for r in range(len(prices)):
            if r != l:
                if prices[r] - prices[l] > res:
                    res = prices[r] - prices[l]
                if prices[r] < prices[l]:
                    l = r

        return res
