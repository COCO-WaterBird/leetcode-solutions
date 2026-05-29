class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        f0 = 0
        f1 = -inf
        for p in prices:
            f0_new = max(f0,f1+p)
            f1_new = max(f1,-p)
            f0 = f0_new
            f1 = f1_new
        return max(f0,f1)