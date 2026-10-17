class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        if not self.stock:
            self.stock.append((price, 1))
        else:
            count = 0
            while self.stock and self.stock[-1][0] <= price:
                _, span = self.stock.pop()
                count += span
            self.stock.append((price, count + 1))

        return self.stock[-1][1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)