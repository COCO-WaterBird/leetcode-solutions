class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)

        # 并查集
        father = list(range(n + 1))
        size   = [1] * (n + 1)

        def find(i):
            if father[i] != i:
                father[i] = find(father[i])
            return father[i]

        def union(x, y):
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

        def is_valid(skip):
            """跳过某条边，检查剩余的边能否构成合法的树"""
            nonlocal father, size
            father = list(range(n + 1))  # 重置并查集
            size   = [1] * (n + 1)
            for i, (a, b) in enumerate(edges):
                if i == skip:            # 跳过这条边
                    continue
                if not union(a, b):      # 发现成环 → 不合法
                    return False
            return True

        # 主逻辑 
        # 第一步：找入度为2的节点，记录两条候选边
        indegree  = [0] * (n + 1)
        candidate = []               # 存入度为2节点对应的两条边的索引

        for i, (a, b) in enumerate(edges):
            indegree[b] += 1
            if indegree[b] == 2:
                # 找到第一条和第二条指向b的边
                for j in range(i):
                    if edges[j][1] == b:
                        candidate = [j, i]  # [先出现的边, 后出现的边]
                        break

        # 情况1：存在入度为2的节点
        if candidate:
            if is_valid(candidate[1]):   # 先尝试删后面那条
                return edges[candidate[1]]
            else:
                return edges[candidate[0]]  # 不行就删前面那条

        # 情况2：只有环，没有入度为2
        father = list(range(n + 1))
        size   = [1] * (n + 1)
        for a, b in edges:
            if not union(a, b):
                return [a, b]        