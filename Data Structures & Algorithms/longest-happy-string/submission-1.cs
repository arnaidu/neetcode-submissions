public class Solution {
    public string LongestDiverseString(int a, int b, int c) {
        var pq = new PriorityQueue<(char ch, int count), int>();

        if (a > 0) pq.Enqueue(('a', a), -a);
        if (b > 0) pq.Enqueue(('b', b), -b);
        if (c > 0) pq.Enqueue(('c', c), -c);

        List<char> happyString = new();

        while (pq.Count > 0) {
            var first = pq.Dequeue();

            // If using this character creates 3 consecutive chars
            if (happyString.Count >= 2 &&
                happyString[^1] == first.ch &&
                happyString[^2] == first.ch) {

                // Need to use another character
                if (pq.Count == 0) {
                    break;
                }

                var second = pq.Dequeue();

                happyString.Add(second.ch);
                second.count--;

                if (second.count > 0) {
                    pq.Enqueue(second, -second.count);
                }

                // Put first character back
                pq.Enqueue(first, -first.count);
            }
            else {
                // Add up to two characters
                int use = Math.Min(2, first.count);

                for (int i = 0; i < use; i++) {
                    happyString.Add(first.ch);
                }

                first.count -= use;

                if (first.count > 0) {
                    pq.Enqueue(first, -first.count);
                }
            }
        }

        return new string(happyString.ToArray());
    }
}