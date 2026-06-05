class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        ndays = len(prices)
        curr_stock_price = prices[0]
        for day in range(1, ndays):
            # get price today
            today_price = prices[day]

            # if profitable sell
            if today_price > curr_stock_price:
                profit += today_price - curr_stock_price
            
            # rebuy in theory for next sell. In case tomorrow is less
            # then we won't get profit and instead will choose to have bought
            # on that day instead via this assignment
            curr_stock_price = today_price
        return profit
                
                

