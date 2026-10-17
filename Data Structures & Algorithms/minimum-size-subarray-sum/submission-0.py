class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_length = n + 1
        curr_sum = 0
        for right in range(n):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return min_length if min_length <= n else 0
