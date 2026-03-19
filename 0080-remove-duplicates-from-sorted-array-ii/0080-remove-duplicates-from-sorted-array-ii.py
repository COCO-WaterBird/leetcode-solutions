class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        slow = 1
        for fast in range(2,len(nums)):
            if nums[fast] != nums[slow-1]:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1