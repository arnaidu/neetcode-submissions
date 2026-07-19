public class Solution {
    public List<List<int>> Permute(int[] nums) {
        List<List<int>> output = [];
        List<int> path = [];
        HashSet<int> seen = [];
        Explore(output, path, nums, seen);
        return output;
    }  

    public void Explore(List<List<int>> output, List<int> path, int[] nums, HashSet<int> seen) {
        if (path.Count == nums.Length) {
            output.Add(path.ToList());
            return;
        }

        for (int i = 0; i < nums.Length; i++) {
            if (seen.Contains(i)) {
                continue;
            }

            // select first number for permutation
            path.Add(nums[i]);
            seen.Add(i);

            // explore search space, but now reduce search to remaining elements only for
            // next selection
            Explore(output, path, nums, seen);

            // remove selection to use other selection cause order matters
            path.RemoveAt(path.Count - 1);
            seen.Remove(i);
        }
    }
}
