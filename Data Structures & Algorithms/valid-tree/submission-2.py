from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree is valid is number of edges = number of nodes - 1
        # and if there are no cycles

        edge_condition = len(edges) == n - 1
        if not edge_condition:
            return False
        
        has_cycles_condition = False
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)

        seen = set()
        seen.add(0)

        def dfs(node, parent):
            neighbours = graph[node]

            for neighbour in neighbours:
                if neighbour == parent:
                    continue

                if neighbour in seen:
                    return False

                seen.add(neighbour)

                if not dfs(neighbour, node):
                    return False

            return True

        return dfs(0, -1) and len(seen) == n # all nodes visited (so no disconected islands) and no cycles