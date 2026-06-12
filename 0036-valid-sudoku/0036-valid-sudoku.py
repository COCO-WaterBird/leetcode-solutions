class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        row = [[0]*10 for _ in range(10)]
        col = [[0]*10 for _ in range(10)]
        matrix = [[[0]*10 for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                else:
                    num = int(num)
                    row[i][num] += 1
                    col[j][num] += 1
                    matrix[i//3][j//3][num] += 1
                    if row[i][num] > 1 or col[j][num] > 1 or matrix[i//3][j//3][num] > 1:
                        return False
        return True        