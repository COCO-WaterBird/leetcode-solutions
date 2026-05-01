class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        target = n * n

        def get_position(num: int) -> tuple[int, int]:
            index = num - 1

            row_from_bottom = index // n
            col = index % n

            row = n - 1 - row_from_bottom

            # 蛇梯棋编号是从左下角开始，方向每一行交替
            if row_from_bottom % 2 == 1:
                col = n - 1 - col

            return row, col

        queue = deque([1])
        visited = set([1])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()

                if cur == target:
                    return steps

                for dice in range(1, 7):
                    next_pos = cur + dice

                    if next_pos > target:
                        break

                    row, col = get_position(next_pos)

                    # 如果目标格子有蛇或梯子，就跳到对应位置
                    if board[row][col] != -1:
                        next_pos = board[row][col]

                    if next_pos not in visited:
                        visited.add(next_pos)
                        queue.append(next_pos)

            steps += 1

        return -1        