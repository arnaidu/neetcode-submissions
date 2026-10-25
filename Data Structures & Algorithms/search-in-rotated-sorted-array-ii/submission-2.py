class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            m = left + (right - left) // 2

            if nums[m] == target:
                return True

            if nums[left] == nums[m] == nums[right]:
                # we can't distinguish the sorted half
                left += 1
                right -= 1
                continue

            # left sorted
            if nums[left] <= nums[m]:
                # target in left half
                if nums[left] <= target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            elif nums[right] >= nums[m]:
                if nums[m] < target <= nums[right]:
                    left = m + 1
                else:
                    right = m - 1
        return False
            