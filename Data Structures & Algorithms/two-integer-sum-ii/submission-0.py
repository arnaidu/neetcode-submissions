class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total > target:
                high -= 1 # reduce largest number
            elif total < target:
                low += 1 # get larger lower number
            else:
                break       
        return [low + 1, high + 1]