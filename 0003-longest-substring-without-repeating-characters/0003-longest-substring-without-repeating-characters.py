class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        count = {}
        res = 0
        left = 0 
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1
            
            while count[s[right]] > 1:
                
                count[s[left]] -= 1
                left += 1
            res = max(res,right-left+1)
        return res