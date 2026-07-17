public class Solution {
    public List<List<int>> SubsetsWithDup(int[] nums) {
        List<List<int>> output = new();
        List<int> path = new();
        Array.Sort(nums);
        Explore(nums, 0, output, path);
        return output;
    }

    public void Explore(int[] nums, int startIndex, List<List<int>> output, List<int> path) {
        output.Add(path.ToList());
        for (int i = startIndex; i < nums.Length; i++) {
            int choice = nums[i];
            if (i > startIndex && nums[i] == nums[i - 1]) {
                continue;
            }

            path.Add(choice);
            Explore(nums, i + 1, output, path);
            path.RemoveAt(path.Count - 1);
        }
    }
}
