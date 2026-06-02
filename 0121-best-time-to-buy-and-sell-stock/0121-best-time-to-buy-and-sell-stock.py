class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[float(-inf)]*2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,len(prices)):
            p = prices[i]
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+p)
            dp[i][1] = max(dp[i-1][1],-p)
        return dp[len(prices)-1][0]