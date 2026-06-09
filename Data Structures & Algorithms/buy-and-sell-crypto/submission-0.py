class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0
        sell_idx = 1
        max_profit = 0
        while sell_idx < len(prices):
            buy_amt = prices[buy_idx]
            sell_amt = prices[sell_idx]
            profit = sell_amt - buy_amt
            if profit > 0:
                max_profit = max(profit, max_profit)
                sell_idx += 1
            else:
                buy_idx += 1
                sell_idx = buy_idx + 1
        return max_profit



            