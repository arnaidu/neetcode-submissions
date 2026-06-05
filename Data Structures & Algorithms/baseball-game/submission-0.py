class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        op_generator = {
            "+" : self.add_scores,
            "D" : self.double,
            "C" : self.invalidate
        }

        for op in operations:
            if op in op_generator:
                op_generator[op](s)
            else:
                s.append(int(op))
        
        return sum(s)

    def add_scores(self, s: list[int]) -> None:
        prev_score1 = s[-1]
        prev_score2 = s[-2]
        s.append(prev_score1 + prev_score2)
    
    def double(self, s: list[int]) -> None:
        s.append(s[-1] * 2)
    
    def invalidate(self, s: list[int]) -> None:
        s.pop()


