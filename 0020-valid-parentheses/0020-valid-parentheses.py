class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(":")",
            "[":"]",
            "{":"}",
        }

        for char in s:
            if char in pairs.keys():
                stack.append(char)
            else:
                if not stack:
                    return False

                if char != pairs[stack.pop()]:
                    return False
        return not stack