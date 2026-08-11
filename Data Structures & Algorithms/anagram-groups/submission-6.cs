public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> seen = [];
        foreach (var str in strs) {
            var arr = str.ToCharArray();
            Array.Sort(arr);
            string key = new string(arr);
            if (!seen.ContainsKey(key)) {
                seen[key] = [];
            }
            
            seen[key].Add(str);
        }

        return seen.Values.ToList();
    }
}
