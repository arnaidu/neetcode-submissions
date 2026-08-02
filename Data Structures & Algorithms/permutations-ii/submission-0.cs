public class Solution {
    public List<List<int>> PermuteUnique(int[] nums) {
        Array.Sort(nums);
        List<List<int>> output = [];
        List<int> path = [];
        bool[] used = new bool[nums.Length];
        Explore(output, path, nums, used);
        return output;
    }

    public void Explore(List<List<int>> output, List<int> path, int[] nums, bool[] used) {
        if (path.Count == nums.Length) {
            output.Add(path.ToList());
            return;
        }

        for (int i = 0; i < nums.Length; i++) {
            if (used[i]) {
                continue;
            }

            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
                continue;
            }

            path.Add(nums[i]);
            used[i] = true;

            Explore(output, path, nums, used);

            used[i] = false;
            path.RemoveAt(path.Count - 1);
        }
    }
}