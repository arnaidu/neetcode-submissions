public class Solution {
    public int SubsetXORSum(int[] nums) {
        return Explore(nums, 0, 0);
    }

    public int Explore(int[] nums, int index, int currentXor) {
        if (index == nums.Length) {
            return currentXor;
        }

        int include = Explore(nums, index + 1, currentXor ^ nums[index]);
        int exclude = Explore(nums, index + 1, currentXor);

        return include + exclude;
    }
}