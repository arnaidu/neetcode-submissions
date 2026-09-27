public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int left = 0;
        Dictionary<char, int> freq = new();
        int longestSubstringNoDups  = 0;
        for (int right = 0; right < s.Length; right++) {
            if (!freq.ContainsKey(s[right])) {
                freq[s[right]] = 0;
            }

            freq[s[right]]++;             

            while (freq[s[right]] > 1) {
                // we encountered a duplicate, so
                freq[s[left]]--;
                left++;
            }

            longestSubstringNoDups = Math.Max(longestSubstringNoDups, right - left + 1);
        }

        return longestSubstringNoDups;
    }
}
