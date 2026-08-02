public class Solution {
    public string ReorganizeString(string s) {
        Dictionary<char, int> freqs = s
            .GroupBy(o => o)
            .ToDictionary(o => o.Key, o => o.Count());
        
        PriorityQueue<(char ch, int count), int> pq = new();

        foreach (var kvp in freqs) {
            pq.Enqueue((kvp.Key, kvp.Value), -kvp.Value);
        }

        List<char> result = [];
        (char ch, int count)? prev = null;

         while (pq.Count > 0) {
            // grab next one
            var curr = pq.Dequeue();



            // add one we grabbed and reduce count, then track it to add
            // back on next loop
            result.Add(curr.ch);
            curr.count--;
            
            //  add back previous one
            if (prev is not null && prev.Value.count > 0) {
                pq.Enqueue(prev.Value, -prev.Value.count);
            }

            prev = curr;
        }

        if (prev is not null && prev.Value.count > 0) {
            return "";
        }

        return string.Join("", result);
    }
}