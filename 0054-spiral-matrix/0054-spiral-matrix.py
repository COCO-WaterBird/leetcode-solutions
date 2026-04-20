class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False]*n for _ in range(m)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        r,c = 0,0
        d = 0
        ans = []

        for _ in range(m*n):
            ans.append(matrix[r][c])
            visited[r][c] = True
            nr = r + dirs[d][0]
            nc = c + dirs[d][1]

            if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                d = (d + 1) % 4
                nr = r + dirs[d][0]
                nc = c + dirs[d][1]
            r,c = nr,nc
        return ans
