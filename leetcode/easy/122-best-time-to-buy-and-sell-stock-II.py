class Solution(object):
    def maxProfit(self, prices):
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit

# Both solutions work, but the above solution is seen as more traditonal / greedy algo.
      
#class Solution(object):
#    def maxProfit(self, prices):
#        
#        min_price = float('inf')
#        max_profit = 0
#
#        for curr in prices:
#            if curr < min_price:
#               min_price = curr
#            else:
#                max_profit += curr - min_price
#                min_price = curr
#
#        return max_profit
