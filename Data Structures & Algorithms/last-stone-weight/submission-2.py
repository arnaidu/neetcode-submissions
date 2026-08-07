import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for weight in stones:
            heapq.heappush(heap, -weight)
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap) # will be lighter
            if x == y:
                continue
            
            heapq.heappush(heap, -(x - y))
        
        return 0 if not heap else -heap[0]


        
