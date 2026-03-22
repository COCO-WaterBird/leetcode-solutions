class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        father = list(range(rows * cols))
        size = [1] * (rows * cols)
        
        def find(i):
            if father[i] != i:
                father[i] = find(father[i])
            return father[i]
        
        def union(x, y):
            fx, fy = find(x), find(y)
            if fx == fy:
                return
            if size[fx] >= size[fy]:
                size[fx] += size[fy]; father[fy] = fx
            else:
                size[fy] += size[fx]; father[fx] = fy
        
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1          # 先假设每个陆地是独立岛
                    for di, dj in [(0,1),(1,0)]:   # 只看右和下，避免重复
                        ni, nj = i+di, j+dj
                        if 0<=ni<rows and 0<=nj<cols and grid[ni][nj]=='1':
                            a = i*cols + j
                            b = ni*cols + nj
                            if find(a) != find(b):
                                union(a, b)
                                islands -= 1  # 合并一次，岛屿数-1
        
        return islands  