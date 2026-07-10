class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        previous_price = prices[0]
        for idx in range(1, len(prices)):
            curr_price = prices[idx]
            if curr_price > previous_price:
                # sell
                max_profit += (curr_price - previous_price)

                # then "buy" today
                previous_price = curr_price
            else:
                # set the previous_price (i.e. buy price to be curr_price)
                previous_price = curr_price
            
        return max_profit