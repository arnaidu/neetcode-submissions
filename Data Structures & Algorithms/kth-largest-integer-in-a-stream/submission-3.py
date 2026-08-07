import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [] # maintain at size k so heappop is k-th largest
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) >= self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)

        return self.heap[0]
