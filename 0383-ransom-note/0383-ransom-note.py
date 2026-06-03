class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_m = Counter(magazine)
        m = len(ransomNote)
        for char in ransomNote:
            if char in count_m and count_m[char] != 0:
                count_m[char] -= 1
            else:
                return False
        return True
