class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        
        dp = [[0]*m for _ in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1,m):
            for j in range(i+1):
                if j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
        return min(dp[m-1])
        