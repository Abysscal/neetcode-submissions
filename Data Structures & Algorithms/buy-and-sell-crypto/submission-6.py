class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        lowest = 0
        maxProfit = 0

        while r < len(prices) and l<len(prices):
            if r <=l:
                r+=1
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
                if prices[r] < prices[l]:
                    l= r
                else:
                    r+=1



        return maxProfit