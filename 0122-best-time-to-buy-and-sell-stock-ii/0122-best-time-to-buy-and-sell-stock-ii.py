class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        n = len(prices)

        dp = [[-inf] * 2 for _ in range(n + 1)]
        dp[0][0] = 0

        for i, p in enumerate(prices):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + p)
            dp[i + 1][1] = max(dp[i][1], dp[i][0]-p)

        return max(dp[n][0],dp[n][1])