public class Solution {
    public int LengthOfLongestSubstring(string s) {
        HashSet<char> seen = new();

        int left = 0;
        int longest = 0;
        for (int right = 0; right < s.Length; right++){
            // if we've seen, remove everything until no longer duplicate
            while (seen.Contains(s[right])) {
                seen.Remove(s[left]);
                left++;
            }

            // now can add back
            seen.Add(s[right]);

            // longest is max of longest and what weve seen so far
            longest = Math.Max(longest, seen.Count);
        }

        return longest;
    }
}
