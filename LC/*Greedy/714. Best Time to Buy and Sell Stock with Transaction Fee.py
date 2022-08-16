# ——————————————Solution1————————————————
# 空间优化版
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [0] * 2

        dp[0] = 0
        dp[1] = -prices[0]

        for i in range(1, len(prices)):
            temp = dp[0]
            dp[0] = max(dp[0], dp[1] + prices[i] - fee)
            dp[1] = max(dp[1], temp - prices[i])

        return dp[0]


# ——————————————Solution2————————————————
# 原版
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, len(prices)):
            dp[i][0], dp[i][1] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee), max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]
