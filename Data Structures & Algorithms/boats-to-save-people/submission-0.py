class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        num_boats = 0
        l, r = 0, len(people) - 1
        while l < r:
            heavy_person, light_person = people[r], people[l]
            if heavy_person + light_person > limit:
                # only take heavy
                r -= 1
                num_boats += 1
            else:
                # can take both
                r -= 1
                l += 1
                num_boats += 1
        if l == r:
            num_boats += 1
        return num_boats
                