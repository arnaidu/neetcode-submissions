import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for p in points:
            x, y = p
            d = (x**2 + y**2) ** 0.5
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-d, p))
            else:
                heapq.heappushpop(maxHeap, (-d, p))
        return [p[1] for p in maxHeap]

            