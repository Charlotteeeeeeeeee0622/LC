class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(grid, i, j):
            # if i<0 or i>=len(grid) or j<0 or j>=(len(grid)+1) or grid[i][j]==0:
            #     return
            # else:
            #     grid[i][j]=0
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(grid, i + 1, j) + dfs(grid, i - 1, j) + dfs(grid, i, j + 1) + dfs(grid, i, j - 1)
            return 0

        areas = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                areas.append(dfs(grid, row, col))
        return max(areas) if areas else 0


def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    size = 0

    def dfs(i, j):
        nonlocal size
        nonlocal grid
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dii = di + i
            djj = dj + j
            if 0 <= dii < len(grid) and 0 <= djj < len(grid[0]) and grid[dii][djj] == 1:
                grid[dii][djj] = 0
                size += 1
                dfs(dii, djj)

    max_size = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                grid[i][j] = 0
                size = 1
                dfs(i, j)
                max_size = max(max_size, size)
    return max_size