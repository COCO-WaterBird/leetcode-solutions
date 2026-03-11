class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s0 = strs[0]
        for i,c in enumerate(s0):
            for s in strs:
                if i == len(s) or s[i] != c:
                    return s0[:i]
        return s0            