public class Solution {
    public bool CarPooling(int[][] trips, int capacity) {
        PriorityQueue<(int numPassengers, int from, int to), int> pq = new();
        Array.Sort(trips, (a, b) => a[1].CompareTo(b[1]));
        int currCapacity = capacity;
        foreach (var trip in trips) {
            (int numPassengers, int from, int to) = (trip[0], trip[1], trip[2]);

            // remove everyone who got out
            while (pq.Count > 0 && pq.Peek().to <= from) {
                var item = pq.Dequeue();
                currCapacity += item.numPassengers;
            }

            if (numPassengers > currCapacity) {
                return false;
            }

            // only if we have remaining capacity then enqueue
            pq.Enqueue((numPassengers, from, to), to);
            currCapacity -= numPassengers;
        }

        return true;
    }
}