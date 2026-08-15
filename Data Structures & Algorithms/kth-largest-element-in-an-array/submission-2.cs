public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        var heap = new PriorityQueue<int, int>();
        foreach (var num in nums) {
            heap.Enqueue(num, num);
            if (heap.Count > k) {
                heap.Dequeue();
            }
        }

        return heap.Dequeue();
    }
}
