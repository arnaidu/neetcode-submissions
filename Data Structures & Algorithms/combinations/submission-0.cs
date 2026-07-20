public class Solution {
    public List<List<int>> Combine(int n, int k) {
        List<List<int>> outputs = [];
        List<int> path = [];
        HashSet<int> seen = [];
        Explore(n, k, path, seen, outputs, 1);
        return outputs;
    }

    public void Explore(int n, int k, List<int> path, HashSet<int> seen, List<List<int>> outputs, int startIndex) {
        if (path.Count == k) {
            outputs.Add(path.ToList());
            return;
        }

        for (int i = startIndex; i <= n; i++) {
            path.Add(i);
            seen.Add(i);

            Explore(n, k, path, seen, outputs, i + 1);

            path.RemoveAt(path.Count - 1);
            seen.Remove(i);
        }
    }
}