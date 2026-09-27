public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int nums1Index = m - 1;
        int nums2Index = n - 1;
        for (int k = m + n - 1; k >= 0; k--) {
            if (nums2Index < 0) {
                break;
            }

            if (nums1Index < 0 || nums1[nums1Index] <= nums2[nums2Index]) {
                nums1[k] = nums2[nums2Index];
                nums2Index--;
            } else {
                nums1[k] = nums1[nums1Index];
                nums1Index--;
            }
        }
    }
}