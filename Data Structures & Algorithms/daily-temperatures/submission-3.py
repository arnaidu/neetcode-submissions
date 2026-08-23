class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mstack = [0]
        result = [0] * len(temperatures)
        for curr_day in range(1, len(temperatures)):
            curr_temp = temperatures[curr_day]
            
            while mstack and temperatures[mstack[-1]] < curr_temp:
                    past_day = mstack.pop()
                    result[past_day] = curr_day - past_day

            mstack.append(curr_day)
                
        return result