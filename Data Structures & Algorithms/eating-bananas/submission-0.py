import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        l, r = 1, max_k
        while l < r:
            k = l + (r - l) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                r = k
            else:
                l = k + 1
        return l
            
            