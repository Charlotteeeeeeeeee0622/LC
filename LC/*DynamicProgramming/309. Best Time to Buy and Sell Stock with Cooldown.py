class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0, 0, 0] for _ in range(len(prices))]

        dp[0][0] = 0  # 不持有股票，没有试图卖出
        dp[0][1] = 0  # 不持有股票，当日卖出
        dp[0][2] = -prices[0]  # 持有股票，今日买入
        dp[0][3] = -prices[0]  # 持有股票，非今日买入的

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])  # 前一天不持有股票的两种情况的最大值
            dp[i][1] = max(dp[i - 1][2], dp[i - 1][3]) + prices[i]  # 今天卖出股票，来着前一天持有股票的最大值+pr
            dp[i][2] = dp[i - 1][0] - prices[i]  # 今天买入股票，这前一天一定没有卖出股票
            dp[i][3] = max(dp[i - 1][2], dp[i - 1][3])  # 今天没买股票，却持有股票，前一天继承来的,有两种情况

        return max(dp[len(prices) - 1][0], dp[len(prices) - 1][1])