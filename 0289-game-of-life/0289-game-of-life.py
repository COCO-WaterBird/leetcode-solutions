class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        
        for r in range(m):
            for c in range(n):
                live_neighbors = 0

                for dr,dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                        live_neighbors += 1

                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1
                else:
                    if live_neighbors == 3:
                        board[r][c] = 2

                    
        for r in range(m):
            for c in range(n):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] =0