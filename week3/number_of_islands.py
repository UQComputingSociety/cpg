class Solution:
    def numIslands(self, grid: List[List[str]]):
        if len(grid) == 0:
            return 0
        r = len(grid)
        c = len(grid[0])
        islands = 0
        
        def dfs(grid: List[List[str]], i: int, j: int):
            # Bounds check
            if i < 0 or i >= r \
            or j < 0 or j >= c or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    islands += 1
        return islands