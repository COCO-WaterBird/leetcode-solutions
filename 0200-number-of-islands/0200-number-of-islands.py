from typing import List

MAXN = 90001          # 最大 300×300 = 90000
father = list(range(MAXN))
size   = [1] * MAXN
stack  = [0] * MAXN

def build(n: int) -> None:
    for i in range(n):
        father[i] = i
        size[i]   = 1

def find(i: int) -> int:
    top = 0
    while i != father[i]:
        stack[top] = i
        top += 1
        i = father[i]
    while top > 0:
        top -= 1
        father[stack[top]] = i
    return i

def is_same_set(x: int, y: int) -> bool:
    return find(x) == find(y)

def union(x: int, y: int) -> None:
    fx, fy = find(x), find(y)
    if fx != fy:
        if size[fx] >= size[fy]:
            size[fx] += size[fy]
            father[fy] = fx
        else:
            size[fy] += size[fx]
            father[fx] = fy

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        build(rows * cols)

        # 统计陆地格子数，初始每个陆地 = 一个独立岛屿
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1

        # 遍历所有陆地，只看右和下两个方向（避免重复合并）
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    cur = i * cols + j          # 当前格子编号

                    # 向右
                    if j + 1 < cols and grid[i][j+1] == '1':
                        right = i * cols + (j + 1)
                        if not is_same_set(cur, right):
                            union(cur, right)
                            islands -= 1        # 两个岛合并，岛屿数 -1

                    # 向下
                    if i + 1 < rows and grid[i+1][j] == '1':
                        down = (i + 1) * cols + j
                        if not is_same_set(cur, down):
                            union(cur, down)
                            islands -= 1        # 两个岛合并，岛屿数 -1

        return islands        