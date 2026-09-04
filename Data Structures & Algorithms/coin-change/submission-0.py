class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        coins = [1, 2, 3, 6, 8, 12]
        amount = 21

        for the k-th amount where 0 <= k <= amount we can store
        min_coins_for_amount_k = []
        
        foreach k from 0 to amount
            foreach coin
                use coin then new amount_k' = amount_k - coins[i]
        """
        min_coins = [-1] * (amount + 1)
        min_coins[0] = 0
        for amount_k in range(1, amount + 1):
            minimum_amount = float("inf")
            for coin in coins:
                lower_amount = amount_k - coin
                if lower_amount >= 0 and min_coins[lower_amount] != -1:
                    minimum_amount = min(minimum_amount, min_coins[lower_amount] + 1)

            min_coins[amount_k] = minimum_amount if minimum_amount != float("inf") else -1
            
        return min_coins[-1]
                        