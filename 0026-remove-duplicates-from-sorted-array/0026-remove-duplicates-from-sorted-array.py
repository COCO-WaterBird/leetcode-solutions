class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n= len(nums)
        
        slow = 0
        fast = 1
        while fast < n:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                
            fast += 1
        return slow + 1
        
# class remove:

# 	def remove_duplicate(self, nums):
        
#         n= len(nums)
        
#         slow = 0
#         fast = 1
#         while fast < n:
#             if nums[fast] != nums[slow]:
#                 slow += 1
#                 nums[slow] = nums[fast]
                
#             fast += 1
#         return slow + 1