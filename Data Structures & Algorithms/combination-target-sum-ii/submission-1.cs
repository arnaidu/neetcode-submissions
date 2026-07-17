public class Solution {
    public List<List<int>> CombinationSum2(int[] candidates, int target) {
        List<List<int>> output = [];
        List<int> path = [];
        Array.Sort(candidates);
        Explore(candidates, target, path, output, 0);
        return output;
    }

    public void Explore(int[] candidates, int target, List<int> path, List<List<int>> output, int startIndex) {
        if (path.Sum() == target) {
            output.Add(path.ToList());
            return;
        }

        if (path.Sum() > target) {
            return;
        }

        HashSet<int> seen = new();
        for (int i = startIndex; i < candidates.Length; i++) {
            var choice = candidates[i];
            if (seen.Contains(choice)) {
                // skip stuff we have already seen at this level
                continue;
            }
            seen.Add(choice);
            path.Add(choice);
            Explore(candidates, target, path, output, i + 1);
            path.RemoveAt(path.Count - 1);
        }
    }
}
