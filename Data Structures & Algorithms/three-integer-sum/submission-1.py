from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # optional early break: since sorted, no need if nums[i] > 0
            if nums[i] > 0:
                break

            l, r = i + 1, n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # skip duplicates for left pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # skip duplicates for right pointer
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res

