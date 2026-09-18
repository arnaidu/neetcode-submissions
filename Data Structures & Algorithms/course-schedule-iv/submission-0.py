from collections import deque, defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for i in range(numCourses)]
        inorder = [0] * numCourses

        for a, b in prerequisites:
            graph[a].append(b)
            inorder[b] += 1
        
        q = deque([])

        for node, val in enumerate(inorder):
            if val == 0:
                q.append(node)

        
        # key = node we are at, value = all the nodes which lead to this key.
        reachable = defaultdict(set)

        while q:
            node = q.popleft()
            for neighbour in graph[node]:
                reachable[neighbour].update(reachable[node])
                reachable[neighbour].add(node)
                inorder[neighbour] -= 1
                if inorder[neighbour] == 0:
                    q.append(neighbour)

        answer = []
        for u, v in queries:
            answer.append(u in reachable[v])
        
        return answer
        


        
