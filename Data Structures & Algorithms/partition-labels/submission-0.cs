public class Solution {
    public List<int> PartitionLabels(string s) {
        Dictionary<char, int> freqs = s
            .ToCharArray()
            .GroupBy(o => o)
            .ToDictionary(o => o.Key, o => o.Count());
        
        List<int> sizes = [];

        HashSet<char> remaining = [];
        int count = 0;
        foreach (char ch in s) {
            // Track current substring size
            // If character not in remaining, then add to it
            remaining.Add(ch); // false if already in there
            // Reduce frequency by 1 and increment count by 1
            freqs[ch]--;
            count++;

            // if frequency hits 0, then we can remove from freqs and remaining
            if (freqs[ch] == 0) {
                freqs.Remove(ch);
                remaining.Remove(ch);
            }

            // if remaining is empty, then all chars seen until now have none
            // remaining so can log the count adding to List<int> sizes then
            // reset count
            if (remaining.Count == 0) {
                sizes.Add(count);
                count = 0;
            }
        }

        return sizes;
    }
}
