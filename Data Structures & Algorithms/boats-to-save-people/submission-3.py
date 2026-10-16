class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lightest = 0
        heaviest = len(people) - 1
        count = 0
        while lightest <= heaviest:
            # take heaviest
            remaining_limit = limit - people[heaviest]
            # if we can take lightest
            if lightest <= heaviest and people[lightest] <= remaining_limit:
                lightest += 1
            
            heaviest -= 1
           
            count += 1
        return count
            


