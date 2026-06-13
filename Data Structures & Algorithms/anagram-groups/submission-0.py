from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            freq = [0] * 26
            for ch in string:
                freq[ord(ch) - ord('a')] += 1
            groups[tuple(freq)].append(string)
        return list(groups.values())