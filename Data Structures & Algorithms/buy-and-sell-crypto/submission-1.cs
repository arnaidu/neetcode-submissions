public class Solution {
    public int MaxProfit(int[] prices) {
        var max_profit = 0;
        var buy = prices[0];
        for (int i = 1; i < prices.Length; i++) {
            if (prices[i] <= buy) {
                buy = prices[i];
            }
            else {
                max_profit = Math.Max(max_profit, prices[i] - buy);
            }
        }
        
        return max_profit;        
    }
}
