import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x == y:
                continue
            
            heapq.heappush(heap, -(abs(y - x)))
        
        return 0 if len(heap) == 0 else -heap[0]
