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
## 🍊 烂橘子瘟疫蔓延记（详细版）

---

### 故事背景

> 古代某个村子，果园里突然爆发了**橘子瘟疫**。
> 凡是腐烂的橘子，每过一分钟就会把**上下左右**紧邻的新鲜橘子传染。
> 村长要知道：**几分钟后全村橘子都烂完？**
> 如果有橘子永远传染不到，就上报朝廷：**-1，无解**。

---

## 第一幕：村长下令普查 🗺️

```python
rows, cols = len(grid), len(grid[0])
fresh = 0
queue = deque()
```

> 村长先搞清楚果园有多大：
> - `rows` = 果园有几行
> - `cols` = 果园有几列
> - `fresh` = 新鲜橘子计数器，先归零
> - `queue` = 隔离区，先清空

记忆画面：**村长拿着空账本和空隔离笼子站在果园门口**

---

## 第二幕：挨格子清点 🔍

```python
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 1:
            fresh += 1
        elif grid[r][c] == 2:
            queue.append((r, c))
```

> 村长派人**一行一行、一列一列**扫过去：
> - 看到 `1`（新鲜橘子）→ **账本上记一笔** `fresh += 1`
> - 看到 `2`（腐烂橘子）→ **直接关进隔离笼子** `queue.append((r,c))`
> - 看到 `0`（空格子）→ **不管，跳过**

记忆口诀：**"1记账，2关笼，0不管"**

---

## 第三幕：没有新鲜橘子，村长直接回家 🏠

```python
if fresh == 0:
    return 0
```

> 普查完，村长一看账本：**fresh = 0，根本没有新鲜橘子！**
> 不需要任何处理，直接回家睡觉，**0分钟搞定**

记忆画面：**账本是空的，村长拍拍手走人**

---

## 第四幕：准备计时，规定传染方向 ⏱️

```python
minutes = 0
directions = [(1,0), (-1,0), (0,1), (0,-1)]
```

> 村长掏出**秒表**，从0开始计时
> 规定瘟疫只能往**上下左右**四个方向传播，不能斜着走

```
        (-1, 0) 上
            ↑
(0,-1) 左 ← 🍊 → 右 (0,1)
            ↓
        (1, 0) 下
```

记忆口诀：**"上负下正，左负右正"**（行列方向别搞混）

---

## 第五幕：瘟疫开始蔓延 🦠

```python
while queue and fresh > 0:
```

> 两个条件同时满足才继续蔓延：
> - `queue` 不为空 → **还有腐烂橘子在活动**
> - `fresh > 0` → **还有新鲜橘子没被感染**
>
> 任何一个不满足就停下来

记忆画面：**隔离笼子空了，或者新鲜橘子全灭了，瘟疫自然停止**

---

## 第六幕：这一分钟内，所有烂橘子同时扩散 💀

```python
    for _ in range(len(queue)):
        r, c = queue.popleft()
```

> `for _ in range(len(queue))` 是关键！
> 意思是：**只处理这一分钟开始时笼子里的橘子**
> 这一分钟新感染的橘子，下一分钟才轮到它们扩散

记忆画面：**村长喊"这一批一起出动！"，新来的关在笼子里等下一轮**

---

## 第七幕：向四周探索，感染新鲜橘子 🎯

```python
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc))
```

> 每个腐烂橘子出笼后，往**四个方向**各探一步：
>
> **三重检查**才能感染：

| 检查 | 代码 | 画面 |
|---|---|---|
| 没出界 | `0 <= nr < rows` | 没跑出果园 |
| 没出界 | `0 <= nc < cols` | 没跑出果园 |
| 是新鲜橘子 | `grid[nr][nc] == 1` | 目标是健康的 |

> 三关都过了：
> - `grid[nr][nc] = 2` → **感染！变腐烂**
> - `fresh -= 1` → **账本划掉一个**
> - `queue.append((nr, nc))` → **关进隔离笼子，等下一分钟扩散**

记忆口诀：**"探→查三关→感染→划账→入笼"**

---

## 第八幕：一分钟过去了 ⏰

```python
    minutes += 1
```

> for循环结束 = 这一分钟所有烂橘子都扩散完了
> 秒表 +1 分钟
>
> 记忆：**for循环在里面，minutes在外面，每轮循环结束才+1**

```
while queue and fresh > 0:
    for _ in range(len(queue)):   ← 这一分钟所有橘子扩散
        ...
    minutes += 1                  ← 一分钟结束
```

---

## 第九幕：村长结案 📋

```python
return minutes if fresh == 0 else -1
```

> 蔓延停止后，村长翻开账本：
> - `fresh == 0` → **全部感染，返回用了几分钟**
> - `fresh > 0` → **还有橘子没被传到，上报朝廷：-1**

记忆画面：**账本清零就报时间，账本还有剩就报-1**

---

## 完整故事主线

```
村长站在果园门口（初始化）
        ↓
挨格子清点：1记账，2关笼（双for初始化）
        ↓
账本是空的？直接回家（if fresh==0 return 0）
        ↓
秒表归零，规定四个方向（minutes=0, directions）
        ↓
笼子不空且还有新鲜橘子（while条件）
        ↓
这批一起出动，向四周探（for循环+directions）
        ↓
三关检查：没出界且是新鲜→感染入笼划账（if条件+三步操作）
        ↓
一分钟结束，秒表+1（minutes+=1）
        ↓
账本清零返回时间，有剩返回-1（return）
```

---

## 现在闭眼默写 ✍️

按这个顺序写：
1. 初始化 rows, cols, fresh, queue
2. 双for普查
3. fresh==0 特判
4. minutes=0, directions
5. while循环主体
6. return
"""