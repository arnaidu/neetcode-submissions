public class Solution {
    public List<List<int>> Subsets(int[] nums) {
        List<List<int>> output = [];
        List<int> path = [];
        Explore(nums, output, path, 0);
        return output;
    }

    public void Explore(int[] nums, List<List<int>> output, List<int> path, int index) {
        // Add subset previsouly created
        output.Add(path.ToList());

        // If we created subset equal size of full set, then we are done
        if (index == nums.Length) {
            return;
        }

        for (int i = index; i < nums.Length; i++){
            var choose = nums[i];
            path.Add(choose);
            Explore(nums, output, path, i + 1);
            path.RemoveAt(path.Count - 1);
        }
    }
}
