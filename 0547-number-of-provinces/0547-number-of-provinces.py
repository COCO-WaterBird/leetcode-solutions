class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        father = list(range(n))
        size = [1] * n

        def find(i):
            if father[i] != i:
                father[i] = find(father[i])
            return father[i]

        def union(i,j):
            fx,fy = find(i),find(j)
            if fx == fy:
                return False
            if size[fx] >= size[fy]:
                size[fx] += size[fy]
                father[fy] = fx
            else:
                size[fy] += size[fx]
                father[fx] = fy

        # def is_same_set(i,j):
        #     return find(i) == find(j)


        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    union(i,j)
        return sum(1 for i in range(n) if father[i] == i)







