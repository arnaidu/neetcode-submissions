class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = { ")" : "(", "}": "{", "]" : "[" }
        for i in s:
            if i in closing:
                if not stack or stack.pop() != closing[i]:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0
                
