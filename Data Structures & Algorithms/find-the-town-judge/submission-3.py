from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_node_count = defaultdict(int)
        out_node_count = defaultdict(int)
        for a, b in trust:
            in_node_count[b - 1] += 1
            out_node_count[a - 1] += 1
        
        for b in in_node_count:
            if in_node_count[b] == n - 1 and out_node_count.get(b, 0) == 0:
                return b + 1

        return -1