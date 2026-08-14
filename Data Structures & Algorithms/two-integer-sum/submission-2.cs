public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var compliments = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            int compliment = target - nums[i];
            if (compliments.TryGetValue(compliment, out var cIdx)) {
                return [Math.Min(i, cIdx), Math.Max(i, cIdx)];
            }

            compliments[nums[i]] = i;
        }

        return [];
    }
}
