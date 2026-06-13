from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_nums = set(nums)
        sequence_lengths = defaultdict(int)
        seen = set()
        for num in unique_nums:
            if num in seen:
                continue

            # then num is start of sequence
            if num - 1 not in unique_nums:
                k = 0
                while num + k in unique_nums:
                    sequence_lengths[num] += 1
                    seen.add(num + k)
                    k += 1
        return max(sequence_lengths.values())
            
            


