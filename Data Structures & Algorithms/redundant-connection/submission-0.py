class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(len(edges))]

        for idx, edge in enumerate(edges):
            a = edge[0] - 1
            b = edge[1] - 1
            graph[a].append((b, idx))
            graph[b].append((a, idx))
        
        seen = set()
        seen.add(0)

        def dfs(node, parent):
            for neighbour_node, neighbour_edge_idx in graph[node]:
                # skip self loops
                if neighbour_node == parent:
                    continue

                # we have loop, so return upwards
                if neighbour_node in seen:
                    return max(neighbour_edge_idx, 0), neighbour_node, True
                
                seen.add(neighbour_node)
                res = dfs(neighbour_node, node)
                if not res:
                    continue
                    
                idx, cycle_node, in_cycle = res
                if not in_cycle:
                    return idx, None, False
                
                # we hit last edge in cycle to check
                if in_cycle:
                    if cycle_node == node:
                        return max(neighbour_edge_idx, idx), None, False
                    else:
                        return max(neighbour_edge_idx, idx), cycle_node, True
        
        idx, _, _ = dfs(0, None)
        return edges[idx]
                    
                
