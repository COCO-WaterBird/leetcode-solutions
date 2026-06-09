class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        cur_sum = 0
        ans = float('inf')
        for right,num in enumerate(nums):
            cur_sum += num
            while cur_sum >= target:
                ans = min(ans,right-left+1)
                cur_sum -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans