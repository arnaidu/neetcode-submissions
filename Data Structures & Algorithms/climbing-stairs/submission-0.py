class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n < 3:
            return dp[n - 1]

        for _ in range(2, n):
            k = dp[1] + dp[0]
            dp[0] = dp[1]
            dp[1] = k

        return dp[-1]