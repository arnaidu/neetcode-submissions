public class Solution {
    public void SortColors(int[] nums) {
        var left = 0;
        var right = nums.Length - 1;
        var mid = 0;

        while (mid <= right) {
            // if 0, then swap with left side
            if (nums[mid] == 0){
                (nums[left], nums[mid]) = (nums[mid], nums[left]);
                left++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                // right can be 0 or 1
                (nums[right], nums[mid]) = (nums[mid], nums[right]);
                right--;
            }
        }
    }
}