class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        slow = m - 1
        fast = n - 1
        tail = m + n - 1
        while fast >= 0:
            if slow >= 0 and nums1[slow] > nums2[fast]:
                nums1[tail] = nums1[slow]
                slow -= 1
            else:
                nums1[tail] = nums2[fast]
                fast -= 1
            tail -= 1