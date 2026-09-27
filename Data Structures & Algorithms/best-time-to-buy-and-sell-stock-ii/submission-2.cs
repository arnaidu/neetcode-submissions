public class Solution {
    public int MaxProfit(int[] prices) {
        int maxProfit = 0;
        int buy = prices[0]; // assume buy first day cause can sell if next day lower
        for (int day = 1; day < prices.Length; day++) {
            int wouldSellAt = prices[day];
            int profit = wouldSellAt - buy;
            if (profit >= 0) {
                // sell
                maxProfit += profit; 
            }

            buy = prices[day];
        }

        return maxProfit;
    }
}