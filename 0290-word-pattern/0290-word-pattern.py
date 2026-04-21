class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        map_p_s = {}
        map_s_p = {}

        if len(pattern) != len(words):
            return False

        for p1,s1 in zip(pattern,words):
            if p1 in map_p_s:
                if map_p_s[p1] != s1:
                    return False
            else:
                map_p_s[p1] = s1
            
            if s1 in map_s_p:
                if map_s_p[s1] != p1:
                    return False
            else:
                map_s_p[s1] = p1
        return True


        