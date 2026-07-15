class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0 
        minPrice = float('inf') 
        for i in prices:
            minPrice = min(minPrice, i)
            profit = i - minPrice
            if profit > maxProfit:
                maxProfit = profit

        return maxProfit