import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        def num_gifts(gifts: list[int], k: int):
            max_heap = []
            total_num_gifts = 0
            for idx, num_gifts in enumerate(gifts):
                heapq.heappush(max_heap, (-num_gifts, idx))
                total_num_gifts += num_gifts
            
            for _ in range(k):
                max_num_gifts, pile = heapq.heappop(max_heap)
                new_num_gifts = ((-max_num_gifts) ** 0.5) // 1
                total_num_gifts -= (-max_num_gifts - new_num_gifts)
                heapq.heappush(max_heap, (-new_num_gifts, pile))
            
            return int(total_num_gifts)
        
        return num_gifts(gifts, k)