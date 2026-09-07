class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        can i segment s[0:i] into dictionary words
        start at s[0: 1] then check dictionayr for each word
        """
        dp = [False] * (len(s) + 1) # empty string
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        dp[i + len(word)] = True
        return dp[-1]
            



