class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        # if n == 1:
        #     return True
        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest,i + nums[i])
            if farthest >= n-1:
                return True
        return False