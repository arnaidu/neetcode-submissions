from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def networkDelayTimeHelper(times: list[list[int]], n: int, k: int) -> int:
            graph = [[] for _ in range(n + 1)]

            for u, v, t in times:
                graph[u].append((t, v))
            
            heap = [(0, k)]
            seen = set()
            max_time = 0
            while heap:
                signal_time, node = heappop(heap)

                if node in seen:
                    continue
                
                max_time = max(max_time, signal_time)
                
                seen.add(node)
                
                for time_to_reach_neighbour, neighbour in graph[node]:
                    heappush(heap, (signal_time + time_to_reach_neighbour, neighbour))
            
            if len(seen) != n:
                return -1

            return max_time
        
        return networkDelayTimeHelper(times, n, k)