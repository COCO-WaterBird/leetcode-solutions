class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        ans = 0
        while i >= 0 and s[i] == " ":
            i -= 1
        
        while i >= 0 and s[i] != ' ':
            i -= 1
            ans += 1
        return ans
        