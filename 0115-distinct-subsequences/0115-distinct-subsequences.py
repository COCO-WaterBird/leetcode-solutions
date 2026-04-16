class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        slen = len(s)
        tlen = len(t)
        dp = [[0]*(slen+1)for _ in range(tlen+1)]
        for j in range(slen+1):
            dp[0][j] = 1
        for i in range(1,tlen+1):
            for j in range(1,slen+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[tlen][slen]