from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        q = deque([])

        # grab all leafs
        for node, val in enumerate(degree):
            if val == 1:
                q.append(node)

        remaining_nodes = n
        while remaining_nodes > 2:
            num_leaves = len(q)

            for _ in range(num_leaves):
                node = q.popleft()

                for neighbour in graph[node]:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        q.append(neighbour)
            
            remaining_nodes -= num_leaves
        
        return list(q)

        

