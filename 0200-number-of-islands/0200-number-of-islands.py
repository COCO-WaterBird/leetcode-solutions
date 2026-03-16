class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])

        #初始化-
        father = list(range(rows * cols))  # 二维坐标 → 一维编号：i * cols + j
        size   = [1] * (rows * cols)

        def find(i):
            if father[i] != i:
                father[i] = find(father[i])
            return father[i]

        def union(x, y) -> bool:
            fx, fy = find(x), find(y)
            if fx == fy:
                return False
            if size[fx] >= size[fy]:
                size[fx] += size[fy]
                father[fy] = fx
            else:
                size[fy] += size[fx]
                father[fx] = fy
            return True

        def is_same_set(x, y) -> bool:
            return find(x) == find(y)

        #主逻辑
        # 统计陆地数，初始每个陆地 = 一个独立岛屿
        islands = sum(grid[i][j] == '1' for i in range(rows) for j in range(cols))

        # 遍历所有陆地，只看右和下两个方向（避免重复合并）
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    cur = i * cols + j

                    if j + 1 < cols and grid[i][j+1] == '1':
                        if union(cur, i * cols + (j+1)):
                            islands -= 1   # 合并成功 → 两岛变一岛

                    if i + 1 < rows and grid[i+1][j] == '1':
                        if union(cur, (i+1) * cols + j):
                            islands -= 1   # 合并成功 → 两岛变一岛

        return islands        