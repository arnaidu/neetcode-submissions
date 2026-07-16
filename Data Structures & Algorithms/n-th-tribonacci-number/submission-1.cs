public class Solution {
    public int Tribonacci(int n) {
        int[] prev = new int[] {0, 1, 1};
        if (n < 3) {
            return prev[n];
        }

        for (int i = 3; i <= n; i++) {
            int total = prev.Sum();
            (prev[0], prev[1], prev[2]) = (prev[1], prev[2], total);
        }

        return prev[^1];
    }
}