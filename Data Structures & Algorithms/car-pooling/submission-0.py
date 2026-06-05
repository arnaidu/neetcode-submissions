class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        total_passengers = trips[0][0]
        curr_start = trips[0][1]
        curr_end = trips[0][2]

        for idx in range(1, len(trips)):
            if total_passengers > capacity:
                return False

            num_passengers, start_pos, end_pos = trips[idx]
            
            # if overlap then increse num_passengers
            if start_pos < curr_end:
                total_passengers = total_passengers + num_passengers
            else:
                total_passengers = num_passengers
                curr_start = start_pos
                curr_end = end_pos
            

        if total_passengers > capacity:
            return False

        return True

