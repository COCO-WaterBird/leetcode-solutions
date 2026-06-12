class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        max_water = 0
        while i < j:
            cur_water = (j - i)*min(height[i],height[j])
            max_water = max(max_water,cur_water)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water
            