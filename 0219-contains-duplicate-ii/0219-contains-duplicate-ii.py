class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i,c in enumerate(nums):
            if c in map:
                if abs(i-map[c]) <= k:
                    return True
                
            map[c] = i
        return False