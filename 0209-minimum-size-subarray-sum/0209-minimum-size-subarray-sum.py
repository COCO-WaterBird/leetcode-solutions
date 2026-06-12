class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        slow = 0
        cur_sum = 0
        res = float('inf')
        for fast in range(n):
            cur_sum += nums[fast]
            while cur_sum >= target:
                res = min(res,fast-slow+1)
                cur_sum -= nums[slow]
                slow += 1
        return res if res != float('inf') else 0
