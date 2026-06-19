from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = deque(arr[0:k])
        def a_closer_than_b(a, b, x):
            if abs(a - x) < abs(b - x):
                return True
            
            if abs(a - x) == abs(b - x) and a < b:
                return True

            return False
        for right in range(k, len(arr)):
            left = right - k

            if a_closer_than_b(arr[right], arr[left], x):
                closest.popleft()
                closest.append(arr[right])

        return list(closest)

