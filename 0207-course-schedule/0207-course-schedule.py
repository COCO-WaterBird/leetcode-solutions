class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        # 1. 构建图和入度数组
        graph = defaultdict(list)  # 存储图的邻接表
        indegree = [0] * numCourses  # 存储每个课程的入度
        
        # 填充图和入度数组
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        # 2. 队列初始化，将入度为0的课程放入队列
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        courses_taken = 0  # 用来记录已处理的课程数量
        
        # 3. 拓扑排序过程
        while queue:
            course = queue.popleft()
            courses_taken += 1  # 当前课程已经可以上
            
            # 减少依赖该课程的其他课程的入度
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        # 4. 如果所有课程都被处理了，返回 True，否则返回 False
        return courses_taken == numCourses        