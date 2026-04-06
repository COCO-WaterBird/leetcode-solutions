class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i,c in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+c)
        return True
