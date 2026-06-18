class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        n = len(nums)
        farthest = 0
        current = 0

        for i in range(n-1):
            farthest = max(farthest,i+nums[i])
            
            if i >= current:
                jump += 1
                current = farthest
        return jump 

