class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        k = 0
        while k < min(len(word1), len(word2)):
            output.append(word1[k])
            output.append(word2[k])
            k += 1
        
        while k < len(word2):
            output.append(word2[k])
            k += 1
        
        while k < len(word1):
            output.append(word1[k])
            k += 1
        
        return "".join(output)