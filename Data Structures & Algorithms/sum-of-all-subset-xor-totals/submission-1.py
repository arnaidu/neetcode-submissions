class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = [0]
        self.explore(nums, 0, result, 0)
        return result[0]

    def explore(self, nums: List[int], startIndex: int, result: list[int], xorValue: int) -> int:
        result[0] += xorValue
        for i in range(startIndex, len(nums)):
            xorValue ^= nums[i]
            self.explore(nums, i + 1, result, xorValue)
            xorValue ^= nums[i]
    


