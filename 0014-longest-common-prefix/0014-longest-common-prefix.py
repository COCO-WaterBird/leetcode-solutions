class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s0 = strs[0]
        for j,c in enumerate(s0):
            for s in strs:
                if j == len(s) or s[j] != c:
                    return s0[:j]
        return s0