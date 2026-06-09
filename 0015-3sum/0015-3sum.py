class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            l = i + 1
            r = n - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res