class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, curr = 0, 0
        while curr < len(nums):
            if nums[left] != nums[curr]:
                nums[curr], nums[left + 1] = nums[left + 1], nums[curr]
                left += 1
            curr += 1
        return left + 1