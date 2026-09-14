class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            k = left + (right - left) // 2 # middle of range
            num_coins = k * (k + 1) // 2
            if num_coins > n:
                # we need less coins
                right = k - 1
            elif num_coins <= n:
                # can potentially make another row
                left = k + 1

        return right