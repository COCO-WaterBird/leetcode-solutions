class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        cur_end = 0    # 当前这跳的边界
        max_reach = 0  # 历史最远能到哪

        for i in range(len(nums) - 1):  # 注意：不用走到最后一个
            max_reach = max(max_reach, i + nums[i])
            if i == cur_end:       # 走到当前跳的边界了
                res += 1           # 必须再跳一次
                cur_end = max_reach  # 下一跳的边界 = 目前最远

        return res