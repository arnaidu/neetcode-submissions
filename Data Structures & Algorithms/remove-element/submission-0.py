from collections import deque
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx_vals = deque([])
        count_vals = 0
        for idx in range(len(nums)):
            if nums[idx] == val:
                idx_vals.append(idx)
                count_vals += 1
            else:
                if idx_vals:
                    idx_seen_val = idx_vals.popleft()
                    nums[idx_seen_val], nums[idx] = nums[idx], nums[idx_seen_val]
                    idx_vals.append(idx)

        return len(nums) - count_vals