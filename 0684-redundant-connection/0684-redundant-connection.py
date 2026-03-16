class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        #并查集初始化
        father = list(range(n + 1))   # 节点编号 1~n，所以开 n+1
        size   = [1] * (n + 1)

        def find(i):
            if father[i] != i:
                father[i] = find(father[i])
            return father[i]

        def union(x, y) -> bool:
            fx, fy = find(x), find(y)
            if fx == fy:
                return False           # 已连通，未合并
            if size[fx] >= size[fy]:
                size[fx] += size[fy]
                father[fy] = fx
            else:
                size[fy] += size[fx]
                father[fx] = fy
            return True

        #主逻辑
        for a, b in edges:
            if not union(a, b):        # union 返回 False = 已连通 = 形成环
                return [a, b]          # 这条边就是多余边

        return []       