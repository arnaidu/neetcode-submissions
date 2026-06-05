class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        res = []

        for i, w in enumerate(words):
            for j in range(i + 1, len(words)):
                if w in words[j]:
                    res.append(w)
                    break
        
        return res