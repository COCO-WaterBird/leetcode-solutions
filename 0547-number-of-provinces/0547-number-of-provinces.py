
from typing import List

MAXN = 1001
father = list(range(MAXN))
size   = [1] * MAXN
stack  = [0] * MAXN

def build(n: int) -> None:
    for i in range(n + 1):
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        build(n)

        for i in range(n):
            for j in range(i + 1, n):    # 只看上三角，避免重复
                if isConnected[i][j] == 1:
                    union(i, j)

        # 统计根节点个数 = 连通分量数
        return sum(1 for i in range(n) if find(i) == i)