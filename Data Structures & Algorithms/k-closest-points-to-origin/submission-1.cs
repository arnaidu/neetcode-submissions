public class Solution {
    public int[][] KClosest(int[][] points, int k) {
        PriorityQueue<(int x, int y), double> pq = new();

        foreach (var point in points) {
            (int x, int y) = (point[0], point[1]);
            double distance = Math.Sqrt(x*x + y*y);
            if (pq.Count >= k) {
                pq.EnqueueDequeue((x, y), -distance);
            }
            else {
                pq.Enqueue((x, y), -distance);
            }
        }
        
        return pq.UnorderedItems
            .Select(o => new int[] { o.Element.x, o.Element.y })
            .ToArray();
    }
}
