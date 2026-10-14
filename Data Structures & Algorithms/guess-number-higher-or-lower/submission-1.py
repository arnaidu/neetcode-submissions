class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            pick = left + (right - left) // 2
            result = guess(pick)

            if result == 0:
                return pick
            elif result == 1:
                left = pick + 1
            else:
                right = pick - 1