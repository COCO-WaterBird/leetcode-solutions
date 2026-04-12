class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        cur = 0
        dir = -1
        for c in s:
            rows[cur] += c

            if cur == 0 or cur == numRows - 1:
                dir *= -1
            cur += dir
        return ''.join(rows)