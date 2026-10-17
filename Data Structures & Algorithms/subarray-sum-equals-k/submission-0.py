class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_prefix_sum = 0
        prev_subarray_prefix_sum_freqs = {0 : 1} # initialize cause 0 sum exists for empty list
        count = 0
        for i in range(len(nums)):
            curr_prefix_sum += nums[i]
            if curr_prefix_sum - k in prev_subarray_prefix_sum_freqs:
                count += prev_subarray_prefix_sum_freqs[curr_prefix_sum - k]
            
            if curr_prefix_sum not in prev_subarray_prefix_sum_freqs:
                prev_subarray_prefix_sum_freqs[curr_prefix_sum] = 1
            else:
                prev_subarray_prefix_sum_freqs[curr_prefix_sum] += 1
        
        return count

            