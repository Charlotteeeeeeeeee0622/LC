"""
1.状态定义:
    dp[i]为以nums[i]结尾的严格递增子序列最大长度
    count[i]为以nums[i]结尾的最长严格递增子序列的数目
2.状态转移:
    2.1 对于dp[i]:若要求dp[i],遍历j∈[0,i-1],若nums[i]>nums[j],维护dp[i]=max(dp[i],dp[j]+1)
    2.2 对于count[i]:在维护dp[i](遍历j)的过程中有两种情形需要更新count[i]
        2.2.1 遇到与dp[i]==dp[j]+1相等的情况应该累加:count[i]+=count[j] (..nums[j1],nums[i]+..nums[j2],nums[i])
        2.2.2 遇到dp[j]+1>dp[i]时,说明最长序列的长度需要更新了,此时count[i]=count[j]
3.初始化:由于最短的递增子序列长度为1,初始化dp[i]=1;同时count[i]初始化为1,因为数目至少有1个
4.遍历顺序:先i后j,i正序,j无所谓
5.返回形式:遍历dp[i]查找最大的dp[i]的值,其对应的count[i]就是整个数组对应的最长严格递增子序列的数目
"""


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [1] * n
        mn = [1] * n

        for i in range(n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        mn[i] = mn[j]
                    elif dp[i] == dp[j] + 1:
                        mn[i] += mn[j]

        ans = 0
        for i in range(n):
            if dp[i] == max(dp):
                ans += mn[i]

                def findNumberOfLIS(self, nums: List[int]) -> int:
                    dp, longest = [[1, 1] for i in range(len(nums))], 1
                    for i, num in enumerate(nums):
                        count = 0
                        for j in range(i):
                            if nums[j] < num:
                                dp[i][0] = max(dp[i][0], dp[j][0] + 1)
                        for j in range(i):
                            if nums[j] < num and dp[j][0] == dp[i][0] - 1:
                                count += dp[j][1]
                        dp[i][1] = max(dp[i][1], count)
                        longest = max(longest, dp[i][0])
                    return sum([item[1] for item in dp if item[0] == longest])

        return ans

    class Solution:
        def findNumberOfLIS(self, nums: List[int]) -> int:
            # time complexity
            # meetingroom和这一题的另外一种写法，space压缩

            # dp[i]为以nums[i]结尾的严格递增子序列最大长度
            # count[i]为以nums[i]结尾的最长严格递增子序列的数目

            if not nums:
                return 0

            dp[0] = 0
            dp[1] = 1

            for i range(2, len(nums)):
                for j in range(0, i)
                    if nums[i] > nums[i - 1]:
                        dp[i] = dp[i - 1] + 1
                    else:
                        dp[i] = dp[i - 1]

            res = 0
            for i in range(len(nums)):
                if dp[i] == max(dp):
                    count += 1
            return count

