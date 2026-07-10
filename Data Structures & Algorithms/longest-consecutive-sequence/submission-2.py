from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest = 0
        for num in elements:
            if num - 1 not in elements:
                # we are start of sequence so build sequence
                k = 1
                while num + k in elements:
                    k += 1
                longest = max(longest, k)
        return longest 


