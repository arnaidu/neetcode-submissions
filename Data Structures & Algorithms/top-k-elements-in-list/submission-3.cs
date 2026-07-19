public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> freqMap = new();
        foreach (var num in nums) {
            if (!freqMap.TryGetValue(num, out var value))
            {
                freqMap[num] = 0;
            }
            
            freqMap[num]++;
        }

        PriorityQueue<int, int> pq = new PriorityQueue<int, int>();
        foreach (var pair in freqMap)
        {
            var num = pair.Key;
            var freq = pair.Value;
            if (pq.Count == k)
            {
                pq.EnqueueDequeue(num, freq);
            }
            else
            {
                pq.Enqueue(num, freq);
            }
        }
        
        return pq.UnorderedItems.Select(o => o.Element).ToArray();
    }
}
