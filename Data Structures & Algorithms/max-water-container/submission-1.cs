public class Solution {
    public int MaxArea(int[] heights) {
        int left = 0;
        int right = heights.Length - 1;
        int maxArea = 0;
        while (left < right) {
            int width = right - left;
            int height = Math.Min(heights[left], heights[right]);
            int currArea = height * width;
            maxArea = Math.Max(maxArea, currArea);
            if (heights[left] <= heights[right]) {
                left++;
            }
            else {
                right--;
            }
        }

        return maxArea;
    }
}
