public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        // consider window size min(nums.Length, k)
        var seen = new HashSet<int>();
        for (int i = 0; i < nums.Length; i++) {
            if (seen.Contains(nums[i])) {
                return true;
            }

            seen.Add(nums[i]);

            // if we just added the next item after sliding window
            //  then remove the i - k item
            if (seen.Count > k) {
                seen.Remove(nums[i - k]);
            }
        }

        return false;
    }
}