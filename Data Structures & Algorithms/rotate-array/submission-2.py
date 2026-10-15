
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return

        k %= n
        seen = set()

        for start in range(n):
            if start in seen:
                continue

            curr = start
            curr_val = nums[curr]

            while curr not in seen:
                seen.add(curr)

                next_idx = (curr + k) % n
                next_val = nums[next_idx]

                nums[next_idx] = curr_val

                curr_val = next_val
                curr = next_idx
