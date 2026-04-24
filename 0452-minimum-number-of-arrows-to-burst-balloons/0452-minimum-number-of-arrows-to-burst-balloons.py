class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x:x[0])
        p = points
        n = len(p)
        res = []
        cur = p[0]
        for i in range(1,n):
            if cur[1] >= p[i][0]:
                cur[0] = max(cur[0],p[i][0])
                cur[1] = min(cur[1],p[i][1])
            else:
                res.append(cur)
                cur = p[i]
        return len(res) + 1
