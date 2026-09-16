class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        [2, 2, 6, 4, 6, 7]
        """
        nums.sort()
        left = 0
        min_difference = float("inf")
        for right in range(len(nums)):
            if right - left + 1 < k:
                continue
            
            min_difference = min(min_difference, nums[right] - nums[left])
            left += 1
        return min_difference
