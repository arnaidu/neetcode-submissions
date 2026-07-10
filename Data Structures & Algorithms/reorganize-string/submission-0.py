from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freqs = Counter(s)

        heap = []
        for char, freq in freqs.items():
            heapq.heappush(heap, (-freq, char))

        ans = []

        while heap:
            freq1, char1 = heapq.heappop(heap)

            if heap:
                freq2, char2 = heapq.heappop(heap)

                ans.append(char1)
                ans.append(char2)

                freq1 += 1
                freq2 += 1

                if freq1 < 0:
                    heapq.heappush(heap, (freq1, char1))

                if freq2 < 0:
                    heapq.heappush(heap, (freq2, char2))

            else:
                # only one character left with duplicates
                if freq1 < -1:
                    return ""

                ans.append(char1)

        return "".join(ans)
