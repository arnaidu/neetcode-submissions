class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        res = [0] * len(temperatures)
        prev_temp = float("inf")
        for i in range(1, len(temperatures)):            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day

            # add current temp to stack
            if not stack or temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
        return res

