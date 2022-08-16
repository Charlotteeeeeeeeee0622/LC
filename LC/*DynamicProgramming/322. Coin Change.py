# https://leetcode.cn/problems/coin-change/solution/dong-tai-gui-hua-tao-lu-xiang-jie-by-wei-lai-bu-ke/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]
            # base case
            if n == 0:
                return 0
            # 减过了头
            if n < 0:
                return -1

            res = float('inf')
            for coin in coins:
                sub = dp(n - coin)
                if sub == -1:
                    continue
                res = min(res, dp(n - coin) + 1)

            # 计入备忘录
            memo[n] = res if res != float('inf') else -1
            return memo[n]

        return dp(amount)