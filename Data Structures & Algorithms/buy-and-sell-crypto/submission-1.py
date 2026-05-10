class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r = 0,1
        gainz = 0
        while r < len(prices):
            price = prices[r] -prices[l]
            gainz = max(price, gainz)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return gainz