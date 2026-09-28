from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # if nothing added for key, or timestamp provided is lower than all available timestamps
        if key not in self.store: 
            return ""
        
        vals = self.store[key]
        if timestamp < vals[0][0]:
            return ""
        
        left = 0
        right = len(vals) - 1
        while left <= right:
            m = left + ((right - left) // 2)
            if vals[m][0] > timestamp:
                right = m - 1
            else:
                left = m + 1
        return vals[right][1]

        
