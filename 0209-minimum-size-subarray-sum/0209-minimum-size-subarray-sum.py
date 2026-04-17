class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cur_num = 0
        res = float('inf')
        
        for right in range(len(nums)):
            cur_num += nums[right]
            while cur_num >= target:
                res = min(res,right-left+1)
                cur_num -= nums[left]
                left +=1
        return 0 if res == float('inf') else res