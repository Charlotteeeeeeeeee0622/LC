# https://leetcode.cn/problems/combination-sum-iv/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-wen-/
"""
动态规划计算可能的方案数
dp[x]表示选取的元素之和等于x的方案数
1<=i<=target，如果存在一种排列期中元素之和等于i，则该排列的最后一个元素一定是数组nums中的一个元素
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]