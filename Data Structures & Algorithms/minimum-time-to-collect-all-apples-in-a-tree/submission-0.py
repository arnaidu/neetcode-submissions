class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for i in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        

        def dfs(node, parent):
            time = 0
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                
                child_time = dfs(neighbour, node)
                
                if child_time > 0 or hasApple[neighbour]:
                    time += child_time + 2
            return time
            
        return dfs(0, -1)