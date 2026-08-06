class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_idx:
                j = num_idx[complement]
                return [i, j] if i < j else [j, i]
            num_idx[num] = i
        
