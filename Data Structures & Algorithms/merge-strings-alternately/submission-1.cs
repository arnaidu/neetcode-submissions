public class Solution {
    public string MergeAlternately(string word1, string word2) {
        var ans = new List<char>();
        var (word1Length, word2Length) = (word1.Length, word2.Length);
        var k = 0;
        while (k < Math.Min(word1Length, word2Length)) {
            ans.Add(word1[k]);
            ans.Add(word2[k]);
            k++;
        }

        var remainingString = k == word1Length ? word2 : word1;
        while (k < remainingString.Length) {
            ans.Add(remainingString[k]);
            k++;
        }
        
        return string.Concat(ans);
    }
}