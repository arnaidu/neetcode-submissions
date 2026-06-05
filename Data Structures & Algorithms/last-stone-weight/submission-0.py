import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def lastStoneWeight(stones: list[int]) -> int:
            maxHeap = [-s for s in stones]
            heapq.heapify(maxHeap)

            while len(maxHeap) > 1:
                firstLargest = -heapq.heappop(maxHeap)
                secondLargest = -heapq.heappop(maxHeap)
                if firstLargest == secondLargest:
                    continue

                heapq.heappush(maxHeap, -(abs(secondLargest - firstLargest)))
            
            return -maxHeap[0] if maxHeap else 0
        return lastStoneWeight(stones)