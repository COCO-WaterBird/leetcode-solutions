class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        
        # -------- 并查集初始化 --------
        father = list(range(n))
        size   = [1] * n
        stack  = [0] * n

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
        # 第一步：合并所有直连的城市
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        # 第二步：统计根节点个数 = 省份数量
        return sum(1 for i in range(n) if find(i) == i)        