# https://leetcode.cn/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/
class Solution:
    def uniquePaths(self, m, n):
        dp = [[1]*n for i in range(m)]
        for i, j in dp(range(1, m), range(1, n)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]