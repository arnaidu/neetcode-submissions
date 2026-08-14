public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        var p1 = m - 1;
        var p2 = n - 1;
        var k = m + n - 1;
        while (k >= 0) {
            if (p1 >= 0 && p2 >= 0 && nums1[p1] >= nums2[p2]) {
                nums1[k] = nums1[p1]; 
                p1 -= 1;
            } else if (p2 >= 0) {
                nums1[k] = nums2[p2];
                p2 -= 1;
            }

            k--;
        }
    }
}