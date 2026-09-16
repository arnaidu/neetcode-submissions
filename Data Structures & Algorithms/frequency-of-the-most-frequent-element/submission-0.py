class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, 0
        window_sum = 0

        window_size_max = 0

        cost = lambda r, l, s: nums[r] * (r - l + 1) - s

        while right < len(nums):
            # sum of elements in the current window
            window_sum += nums[right]

            # check if <= k ops
            c = cost(right, left, window_sum)

            while c > k:
                # remove leftmost
                window_sum -= nums[left]

                # move left side of window
                left += 1

                # recalculate cost
                c = cost(right, left, window_sum)
            
            window_size_max = max(window_size_max, right - left + 1)
            right += 1

        return window_size_max
            
            


        