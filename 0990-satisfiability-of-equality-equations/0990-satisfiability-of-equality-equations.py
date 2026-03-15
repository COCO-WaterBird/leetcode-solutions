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
    def equationsPossible(self, equations: List[str]) -> bool:
        build(26)    # 只有 a-z，映射到 0-25

        # 第一遍：处理所有 ==
        for eq in equations:
            if eq[1] == '=':           # "a==b" 格式：eq[1]='=', eq[3]=b
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                union(a, b)

        # 第二遍：检查所有 !=
        for eq in equations:
            if eq[1] == '!':           # "a!=b" 格式：eq[1]='!', eq[3]=b
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                if is_same_set(a, b):  # 不等的两个变量却在同一集合 → 矛盾
                    return False

        return True  