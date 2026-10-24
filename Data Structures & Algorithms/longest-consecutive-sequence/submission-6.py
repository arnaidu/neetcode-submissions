class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        seen = set(nums)
        sequence_starts = set()
        for num in nums:
            if num - 1 not in seen:
                sequence_starts.add(num)
        
        longest_consecutive_sequence = 1
        for num in sequence_starts:
            k = num
            curr_sequence_length = 1

            while k + 1 in seen:
                curr_sequence_length += 1
                k += 1

            longest_consecutive_sequence = max(
                longest_consecutive_sequence,
                curr_sequence_length)
        
        return longest_consecutive_sequence


