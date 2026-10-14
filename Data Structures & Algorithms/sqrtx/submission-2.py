class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            m = left + ((right - left) // 2)
            if m ** 2 == x:
                return m
            elif m**2 < x:
                left = m + 1
            else:
                right = m - 1
        return right