from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        neighbours = defaultdict(list)
        for a, b in prerequisites:
            indegree[a] += 1
            neighbours[b].append(a)
        
        coursesCanTake = [course for course in range(numCourses) if indegree[course] == 0] 
        while coursesCanTake:
            pre_requisite = coursesCanTake.pop()
            for post_requisite in neighbours[pre_requisite]:
                indegree[post_requisite] -= 1
                if indegree[post_requisite] == 0:
                    coursesCanTake.append(post_requisite)
        
        return sum(indegree) == 0


