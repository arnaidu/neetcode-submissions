class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_possible_capacity = max(weights) # worst case len(weights) days shipping
        max_possible_capacity = sum(weights) # 1 day shipping
        
        
        def num_days_to_ship(weights, capacity):
            num_days = 1
            total = 0
            for weight in weights:
                if total + weight > capacity:
                    num_days += 1
                    total = weight
                    continue

                total += weight
                    
            return num_days

        while min_possible_capacity <= max_possible_capacity:
            capacity = min_possible_capacity + (max_possible_capacity - min_possible_capacity) // 2

            num_days = num_days_to_ship(weights, capacity)
            if num_days <= days:
                # this means we have shipped everything in less days, so lower capacity
                # if equal search for lower capacity
                max_possible_capacity = capacity - 1
            else:
                min_possible_capacity = capacity + 1
        
        return min_possible_capacity