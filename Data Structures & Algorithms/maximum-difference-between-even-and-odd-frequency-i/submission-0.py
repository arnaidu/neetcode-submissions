from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = Counter(s)
        evenMin, oddMax = float("inf"), -float("inf")
        for i, v in freqs.items():
            if v % 2 == 1 and v > oddMax:
                    oddMax = v
            if v % 2 == 0 and v < evenMin:
                evenMin = v

        return oddMax - evenMin