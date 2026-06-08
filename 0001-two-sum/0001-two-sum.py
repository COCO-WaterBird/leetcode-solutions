class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
       
        n = len(nums)
        for i in range(n):
            comple = target - nums[i]
            if comple in seen:
                return [seen[comple],i]
            else:
                seen[nums[i]] = i