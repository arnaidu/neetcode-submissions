class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        for i in arr:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        for key, v in seen.items():
            if v == 1:
                k -= 1
            
            if k == 0:
                return key
        return ""
        
