class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0

        for r in range(len(prices)):
            if l == r:
                continue

            profit = prices[r] - prices[l]
            res = max(profit, res)
            if prices[r] < prices[l]:
                l = r
            
        return res
