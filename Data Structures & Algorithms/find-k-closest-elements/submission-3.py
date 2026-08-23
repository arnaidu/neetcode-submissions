from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def isCloser(a, b, x):
            return abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b)
        
        closest = deque([])
        for num in arr:
            if len(closest) < k:
                closest.append(num)
            else:
                # check the furthest idx = 0 and curr num to see which is closer
                # curr is closer, then remove idx = 0 and add new one
                if isCloser(num, closest[0], x):
                    closest.popleft()
                    closest.append(num)
        return list(closest)
