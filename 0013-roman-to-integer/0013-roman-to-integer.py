class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = len(s)
        ans = 0
        for i in range(n):
            ans += dic[s[i]]
            if i < n-1 and dic[s[i]] < dic[s[i+1]]:
                ans -= 2 * dic[s[i]]
        return ans
             