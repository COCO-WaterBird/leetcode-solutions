class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        
        for i in range(len(intervals)):
            # 第一类：完全在新区间左边
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            
            # 第三类：完全在新区间右边
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                newInterval = intervals[i]
            
            # 第二类：重叠，合并进newInterval
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        res.append(newInterval)  # 最后手动放入
        return res        