class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0 

        for i in range(len(prices)-1):
            nextValues = prices[i+1:]
            newProfit = max(nextValues) - prices[i]

            if newProfit>maxProfit:
                maxProfit = newProfit

        return maxProfit