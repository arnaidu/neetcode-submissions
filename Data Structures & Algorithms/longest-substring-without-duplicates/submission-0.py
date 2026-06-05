from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_length = 0
        seen_in_window = defaultdict(int)
        
        for right in range(len(s)):
            seen_in_window[s[right]] += 1

            while seen_in_window[s[right]] > 1:
                seen_in_window[s[left]] -= 1
                left += 1

            longest_length = max(longest_length, right - left + 1)


        return longest_length
