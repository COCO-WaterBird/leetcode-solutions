class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ans = nums[0]
        count = 1    
        for i in range(1,n):
            
            if nums[i] == ans:
                count += 1
            else:
                count -= 1
                if count == 0:
                    ans = nums[i]
                    count = 1
        return ans

