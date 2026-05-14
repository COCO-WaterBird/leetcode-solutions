class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        max_len = max(len(word) for word in wordDict)if wordDict else 0

        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            for j in range(i+1,min(i+max_len+1,n+1)):
                if s[i:j] in word_set:
                    dp[j] = True
                    if dp[n]:
                        return True
        return dp[n]