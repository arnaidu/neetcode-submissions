public class Solution {
    public bool IsAnagram(string s, string t) {
        var charsS = s.ToCharArray();
        var charsT = t.ToCharArray();

        Array.Sort(charsS);
        Array.Sort(charsT);

        return new string(charsS) == new string(charsT);
    }
}
