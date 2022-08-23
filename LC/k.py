from typing import List

if __name__ == '__main__':

    def numDistinctIslands(grid: List[List[int]]) -> int:
        def dfs(r, c, grid, path):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                steps += path
                # visited
                grid[r][c] = 0
                dfs(r + 1, c, grid, path + 'd') or dfs(r - 1, c, grid, path + 'u') \
                or dfs(r, c + 1, grid, path + 'r') or dfs(r, c - 1, grid, path + 'l')
                steps += 'b'  # back

        m = len(grid)
        n = len(grid[0])
        rset = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    global steps
                    steps=''
                    dfs(r, c, grid, '')
                    rset.add(steps)
        return len(rset)

    numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])