class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping_s_t = {}
        seen_t = set()
        for i in range(len(s)):
            if s[i] in mapping_s_t:
                if t[i] != mapping_s_t[s[i]]:
                    return False
            if s[i] not in mapping_s_t:
                if t[i] in seen_t:
                    return False
                mapping_s_t[s[i]] = t[i]
                seen_t.add(t[i])
        return True

                

        