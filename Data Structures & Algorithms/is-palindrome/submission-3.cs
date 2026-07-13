public class Solution {
    public bool IsPalindrome(string s) {
        var (left, right) = (0, s.Length - 1);
        while(left < right)
        {
            if(!char.IsLetterOrDigit(s[left]))
            {
                left++;
                continue;
            }

            if(!char.IsLetterOrDigit(s[right]))
            {
                right--;
                continue;
            }

            if(char.ToLower(s[left]) != char.ToLower(s[right]))
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
