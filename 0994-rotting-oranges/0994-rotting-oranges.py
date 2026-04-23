class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        # Step 1: 初始化腐烂橘子和新鲜橘子数量
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # 新鲜橘子
                    fresh += 1
                elif grid[r][c] == 2:  # 腐烂橘子
                    queue.append((r, c))

        # 如果没有新鲜橘子，直接返回 0
        if fresh == 0:
            return 0

        # Step 2: BFS 每次表示 1 分钟
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 上下左右四个方向

        while queue and fresh > 0:
            # 每一轮 BFS
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc  # 计算新的位置

                    # 只考虑新鲜橘子，且位置合法
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # 变成腐烂橘子
                        fresh -= 1  # 减少新鲜橘子的数量
                        queue.append((nr, nc))  # 把腐烂橘子的邻居加入队列

            # 每次遍历完一层的节点，增加 1 分钟
            minutes += 1

        # 如果还有新鲜橘子，说明无法腐烂所有橘子
        return minutes if fresh == 0 else -1        

"""
## 没有固定顺序，随便写！

---

### 为什么顺序无所谓？

因为代码是**四个方向全部探索**，不是只探一个方向：

```python
for dr, dc in directions:
    nr, nc = r + dr, c + dc
    if ...:
        # 感染
```

> 这个for循环会把四个方向**全部走一遍**，不管你写的顺序是什么，最终结果一样。

---

### 打个比方

> 腐烂橘子向四周扩散，它不在乎**先感染上面还是先感染右边**，反正四个邻居它都会感染到。

---

### 所以这四种写法完全等价

```python
directions = [(1,0), (-1,0), (0,1), (0,-1)]   # 下上右左
directions = [(0,1), (0,-1), (1,0), (-1,0)]   # 右左下上
directions = [(-1,0), (1,0), (0,-1), (0,1)]   # 上下左右
directions = [(1,0), (0,1), (-1,0), (0,-1)]   # 随便
```

结果全部一样 ✅

---

### 唯一需要记住的

不是顺序，而是**这四个元组本身**：

```
上: (-1, 0)   ← 行-1
下: (1, 0)    ← 行+1
左: (0, -1)   ← 列-1
右: (0, 1)    ← 列+1
```

记忆：**行动上下，列动左右**
"""