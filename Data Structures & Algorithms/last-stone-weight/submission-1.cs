public class Solution {
    public int LastStoneWeight(int[] stones) {
        var pq = new PriorityQueue<int, int>();
        for (int i = 0; i < stones.Length; i++) {
            pq.Enqueue(stones[i], -stones[i]);
        }

        while (pq.Count > 1) {
            var heaviest = pq.Dequeue();
            var secondHeaviest = pq.Dequeue();

            if (heaviest != secondHeaviest) {
                var newWeight = Math.Abs(heaviest - secondHeaviest);
                pq.Enqueue(newWeight, -newWeight);
            }
        }

        return pq.Count == 1 ? pq.Peek() : 0;
    }
}
