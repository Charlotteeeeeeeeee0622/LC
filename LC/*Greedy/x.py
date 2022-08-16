# 一、第i天不持股且没卖出的状态dp[i][0]，也就是我没有股票，而且还不是因为我卖了它才没有的，那换句话说是从i-1天到第i天转移时，它压根就没给我股票！所以i-1天一定也是不持有，那就是不持有的两种可能：i-1天不持股且当天没有卖出dp[i-1][0]；i-1天不持股但是当天卖出去了dp[i-1][2]；
# 所以： dp[i][0]=max(dp[i-1][0],dp[i-1][2])
#
# 二、第i天持股dp[i][1]，今天我持股，来自两种可能：
# 1、要么是昨天我就持股，今天继承昨天的，也就是dp[i-1][1]，这种可能很好理解；
# 2、要么：是昨天我不持股，今天我买入的，但前提是昨天我一定没卖！因为如果昨天我卖了，那么今天我不能交易！也就是题目中所谓“冷冻期”的含义，只有昨天是“不持股且当天没卖出”这个状态，我今天才能买入！所以是dp[i-1][0]-p[i]
# 所以： dp[i][1]=max(dp[i-1][1],dp[i-1][0]-p[i])
#
# 三、i天不持股且当天卖出了，这种就简单了，那就是说昨天我一定是持股的，要不然我今天拿什么卖啊，而持股只有一种状态，昨天持股的收益加上今天卖出得到的新收益，就是dp[i-1][1]+p[i]啦
# 所以：dp[i][2]=dp[i-1][1]+p[i]
#
# 总结：最后一天的最大收益有两种可能，而且一定是“不持有”状态下的两种可能，把这两种“不持有”比较一下大小，返回即可
#     vector<vector<int>>dp(prices.size(),vector<int>(4));
#     dp[0][0]=0;//不持有股票，没卖出的
#     dp[0][1]=0;//不持有股票，卖出去了
#     dp[0][2]=-1*prices[0];//持有股票，今天买入；
#     dp[0][3]=-1*prices[0];//持有股票，非今天买入的；
#     for(int i=1;i<prices.size();i++){
#         dp[i][0]=max(dp[i-1][0],dp[i-1][1]);//前一天不持有股票的两种情况的最大值
#         dp[i][1]=max(dp[i-1][2],dp[i-1][3])+prices[i];//今天卖出股票，来着前一天持有股票的最大值+pr
#         dp[i][2]=dp[i-1][0]-prices[i];//今天买入股票，这前一天一定没有卖出股票
#         dp[i][3]=max(dp[i-1][2],dp[i-1][3]);//今天没买股票，却持有股票，前一天继承来的,有两种情况
#     }
#     return max(dp[prices.size()-1][0],dp[prices.size()-1][1]);
# }

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