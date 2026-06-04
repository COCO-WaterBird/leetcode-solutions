class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # count_m = Counter(magazine)
        # for char in ransomNote:
        return Counter(ransomNote) <= Counter(magazine)
