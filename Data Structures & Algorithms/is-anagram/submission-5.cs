public class Solution {
    public bool IsAnagram(string s, string t) {
        var freqS = new Dictionary<char, int>();

        foreach (var ch in s) {
            if (!freqS.ContainsKey(ch)) {
                freqS[ch] = 0;
            }

            freqS[ch] += 1;
        }

        foreach (var ch in t) {
            if (!freqS.ContainsKey(ch)) {
                return false;
            }

            freqS[ch] -= 1;
            if (freqS[ch] == 0) {
                freqS.Remove(ch);
            }
        }

        return freqS.Count == 0;
    }
}
