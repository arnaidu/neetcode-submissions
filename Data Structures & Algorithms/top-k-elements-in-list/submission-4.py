from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        heap = []
        for item, count in freqs.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (count, item))
            else:
                heapq.heappush(heap, (count, item))
        return [i[1] for i in heap]