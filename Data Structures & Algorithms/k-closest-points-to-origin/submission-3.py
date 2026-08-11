import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = (x**2 + y**2) ** 0.5
            if len(heap) < k:
                heapq.heappush(heap, (-distance, [x, y]))
            else:
                if distance < -heap[0][0]:
                    heapq.heappushpop(heap, (-distance, [x, y]))

        return [p[1] for p in heap]
