class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            prev = prices.copy()

            for start, end, price in flights:
                if prev[start] != float("inf"):
                    prices[end] = min(
                        prices[end],
                        prev[start] + price
                    )

        return prices[dst] if prices[dst] != float("inf") else -1