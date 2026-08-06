class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = []
        first, last = strs[0], strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break

            prefix.append(first[i])


        return "".join(prefix)
