class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            sell = prices[i]
            if sell < buy:
                buy = sell
            
            if sell > buy:
                profit = sell - buy
                max_profit = max(max_profit, profit)
        return max_profit


            