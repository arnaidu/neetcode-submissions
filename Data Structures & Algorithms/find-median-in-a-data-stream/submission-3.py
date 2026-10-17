import heapq
class MedianFinder:

    def __init__(self):
        self.lower_half = []
        self.upper_half = []

    def addNum(self, num: int) -> None:
        if not self.lower_half:
            self.lower_half.append(-num)
        elif num <= -self.lower_half[0]:
            heapq.heappush(self.lower_half, -num)
        elif not self.upper_half:
            self.upper_half.append(num)
        elif num >= self.upper_half[0]:
            heapq.heappush(self.upper_half, num)
        else:
            # add to the smaller of the two
            if len(self.lower_half) < len(self.upper_half):
                heapq.heappush(self.lower_half, -num)
            else:
                heapq.heappush(self.upper_half, num)
        
        self._rebalance_halves()

    def findMedian(self) -> float:
        if len(self.lower_half) == len(self.upper_half):
            return (-self.lower_half[0] + self.upper_half[0]) / 2
        elif len(self.lower_half) < len(self.upper_half):
            return self.upper_half[0]
        else:
            return -self.lower_half[0]
    
    def _rebalance_halves(self) -> None:
        if len(self.lower_half) > 1 + len(self.upper_half):
            # take max from lower_half and add to upper_half
            max_lower_half = heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, -max_lower_half)

        if len(self.upper_half) > 1 + len(self.lower_half):
            min_upper_half = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -min_upper_half)
    
        