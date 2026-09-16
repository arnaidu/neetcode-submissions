class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
    
        left = 0
        prod = 1
        num_subarrays = 0
        for right in range(len(nums)):
            prod *= nums[right]
            
            while prod >= k:
                prod //= nums[left]
                left += 1
            
            num_subarrays += (right - left + 1) # right - left + 1 is number new valid contiguous subarrays formed adding nums[right]
        return num_subarrays
            