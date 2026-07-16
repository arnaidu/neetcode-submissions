public class Solution {
    public List<List<int>> CombinationSum(int[] nums, int target) {
        List<List<int>> output = [];
        List<int> path = [];
        Explore(nums, target, output, path, 0);
        return output;
        
    }

    public void Explore(int[] nums, int target, List<List<int>> output, List<int> path, int startIndex) {
        if (path.Sum() == target) {
            // this is exactly true. Add to output and stop exploring.
            output.Add(path.ToList()); // create new list to avoid mutation
        }

        if (path.Sum() > target) {
            // stop exploring this path as can never work
            return;
        }

        for (int i = startIndex; i < nums.Length; i++) {
            var choose = nums[i];

            // Update combination path
            path.Add(choose);

            // Explore into this new combination
            Explore(nums, target, output, path, i);

            // Backtrack by undoing choice
            path.RemoveAt(path.Count - 1);
        }
    }
}
