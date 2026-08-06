class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = { ')' : '(', ']': '[', '}':'{' }
        for b in s:
            if b not in valid:
                stack.append(b)
            else:
                if not stack or stack.pop() != valid[b]:
                    return False
        return len(stack) == 0
            