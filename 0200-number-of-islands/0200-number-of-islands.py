class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        def infect(grid,x,y):
            if x<0 or x >= rows or y<0 or y >= cols or grid[x][y] != "1":
                return
            grid[x][y] = "2"
            infect(grid, x+1, y)
            infect(grid, x-1, y)
            infect(grid, x, y+1)
            infect(grid, x, y-1)
            

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    infect(grid,i,j)
        return count