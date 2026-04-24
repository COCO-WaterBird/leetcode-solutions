class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []
        
        n = len(nums)
        res = []
        start = 0                        # ← 初始化start

        for i in range(1, n):
            if nums[i] - nums[i-1] != 1:  # ← 不连续才处理
                end = i - 1
                if nums[start] == nums[end]:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start]) + "->" + str(nums[end]))
                start = i                  # ← 新区间开始

        # ← 最后一段手动append
        end = n - 1
        if nums[start] == nums[end]:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[end]))

        return res        