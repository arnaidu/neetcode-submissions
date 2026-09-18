class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_consecutive_ones = 0
        curr_consecutive_ones = 0
        num_flipped = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                while num_flipped >= k:
                    if nums[left] == 0:
                        num_flipped -= 1

                    curr_consecutive_ones -= 1
                    left += 1        
                
                num_flipped += 1

            curr_consecutive_ones += 1
            max_consecutive_ones = max(max_consecutive_ones, curr_consecutive_ones)
        
        return max_consecutive_ones