public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        Array.Sort(strs);
        // compare first and last
        var first = strs[0];
        var last = strs[strs.Length - 1];
        string res = "";

        for (int i = 0; i < Math.Min(first.Length, last.Length); i++) {
            if (first[i] != last[i]) {
                break;
            }

            res += first[i];
        }

        return res;
    }
}