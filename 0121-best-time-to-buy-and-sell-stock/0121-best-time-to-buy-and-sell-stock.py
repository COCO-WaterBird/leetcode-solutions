class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        min_p = prices[0]
        for p in prices:
            min_p = min(min_p,p)
            ans = max(ans,p-min_p)
        return ans