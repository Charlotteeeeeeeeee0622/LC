# https://leetcode.cn/problems/island-perimeter/solution/tu-jie-jian-ji-er-qiao-miao-de-dfs-fang-fa-java-by/
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c):
            # 从一个岛屿方格走向网格边界，周长加 1
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return 1
            # 从一个岛屿方格走向水域方格，周长加 1
            if grid[r][c] == 0:
                return 1
            if grid[r][c] != 1:
                return 0
            grid[r][c] = 2
            return dfs(grid, r - 1, c) + dfs(grid, r + 1, c) + dfs(grid, r, c - 1) + dfs(grid, r, c + 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(grid, r, c)
        return 0
