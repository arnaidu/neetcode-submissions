class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in seen:
                seen[key] = []

            seen[key].append(string)
            
        
        return list(seen.values())
