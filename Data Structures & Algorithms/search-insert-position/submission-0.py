class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m - 1

        return l + 1 if target > nums[l] else l