import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for i in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if i[0]:
                heapq.heappush(heap, i)

        s = []
        while heap:
            element = heapq.heappop(heap)
            amount, ch = -element[0], element[1]
            if len(s) >= 2 and s[-1] == ch and s[-2] == ch:
                if not heap:
                    break
                
                next_chr_amount, ch2 = heapq.heappop(heap)
                next_chr_amount = -next_chr_amount

                s.append(ch2)
                next_chr_amount -= 1
                if next_chr_amount:
                    heapq.heappush(heap, (-next_chr_amount, ch2))
                
                heapq.heappush(heap, (-amount, ch))
            else:
                s.append(ch)
                amount -= 1
                if amount:
                    heapq.heappush(heap, (-amount, ch))
        return "".join(s)
            


