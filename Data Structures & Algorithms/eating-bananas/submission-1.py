class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid_rate = left + (right - left) // 2
            total_hours = 0
            for pile in piles:
                total_hours += pile // mid_rate + (pile % mid_rate != 0)

            if total_hours > h:
                # need to eat faster
                left = mid_rate + 1
            else:
                right = mid_rate - 1
        return left
        