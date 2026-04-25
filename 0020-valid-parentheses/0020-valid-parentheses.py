class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {"(":")","[":"]","{":"}"}
        for p in s:
            if p in lookup.keys():
                stack.append(p)
            elif len(stack) == 0 or lookup[stack.pop()] != p:
                return False
        return len(stack) == 0
