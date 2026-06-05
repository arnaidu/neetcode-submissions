from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for edge in trust:
            person_who_trusts, person_who_is_trusted = edge
            indegree[person_who_is_trusted] += 1
            outdegree[person_who_is_trusted] = 0
            outdegree[person_who_trusts] += 1
        
        for i in indegree:
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1

