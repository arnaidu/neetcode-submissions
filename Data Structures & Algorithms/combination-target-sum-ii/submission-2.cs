public class Solution {
    public List<List<int>> CombinationSum2(int[] candidates, int target) {
        List<List<int>> output = [];
        List<int> path = [];
        Array.Sort(candidates);
        Explore(candidates, target, path, output, 0);
        return output;
    }

    public void Explore(int[] candidates, int remainingTarget, List<int> path, List<List<int>> output, int startIndex) {
        if (remainingTarget == 0) {
            output.Add(path.ToList());
            return;
        }

        if (remainingTarget < 0) {
            return;
        }

        for (int i = startIndex; i < candidates.Length; i++) {
            var choice = candidates[i];
            if (i > startIndex && candidates[i] == candidates[i - 1]) {
                // skip duplicates
                continue;
            }
            path.Add(choice);
            Explore(candidates, remainingTarget - choice, path, output, i + 1);
            path.RemoveAt(path.Count - 1);
        }
    }
}
