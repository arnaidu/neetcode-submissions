public class Solution {
    public int FindJudge(int n, int[][] trust) {
        // This is a start graph which edges inwards to a center node being the judge
        int[] inDegree = new int[n];
        int[] outDegree = new int[n];
        foreach (var edge in trust) {
            var from = edge[0];
            var to = edge[1];

            inDegree[to - 1]++;
            outDegree[from - 1]++;
        }

        if (trust.Length > 0 && inDegree[trust[0][1] - 1] == n - 1 && outDegree[trust[0][1] - 1] == 0) {
            return trust[0][1];
        }

        return -1;
    }
}