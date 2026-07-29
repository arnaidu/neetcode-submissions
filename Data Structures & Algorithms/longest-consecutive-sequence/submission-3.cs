public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> elements = nums.ToHashSet();
        int longest = 0;
        for (int i = 0; i < nums.Length; i++) {
            int currNum = nums[i];
            // IF we hit the start of a sequence (i.e nothing exists before it)
            // then we can iterate through and figure out the lenght of this sequence
            if (!elements.Contains(currNum - 1)){
                int longestLocal = 1;
                int k = 1;
                while (elements.Contains(currNum + k)) {
                    longestLocal += 1;
                    k += 1;
                }
                
                longest = Math.Max(longestLocal, longest);  
            }
        }
        
        return longest;
    }
}