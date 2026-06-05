class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_valid_palindrome(s: str, l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return is_valid_palindrome(s, left + 1, right) or is_valid_palindrome(s, left, right - 1)
        return True
        

