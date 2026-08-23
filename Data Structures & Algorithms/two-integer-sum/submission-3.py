class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        for idx, num in enumerate(nums):
            c = target - num
            if c in compliment:
                return [min(idx, compliment[c]), max(idx, compliment[c])]
            
            compliment[num] = idx;