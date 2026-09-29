public class Solution {
    public int FindJudge(int n, int[][] trust) {
        int[] inorder = new int[n];
        int[] trustFreq = new int[n];

        foreach (var pair in trust) {
            var a = pair[0];
            var b = pair[1];

            inorder[b - 1] += 1;
            trustFreq[a - 1] += 1;
        }

        for (int person = 0; person < n; person++) {
            if (inorder[person] == n - 1 && trustFreq[person] == 0) {
                return person + 1;
            }
        }

        return -1;
    }
}