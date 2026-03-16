class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        #初始化
        father = list(range(26))      # 只有 a-z，固定 26 个节点
        size   = [1] * 26

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
        # 第一遍：处理所有 ==，建立连通关系
        for eq in equations:
            if eq[1] == '=':
                union(ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'))

        # 第二遍：检查所有 !=，验证是否矛盾
        for eq in equations:
            if eq[1] == '!':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                if is_same_set(a, b):  # 不等的两端却在同一集合 → 矛盾
                    return False

        return True        