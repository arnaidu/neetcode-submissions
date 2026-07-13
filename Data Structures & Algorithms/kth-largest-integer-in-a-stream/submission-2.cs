public class KthLargest {

    private PriorityQueue<int, int> _pq = new PriorityQueue<int, int>();
    private int _k = 0;

    public KthLargest(int k, int[] nums) {
        _k = k;

        foreach (var num in nums) {
            Add(num);
        }
    }
    
    public int Add(int val) {
        _pq.Enqueue(val, val);
        if (_pq.Count > _k) {
            _pq.Dequeue();
        }
        return _pq.Peek();
    }
}
