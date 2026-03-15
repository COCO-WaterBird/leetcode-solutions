class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        # 并查集初始化
        father = list(range(26))   # a~z 对应 0~25
        size   = [1] * 26
        stack  = [0] * 26

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
        # 第一步：处理所有 ==
        for eq in equations:
            a, op, b = eq[0], eq[1:3], eq[3]
            if op == "==":
                union(ord(a) - ord('a'), ord(b) - ord('a'))

        # 第二步：处理所有 !=
        for eq in equations:
            a, op, b = eq[0], eq[1:3], eq[3]
            if op == "!=":
                if is_same_set(ord(a) - ord('a'), ord(b) - ord('a')):
                    return False   # 矛盾

        return True       