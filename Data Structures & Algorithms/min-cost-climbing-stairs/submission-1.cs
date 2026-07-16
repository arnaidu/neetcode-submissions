public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        int[] dp = new int[2] { 0, 0 };

        for (int i = 2; i <= cost.Length; i++) {
            int total = Math.Min(dp[0] + cost[i - 2], dp[1] + cost[i - 1]);
            (dp[0], dp[1]) = (dp[1], total);

        }

        return dp[^1];
    }
}
