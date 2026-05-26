class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1
        while l <= r:
            mid = (l+r)//2
            x = matrix[mid//n][mid%n]
            if x == target:
                return True
            elif x < target:
                l = mid + 1
            else:
                r = mid - 1
        return False