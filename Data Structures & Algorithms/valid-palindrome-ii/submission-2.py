class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        def isPalindrome(left, right, s):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(left + 1, right, s) or isPalindrome(left, right - 1, s)
            
            left += 1
            right -= 1
        return True;
