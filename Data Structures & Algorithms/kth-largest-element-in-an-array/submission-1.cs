public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        var pq = new PriorityQueue<int, int>();
        foreach (var num in nums) {           
            if (pq.Count < k) {
                pq.Enqueue(num, num);
            }
            else if (pq.Peek() < num) {
                pq.EnqueueDequeue(num, num);
            }
        }
        
        return pq.Dequeue();
    }
}