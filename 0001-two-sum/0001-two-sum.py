class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for i in range(n):
            comple = target - nums[i]

            if comple not in seen:
                seen[nums[i]] = i
            else:
                return [seen[comple],i]