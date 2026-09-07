class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        max_len = max(map(len, words))

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for length in range(1, min(i, max_len) + 1):
                if dp[i - length] and s[i - length:i] in words:
                    dp[i] = True
                    break

        return dp[-1]
            



