class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        # -------- 并查集初始化 --------
        # 把二维坐标 (i,j) 映射成一维索引 i*n+j
        total = m * n
        father = list(range(total))
        size   = [1] * total
        stack  = [0] * total

        def find(i):
            top = 0
            while i != father[i]:
                stack[top] = i
                top += 1
                i = father[i]
            while top > 0:
                top -= 1
                father[stack[top]] = i
            return i

        def union(x, y):
            fx, fy = find(x), find(y)
            if fx != fy:
                if size[fx] >= size[fy]:
                    size[fx] += size[fy]
                    father[fy] = fx
                else:
                    size[fy] += size[fx]
                    father[fx] = fy

        # -------- 主逻辑 --------
        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    idx = i * n + j
                    father[idx] = idx   # 初始化这个节点
                    islands += 1        # 先假设它是独立岛屿

                    # 检查上边
                    if i > 0 and grid[i-1][j] == '1':
                        if find(idx) != find((i-1) * n + j):
                            islands -= 1   # 合并 → 岛屿数-1
                            union(idx, (i-1) * n + j)

                    # 检查左边
                    if j > 0 and grid[i][j-1] == '1':
                        if find(idx) != find(i * n + j - 1):
                            islands -= 1   # 合并 → 岛屿数-1
                            union(idx, i * n + j - 1)

        return islands        