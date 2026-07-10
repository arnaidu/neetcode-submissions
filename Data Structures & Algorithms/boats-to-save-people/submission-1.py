class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lightest, heaviest = 0, len(people) - 1
        num_boats = 0
        while lightest < heaviest:
            if people[heaviest] + people[lightest] <= limit:
                num_boats += 1
                heaviest -= 1
                lightest += 1
            else:
                num_boats += 1
                heaviest -= 1

        # for last person if one left        
        if lightest == heaviest:
            num_boats += 1
        return num_boats
            
                