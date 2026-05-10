class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 0

        richest = 0

        while r < len(prices):
            if l == r:
                r+=1
            elif prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                richest = max(profit, richest)
                r +=1
        return richest
                
                    
                
                