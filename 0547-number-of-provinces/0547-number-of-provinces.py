class UnionFind:                          # ← 独立的类
    def __init__(self):
        self.father = {}
    
    def find(self, x):
        root = x
        while self.father[root] is not None:
            root = self.father[root]
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root
    
    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind()                  # ← 在这里使用 UnionFind
        n = len(isConnected)
        
        for i in range(n):
            uf.add(i)                     # 先把所有节点加进去
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.merge(i, j)        # 连通的城市合并
        
        # 统计有多少个根节点，就有多少个省份
        return sum(1 for i in range(n) if uf.find(i) == i)