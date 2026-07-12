public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) {
            return false;
        }

        var counterS = new Dictionary<char, int>();
        var counterT = new Dictionary<char, int>();

        foreach (var ch in s) {
            if (counterS.TryGetValue(ch, out var count)) {
                counterS[ch] = count + 1;
            }
            else {
                counterS[ch] = 1;
            }
        }

        foreach (var ch in t) {
            if (counterT.TryGetValue(ch, out var count)) {
                counterT[ch] = count + 1;
            }
            else {
                counterT[ch] = 1;
            }
        }

        foreach (var kv in counterS) {
            var key = kv.Key;
            if (!counterT.ContainsKey(key) || counterT[key] != kv.Value) {
                return false;
            }
        }

        return true;
    }
}
