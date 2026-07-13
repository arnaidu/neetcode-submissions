public class Solution {
    public bool IsPalindrome(string s) {
        var (left, right) = (0, s.Length - 1);
        while (left < right) {
            while (left < right && !char.IsLetterOrDigit(s[left])){
                left++;
            }

            while (left < right && !char.IsLetterOrDigit(s[right])) {
                right--;
            }

            // at this point we have letters if valid
            if (left < right && char.ToLower(s[left]) != char.ToLower(s[right])) {
                return false;
            }
            
            left++;
            right--;
        }

        return true;
    }
}
