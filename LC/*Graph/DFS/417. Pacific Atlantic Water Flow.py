# https://leetcode.cn/problems/pacific-atlantic-water-flow/solution/shui-wang-gao-chu-liu-by-xiaohu9527-xxsx/
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pac = [[0] * n for _ in range(m)]
        atl = [[0] * n for _ in range(m)]
        res = []

        def dfs(heights, visited, row, col):
            if visited[row][col]:
                return
            visited[row][col] = 1

            if pac[row][col] and atl[row][col]:
                res.append([row, col])

            if row - 1 >= 0 and heights[row - 1][col] >= heights[row][col]:
                dfs(heights, visited, row - 1, col)
            if row + 1 < m and heights[row + 1][col] >= heights[row][col]:
                dfs(heights, visited, row + 1, col)
            if col - 1 >= 0 and heights[row][col - 1] >= heights[row][col]:
                dfs(heights, visited, row, col - 1)
            if col + 1 < n and heights[row][col + 1] >= heights[row][col]:
                dfs(heights, visited, row, col + 1)
            return

        for i in range(m):
            dfs(heights, pac, i, 0)
            dfs(heights, atl, i, n - 1)
        for j in range(n):
            dfs(heights, pac, 0, j)
            dfs(heights, atl, m - 1, j)
        return res

