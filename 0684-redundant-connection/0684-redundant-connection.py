class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        # -------- 并查集初始化 --------
        father = list(range(n + 1))   # 节点编号 1~n
        size   = [1] * (n + 1)
        stack  = [0] * (n + 1)

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

        def is_same_set(x, y):
            return find(x) == find(y)

        # -------- 主逻辑 --------
        for a, b in edges:
            if is_same_set(a, b):   # 已连通 → 这条边多余
                return [a, b]
            union(a, b)             # 未连通 → 合并       