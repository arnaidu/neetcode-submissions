import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for key, count in counts.items():
            print(key, count)
            if len(heap) < k:
                heapq.heappush(heap, (count, key))
            else:
                minimum = heap[0]
                if minimum[0] < count:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (count, key))
            print(heap)
        return [item[1] for item in heap]