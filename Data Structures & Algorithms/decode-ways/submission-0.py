class Solution:
    def numDecodings(self, s: str) -> int:
        """
        702124598024
        72124591024

        (7)
        (7 2)
        (7 2 1) (7 21)
        (7 2 1 2) (7 2 12) (7 21 2)
        (7 2 1 2 4) (7 2 1 24) (7 2 12 4) (7 21 2 4) (7 21 24)
        (7 2 1 2 4 5 9 10 2) (7 2 1 24 5 9 10 2) (7 2 12 4 5 9 10 2) (7 21 2 4 5 9 10 2) ( 7 21 24 5 9 10 2)

        num_ways = 0
        if curr_digit can stand alone:
            num_ways += num_ways to reach previous digit
        
        if curr_digit can pair with previous digit:
            num_ways += num_ways to reach previous previous digit
        """        
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

            if num_ways == 0:
                return 0

            num_ways_till_previous_previous = num_ways_till_previous
            num_ways_till_previous = num_ways
        return num_ways_till_previous
        
        

        
