class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        for num,occ in freq.items():
            if occ == 1:
                return num