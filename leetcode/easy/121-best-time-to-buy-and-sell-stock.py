class Solution(object):
    def maxProfit(self, prices):
        
        min_price = float('inf')
        max_profit = 0

        for curr in prices:
            if curr < min_price:
                min_price = curr
            else:
                max_profit = max(max_profit, curr - min_price)
        
        return max_profit
