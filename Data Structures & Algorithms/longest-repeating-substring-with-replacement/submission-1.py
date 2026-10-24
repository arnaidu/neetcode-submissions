from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count_single_char = 0
        window_char_counts = defaultdict(int)
        longest_substring = 0
        for right in range(len(s)):
            window_char_counts[s[right]] += 1

            max_count_single_char = max(
                max_count_single_char,
                window_char_counts[s[right]]
            )

            total = right - left + 1
            while total - max_count_single_char > k:
                window_char_counts[s[left]] -=1
                left += 1
                total -= 1
            
            longest_substring = max(longest_substring, total)
        return longest_substring



