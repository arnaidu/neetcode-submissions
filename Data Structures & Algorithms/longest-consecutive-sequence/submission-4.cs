public class Solution {
    public int LongestConsecutive(int[] nums) {
        var elements = new HashSet<int>();
        foreach (int num in nums) {
            elements.Add(num);
        }

        int longest = 0;

        foreach (int num in nums) {
            if (elements.Contains(num - 1)) {
                continue;
            }

            int count = 0;
            while (elements.Contains(num + count)) {
                count++;
            }

            longest = Math.Max(longest, count);
        }

        return longest;
    }
}
