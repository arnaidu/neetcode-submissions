class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            freqs = [0] * 26
            for ch in string:
                freqs[ord(ch) - 97] += 1
            key = tuple(freqs)
            if key not in seen:
                seen[tuple(freqs)] = [string]
            else:
                seen[tuple(freqs)].append(string)
            
        
        return list(seen.values())
