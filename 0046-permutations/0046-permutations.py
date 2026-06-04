class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        res = []
        def backtrack(current):
            if len(current) == len(nums):
                res.append(current[:])
                return 
            for num in nums:
                if num not in used:
                    current.append(num)
                    used.add(num)
                    backtrack(current)
                    current.pop()
                    used.remove(num)
        backtrack([])
        return res