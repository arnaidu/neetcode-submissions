class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # house robber if we dont rob house 0
        prev1, prev2 = 0, 0
        for i in range(1, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current


        max1 = prev1
        prev1, prev2 = 0, 0

        #house robber if we don't rob house n - 1
        for i in range(0, len(nums) - 1):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        
        return max(max1, prev1)