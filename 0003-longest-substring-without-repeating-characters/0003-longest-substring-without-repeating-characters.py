class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        ans = 0
        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right],0)+ 1
            
            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1

            ans = max(ans,right - left+1)
        return ans