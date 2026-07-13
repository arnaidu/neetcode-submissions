public class Solution {
    public int SearchInsert(int[] nums, int target) {
        var (left, right) = (0, nums.Length - 1);
        while (left <= right) {
            var m = left + (right - left) / 2;
            if (nums[m] == target) {
                return m;
            }
            else if (nums[m] > target) {
                right = m - 1;
            }
            else {
                left = m + 1;
            }
        }

        return left;
    }
}