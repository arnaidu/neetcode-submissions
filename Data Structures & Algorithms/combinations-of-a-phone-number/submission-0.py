class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        if len(digits) == 0:
            return []
            
        def traverse(digits, digit_idx, path):
            if len(path) == len(digits):
                result.append("".join(path))
                return
            
            digit = int(digits[digit_idx])
            options = digit_map[digit]

            for op in options:
                path.append(op)
                traverse(digits, digit_idx + 1, path)
                path.pop()
        
        traverse(digits, 0, [])
        return result