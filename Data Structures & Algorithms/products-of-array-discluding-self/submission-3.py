class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        left_prefix = 1
        for i in range(len(nums)):
            output[i] = left_prefix * output[i]
            left_prefix *= nums[i]
        
        right_prefix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] = output[j] * right_prefix
            right_prefix *= nums[j]
        
        return output
