class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # every position of grid stores the min path sum

        # initialize first col
        for c in range(1, len(grid[0])):
            grid[0][c] += grid[0][c - 1]

        # initialize first row
        for r in range(1, len(grid)):
            grid[r][0] += grid[r - 1][0]

        # calculate
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                grid[r][c] = min(grid[r - 1][c] + grid[r][c], grid[r][c - 1] + grid[r][c])

        return grid[-1][-1]