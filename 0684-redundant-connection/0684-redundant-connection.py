
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        build(n)

        for a, b in edges:
            if is_same_set(a, b):      # 加这条边会形成环
                return [a, b]
            union(a, b)

        return []   