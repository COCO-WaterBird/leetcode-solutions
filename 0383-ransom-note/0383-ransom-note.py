class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for c in magazine:
            count[c] = count.get(c,0) + 1
        for c in ransomNote:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1
        return True