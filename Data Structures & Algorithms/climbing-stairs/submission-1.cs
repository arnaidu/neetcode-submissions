public class Solution {
    public int ClimbStairs(int n) {     
        int[] dp = new int[2] { 1, 2 };
        if (n < 3) {
            return dp[n - 1];
        }

        for (int i = 2; i < n; i++) {
            int numWays = dp[0] + dp[1];
            (dp[0], dp[1]) = (dp[1], numWays);
        }

        return dp[^1];
    }
}
