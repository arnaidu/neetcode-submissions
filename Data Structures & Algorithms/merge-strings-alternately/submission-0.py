class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        min_length = min(len(word1), len(word2))
        i = 0
        while i < min_length:
            res.append(word1[i])
            res.append(word2[i])
            i += 1
        
        for ch in word1[i:]:
            res.append(ch)
        
        for ch in word2[i:]:
            res.append(ch)
        
        return "".join(res)
        

