class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n-2):
            j = i + 1
            k = len(nums) - 1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1 
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return res