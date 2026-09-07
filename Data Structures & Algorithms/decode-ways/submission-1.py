class Solution:
    def numDecodings(self, s: str) -> int:    
        num_ways_till_previous = 1
        num_ways_till_previous_previous = 1
        for i in range(len(s)):
            num_ways = 0
            curr_digit = int(s[i])
            if 1 <= curr_digit <= 9:
                num_ways += num_ways_till_previous

            if i - 1 >= 0:
                prev_digit = int(s[i - 1])
                if 1 <= prev_digit <= 2 and 1 <= prev_digit * 10 + curr_digit <= 26:
                    num_ways += num_ways_till_previous_previous

            # if equal to 0, then no valid way so return 0 early
            if num_ways == 0:
                return 0

            num_ways_till_previous_previous = num_ways_till_previous
            num_ways_till_previous = num_ways
        return num_ways_till_previous
        
        

        
