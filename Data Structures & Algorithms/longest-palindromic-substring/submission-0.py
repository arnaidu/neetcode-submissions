class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left + 1, right - 1
        
        max_length = 0
        string_start = 0
        string_end = 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)
            odd_length = r1 - l1 + 1
            even_length = r2 - l2 + 1
            if odd_length > max_length:
                string_start = l1
                string_end = r1
                max_length = odd_length
            
            if even_length > max_length:
                string_start = l2
                string_end = r2
                max_length = even_length
            
        return s[string_start:string_end + 1]
