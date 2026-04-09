class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        # answer[i] 先存 i 左边所有数的乘积
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # 再乘上 i 右边所有数的乘积
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer        