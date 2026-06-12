class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            m = low + (high - low) // 2
            sqrt_squared = m * m
            if sqrt_squared == x:
                return m
            elif sqrt_squared > x:
                high = m - 1
            else:
                low = m + 1
        return high
