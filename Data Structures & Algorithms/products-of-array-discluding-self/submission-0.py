class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix_product = 1
        for prefix_idx in range(1, len(nums)):
            prefix_product *= nums[prefix_idx - 1]
            res[prefix_idx] = prefix_product
        
        suffix_product = 1
        for suffix_idx in range(len(nums) - 1, 0, -1):
            suffix_product *= nums[suffix_idx]
            res[suffix_idx - 1] *= suffix_product
        
        return res
