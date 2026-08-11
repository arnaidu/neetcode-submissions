public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> seen = [];
        foreach (var str in strs) {
            int[] freqs = new int[26];
            foreach (var ch in str) {
                freqs[ch - 'a']++;
            }
            string key = string.Join(",", freqs);
            if (!seen.ContainsKey(key)) {
                seen[key] = [];
            }
            
            seen[key].Add(str);
        }

        return seen.Values.ToList();
    }
}
