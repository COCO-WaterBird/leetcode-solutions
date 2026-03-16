class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        # 并查集初始化
        father = list(range(n))
        size   = [1] * n

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

        # 主逻辑
        # 第一步：合并
        for i in range(n):
            for j in range(i + 1, n):      # 只看上三角，避免重复
                if isConnected[i][j] == 1:
                    union(i, j)

        # 第二步：查询
        return sum(1 for i in range(n) if find(i) == i)  # 根节点数 = 省份数        