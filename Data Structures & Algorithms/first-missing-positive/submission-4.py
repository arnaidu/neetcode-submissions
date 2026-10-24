class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(-1) # to ensure we have enough to hold 100,000 integers
        for num in nums:
            if num < 0 or num > n:
                continue

            k = num
            while 0 < k <= n and nums[k] != k:
                nums[k], k = k, nums[k]

        curr_smallest_int = 0
        for num in nums:
            if num - curr_smallest_int == 1:
                curr_smallest_int = num

        return curr_smallest_int + 1
            

            