from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        def max_fruits(fruits: list[int]):
            baskets = defaultdict(int)
            left = 0
            max_num_fruits_picked, local_num_fruits_picked = 0, 0
            for right in range(len(fruits)):
                # add fruit to basket
                fruit_type = fruits[right]
                baskets[fruit_type] += 1
                local_num_fruits_picked += 1

                # while basket length > 2, remove fruit until one gone from basket
                while len(baskets) > 2:
                    left_type_fruit = fruits[left]
                    baskets[left_type_fruit] -= 1
                    local_num_fruits_picked -= 1
                    if baskets[left_type_fruit] == 0:
                        del baskets[left_type_fruit]
                    left += 1

                # at this point we can compute new maximum num of fruits by summing both values sum(baskets.values())
                max_num_fruits_picked = max(max_num_fruits_picked, local_num_fruits_picked)
            return max_num_fruits_picked
        return max_fruits(fruits)