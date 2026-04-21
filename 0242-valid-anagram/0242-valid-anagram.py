class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for s1,t1 in zip(s,t):
            count[s1] = count.get(s1,0) + 1
            count[t1] = count.get(t1,0) - 1
        return all(v==0 for v in count.values())