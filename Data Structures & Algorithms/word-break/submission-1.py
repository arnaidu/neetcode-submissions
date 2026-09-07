class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        lengths = {len(word) for word in words}

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if not dp[i]:
                continue

            for length in lengths:
                if i + length <= len(s) and s[i:i + length] in words:
                    dp[i + length] = True

        return dp[-1]
            



