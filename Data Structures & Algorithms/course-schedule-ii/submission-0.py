from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        indegree = [0] * numCourses
        post_requisites = defaultdict(list)

        for a, b in prerequisites:
            indegree[a] += 1
            post_requisites[b].append(a)
        
        coursesCanTake = [course for course in range(numCourses) if indegree[course] == 0]

        while coursesCanTake:
            course = coursesCanTake.pop()
            result.append(course)

            for postreq in post_requisites[course]:
                indegree[postreq] -= 1
                if indegree[postreq] == 0:
                    coursesCanTake.append(postreq)
        
        return result if sum(indegree) == 0 else []