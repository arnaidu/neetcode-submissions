class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        result = [0] * len(temperatures)
        for idx in range(1, len(temperatures)):
            temp = temperatures[idx]
            while stack and temp > temperatures[stack[-1]]:
                prev_temp = stack.pop()
                result[prev_temp] = idx - prev_temp
            stack.append(idx)
        
        return result
