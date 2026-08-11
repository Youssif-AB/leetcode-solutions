class Solution(object):
    def maxProfit(self, prices):
        cheapest = max(prices)
        bestprofit = 0

        for i in range(len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
            
            if prices[i] - cheapest > bestprofit:
                bestprofit = prices[i] - cheapest
        
        return bestprofit

                