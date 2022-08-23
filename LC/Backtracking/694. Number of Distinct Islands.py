class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(r, c, grid, path):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                self.steps += path
                grid[r][c] = 0
                dfs(r + 1, c, grid, path + 'd') or dfs(r - 1, c, grid, path + 'u') \
                or dfs(r, c + 1, grid, path + 'r') or dfs(r, c - 1, grid, path + 'l')

        m = len(grid)
        n = len(grid[0])
        rset = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    self.steps = ''
                    dfs(r, c, grid, '')
                    rset.add(self.steps)
        return len(rset)


