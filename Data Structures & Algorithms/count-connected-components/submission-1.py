from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        def dfs(node):
            for neighbour in graph[node]:
                if neighbour in seen:
                    continue
                
                seen.add(neighbour)
                dfs(neighbour)
        
        num_connected = 0
        for node in range(n):
            if node in seen:
                continue

            seen.add(node)
            dfs(node)
            num_connected += 1

        return num_connected
        
