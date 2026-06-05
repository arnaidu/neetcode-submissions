class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def getCommonPrefix(string: str, prefix: str) -> str:
            minimum_len = min(len(string), len(prefix))
            common_prefix = ""
            for i in range(minimum_len):
                if prefix[i] != string[i]:
                    break
                common_prefix += prefix[i]

            return common_prefix
        prefix = strs[0]
        for string in strs[1:]:
            prefix = getCommonPrefix(string, prefix)
        return prefix
