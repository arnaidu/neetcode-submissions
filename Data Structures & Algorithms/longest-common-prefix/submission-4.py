class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]
        k = 0
        while k < min(len(first), len(last)):
            if first[k] == last[k]:
                k += 1
            else:
                break
        return first[:k]
