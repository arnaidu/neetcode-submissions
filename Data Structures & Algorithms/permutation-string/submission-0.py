class FixedWindow:
    def __init__(self, s1: str, s2: str):
        self.size = len(s1)
        self.s1 = s1
        self.s2 = s2
        self.counts = {}
        self.total = len(s1)
        self.right = self.size - 1

        for ch in self.s1:
            self.counts[ch] = self.counts.get(ch, 0) + 1

        for j in range(self.size):
            char = self.s2[j]
            if char in self.counts:
                if self.counts[char] > 0:
                    self.total -= 1 # don't let total decrease past 0 to account for duplicates
                self.counts[char] -= 1
    
    @property
    def permutationExists(self):
        return self.total == 0
    
    @property
    def end(self):
        return self.right == len(self.s2) - 1

    def moveWindowRight(self):
        self.right += 1
        left_char = self.s2[self.right - self.size]
        if left_char in self.counts:
            # if there is negative count, then we have duplicates in window
            # therefore, if one leaves, then it is okay still, so total
            # doesn't need to increment again
            if self.counts[left_char] >= 0:
                self.total += 1
            self.counts[left_char] += 1
        
        right_char = self.s2[self.right]
        if right_char in self.counts:
            if self.counts[right_char] > 0:
                self.total -= 1
            self.counts[right_char] -= 1
        return self.permutationExists


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        window = FixedWindow(s1, s2)
        while not window.permutationExists and not window.end:
            window.moveWindowRight()
        
        return window.permutationExists



         