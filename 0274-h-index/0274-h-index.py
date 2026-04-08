class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cit = sorted(citations)
        n = len(cit)
        
        for i,c in enumerate(cit):
            if c >= n - i:
                return n - i
        return 0


       