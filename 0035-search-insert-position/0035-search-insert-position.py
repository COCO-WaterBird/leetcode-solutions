class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n -1
        # if nums[0] > target:
        #     return 0
        # if nums[n-1] < target:
        #     return n
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid -1
            else:
                return mid
        return l