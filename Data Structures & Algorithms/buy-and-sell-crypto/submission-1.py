class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0 
        suffix = [0] * len(prices)
        temp = 0
        for i in range(len(prices)-1, -1, -1):
            
            if temp>prices[i]:
                suffix[i] = temp
            else:
                suffix[i] = 0
                temp = prices[i]

        for i in range(len(prices)):
            if suffix[i] == 0:
                continue
            else:
                profit = suffix[i] - prices[i]
                if profit>maxProfit:
                    maxProfit = profit

        return maxProfit