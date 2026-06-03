class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False

                left = stack.pop()
                if pairs[left] != char:
                    return False
                
        return len(stack) == 0