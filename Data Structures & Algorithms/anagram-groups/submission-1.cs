public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> anagrams = new();
        foreach (var str in strs) {
            var key = ComputeFrequencyKey(str);
            if (anagrams.ContainsKey(key)){
                anagrams[key].Add(str);
            }
            else {
                anagrams[key] = [str];
            }
        }

        return anagrams.Select(o => o.Value).ToList();
    }

    public string ComputeFrequencyKey(string str) {
        int[] freq = new int[26];
        foreach (var ch in str) {
            freq[ch - 'a']++;
        }

        return string.Join(",", freq);
    }
}
